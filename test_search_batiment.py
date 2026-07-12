import pytest

from config.constants import TOOL_GPF_SEARCH_TYPES

USER_INPUT = "Dans quelle table peut-on trouver des informations sur les bâtiments?"

@pytest.mark.asyncio
async def test_chaining_geocode_altitude(mcp_agent, mcp_tools, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    search_calls = [c for c in tracker.tool_calls if c.get("name") == TOOL_GPF_SEARCH_TYPES]
    assert len(search_calls) > 0, f"{TOOL_GPF_SEARCH_TYPES} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    keywords = ["bdtopo", "batiment", "bâtiment", "parcellaire", "cadastre"]
    assert any(k in message_text for k in keywords), \
        f"None of {keywords} found in response"

