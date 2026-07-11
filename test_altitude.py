import pytest
from langchain.agents import create_agent
from pydantic import BaseModel, Field

USER_INPUT = "Quelle est l'altitude au point de coordonnées longitude 6.8692556, latitude 45.9236946 ?"


class AltitudeResponse(BaseModel):
    altitude_m: float = Field(description="Altitude au point demandé, en mètres")

@pytest.mark.asyncio
async def test_altitude(model, mcp_tools, tracker):
    altitude_tool = next((t for t in mcp_tools if t.name == "altitude"), None)
    assert altitude_tool is not None, "Tool 'altitude' not found"

    agent = create_agent(
        model=model,
        tools=mcp_tools,
        system_prompt=(
            "You are a helpful assistant for geospatial data. "
            "Use the tools when needed."
        ),
        response_format=AltitudeResponse,
    )

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    altitude_calls = [c for c in tracker.tool_calls if c.get("name") == "altitude"]
    assert len(altitude_calls) > 0, "altitude tool was not called"

    structured_response = result.get("structured_response")
    assert structured_response is not None, "No structured response returned"

    altitude_value = (
        structured_response.altitude_m
        if hasattr(structured_response, "altitude_m")
        else structured_response["altitude_m"]
    )

    # Chamonix area (6.87, 45.92) → altitude ~1000-1100m
    assert 900 <= altitude_value <= 1200, (
        f"Expected altitude around 1000m, got {altitude_value}"
    )
