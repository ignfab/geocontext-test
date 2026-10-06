import pytest

from config.constants import (
	GEOCONTEXT_DEV,
	TOOL_GEOCODE,
	TOOL_GPF_SEARCH_TYPES,
	TOOL_GPF_DESCRIBE_TYPE,
	TOOL_GPF_GET_FEATURES,
	TOOL_GPF_COUNT_FEATURES,
)

USER_INPUT = "Combien de lycées sont situés à 2km du chateau de vincennes?"
EXPECTED_RESPONSE_FRAGMENTS = ["14", "lycées"]

@pytest.mark.asyncio
async def test_count_lycees_2km_chateau_vincennes(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = tracker.get_names()

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
        assert fragment.lower() in message_text, f"Expected fragment not found in response: {fragment}"
