import pytest

from config.constants import (
    GEOCONTEXT_DEV,
    TOOL_GPF_SEARCH_TYPES,
    TOOL_GPF_DESCRIBE_TYPE,
    TOOL_GPF_GET_FEATURES,
)
from helpers import extract_numbers

pytestmark = pytest.mark.skipif(
    not GEOCONTEXT_DEV, reason="spatial_extras requires geocontext 0.10.x (GEOCONTEXT_DEV=1)"
)

USER_INPUT = "Quelle est la superficie du lac Daumesnil ?"
# BDTOPO_V3:plan_d_eau with toponyme "Lac Daumesnil": ~101 000 m² (~10.1 ha)
EXPECTED_AREA_M2_RANGE = (95000, 110000)
EXPECTED_AREA_HA_RANGE = (9.5, 11)

@pytest.mark.asyncio
async def test_area_lac_daumesnil(mcp_agent, tracker):
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
    spatial_extras = [
        tool_call.get("args", {}).get("spatial_extras") or []
        for message in result["messages"]
        for tool_call in getattr(message, "tool_calls", None) or []
        if tool_call.get("name") == TOOL_GPF_GET_FEATURES
    ]
    assert any("area" in extras for extras in spatial_extras), \
        f"Expected spatial_extras containing area, got {spatial_extras}"

    last_message = result["messages"][-1]
    message_text = str(last_message)

    numbers = extract_numbers(message_text)
    assert any(
        EXPECTED_AREA_M2_RANGE[0] <= n <= EXPECTED_AREA_M2_RANGE[1]
        or EXPECTED_AREA_HA_RANGE[0] <= n <= EXPECTED_AREA_HA_RANGE[1]
        for n in numbers
    ), f"Expected area in {EXPECTED_AREA_M2_RANGE} m² or {EXPECTED_AREA_HA_RANGE} ha in response: {message_text[:300]}"
