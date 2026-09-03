import pytest

from config.constants import (
    GEOCONTEXT_DEV,
    TOOL_GEOCODE,
	TOOL_GPF_SEARCH_TYPES,
	TOOL_GPF_DESCRIBE_TYPE,
	TOOL_GPF_GET_FEATURES,
	TOOL_GPF_COUNT_FEATURES,
)

USER_INPUT = (
    "Combien y a t il de batiments de plus de 30 mètres sur la commune d'Angoulême? "
)
EXPECTED_RESPONSE_FRAGMENTS = ["19", "batiments", "bâtiments"]


@pytest.mark.asyncio
async def test_count_batiment_30m_angouleme(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = {c.get("name") for c in tracker.tool_calls if c.get("type") == "start"}

    required_tools = [
        TOOL_GEOCODE,
        TOOL_GPF_SEARCH_TYPES,
        TOOL_GPF_DESCRIBE_TYPE,
        TOOL_GPF_COUNT_FEATURES if GEOCONTEXT_DEV else TOOL_GPF_GET_FEATURES,
    ]
    for tool_name in required_tools:
        assert tool_name in tool_names_called, f"{tool_name} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    for fragment in EXPECTED_RESPONSE_FRAGMENTS:
        if fragment.lower() in message_text:
            break
    else:
        assert False, f"None of {EXPECTED_RESPONSE_FRAGMENTS} found in response"

    assert "19" in message_text, "Expected '19' in response"
