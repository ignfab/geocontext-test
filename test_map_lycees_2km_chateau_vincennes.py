import json
import urllib.request

import pytest

from config.constants import (
    GEOCONTEXT_DEV,
    TOOL_GEOCODE,
    TOOL_GPF_SEARCH_TYPES,
    TOOL_GPF_DESCRIBE_TYPE,
    TOOL_GPF_GET_FEATURES_LAYER,
    TOOL_SHOW_MAP,
)
from helpers import get_layer_data_urls, get_tool_call_args

pytestmark = pytest.mark.skipif(
    not GEOCONTEXT_DEV, reason="gpf_get_features_layer requires geocontext 0.10.x (GEOCONTEXT_DEV=1)"
)

USER_INPUT = "Affiche sur une carte les lycées à 2 km du château de Vincennes"
# BDTOPO_V3:zone_d_activite_ou_d_interet with nature "Lycée" within 2 km of the château
# (consistent with test_count_lycees_2km_chateau_vincennes.py)
EXPECTED_FEATURE_COUNT = 14

@pytest.mark.asyncio
async def test_map_lycees_2km_chateau_vincennes(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = {c.get("name") for c in tracker.tool_calls if c.get("type") == "start"}

    required_tools = [
        TOOL_GEOCODE,
        TOOL_GPF_SEARCH_TYPES,
        TOOL_GPF_DESCRIBE_TYPE,
        TOOL_GPF_GET_FEATURES_LAYER,
        TOOL_SHOW_MAP,
    ]
    for tool_name in required_tools:
        assert tool_name in tool_names_called, f"{tool_name} tool was not called"

    # show_map must display the layer returned by gpf_get_features_layer, not a made up URL
    data_urls = get_layer_data_urls(result["messages"], TOOL_GPF_GET_FEATURES_LAYER)
    show_map_urls = [args.get("data_url") for args in get_tool_call_args(result["messages"], TOOL_SHOW_MAP)]
    displayed_urls = [url for url in show_map_urls if url in data_urls]
    assert displayed_urls, \
        f"Expected {TOOL_SHOW_MAP} to be called with a data_url from {TOOL_GPF_GET_FEATURES_LAYER} {data_urls}, got {show_map_urls}"

    # The displayed layer is a FeatureCollection with the high schools
    with urllib.request.urlopen(displayed_urls[-1], timeout=30) as response:
        feature_collection = json.load(response)
    assert feature_collection.get("type") == "FeatureCollection"
    assert len(feature_collection["features"]) == EXPECTED_FEATURE_COUNT, \
        f"Expected {EXPECTED_FEATURE_COUNT} high schools in the displayed layer, got {len(feature_collection['features'])}"
