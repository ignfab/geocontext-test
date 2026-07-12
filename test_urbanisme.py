import pytest

from config.constants import TOOL_URBANISME

USER_INPUT = "Quelles sont les règles d'urbanisme applicables au 73 avenue de Paris, Saint-Mandé?"

@pytest.mark.asyncio
async def test_urbanisme(mcp_agent, mcp_tools, tracker):
    urbanisme_tool = next((t for t in mcp_tools if t.name == TOOL_URBANISME), None)
    assert urbanisme_tool is not None, f"Tool '{TOOL_URBANISME}' not found"

    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    urbanisme_calls = [c for c in tracker.tool_calls if c.get("name") == TOOL_URBANISME]
    assert len(urbanisme_calls) > 0, f"{TOOL_URBANISME} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message)

    keywords = ["saint-mandé", "saint mandé", "saint mande", "urbanisme", "zone", "plu", "règle", "regle"]
    assert any(k in message_text.lower() for k in keywords), \
        f"None of {keywords} found in response"
