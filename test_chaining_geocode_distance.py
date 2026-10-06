import pytest

from config.constants import GEOCONTEXT_DEV, TOOL_DISTANCE, TOOL_GEOCODE
from helpers import extract_numbers

pytestmark = pytest.mark.skipif(
    not GEOCONTEXT_DEV, reason="distance tool requires geocontext 0.10.x (GEOCONTEXT_DEV=1)"
)

USER_INPUT = "Quelle distance à pied entre la gare de Lyon et la tour Eiffel ?"

@pytest.mark.asyncio
async def test_chaining_geocode_distance(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = tracker.get_names()

    assert TOOL_GEOCODE in tool_names_called, f"{TOOL_GEOCODE} tool was not called"
    assert TOOL_DISTANCE in tool_names_called, f"{TOOL_DISTANCE} tool was not called"

    distance_profiles = [args.get("profile") for args in tracker.get_args(TOOL_DISTANCE)]
    assert "pedestrian" in distance_profiles, \
        f"Expected {TOOL_DISTANCE} to be called with profile=pedestrian, got {distance_profiles}"

    last_message = result["messages"][-1]
    message_text = str(last_message)

    # Gare de Lyon → Eiffel Tower on foot: ~7 km
    numbers = extract_numbers(message_text)
    assert any(5 <= n <= 9 or 5000 <= n <= 9000 for n in numbers), \
        f"Expected a walking distance around 7 km in response: {message_text[:200]}"
