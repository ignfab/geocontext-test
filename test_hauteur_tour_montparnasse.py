import pytest

from config.constants import (
    GEOCONTEXT_DEV,
    TOOL_GPF_SEARCH_TYPES,
    TOOL_GPF_DESCRIBE_TYPE,
    TOOL_GPF_GET_FEATURES,
)
from helpers import extract_numbers

pytestmark = pytest.mark.skipif(
    not GEOCONTEXT_DEV, reason="intersects_point_filter requires geocontext 0.10.x (GEOCONTEXT_DEV=1)"
)

# Coordinates of the Tour Montparnasse (centroid of its footprint) are given to avoid
# testing the geocode chaining (geocode only returns streets for "Tour Montparnasse")
TOUR_LON, TOUR_LAT = 2.321983, 48.842111
USER_INPUT = (
    "Quelle est la hauteur du bâtiment situé au point "
    f"(longitude {TOUR_LON}, latitude {TOUR_LAT}) ?"
)
# BDTOPO_V3:batiment batiment.5799364 : hauteur = 207.4 m (ground to gutter, not the commonly cited 210 m)
EXPECTED_HEIGHT_M_RANGE = (197.4, 217.4)

@pytest.mark.asyncio
async def test_hauteur_tour_montparnasse(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = {c.get("name") for c in tracker.tool_calls if c.get("type") == "start"}

    required_tools = [
        TOOL_GPF_SEARCH_TYPES,
        TOOL_GPF_DESCRIBE_TYPE,
        TOOL_GPF_GET_FEATURES,
    ]
    for tool_name in required_tools:
        assert tool_name in tool_names_called, f"{tool_name} tool was not called"

    # The tracker only records tool names, arguments are read from the AI messages
    get_features_args = [
        tool_call.get("args", {})
        for message in result["messages"]
        for tool_call in getattr(message, "tool_calls", None) or []
        if tool_call.get("name") == TOOL_GPF_GET_FEATURES
    ]
    assert any(
        args.get("typename") == "BDTOPO_V3:batiment"
        and (args.get("intersects_point_filter") or {})
        and abs(args["intersects_point_filter"].get("lon", 0) - TOUR_LON) < 0.0001
        and abs(args["intersects_point_filter"].get("lat", 0) - TOUR_LAT) < 0.0001
        for args in get_features_args
    ), f"Expected intersects_point_filter on BDTOPO_V3:batiment at the given point, got {get_features_args}"

    last_message = result["messages"][-1]
    message_text = str(last_message)

    numbers = extract_numbers(message_text)
    assert any(EXPECTED_HEIGHT_M_RANGE[0] <= n <= EXPECTED_HEIGHT_M_RANGE[1] for n in numbers), \
        f"Expected height in {EXPECTED_HEIGHT_M_RANGE} m in response: {message_text[:300]}"
