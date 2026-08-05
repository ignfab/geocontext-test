"""Check that geocontext answers concurrent tool calls without crossing them.

This test needs no model: it calls two tools with clearly distinct output
schemas at the same time, the way LangGraph does when a model emits several
tool calls in a single turn, and verifies that each call gets *its own* answer.

Over HTTP, geocontext 0.10.x crosses these answers (see
https://github.com/ignfab/geocontext-test/issues/33). The stdio transport is
immune, since each tool call spawns its own server process.

The tools are loaded here with `client.get_tools()`, which opens a new MCP
session per call: that is the topology the server trips on, and the one the
`mcp_tools` fixture deliberately avoids while the bug is open.
"""
import asyncio
import json

import pytest

from conftest import get_mcp_client
from config.constants import TOOL_GEOCODE, TOOL_GPF_SEARCH_TYPES
from helpers import get_mcp_servers_path, load_mcp_servers


def attempts() -> int:
    """Number of concurrent rounds to run.

    Over HTTP the crossing is a race, lost in roughly 40 % of the rounds, so
    several of them are needed to catch it. On stdio each call starts its own
    server process: the crossing cannot happen, and every round costs a process
    start, so a single round is enough as a sanity check.
    """
    servers = load_mcp_servers(str(get_mcp_servers_path()))
    only_stdio = all(config.get("transport") == "stdio" for config in servers.values())
    return 1 if only_stdio else 10


ATTEMPTS = attempts()


def first_result(tool_output) -> dict:
    """Return the first entry of `results` in a tool output."""
    text = "".join(block["text"] for block in tool_output if block["type"] == "text")
    results = json.loads(text)["results"]
    assert results, f"empty results: {text[:200]}"
    return results[0]


@pytest.mark.asyncio
async def test_concurrent_tool_calls_are_not_crossed():
    tools = {tool.name: tool for tool in await get_mcp_client().get_tools()}

    # Warm up with a sequential call: on the stdio transport, each tool call
    # starts its own server, and two concurrent `npx` would race to populate the
    # same download cache.
    await tools[TOOL_GEOCODE].ainvoke({"text": "Angoulême"})

    for attempt in range(1, ATTEMPTS + 1):
        try:
            geocode_output, search_output = await asyncio.gather(
                tools[TOOL_GEOCODE].ainvoke({"text": "Angoulême"}),
                tools[TOOL_GPF_SEARCH_TYPES].ainvoke({"query": "bâtiments"}),
            )
        except RuntimeError as exc:
            # The MCP client validates the payload against the output schema of
            # the tool it called, so a crossed answer surfaces as a schema error.
            pytest.fail(
                f"attempt {attempt}/{ATTEMPTS}: concurrent calls crossed, "
                f"see https://github.com/ignfab/geocontext-test/issues/33"
                f"\n{str(exc)[:200]}"
            )

        # A crossing whose payload happens to validate would go unnoticed above.
        assert "lon" in first_result(geocode_output), \
            f"attempt {attempt}/{ATTEMPTS}: {TOOL_GEOCODE} did not answer its own call"
        assert "score" in first_result(search_output), \
            f"attempt {attempt}/{ATTEMPTS}: {TOOL_GPF_SEARCH_TYPES} did not answer its own call"
