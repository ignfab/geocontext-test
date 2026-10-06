import asyncio
import os
import logging
import pytest
import pytest_asyncio

from contextlib import AsyncExitStack

from langchain.chat_models import init_chat_model
from langchain_core.callbacks.base import BaseCallbackHandler
from langchain_core.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI

from helpers import get_mcp_servers_path, load_mcp_servers, write_agent_trace

from config.constants import TOOL_GPF_SEARCH_TYPES, TOOL_GPF_DESCRIBE_TYPE,TOOL_GPF_GET_FEATURES,TOOL_GPF_COUNT_FEATURES,TOOL_SHOW_MAP

# The model name can be set via the MODEL_NAME environment variable.
# If not set, it defaults to "anthropic:claude-haiku-4-5".
MODEL_NAME = os.getenv("MODEL_NAME", "anthropic:claude-haiku-4-5")

# The final instructions are required for some small models.
# For larger models, it doesn't change much.
SYSTEM_PROMPT = (
    "Tu es un assistant répondant à des questions qui exploitent des données geospatiales. "
    "Tu peux utiliser les outils pour répondre aux questions sur les données geospatiales. "
    "IMPORTANT : "
    "- Exprime les nombres sans séparateur de milliers, avec un point comme séparateur décimal, sans localisation. "
    "- N'invente pas de coordonnées : utilise l'outil approprié pour geocoder les lieux. "
    f"- N'invente pas de noms de tables : utilise {TOOL_GPF_SEARCH_TYPES} pour rechercher les données. "
    f"- N'invente pas de noms de colonnes : utilise {TOOL_GPF_DESCRIBE_TYPE} pour décrire les tables avant d'appeler {TOOL_GPF_GET_FEATURES} ou {TOOL_GPF_COUNT_FEATURES}."
)

logger = logging.getLogger(__name__)

def get_mcp_client():
    """Create an MCP client from configuration.
    
    Configuration is loaded from config/mcp-servers.json by default,
    or from the path specified in MCP_SERVERS_PATH environment variable.
    Proxy variables (HTTP_PROXY, HTTPS_PROXY, NO_PROXY) are automatically
    injected into the server environment.
    """
    path = get_mcp_servers_path()
    logger.info("Loading MCP servers config from %s", path)
    servers_config = load_mcp_servers(str(path))
    client = MultiServerMCPClient(servers_config)
    return client

class ToolCallTracker(BaseCallbackHandler):
    """Record the tool calls of the agent, with their arguments and outputs."""

    def __init__(self):
        self.tool_calls = []

    def on_tool_start(self, serialized, input_str, *, run_id=None, inputs=None, **kwargs):
        self.tool_calls.append({
            "name": serialized.get("name", "unknown"),
            "run_id": run_id,
            "args": inputs or {},
            "output": None,
        })

    def on_tool_end(self, output, *, run_id=None, **kwargs):
        for tool_call in self.tool_calls:
            if tool_call["run_id"] == run_id:
                tool_call["output"] = _output_text(output)

    def get_names(self) -> set[str]:
        """Return the names of the called tools."""
        return {c["name"] for c in self.tool_calls}

    def get_args(self, tool_name: str) -> list[dict]:
        """Return the arguments of each call to tool_name."""
        return [c["args"] for c in self.tool_calls if c["name"] == tool_name]

    def get_outputs(self, tool_name: str) -> list[str]:
        """Return the text output of each successful call to tool_name."""
        return [c["output"] for c in self.tool_calls if c["name"] == tool_name and c["output"] is not None]


def _output_text(output) -> str:
    """Return the text of a tool output (ToolMessage with str or MCP content blocks)."""
    content = getattr(output, "content", output)
    if isinstance(content, list):
        return "".join(block.get("text", "") if isinstance(block, dict) else str(block) for block in content)
    return str(content)


def _create_model_onyxia(model_name) -> ChatOpenAI:
    ONYXIA_API_KEY = os.getenv("ONYXIA_API_KEY")
    
    if not ONYXIA_API_KEY:
        raise ValueError("ONYXIA_API_KEY is not set")
    
    return ChatOpenAI(
        base_url="https://llm.lab.sspcloud.fr/api/v1",
        api_key=ONYXIA_API_KEY,
        model=model_name.replace("onyxia:", ""),
        temperature=0.0,
        model_kwargs={
            "extra_headers": {
                "enable-auto-tool-choice": "true",
                "tool-call-parser": "true"
            }
        }
    )


def _create_model_albert(model_name) -> ChatOpenAI:
    ALBERT_API_KEY = os.getenv("ALBERT_API_KEY")
    
    if not ALBERT_API_KEY:
        raise ValueError("ALBERT_API_KEY is not set")
    
    return ChatOpenAI(
        base_url="https://albert.api.etalab.gouv.fr/v1",
        api_key=ALBERT_API_KEY,
        model=model_name.replace("albert:", ""),
        temperature=0.0,
        model_kwargs={
            "extra_headers": {
                "enable-auto-tool-choice": "true",
                "tool-call-parser": "true"
            }
        }
    )


@pytest.fixture(scope="session")
def model():
    if MODEL_NAME.startswith("onyxia:"):
        return _create_model_onyxia(MODEL_NAME)

    if MODEL_NAME.startswith("albert:"):
        return _create_model_albert(MODEL_NAME)

    if MODEL_NAME.startswith("mistralai:") and not os.getenv("MISTRAL_API_KEY"):
        raise ValueError("MISTRAL_API_KEY is not set")

    return init_chat_model(MODEL_NAME, temperature=0.0)

@pytest_asyncio.fixture(scope="session")
async def mcp_tools():
    """Session-scoped MCP tools, bound to one long-lived session per server.

    `client.get_tools()` would open a *new* MCP session for each tool call. When
    the model emits several tool calls in the same turn, LangGraph runs them
    concurrently, and geocontext crosses the responses of these concurrent
    sessions over HTTP (see
    https://github.com/ignfab/geocontext-test/issues/33). Reusing a single
    session per server avoids it, and is also how a real MCP client connects.
    """
    client = get_mcp_client()
    loaded: asyncio.Future = asyncio.get_running_loop().create_future()
    closing = asyncio.Event()

    async def keep_sessions_open():
        """Own the sessions from a single task, from opening to closing.

        The MCP transports rely on anyio cancel scopes, which must be exited by
        the task that entered them. pytest-asyncio runs fixture setup and
        teardown in two different tasks, so the sessions are held by this task
        instead, and the teardown only signals it.
        """
        try:
            async with AsyncExitStack() as stack:
                tools = []
                for server_name in client.connections:
                    session = await stack.enter_async_context(client.session(server_name))
                    tools.extend(await load_mcp_tools(session, server_name=server_name))
                loaded.set_result(tools)
                await closing.wait()
        except Exception as exc:
            if not loaded.done():
                loaded.set_exception(exc)
            else:
                raise

    task = asyncio.create_task(keep_sessions_open())
    yield await loaded
    closing.set()
    await task

# TODO : remove this and instanciate in test cases
@pytest.fixture
def tracker():
    """Per-test tool call tracker."""
    return ToolCallTracker()

# Fake map display tool: a real component (MCP Carto, ...) would for example
# produce an HTML map loading the GeoJSON layer from data_url. Here, only the
# call and its arguments matter.
@tool(TOOL_SHOW_MAP)
def show_map(title: str, data_url: str) -> str:
    """Display GeoJSON data on a map to the user.

    Args:
        title: Title of the map.
        data_url: URL of the GeoJSON data to display.
    """
    return f"map displayed: {title}"


@pytest_asyncio.fixture(scope="session")
async def mcp_agent_session(model, mcp_tools):
    """Session-scoped MCP agent - reuses the shared model and MCP tools.

    The fake show_map tool mimics a map MCP (MCP Carto, ...) used next to
    geocontext. It is enabled on all the tests to detect side effects
    (see https://github.com/ignfab/geocontext-test/issues/43).
    """
    tools = mcp_tools + [show_map]
    agent = create_agent(model=model, tools=tools, system_prompt=SYSTEM_PROMPT, checkpointer=MemorySaver())
    yield agent


class RecordingAgent:
    """Proxy on the agent keeping each ainvoke result, so it can be traced."""

    def __init__(self, agent):
        self._agent = agent
        self.results = []

    async def ainvoke(self, *args, **kwargs):
        result = await self._agent.ainvoke(*args, **kwargs)
        self.results.append(result)
        return result

    def __getattr__(self, name):
        return getattr(self._agent, name)


TEST_STATUS_KEY = pytest.StashKey[str]()


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    """Store the test outcome so that fixtures can report it during teardown."""
    report = yield
    if report.when == "call":
        item.stash[TEST_STATUS_KEY] = report.outcome
    return report


@pytest.fixture
def mcp_agent(mcp_agent_session, request):
    """Per-test MCP agent writing the conversation to reports/<model>/<test>.txt.

    The trace is written on teardown, hence whether the test passed or failed.
    """
    agent = RecordingAgent(mcp_agent_session)
    yield agent
    write_agent_trace(
        MODEL_NAME,
        request.node.name,
        agent.results,
        status=request.node.stash.get(TEST_STATUS_KEY, "unknown"),
    )
