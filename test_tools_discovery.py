import pytest

from config.constants import EXPECTED_TOOLS

@pytest.mark.asyncio
async def test_all_tools_exposed(mcp_tools):
    """Check that all the expected MCP tools are exposed by the server."""
    tool_names = {t.name for t in mcp_tools}
    for expected in EXPECTED_TOOLS:
        assert expected in tool_names, f"Tool '{expected}' not exposed by MCP server"
    assert len(tool_names) >= len(EXPECTED_TOOLS), \
        f"Expected at least {len(EXPECTED_TOOLS)} tools, got {len(tool_names)}"
