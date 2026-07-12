import pytest

from config.constants import TOOL_ASSIETTE_SUP

USER_INPUT = "Quelles sont les servitudes d'utilité publique aux coordonnées longitude 4.83, latitude 45.76?"

@pytest.mark.asyncio
async def test_assiette_sup(mcp_agent, mcp_tools, tracker):
    assiette_sup_tool = next((t for t in mcp_tools if t.name == TOOL_ASSIETTE_SUP), None)
    assert assiette_sup_tool is not None, f"Tool '{TOOL_ASSIETTE_SUP}' not found"

    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    assiette_calls = [c for c in tracker.tool_calls if c.get("name") == TOOL_ASSIETTE_SUP]
    assert len(assiette_calls) > 0, f"{TOOL_ASSIETTE_SUP} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    keywords = ["servitude", "assiette", "sup", "utilité publique"]
    assert any(k in message_text for k in keywords), \
        f"None of {keywords} found in response"
