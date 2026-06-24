import pytest

from langchain.agents import create_agent
from config import SYSTEM_PROMPT

USER_INPUT = "Donne-moi les coordonnées géographiques de l'adresse '99999 rue inexistante, Villeimaginaire'."


@pytest.mark.asyncio
async def test_adresse_inexistante(mcp_tools, model, tracker):
    """Test négatif : adresse qui n'existe pas.

    L'agent doit signaler qu'il n'a pas trouvé de résultat plutôt que
    d'inventer des coordonnées.
    """
    agent = create_agent(model=model, tools=mcp_tools, system_prompt=SYSTEM_PROMPT)
    assert agent is not None

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker]},
    )

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    # L'agent doit signaler un problème
    indicateurs = [
        "pas trouvé", "introuvable", "n'existe pas", "aucun résultat",
        "not found", "no result", "impossible", "cannot find",
        "pas de résultat", "erreur", "inconnue", "unknown"
    ]
    assert any(k in message_text for k in indicateurs), \
        f"L'agent n'a pas signalé que l'adresse est introuvable: {message_text[:300]}"
