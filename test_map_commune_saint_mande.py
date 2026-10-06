import json
import urllib.request

import pytest

from config.constants import (
    GEOCONTEXT_DEV,
    TOOL_ADMINEXPRESS,
    TOOL_GPF_GET_FEATURE_BY_ID_LAYER,
    TOOL_SHOW_MAP,
)
from helpers import get_layer_data_urls, get_tool_call_args

pytestmark = pytest.mark.skipif(
    not GEOCONTEXT_DEV, reason="gpf_get_feature_by_id_layer requires geocontext 0.10.x (GEOCONTEXT_DEV=1)"
)

USER_INPUT = "Affiche la commune de Saint-Mandé sur une carte"
# adminexpress returns the feature_ref of the commune (ADMINEXPRESS-COG.LATEST:commune, code INSEE 94067)
EXPECTED_TYPENAME = "ADMINEXPRESS-COG.LATEST:commune"
EXPECTED_CODE_INSEE = "94067"

@pytest.mark.asyncio
async def test_map_commune_saint_mande(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = {c.get("name") for c in tracker.tool_calls if c.get("type") == "start"}

    # note that geocode is not required: the model may know the coordinates of Saint-Mandé
    required_tools = [
        TOOL_ADMINEXPRESS,
        TOOL_GPF_GET_FEATURE_BY_ID_LAYER,
        TOOL_SHOW_MAP,
    ]
    for tool_name in required_tools:
        assert tool_name in tool_names_called, f"{tool_name} tool was not called"

    layer_args = get_tool_call_args(result["messages"], TOOL_GPF_GET_FEATURE_BY_ID_LAYER)
    assert any(args.get("typename") == EXPECTED_TYPENAME for args in layer_args), \
        f"Expected {TOOL_GPF_GET_FEATURE_BY_ID_LAYER} on {EXPECTED_TYPENAME}, got {layer_args}"

    # show_map must display the layer returned by gpf_get_feature_by_id_layer, not a made up URL
    data_urls = get_layer_data_urls(result["messages"], TOOL_GPF_GET_FEATURE_BY_ID_LAYER)
    show_map_urls = [args.get("data_url") for args in get_tool_call_args(result["messages"], TOOL_SHOW_MAP)]
    displayed_urls = [url for url in show_map_urls if url in data_urls]
    assert displayed_urls, \
        f"Expected {TOOL_SHOW_MAP} to be called with a data_url from {TOOL_GPF_GET_FEATURE_BY_ID_LAYER} {data_urls}, got {show_map_urls}"

    # The displayed layer contains the commune only
    with urllib.request.urlopen(displayed_urls[-1], timeout=30) as response:
        feature_collection = json.load(response)
    assert feature_collection.get("type") == "FeatureCollection"
    features = feature_collection["features"]
    assert len(features) == 1, f"Expected a single commune in the displayed layer, got {len(features)}"
    assert features[0]["id"].startswith("commune."), f"Expected a commune, got {features[0]['id']}"
    # code_insee may be missing if the model restricted the properties with select
    code_insee = features[0]["properties"].get("code_insee")
    assert code_insee in (None, EXPECTED_CODE_INSEE), f"Expected Saint-Mandé ({EXPECTED_CODE_INSEE}), got {code_insee}"
