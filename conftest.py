import pytest
import pytest_asyncio

from langchain.chat_models import init_chat_model
from langchain_core.callbacks.base import BaseCallbackHandler
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

from config import MODEL_NAME, SYSTEM_PROMPT, get_mcp_client

class ToolCallTracker(BaseCallbackHandler):
    def __init__(self):
        self.tool_calls = []

    def on_tool_start(self, serialized, input_str, **kwargs):
        self.tool_calls.append({"name": serialized.get("name", "unknown"), "type": "start"})


@pytest.fixture(scope="session")
def model():
    """Session-scoped model instance."""
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
