import pytest

from config.constants import TOOL_GEOCODE

USER_INPUT = (
    "Donne-moi les coordonnées géographiques du 15 avenue de Paris à Loray (25390). "
    "Si le résultat ne porte pas exactement sur cette voie (avenue de Paris), "
    "ne donne aucune coordonnée et réponds uniquement 'adresse non trouvée'."
)

@pytest.mark.asyncio
async def test_geocode_address_not_found(mcp_agent, tracker):
    """Negative test: the address does not exist.

    The agent should report that no result was found rather than
    make up coordinates.
    """

    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    assert TOOL_GEOCODE in tracker.get_names(), f"{TOOL_GEOCODE} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    # The agent must explicitly report that the address was not found.
    assert "adresse non trouvée" in message_text, \
        f"The agent did not report 'adresse non trouvée': {message_text[:300]}"
