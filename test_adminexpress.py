import pytest

from config.constants import TOOL_ADMINEXPRESS

USER_INPUT = "Dans quelle commune et quel département se trouve le point de coordonnées longitude 2.35, latitude 48.85?"

@pytest.mark.asyncio
async def test_adminexpress(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    admin_calls = [c for c in tracker.tool_calls if c.get("name") == TOOL_ADMINEXPRESS]
    assert len(admin_calls) > 0, f"{TOOL_ADMINEXPRESS} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    keywords = ["paris", "75", "île-de-france", "ile-de-france"]
    assert any(k in message_text for k in keywords), \
        f"None of {keywords} found in response"
