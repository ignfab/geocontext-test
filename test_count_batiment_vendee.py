import os

import pytest

from config.constants import (
    GEOCONTEXT_DEV,
    TOOL_GPF_COUNT_FEATURES,
    TOOL_GPF_GET_FEATURES,
)
from helpers import extract_numbers

pytestmark = [
    pytest.mark.skipif(
        not GEOCONTEXT_DEV, reason="intersects_feature_filter requires geocontext 0.10.x (GEOCONTEXT_DEV=1)"
    ),
    pytest.mark.skipif(
        os.getenv("SKIP_TEST_COUNT_BATIMENT_VENDEE", "1") == "1",
        reason="the GPF WFS ignores the cql_filter of a too large Vendée geometry and returns the count for "
        "the whole of France, see https://github.com/ignfab/geocontext-test/issues/42 "
        "(set SKIP_TEST_COUNT_BATIMENT_VENDEE=0 to run it)",
    ),
]

# Large administrative unit geometry, see ignfab/demo-geocontext#70 and ignfab/geocontext#130
USER_INPUT = "Combien y a-t-il de bâtiments dans le département de la Vendée ?"
# ~857 000 buildings (sum of the counts per commune of Vendée)
EXPECTED_MIN = 800_000
EXPECTED_MAX = 900_000

@pytest.mark.asyncio
async def test_count_batiment_vendee(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = {c.get("name") for c in tracker.tool_calls if c.get("type") == "start"}

    assert TOOL_GPF_COUNT_FEATURES in tool_names_called, f"{TOOL_GPF_COUNT_FEATURES} tool was not called"

    # The tracker only records tool names, arguments are read from the AI messages
    count_tool_calls = [
        tool_call.get("args", {})
        for message in result["messages"]
        for tool_call in getattr(message, "tool_calls", None) or []
        if tool_call.get("name") in (TOOL_GPF_COUNT_FEATURES, TOOL_GPF_GET_FEATURES)
    ]
    assert any(args.get("intersects_feature_filter") for args in count_tool_calls), \
        f"Expected intersects_feature_filter to be used, got {count_tool_calls}"

    last_message = result["messages"][-1]
    message_text = str(last_message)
    numbers = extract_numbers(message_text)
    assert any(EXPECTED_MIN <= n <= EXPECTED_MAX for n in numbers), \
        f"Expected a number of buildings between {EXPECTED_MIN} and {EXPECTED_MAX} in response: {message_text[:300]}"
