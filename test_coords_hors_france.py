import pytest

from langchain.agents import create_agent
from config import SYSTEM_PROMPT

USER_INPUT = "Dans quelle commune se trouve le point de coordonnées longitude 10.0, latitude 60.0?"


@pytest.mark.asyncio
async def test_coords_hors_france(mcp_tools, model, tracker):
    """Test négatif : coordonnées hors France (Norvège).

    L'agent doit indiquer qu'il ne peut pas répondre ou que les coordonnées
    sont hors du périmètre couvert, sans crasher.
    """
    agent = create_agent(model=model, tools=mcp_tools, system_prompt=SYSTEM_PROMPT)
    assert agent is not None

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": USER_INPUT}]},
        config={"callbacks": [tracker]},
    )

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    # Le LLM ne doit PAS inventer une commune française
    communes_inventees = ["paris", "lyon", "marseille", "toulouse", "bordeaux"]
    assert not any(c in message_text for c in communes_inventees), \
        f"L'agent a inventé une commune française pour des coordonnées en Norvège: {message_text[:300]}"

    # L'agent doit signaler un problème ou mentionner que c'est hors France
    indicateurs = [
        "hors", "outside", "france", "norvège", "norway", "erreur", "error",
        "impossible", "cannot", "pas de résultat", "no result", "not available",
        "ne couvre", "does not cover", "en dehors", "hors périmètre"
    ]
    assert any(k in message_text for k in indicateurs), \
        f"L'agent n'a pas signalé que les coordonnées sont hors France: {message_text[:300]}"
