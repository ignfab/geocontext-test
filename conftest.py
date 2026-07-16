import os
import logging
import pytest
import pytest_asyncio

from langchain.chat_models import init_chat_model
from langchain_core.callbacks.base import BaseCallbackHandler
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI

from helpers import get_mcp_servers_path, load_mcp_servers

from config.constants import TOOL_GPF_SEARCH_TYPES, TOOL_GPF_DESCRIBE_TYPE,TOOL_GPF_GET_FEATURES,TOOL_GPF_COUNT_FEATURES

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

    if MODEL_NAME.startswith("mistralai:") and not os.getenv("MISTRAL_API_KEY"):
        raise ValueError("MISTRAL_API_KEY is not set")
    
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
