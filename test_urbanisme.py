import pytest

from config.constants import TOOL_URBANISME

USER_INPUT = "Quelles sont les règles d'urbanisme applicables au 73 avenue de Paris, Saint-Mandé?"

@pytest.mark.asyncio
async def test_urbanisme(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    assert TOOL_URBANISME in tracker.get_names(), f"{TOOL_URBANISME} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message)

    keywords = ["saint-mandé", "saint mandé", "saint mande", "urbanisme", "zone", "plu", "règle", "regle"]
    assert any(k in message_text.lower() for k in keywords), \
        f"None of {keywords} found in response"
