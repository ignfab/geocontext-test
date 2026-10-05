import pytest

from config.constants import (
    GEOCONTEXT_DEV,
    TOOL_GPF_SEARCH_TYPES,
    TOOL_GPF_DESCRIBE_TYPE,
    TOOL_GPF_GET_FEATURES,
)

pytestmark = pytest.mark.skipif(
    not GEOCONTEXT_DEV, reason="spatial_extras requires geocontext 0.10.x (GEOCONTEXT_DEV=1)"
)

# Coordinates of the château are given to avoid testing the geocode chaining
CHATEAU_LON, CHATEAU_LAT = 2.435792, 48.842681
USER_INPUT = (
    "Quel est le lycée le plus proche du château de Vincennes "
    f"(longitude {CHATEAU_LON}, latitude {CHATEAU_LAT}) ?"
)
# BDTOPO_V3:zone_d_activite_ou_d_interet with nature "Lycée": Lycée Professionnel Jean Moulin
# at ~480 m, the next one (Lycée Notre-Dame de la Providence) is at ~630 m
EXPECTED_RESPONSE_FRAGMENTS = ["Jean Moulin"]

@pytest.mark.asyncio
async def test_nearest_lycee_chateau_vincennes(mcp_agent, tracker):
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
        (args.get("dwithin_point_filter") or {})
        and abs(args["dwithin_point_filter"].get("lon", 0) - CHATEAU_LON) < 0.0001
        and abs(args["dwithin_point_filter"].get("lat", 0) - CHATEAU_LAT) < 0.0001
        and "distance_to_filter_center" in (args.get("spatial_extras") or [])
        for args in get_features_args
    ), f"Expected dwithin_point_filter from the château with spatial_extras containing distance_to_filter_center, got {get_features_args}"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    for fragment in EXPECTED_RESPONSE_FRAGMENTS:
        assert fragment.lower() in message_text, f"Expected fragment not found in response: {fragment}"
