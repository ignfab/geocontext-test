# Contributing and Local Development

## Requirements

- **UV** (fast Python package installer): [install UV](https://docs.astral.sh/uv/getting-started/)
- **Node.js** 18+: Required by the MCP server `@ignfab/geocontext`
- **API Keys**: Depending on the LLM provider you want to test

## Configuration

### API Keys

Set environment variables for the LLM providers you want to test:

```bash
# For Anthropic models
export ANTHROPIC_API_KEY=your_key_here

# For Google GenAI models
export GOOGLE_API_KEY=your_key_here

# For Onyxia LLM (sspcloud service)
export ONYXIA_API_KEY=your_key_here
```

### Proxy Configuration

If you're behind a proxy, set the standard proxy variables:

```bash
export HTTP_PROXY=http://proxy-host:port
export HTTPS_PROXY=http://proxy-host:port
export NO_PROXY=localhost,127.0.0.1
```

These are automatically injected into the MCP server environment.

## Running Tests

### Testing with a Single Model

Run all tests with the default MCP configuration [config/mcp-servers.json](config/mcp-servers.json) :

```bash
# Set model name (defaulted to claude-haiku-4-5)
export MODEL_NAME="anthropic:claude-haiku-4-5"
# Set your API key
export ANTHROPIC_API_KEY=your_key

# Run all tests
uv run pytest

# Run a specific test
uv run pytest -k test_geocode -v

# Run with verbose logging
# edit LOG_LEVEL in your MCP config, then:
uv run pytest

# Run test_mcp_concurrency.py, skipped by default until #33 is fixed
SKIP_TEST_MCP_CONCURRENCY=0 uv run pytest test_mcp_concurrency.py -v

# Run test_count_batiment_vendee.py, skipped by default until #42 is fixed
GEOCONTEXT_DEV=1 SKIP_TEST_COUNT_BATIMENT_VENDEE=0 uv run pytest test_count_batiment_vendee.py -v
```

### Inspecting the Agent Conversations

Each test using the `mcp_agent` fixture writes its conversation to
`reports/<model>/<test name>.txt`, whether the test passed or failed:

```bash
export MODEL_NAME="anthropic:claude-haiku-4-5"
uv run pytest -k test_geocode

cat reports/claude-haiku-4-5/test_geocode.txt
```

```
# model  : anthropic:claude-haiku-4-5
# test   : test_geocode
# status : passed
================================ Human Message ================================
...
```

These traces are not versioned (see [.gitignore](.gitignore)); they are meant to debug what a
model actually did (tool calls, arguments, answers).

### Testing with Multiple Models

Use the provided test runner ([scripts/run_tests.py](scripts/run_tests.py)) to run the same test suite against multiple models defined in a YAML config:

```bash
# Test with all Anthropic models
export ANTHROPIC_API_KEY=your_key
uv run scripts/run_tests.py config/models-anthropic.yaml

# Test with a single model
uv run scripts/run_tests.py config/models-anthropic.yaml --model=claude-haiku-4-5

# List available models without running
uv run scripts/run_tests.py config/models-anthropic.yaml --list
```

## Testing a Local Version of geocontext

For testing the latest development version with HTTP transport:

**Terminal 1** (in geocontext repository):

```bash
TRANSPORT_TYPE=http npm run start
```

**Terminal 2** (in geocontext-test repository):

```bash
GEOCONTEXT_DEV=1 MCP_SERVERS_PATH=config/mcp-servers-dev.json uv run pytest test_tools_discovery.py
```

Or run all tests:

```bash
GEOCONTEXT_DEV=1 MCP_SERVERS_PATH=config/mcp-servers-dev.json uv run pytest
```


## Further Reading

- [geocontext Documentation](https://github.com/ignfab/geocontext)
- [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters)
- [Pytest Documentation](https://docs.pytest.org/)
