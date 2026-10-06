import pytest

from config.constants import TOOL_GPF_DESCRIBE_TYPE


USER_INPUT = "Quels sont les attributs de la table BDTOPO_V3:batiment?"

@pytest.mark.asyncio
async def test_describe_type(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    assert TOOL_GPF_DESCRIBE_TYPE in tracker.get_names(), f"{TOOL_GPF_DESCRIBE_TYPE} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    assert "geometrie" in message_text or "geometry" in message_text or "hauteur" in message_text
