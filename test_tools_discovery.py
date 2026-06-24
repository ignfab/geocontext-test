import pytest

EXPECTED_TOOLS = [
    "geocode",
    "altitude",
    "adminexpress",
    "cadastre",
    "urbanisme",
    "assiette_sup",
    "gpf_wfs_search_types",
    "gpf_wfs_describe_type",
    "gpf_wfs_get_features",
    "gpf_wfs_get_feature_by_id",
]


@pytest.mark.asyncio
async def test_all_tools_exposed(mcp_tools):
    """Vérifie que les 10 outils MCP sont bien exposés par le serveur."""
    tool_names = {t.name for t in mcp_tools}
    for expected in EXPECTED_TOOLS:
        assert expected in tool_names, f"Tool '{expected}' not exposed by MCP server"
    assert len(tool_names) >= len(EXPECTED_TOOLS), \
        f"Expected at least {len(EXPECTED_TOOLS)} tools, got {len(tool_names)}"
