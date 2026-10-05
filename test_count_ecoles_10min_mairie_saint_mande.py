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
    "Combien d'écoles à moins de 10 minutes à pied de la mairie de Saint-Mandé "
    f"(longitude {MAIRIE_LON}, latitude {MAIRIE_LAT}) ?"
)
# BDTOPO_V3:zone_d_activite_ou_d_interet within 10 minutes on foot from the mairie:
# 9 with nature "Enseignement primaire", 21 with categorie "Science et enseignement"
EXPECTED_MIN = 8
EXPECTED_MAX = 22

@pytest.mark.asyncio
async def test_count_ecoles_10min_mairie_saint_mande(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = {c.get("name") for c in tracker.tool_calls if c.get("type") == "start"}

    required_tools = [
            TOOL_GPF_SEARCH_TYPES,
        TOOL_GPF_DESCRIBE_TYPE,
        TOOL_GPF_COUNT_FEATURES,
    ]
    for tool_name in required_tools:
        assert tool_name in tool_names_called, f"{tool_name} tool was not called"

    # The tracker only records tool names, arguments are read from the AI messages
    travel_time_filters = [
        tool_call.get("args", {}).get("travel_time_filter")
        for message in result["messages"]
        for tool_call in getattr(message, "tool_calls", None) or []
        if tool_call.get("name") in (TOOL_GPF_COUNT_FEATURES, TOOL_GPF_GET_FEATURES)
    ]
    assert any(
        f
        and f.get("profile") == "pedestrian"
        and f.get("minutes") == 10
        and abs(f.get("lon", 0) - MAIRIE_LON) < 0.0001
        and abs(f.get("lat", 0) - MAIRIE_LAT) < 0.0001
        for f in travel_time_filters
    ), f"Expected travel_time_filter from the mairie with profile=pedestrian and minutes=10, got {travel_time_filters}"

    last_message = result["messages"][-1]
    message_text = str(last_message)

    numbers = extract_numbers(message_text)
    assert any(EXPECTED_MIN <= n <= EXPECTED_MAX for n in numbers), \
        f"Expected a number of schools between {EXPECTED_MIN} and {EXPECTED_MAX} in response: {message_text[:300]}"
