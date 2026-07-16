import pytest

from config.constants import TOOL_ALTITUDE, TOOL_GEOCODE
from helpers import extract_numbers

USER_INPUT = (
    "Quelle est l'altitude de la mairie de Chamonix? "
)

@pytest.mark.asyncio
async def test_chaining_geocode_altitude(mcp_agent, tracker):
    # Invoke agent with callback handler to track tool calls
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = {c.get("name") for c in tracker.tool_calls if c.get("type") == "start"}

    assert TOOL_GEOCODE in tool_names_called, f"{TOOL_GEOCODE} tool was not called"
    assert TOOL_ALTITUDE in tool_names_called, f"{TOOL_ALTITUDE} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message)

    # Chamonix area → altitude ~900-1200m
    numbers = extract_numbers(message_text)
    assert any(900 <= n <= 1200 for n in numbers), \
        f"Expected altitude around 1000m in response: {message_text[:200]}"
