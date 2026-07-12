import pytest

from helpers import extract_numbers

USER_INPUT = (
    "Quelle est l'altitude au point de coordonnées longitude 6.87, latitude 45.92? "
    "Exprime le nombre sans séparateur de milliers, avec un point comme séparateur décimal, sans localisation."
)

@pytest.mark.asyncio
async def test_altitude(mcp_agent, mcp_tools, tracker):
    altitude_tool = next((t for t in mcp_tools if t.name == "altitude"), None)
    assert altitude_tool is not None, "Tool 'altitude' not found"

    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    altitude_calls = [c for c in tracker.tool_calls if c.get("name") == "altitude"]
    assert len(altitude_calls) > 0, "altitude tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message)

    # Chamonix area → altitude ~900-1200m
    numbers = extract_numbers(message_text)
    assert any(900 <= n <= 1200 for n in numbers), \
        f"Expected altitude around 1000m in response: {message_text[:200]}"
