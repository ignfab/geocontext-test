import pytest

from config.constants import TOOL_ADMINEXPRESS, TOOL_GEOCODE

USER_INPUT = "Dans quelle commune et quel département se trouve le 1 rue de Rivoli, Paris?"

@pytest.mark.asyncio
async def test_chaining_geocode_adminexpress(mcp_agent, tracker):
    """Test chaining: geocode -> adminexpress.

    The agent should geocode the address first, then use adminexpress
    to find the commune and département from the coordinates.
    """

    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = tracker.get_names()

    assert TOOL_GEOCODE in tool_names_called, f"{TOOL_GEOCODE} tool was not called"
    assert TOOL_ADMINEXPRESS in tool_names_called, f"{TOOL_ADMINEXPRESS} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    keywords = ["paris", "75", "île-de-france", "ile-de-france"]
    assert any(k in message_text for k in keywords), \
        f"None of {keywords} found in response"
