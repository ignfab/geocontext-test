import pytest

from config.constants import TOOL_GEOCODE

USER_INPUT = (
    "Donne-moi les coordonnées géographiques du 15 avenue de Paris à Loray (25390)."
    "Si tu ne trouves pas l'adresse exacte, indique simplement 'adresse non trouvée'"
)

@pytest.mark.asyncio
async def test_geocode_address_not_found(mcp_agent, tracker):
    """Test négatif : adresse qui n'existe pas.

    L'agent doit signaler qu'il n'a pas trouvé de résultat plutôt que
    d'inventer des coordonnées.
    """

    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    geocode_calls = [c for c in tracker.tool_calls if c.get("name") == TOOL_GEOCODE]
    assert len(geocode_calls) > 0, f"{TOOL_GEOCODE} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    # L'agent doit signaler explicitement que l'adresse est introuvable.
    assert "adresse non trouvée" in message_text, \
        f"L'agent n'a pas signalé 'adresse non trouvée': {message_text[:300]}"
