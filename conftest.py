import os
import pytest
import pytest_asyncio

from langchain.chat_models import init_chat_model
from langchain_core.callbacks.base import BaseCallbackHandler
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI

# The model name can be set via the MODEL_NAME environment variable.
# If not set, it defaults to "anthropic:claude-haiku-4-5".
MODEL_NAME = os.getenv("MODEL_NAME", "anthropic:claude-haiku-4-5")

# required for some small models. For larger models, it doesn't change much.
SYSTEM_PROMPT = "You are a helpful assistant for geospatial data. You can use the tools to answer questions about geospatial data."

def get_mcp_client():
    # Préparer les variables d'environnement pour le proxy
    env = os.environ.copy()
    proxy_vars = ["HTTP_PROXY", "HTTPS_PROXY", "NO_PROXY", "http_proxy", "https_proxy", "no_proxy"]
    proxy_env = {var: env[var] for var in proxy_vars if var in env}
    # Ensure uppercase variants are set (needed by Node.js libraries)
    if "HTTP_PROXY" not in proxy_env and "http_proxy" in proxy_env:
        proxy_env["HTTP_PROXY"] = proxy_env["http_proxy"]
    if "HTTPS_PROXY" not in proxy_env and "https_proxy" in proxy_env:
        proxy_env["HTTPS_PROXY"] = proxy_env["https_proxy"]
    if "NO_PROXY" not in proxy_env and "no_proxy" in proxy_env:
        proxy_env["NO_PROXY"] = proxy_env["no_proxy"]
    log_level = env.get("GEOCONTEXT_LOG_LEVEL", "error")

    mcp_env = {**proxy_env, "LOG_LEVEL": log_level}

    client = MultiServerMCPClient(
        {
            "geocontext": {
                "command": "npx",
                "args": ["-y", "@ignfab/geocontext"],
                "transport": "stdio",
                "env": mcp_env
            }
        }
    )
    return client

class ToolCallTracker(BaseCallbackHandler):
    def __init__(self):
        self.tool_calls = []

    def on_tool_start(self, serialized, input_str, **kwargs):
        self.tool_calls.append({"name": serialized.get("name", "unknown"), "type": "start"})


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

@pytest.fixture(scope="session")
def model():
    if MODEL_NAME.startswith("onyxia:"):
        return _create_model_onyxia(MODEL_NAME)

    return init_chat_model(MODEL_NAME, temperature=0.0)

@pytest_asyncio.fixture(scope="session")
async def mcp_tools():
    """Session-scoped MCP tools - spawns the MCP server only once."""
    client = get_mcp_client()
    tools = await client.get_tools()
    yield tools

# TODO : remove this and instanciate in test cases
@pytest.fixture
def tracker():
    """Per-test tool call tracker."""
    return ToolCallTracker()

@pytest_asyncio.fixture(scope="session")
async def mcp_agent(model, mcp_tools):
    """Session-scoped MCP agent - reuses the shared model and MCP tools."""
    agent = create_agent(model=model, tools=mcp_tools, system_prompt=SYSTEM_PROMPT, checkpointer=MemorySaver())
    yield agent
