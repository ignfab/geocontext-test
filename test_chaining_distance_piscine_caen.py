import pytest

from config.constants import (
    GEOCONTEXT_DEV,
    TOOL_DISTANCE,
    TOOL_GEOCODE,
    TOOL_GPF_SEARCH_TYPES,
    TOOL_GPF_DESCRIBE_TYPE,
    TOOL_GPF_GET_FEATURES,
)
from helpers import extract_numbers

pytestmark = pytest.mark.skipif(
    not GEOCONTEXT_DEV, reason="distance tool requires geocontext 0.10.x (GEOCONTEXT_DEV=1)"
)

# Scenario from https://github.com/ignfab/geocontext/pull/207
USER_INPUT = (
    "Quel est le temps de marche exact entre le cinéma LUX, situé au sud-est de Caen, "
    "et la piscine la plus proche ?"
)
EXPECTED_RESPONSE_FRAGMENTS = ["Sivom", "Mondeville"]

@pytest.mark.asyncio
async def test_chaining_distance_piscine_caen(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = tracker.get_names()

    required_tools = [
        TOOL_GEOCODE,
        TOOL_GPF_SEARCH_TYPES,
        TOOL_GPF_DESCRIBE_TYPE,
        TOOL_GPF_GET_FEATURES,
        TOOL_DISTANCE,
    ]
    for tool_name in required_tools:
        assert tool_name in tool_names_called, f"{tool_name} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message)

    for fragment in EXPECTED_RESPONSE_FRAGMENTS:
        assert fragment.lower() in message_text.lower(), f"Expected fragment not found in response: {fragment}"

    # Walking time between 25 and 35 minutes
    numbers = extract_numbers(message_text)
    assert any(25 <= n <= 35 for n in numbers), \
        f"Expected a walking time between 25 and 35 min in response: {message_text[:200]}"
