import pytest

from config.constants import (
    TOOL_GPF_DESCRIBE_TYPE,
    TOOL_GPF_GET_FEATURES,
    TOOL_GPF_SEARCH_TYPES,
)

USER_INPUT = "Trouve une table contenant des cours d'eau, décris ses attributs, et donne-moi le nom du cours d'eau proche de la Tour Eiffel (longitude 2.2945, latitude 48.8584)."

@pytest.mark.asyncio
async def test_chaining_discovery(mcp_agent, tracker):
    """Test full discovery workflow: search_types -> describe_type -> get_features.

    The agent should:
    1. Search for WFS types related to waterways
    2. Describe the schema of the found type
    3. Query features near the Eiffel Tower and return the waterway name (La Seine)
    """

    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = {c.get("name") for c in tracker.tool_calls if c.get("type") == "start"}

    assert TOOL_GPF_SEARCH_TYPES in tool_names_called, f"{TOOL_GPF_SEARCH_TYPES} tool was not called"
    assert TOOL_GPF_DESCRIBE_TYPE in tool_names_called, f"{TOOL_GPF_DESCRIBE_TYPE} tool was not called"
    assert TOOL_GPF_GET_FEATURES in tool_names_called, f"{TOOL_GPF_GET_FEATURES} tool was not called"
    assert len(tool_names_called) >= 3, f"Expected at least 3 tools chained, got: {tool_names_called}"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    assert "seine" in message_text, \
        f"Expected 'La Seine' in response, got: {message_text}"
