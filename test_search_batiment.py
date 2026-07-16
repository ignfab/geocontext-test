import pytest

from config.constants import TOOL_GPF_SEARCH_TYPES

USER_INPUT = "Dans quelles tables peut-on trouver des informations sur les bâtiments?"
EXPECTED_RESPONSE_FRAGMENTS = [
    "bdtopo_v3:batiment",
    "cadastralparcels.parcellaire_express:batiment",
]

@pytest.mark.asyncio
async def test_search_batiment(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    search_calls = [c for c in tracker.tool_calls if c.get("name") == TOOL_GPF_SEARCH_TYPES]
    assert len(search_calls) > 0, f"{TOOL_GPF_SEARCH_TYPES} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    for fragment in EXPECTED_RESPONSE_FRAGMENTS:
        assert fragment in message_text, f"Expected fragment not found in response: {fragment}"

