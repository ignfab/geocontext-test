import pytest

from config.constants import (
    GEOCONTEXT_DEV,
    TOOL_GPF_SEARCH_TYPES,
    TOOL_GPF_DESCRIBE_TYPE,
    TOOL_GPF_COUNT_FEATURES,
    TOOL_GPF_GET_FEATURES,
)
from helpers import extract_numbers

pytestmark = pytest.mark.skipif(
    not GEOCONTEXT_DEV, reason="travel_time_filter requires geocontext 0.10.x (GEOCONTEXT_DEV=1)"
)

# Coordinates of the mairie are given to avoid testing the geocode chaining
MAIRIE_LON, MAIRIE_LAT = 2.419123, 48.843218
USER_INPUT = (
    "Combien de lycées à moins de 15 minutes à pied de la mairie de Saint-Mandé "
    f"(longitude {MAIRIE_LON}, latitude {MAIRIE_LAT}) ?"
)
# BDTOPO_V3:zone_d_activite_ou_d_interet with nature "Lycée" within 15 minutes on foot from the mairie
EXPECTED_COUNT = 7

@pytest.mark.asyncio
async def test_count_lycees_15min_mairie_saint_mande(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = tracker.get_names()

    required_tools = [
        TOOL_GPF_SEARCH_TYPES,
        TOOL_GPF_DESCRIBE_TYPE,
    ]
    for tool_name in required_tools:
        assert tool_name in tool_names_called, f"{tool_name} tool was not called"
    # travel_time_filter is available in both gpf_count_features and gpf_get_features
    assert {TOOL_GPF_COUNT_FEATURES, TOOL_GPF_GET_FEATURES} & tool_names_called, \
        f"Neither {TOOL_GPF_COUNT_FEATURES} nor {TOOL_GPF_GET_FEATURES} tool was called"

    travel_time_filters = [
        args.get("travel_time_filter")
        for args in tracker.get_args(TOOL_GPF_COUNT_FEATURES) + tracker.get_args(TOOL_GPF_GET_FEATURES)
    ]
    assert any(
        f
        and f.get("profile") == "pedestrian"
        and f.get("minutes") == 15
        and abs(f.get("lon", 0) - MAIRIE_LON) < 0.0001
        and abs(f.get("lat", 0) - MAIRIE_LAT) < 0.0001
        for f in travel_time_filters
    ), f"Expected travel_time_filter from the mairie with profile=pedestrian and minutes=15, got {travel_time_filters}"

    last_message = result["messages"][-1]
    message_text = str(last_message)

    numbers = extract_numbers(message_text)
    assert EXPECTED_COUNT in numbers, \
        f"Expected {EXPECTED_COUNT} high schools in response: {message_text[:300]}"
