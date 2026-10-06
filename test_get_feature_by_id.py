import pytest
import httpx

from config.constants import TOOL_GPF_GET_FEATURE_BY_ID

WFS_URL = (
    "https://data.geopf.fr/wfs"
    "?service=WFS&request=GetFeature"
    "&typeName=ADMINEXPRESS-COG.LATEST:commune"
    "&count=1&outputformat=application/json"
)


USER_INPUT = (
    "Récupère toutes les données disponibles pour l'objet WFS de ADMINEXPRESS-COG.LATEST:commune "
    "dont le feature_id est '{FEATURE_ID}' "
    "sur le typename 'ADMINEXPRESS-COG.LATEST:commune'. "
    "Donne-moi son code_insee."
)


def fetch_sample_commune():
    """Fetch the first commune feature from the WFS service and return (feature_id, code_insee)."""
    response = httpx.get(WFS_URL, timeout=30)
    response.raise_for_status()
    data = response.json()
    feature = data["features"][0]
    feature_id = feature["id"]
    props = feature["properties"]
    code_insee = props["code_insee"]
    return feature_id, code_insee


@pytest.mark.asyncio
async def test_get_feature_by_id(mcp_agent, tracker):
    
    feature_id, code_insee = fetch_sample_commune()

    user_input = USER_INPUT.replace("{FEATURE_ID}", feature_id)

    result = await mcp_agent.ainvoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config={"callbacks": [tracker], "thread_id": __name__},
    )

    assert TOOL_GPF_GET_FEATURE_BY_ID in tracker.get_names(), f"{TOOL_GPF_GET_FEATURE_BY_ID} tool was not called"

    last_message = result["messages"][-1]
    message_text = str(last_message).lower()

    assert code_insee in message_text, \
        f"Code INSEE '{code_insee}' not found in response: {message_text[:500]}"
