import pytest

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.callbacks.base import BaseCallbackHandler
from config import MODEL_NAME, SYSTEM_PROMPT, get_mcp_client

USER_INPUT = "Récupère l'objet WFS de la commune dont le feature_id est 'commune.8952' sur le typename 'ADMINEXPRESS-COG.LATEST:commune'. Donne-moi son nom et son code INSEE."


class ToolCallTracker(BaseCallbackHandler):
    def __init__(self):
        self.tool_calls = []

    def on_tool_start(self, serialized, input_str, **kwargs):
        self.tool_calls.append({"name": serialized.get("name", "unknown"), "type": "start"})


@pytest.mark.asyncio
async def test_get_feature_by_id():
    client = get_mcp_client()
    tools = await client.get_tools()

    tool = next((t for t in tools if t.name == "gpf_wfs_get_feature_by_id"), None)
    assert tool is not None, "Tool 'gpf_wfs_get_feature_by_id' not found"

    model = init_chat_model(MODEL_NAME, temperature=0.0)
    agent = create_agent(model=model, tools=tools, system_prompt=SYSTEM_PROMPT)
    assert agent is not None

    tracker = ToolCallTracker()
    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker]},
    )

    get_by_id_calls = [c for c in tracker.tool_calls if c.get("name") == "gpf_wfs_get_feature_by_id"]
    assert len(get_by_id_calls) > 0, "gpf_wfs_get_feature_by_id tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    # commune.8952 corresponds to Montpellier (code INSEE 34172)
    keywords = ["montpellier", "34172"]
    assert any(k in message_text for k in keywords), \
        f"None of {keywords} found in response: {message_text[:500]}"
