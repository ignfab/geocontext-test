import pytest

from langchain.agents import create_agent
from config import SYSTEM_PROMPT

USER_INPUT = "Quelles sont les coordonnées géographiques du 1 rue de Rivoli à Paris?"


@pytest.mark.asyncio
async def test_geocode(mcp_tools, model, tracker):
    geocode_tool = next((t for t in mcp_tools if t.name == "geocode"), None)
    assert geocode_tool is not None, "Tool 'geocode' not found"

    agent = create_agent(model=model, tools=mcp_tools, system_prompt=SYSTEM_PROMPT)
    assert agent is not None

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker]},
    )

    geocode_calls = [c for c in tracker.tool_calls if c.get("name") == "geocode"]
    assert len(geocode_calls) > 0, "geocode tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    # 1 rue de Rivoli, Paris → approx lon 2.36, lat 48.86
    keywords = ["2.3", "48.8", "rivoli", "paris"]
    assert any(k in message_text for k in keywords), \
        f"None of {keywords} found in response"
