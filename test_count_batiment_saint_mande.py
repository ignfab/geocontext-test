import pytest

from config.constants import (
	TOOL_GEOCODE,
	TOOL_GPF_DESCRIBE_TYPE,
	TOOL_GPF_GET_FEATURES,
	TOOL_GPF_SEARCH_TYPES,
)
from helpers import extract_numbers

USER_INPUT = "Combien y a t il de batiments sur la commune de saint mandé?"
EXPECTED_RESPONSE_FRAGMENTS = ["batiments", "bâtiments"]


@pytest.mark.asyncio
async def test_count_batiment_saint_mande(mcp_agent, tracker):
	result = await mcp_agent.ainvoke(
		{"messages": [{"role": "user", "content": USER_INPUT}]},
		config={"callbacks": [tracker], "thread_id": __name__},
	)

	tool_names_called = {c.get("name") for c in tracker.tool_calls if c.get("type") == "start"}

	required_tools = [
		TOOL_GEOCODE,
		TOOL_GPF_SEARCH_TYPES,
		TOOL_GPF_DESCRIBE_TYPE,
		TOOL_GPF_GET_FEATURES,
	]
	for tool_name in required_tools:
		assert tool_name in tool_names_called, f"{tool_name} tool was not called"

	last_message = result["messages"][-1]
	message_text = str(last_message).lower()

	assert any(fragment in message_text for fragment in EXPECTED_RESPONSE_FRAGMENTS), \
		f"None of {EXPECTED_RESPONSE_FRAGMENTS} found in response"

	numbers = extract_numbers(message_text)
	assert any(1700 <= n <= 1800 for n in numbers), \
		f"Expected a number between 1700 and 1800 in response: {message_text[:300]}"
