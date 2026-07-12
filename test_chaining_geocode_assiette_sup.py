import pytest

from config.constants import TOOL_ASSIETTE_SUP, TOOL_GEOCODE

USER_INPUT = "Y a-t-il des servitudes d'utilité publique au 10 place Bellecour, Lyon?"

@pytest.mark.asyncio
async def test_chaining_geocode_assiette_sup(mcp_agent, tracker):
    """Test chaining: geocode -> assiette_sup.

    The agent should geocode the address first, then use assiette_sup
    to look up servitudes d'utilité publique at those coordinates.
    """

    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    tool_names_called = {c.get("name") for c in tracker.tool_calls if c.get("type") == "start"}

    assert TOOL_GEOCODE in tool_names_called, f"{TOOL_GEOCODE} tool was not called"
    assert TOOL_ASSIETTE_SUP in tool_names_called, f"{TOOL_ASSIETTE_SUP} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    keywords = ["servitude", "assiette", "sup", "bellecour", "lyon", "utilité publique"]
    assert any(k in message_text for k in keywords), \
        f"None of {keywords} found in response"
