# Contributing and Local Development

## Environment Setup

### Prerequisites

- **Python** 3.10+
- **UV** (fast Python package installer): [install UV](https://docs.astral.sh/uv/getting-started/)
- **Node.js** 18+: Required by the MCP server `@ignfab/geocontext`
- **API Keys**: Depending on the LLM provider you want to test

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

### Quick Test with Default Config

Run all tests with the default configuration (remote MCP server via `npx @ignfab/geocontext`):

```bash
# Set your API key
export ANTHROPIC_API_KEY=your_key

# Run all tests
uv run pytest

# Run a specific test
uv run pytest -k test_geocode -v

# Run with verbose logging
# edit LOG_LEVEL in your MCP config, then:
uv run pytest
```

### Testing with Multiple Models

Use the provided test runner to run the same test suite against multiple models defined in a YAML config:

```bash
# Test with all Anthropic models
export ANTHROPIC_API_KEY=your_key
uv run scripts/run_tests.py config/models-anthropic.yaml

# Test with a single model
uv run scripts/run_tests.py config/models-anthropic.yaml --model=claude-haiku-4-5

# List available models without running
uv run scripts/run_tests.py config/models-anthropic.yaml --list
```

Pass additional pytest arguments after `--`:

```bash
uv run scripts/run_tests.py config/models-anthropic.yaml -- -k geocode -x
```

## Testing a Local Version of geocontext

### Setup

If you're developing `@ignfab/geocontext` locally or need to test a custom build, you can configure the test suite to use your local version instead of the published npm package.

#### 1. Build or Prepare Your Local geocontext

```bash
# Clone the geocontext repository (if not already done)
git clone https://github.com/ignfab/geocontext.git /path/to/local/geocontext

# Build it
cd /path/to/local/geocontext
npm install
npm run build

# Or use the development build directly (depending on the project structure)
```

#### 2. Create a Local MCP Configuration

Create a file `config/mcp-servers-local.json` to point to your local build:

```json
{
  "servers": {
    "geocontext": {
      "command": "node",
      "args": ["/path/to/local/geocontext/dist/index.js"],
      "transport": "stdio",
      "env": {}
    }
  }
}
```

**Note:** Replace `/path/to/local/geocontext` with the actual path to your local clone.

Alternatively, if you use `npx` to run a local package:

```json
{
  "servers": {
    "geocontext": {
      "command": "npx",
      "args": ["--yes", "/path/to/local/geocontext"],
      "transport": "stdio",
      "env": {}
    }
  }
}
```

#### 3. Set the MCP_SERVERS_PATH Environment Variable

Point the test suite to your custom configuration:

```bash
export MCP_SERVERS_PATH=/path/to/geocontext-test/config/mcp-servers-local.json
uv run pytest
```

Or pass it to the test runner:

```bash
export ANTHROPIC_API_KEY=your_key
uv run scripts/run_tests.py config/models-anthropic.yaml --mcp-servers-path config/mcp-servers-local.json
```

### Environment Variables

- `MCP_SERVERS_PATH`: Path to a JSON file defining MCP server configurations. If not set, defaults to `config/mcp-servers.json`.
- `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`: Standard proxy variables (automatically injected into the server environment).
- `MODEL_NAME`: LLM provider and model to use (default: `"anthropic:claude-haiku-4-5"`). Format: `provider:model_id`.

### Understanding the Configuration

The MCP server configuration is stored in JSON files with the following structure:

```json
{
  "servers": {
    "geocontext": {
      "command": "npx",
      "args": ["-y", "@ignfab/geocontext"],
      "transport": "stdio",
      "env": {
        "LOG_LEVEL": "error",
        "CUSTOM_VAR": "value"
      }
    }
  }
}
```

**Fields:**
- `command`: The executable to run (e.g., `npx`, `node`, custom executable path)
- `args`: Command-line arguments passed to the executable
- `transport`: Communication protocol with the MCP server (typically `stdio`)
- `env`: Optional environment variables for the server process

**Auto-injected Environment Variables:**
The test harness automatically injects proxy variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY` and lowercase variants).

These override proxy values defined in the JSON `env` section.

## Adding New Tests

### Test Structure

Tests follow this pattern:

```python
from conftest import mcp_agent, mcp_tools

@pytest.mark.asyncio
async def test_my_feature(mcp_agent, mcp_tools):
    """Test description."""
    # Arrange
    input_data = {"question": "What is X?"}
    
    # Act
    result = await mcp_agent.invoke({"messages": [{"role": "user", "content": input_data["question"]}]})
    
    # Assert
    assert "expected_value" in result["output"]
```

**Fixtures provided by `conftest.py`:**
- `mcp_agent`: LangGraph agent with MCP tools, shared across all tests (session-scoped)
- `mcp_tools`: List of available MCP tools, shared across all tests (session-scoped)
- `model`: The LLM model instance (session-scoped)
- `tracker`: Per-test tool call tracker for inspecting which tools were invoked

### Running a Single Test

```bash
uv run pytest -k test_my_feature -v -s
```

The `-s` flag shows print statements and logging output.

## Debugging

### Enable Detailed Logging

```bash
uv run pytest -k test_name -v -s
```

### Inspect Tool Calls

```python
@pytest.mark.asyncio
async def test_example(mcp_agent, tracker):
    result = await mcp_agent.invoke({"messages": [{"role": "user", "content": "..."}]})
    print(f"Tools called: {tracker.tool_calls}")
    assert len(tracker.tool_calls) > 0
```

### Check Available MCP Tools

```bash
python -c "
import asyncio
from conftest import get_mcp_client

async def main():
    client = get_mcp_client()
    tools = await client.get_tools()
    for tool in tools:
        print(f'{tool.name}: {tool.description}')

asyncio.run(main())
"
```

## Further Reading

- [geocontext Documentation](https://github.com/ignfab/geocontext)
- [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters)
- [Pytest Documentation](https://docs.pytest.org/)
