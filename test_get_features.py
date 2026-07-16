import pytest

from config.constants import TOOL_GPF_GET_FEATURES, TOOL_GPF_SEARCH_TYPES

USER_INPUT = "Donne-moi les bâtiments de la BDTOPO proches du point longitude 6.87, latitude 45.92 (Chamonix)."

@pytest.mark.asyncio
async def test_get_features(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    wfs_calls = [
        c
        for c in tracker.tool_calls
        if c.get("name") in (TOOL_GPF_GET_FEATURES, TOOL_GPF_SEARCH_TYPES)
    ]
    assert len(wfs_calls) > 0, "No WFS tool was called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    assert "bâtiment" in message_text or "batiment" in message_text or "bdtopo" in message_text
