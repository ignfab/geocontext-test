import pytest

from langchain.agents import create_agent
from config import SYSTEM_PROMPT

USER_INPUT = "Quelles sont les servitudes d'utilité publique aux coordonnées longitude 4.83, latitude 45.76?"


@pytest.mark.asyncio
async def test_assiette_sup(mcp_tools, model, tracker):
    assiette_sup_tool = next((t for t in mcp_tools if t.name == "assiette_sup"), None)
    assert assiette_sup_tool is not None, "Tool 'assiette_sup' not found"

    agent = create_agent(model=model, tools=mcp_tools, system_prompt=SYSTEM_PROMPT)
    assert agent is not None

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker]},
    )

    assiette_calls = [c for c in tracker.tool_calls if c.get("name") == "assiette_sup"]
    assert len(assiette_calls) > 0, "assiette_sup tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    keywords = ["servitude", "assiette", "sup", "utilité publique"]
    assert any(k in message_text for k in keywords), \
        f"None of {keywords} found in response"
