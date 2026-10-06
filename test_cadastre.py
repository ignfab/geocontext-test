import pytest

from config.constants import TOOL_CADASTRE

USER_INPUT = "Quelle est la parcelle cadastrale au 73 avenue de Paris, Saint-Mandé?"

@pytest.mark.asyncio
async def test_cadastre(mcp_agent, tracker):
    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    assert TOOL_CADASTRE in tracker.get_names(), f"{TOOL_CADASTRE} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    keywords = ["saint-mandé", "saint mandé", "saint mande", "parcelle", "cadastre"]
    assert any(k in message_text for k in keywords), \
        f"None of {keywords} found in response"
