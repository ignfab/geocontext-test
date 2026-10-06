import pytest

from config.constants import (
    GEOCONTEXT_DEV,
    TOOL_GPF_SEARCH_TYPES,
    TOOL_GPF_DESCRIBE_TYPE,
    TOOL_GPF_GET_FEATURES,
)
from helpers import extract_numbers

pytestmark = pytest.mark.skipif(
    not GEOCONTEXT_DEV, reason="bbox_filter requires geocontext 0.10.x (GEOCONTEXT_DEV=1)"
)

# Bounding box around the Château de Vincennes, given to avoid testing the geocode chaining
BBOX = {"west": 2.432, "south": 48.841, "east": 2.438, "north": 48.845}
USER_INPUT = (
    "Quel est le bâtiment le plus haut dans la boîte englobante "
    f"(ouest {BBOX['west']}, sud {BBOX['south']}, est {BBOX['east']}, nord {BBOX['north']}) "
    "autour du château de Vincennes ?"
)
# BDTOPO_V3:batiment batiment.5694132, nature "Tour, donjon", hauteur = 50.1 m (then a "Château" building at 42 m).
# The strategy is not checked, only the answer: 238 buildings intersect the bbox (default limit: 100)
# and order_by hauteur desc returns the 56 buildings without hauteur first (where hauteur gt 0 avoids it).
EXPECTED_RESPONSE_FRAGMENTS = ["donjon"]
EXPECTED_HEIGHT_M_RANGE = (49.1, 51.1)

@pytest.mark.asyncio
async def test_highest_batiment_bbox_chateau_vincennes(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = tracker.get_names()

    required_tools = [
        TOOL_GPF_SEARCH_TYPES,
        TOOL_GPF_DESCRIBE_TYPE,
        TOOL_GPF_GET_FEATURES,
    ]
    for tool_name in required_tools:
        assert tool_name in tool_names_called, f"{tool_name} tool was not called"

    get_features_args = tracker.get_args(TOOL_GPF_GET_FEATURES)
    assert any(
        args.get("typename") == "BDTOPO_V3:batiment"
        and (args.get("bbox_filter") or {})
        and all(abs(args["bbox_filter"].get(k, 0) - v) < 0.0001 for k, v in BBOX.items())
        for args in get_features_args
    ), f"Expected bbox_filter {BBOX} on BDTOPO_V3:batiment, got {get_features_args}"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    for fragment in EXPECTED_RESPONSE_FRAGMENTS:
        assert fragment.lower() in message_text, f"Expected fragment not found in response: {fragment}"

    numbers = extract_numbers(message_text)
    assert any(EXPECTED_HEIGHT_M_RANGE[0] <= n <= EXPECTED_HEIGHT_M_RANGE[1] for n in numbers), \
        f"Expected height in {EXPECTED_HEIGHT_M_RANGE} m in response: {message_text[:300]}"
