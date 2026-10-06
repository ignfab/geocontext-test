import pytest

from config.constants import (
    GEOCONTEXT_DEV,
    TOOL_GPF_SEARCH_TYPES,
    TOOL_GPF_COUNT_FEATURES,
)
from helpers import extract_numbers

pytestmark = pytest.mark.skipif(
    not GEOCONTEXT_DEV, reason="bbox_filter requires geocontext 0.10.x (GEOCONTEXT_DEV=1)"
)

# Bounding box around the Château de Vincennes, given to avoid testing the geocode chaining
BBOX = {"west": 2.432, "south": 48.841, "east": 2.438, "north": 48.845}
USER_INPUT = (
    "Combien y a-t-il de bâtiments dans la boîte englobante "
    f"(ouest {BBOX['west']}, sud {BBOX['south']}, est {BBOX['east']}, nord {BBOX['north']}) "
    "autour du château de Vincennes ?"
)
# BDTOPO_V3:batiment intersecting the bbox: 238 (small tolerance for data updates)
EXPECTED_COUNT_RANGE = (230, 245)

@pytest.mark.asyncio
async def test_count_batiment_bbox_chateau_vincennes(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = tracker.get_names()

    required_tools = [
        TOOL_GPF_SEARCH_TYPES,
        TOOL_GPF_COUNT_FEATURES,
    ]
    for tool_name in required_tools:
        assert tool_name in tool_names_called, f"{tool_name} tool was not called"

    count_args = tracker.get_args(TOOL_GPF_COUNT_FEATURES)
    assert any(
        args.get("typename") == "BDTOPO_V3:batiment"
        and (args.get("bbox_filter") or {})
        and all(abs(args["bbox_filter"].get(k, 0) - v) < 0.0001 for k, v in BBOX.items())
        for args in count_args
    ), f"Expected bbox_filter {BBOX} on BDTOPO_V3:batiment, got {count_args}"

    last_message = result["messages"][-1]
    message_text = str(last_message)

    numbers = extract_numbers(message_text)
    assert any(EXPECTED_COUNT_RANGE[0] <= n <= EXPECTED_COUNT_RANGE[1] for n in numbers), \
        f"Expected a number of buildings in {EXPECTED_COUNT_RANGE} in response: {message_text[:300]}"
