"""Tests for the helpers module."""

import json
import os
from pathlib import Path

import pytest

from langchain_core.messages import AIMessage, HumanMessage

from helpers import extract_numbers, get_json_from_url, get_mcp_servers_path, load_mcp_servers, slugify, write_agent_trace


class TestExtractNumbers:
    """Test suite for extract_numbers utility function."""

    def test_extract_integers(self):
        """Test extracting simple integers."""
        result = extract_numbers("Found 5 items and 10 objects")
        assert result == [5.0, 10.0]

    def test_extract_floats(self):
        """Test extracting floating-point numbers."""
        result = extract_numbers("Latitude 48.85 and longitude 2.35")
        assert result == [48.85, 2.35]

    def test_extract_mixed_numbers(self):
        """Test extracting mixed integers and floats."""
        result = extract_numbers("Point at 45, 6.87, elevation 1000.5")
        assert result == [45.0, 6.87, 1000.5]

    def test_no_numbers(self):
        """Test with text containing no numbers."""
        result = extract_numbers("No numbers here")
        assert result == []

    def test_empty_string(self):
        """Test with empty string."""
        result = extract_numbers("")
        assert result == []


class TestGetJsonFromUrl:
    """Test suite for get_json_from_url."""

    def test_download_json(self, tmp_path):
        """Test that the JSON served by the URL is returned."""
        feature_collection = {"type": "FeatureCollection", "features": []}
        layer_file = tmp_path / "layer.json"
        layer_file.write_text(json.dumps(feature_collection))
        assert get_json_from_url(layer_file.as_uri()) == feature_collection


class TestGetMcpServersPath:
    """Test suite for get_mcp_servers_path path resolution function."""

    def test_explicit_path(self):
        """Test with explicit path argument."""
        path = get_mcp_servers_path("/custom/path/config.json")
        assert path == Path("/custom/path/config.json")

    def test_env_var_path(self):
        """Test with MCP_SERVERS_PATH environment variable."""
        old_val = os.environ.get("MCP_SERVERS_PATH")
        try:
            os.environ["MCP_SERVERS_PATH"] = "/env/path/config.json"
            path = get_mcp_servers_path()
            assert path == Path("/env/path/config.json")
        finally:
            if old_val is not None:
                os.environ["MCP_SERVERS_PATH"] = old_val
            else:
                os.environ.pop("MCP_SERVERS_PATH", None)

    def test_default_path(self):
        """Test with default path (no arg, no env var)."""
        old_val = os.environ.pop("MCP_SERVERS_PATH", None)
        try:
            path = get_mcp_servers_path()
            # Should be config/mcp-servers.json relative to repo root
            assert path.name == "mcp-servers.json"
            assert path.parent.name == "config"
        finally:
            if old_val is not None:
                os.environ["MCP_SERVERS_PATH"] = old_val

    def test_explicit_overrides_env(self):
        """Test that explicit path overrides environment variable."""
        old_val = os.environ.get("MCP_SERVERS_PATH")
        try:
            os.environ["MCP_SERVERS_PATH"] = "/env/path/config.json"
            path = get_mcp_servers_path("/explicit/path/config.json")
            assert path == Path("/explicit/path/config.json")
        finally:
            if old_val is not None:
                os.environ["MCP_SERVERS_PATH"] = old_val
            else:
                os.environ.pop("MCP_SERVERS_PATH", None)

    def test_env_overrides_default(self):
        """Test that environment variable overrides default."""
        old_val = os.environ.get("MCP_SERVERS_PATH")
        try:
            os.environ["MCP_SERVERS_PATH"] = "/env/config.json"
            path = get_mcp_servers_path()
            assert path == Path("/env/config.json")
        finally:
            if old_val is not None:
                os.environ["MCP_SERVERS_PATH"] = old_val
            else:
                os.environ.pop("MCP_SERVERS_PATH", None)


class TestLoadMcpServers:
    """Test suite for load_mcp_servers configuration loader."""

    def test_load_valid_config(self, tmp_path):
        """Test loading a valid configuration."""
        config_file = tmp_path / "valid-config.json"
        config_file.write_text(json.dumps({
            "servers": {
                "geocontext": {
                    "command": "npx",
                    "args": ["-y", "@ignfab/geocontext"],
                    "transport": "stdio",
                    "env": {}
                }
            }
        }))
        
        config = load_mcp_servers(str(config_file))
        
        assert "geocontext" in config
        assert config["geocontext"]["command"] == "npx"
        assert "LOG_LEVEL" not in config["geocontext"]["env"]

    def test_load_default_config(self):
        """Test loading the default config/mcp-servers.json."""
        path = get_mcp_servers_path()
        config = load_mcp_servers(str(path))
        
        assert "geocontext" in config
        geocontext = config["geocontext"]
        assert geocontext["transport"] in ["stdio", "http"]
        if geocontext["transport"] == "stdio":
            assert geocontext["command"] == "npx"
        else:
            assert geocontext["url"].startswith("http")

    def test_load_http_transport_config(self):
        """Test loading an HTTP transport config with URL."""
        path = Path(__file__).resolve().parent / "config" / "mcp-servers-http.json"
        config = load_mcp_servers(str(path))

        assert "geocontext" in config
        geocontext = config["geocontext"]
        assert geocontext["transport"] == "http"
        assert geocontext["url"] == "https://geollm.beta.ign.fr/geocontext/mcp"
        assert "env" not in geocontext

    def test_file_not_found(self):
        """Test that FileNotFoundError is raised for non-existent file."""
        with pytest.raises(FileNotFoundError, match="MCP servers config not found"):
            load_mcp_servers("/nonexistent/path/config.json")

    def test_invalid_json(self, tmp_path):
        """Test that ValueError is raised for invalid JSON."""
        config_file = tmp_path / "invalid.json"
        config_file.write_text("{ invalid json }")
        
        with pytest.raises(ValueError, match="Invalid JSON"):
            load_mcp_servers(str(config_file))

    def test_missing_servers_key(self, tmp_path):
        """Test that ValueError is raised when 'servers' key is missing."""
        config_file = tmp_path / "no-servers.json"
        config_file.write_text(json.dumps({"other_key": {}}))
        
        with pytest.raises(ValueError, match="must contain a 'servers' key"):
            load_mcp_servers(str(config_file))

    def test_servers_not_dict(self, tmp_path):
        """Test that ValueError is raised when 'servers' is not a dict."""
        config_file = tmp_path / "servers-not-dict.json"
        config_file.write_text(json.dumps({"servers": ["item1", "item2"]}))
        
        with pytest.raises(ValueError, match="must be a non-empty dict"):
            load_mcp_servers(str(config_file))

    def test_empty_servers(self, tmp_path):
        """Test that ValueError is raised when 'servers' is empty."""
        config_file = tmp_path / "empty-servers.json"
        config_file.write_text(json.dumps({"servers": {}}))
        
        with pytest.raises(ValueError, match="must be a non-empty dict"):
            load_mcp_servers(str(config_file))

    def test_server_config_not_dict(self, tmp_path):
        """Test that ValueError is raised when a server config is not a dict."""
        config_file = tmp_path / "invalid-server-config.json"
        config_file.write_text(json.dumps({"servers": {"test": "not a dict"}}))
        
        with pytest.raises(ValueError, match="config must be a dict"):
            load_mcp_servers(str(config_file))

    def test_http_transport_requires_url(self, tmp_path):
        """Test that HTTP transport rejects missing URL."""
        config_file = tmp_path / "http-missing-url.json"
        config_file.write_text(json.dumps({
            "servers": {
                "geocontext": {
                    "transport": "http"
                }
            }
        }))

        with pytest.raises(ValueError, match="requires a non-empty 'url'"):
            load_mcp_servers(str(config_file))

    def test_stdio_transport_requires_command(self, tmp_path):
        """Test that stdio transport rejects missing command."""
        config_file = tmp_path / "stdio-missing-command.json"
        config_file.write_text(json.dumps({
            "servers": {
                "geocontext": {
                    "transport": "stdio",
                    "args": ["-y", "@ignfab/geocontext"]
                }
            }
        }))

        with pytest.raises(ValueError, match="requires a non-empty 'command'"):
            load_mcp_servers(str(config_file))

    def test_invalid_transport(self, tmp_path):
        """Test that invalid transport values are rejected."""
        config_file = tmp_path / "invalid-transport.json"
        config_file.write_text(json.dumps({
            "servers": {
                "geocontext": {
                    "transport": "ws",
                    "url": "https://example.com/mcp"
                }
            }
        }))

        with pytest.raises(ValueError, match="transport must be one of"):
            load_mcp_servers(str(config_file))

    def test_proxy_variables_injected(self, tmp_path):
        """Test that proxy environment variables are injected."""
        config_file = tmp_path / "proxy-test.json"
        config_file.write_text(json.dumps({
            "servers": {
                "test": {
                    "command": "echo",
                    "args": [],
                    "transport": "stdio",
                    "env": {}
                }
            }
        }))
        
        old_http = os.environ.get("HTTP_PROXY")
        old_https = os.environ.get("HTTPS_PROXY")
        
        try:
            os.environ["HTTP_PROXY"] = "http://proxy.example.com:8080"
            os.environ["HTTPS_PROXY"] = "https://proxy.example.com:8080"
            
            config = load_mcp_servers(str(config_file))
            
            assert config["test"]["env"]["HTTP_PROXY"] == "http://proxy.example.com:8080"
            assert config["test"]["env"]["HTTPS_PROXY"] == "https://proxy.example.com:8080"
        finally:
            for var, val in [("HTTP_PROXY", old_http), ("HTTPS_PROXY", old_https)]:
                if val is not None:
                    os.environ[var] = val
                else:
                    os.environ.pop(var, None)

    def test_existing_env_is_preserved(self, tmp_path):
        """Test that env from JSON is preserved when no proxy override exists."""
        config_file = tmp_path / "env-test.json"
        config_file.write_text(json.dumps({
            "servers": {
                "test": {
                    "command": "echo",
                    "args": [],
                    "transport": "stdio",
                    "env": {
                        "LOG_LEVEL": "debug"
                    }
                }
            }
        }))

        config = load_mcp_servers(str(config_file))
        assert config["test"]["env"]["LOG_LEVEL"] == "debug"

    def test_runtime_env_overrides_json_env(self, tmp_path):
        """Test that runtime proxy variables override JSON env values."""
        config_file = tmp_path / "override-test.json"
        config_file.write_text(json.dumps({
            "servers": {
                "test": {
                    "command": "echo",
                    "args": [],
                    "transport": "stdio",
                    "env": {"HTTP_PROXY": "http://json-proxy.example.com:8080"}
                }
            }
        }))
        
        old_http = os.environ.get("HTTP_PROXY")
        
        try:
            os.environ["HTTP_PROXY"] = "http://runtime-proxy.example.com:9999"
            config = load_mcp_servers(str(config_file))
            assert config["test"]["env"]["HTTP_PROXY"] == "http://runtime-proxy.example.com:9999"
        finally:
            if old_http is not None:
                os.environ["HTTP_PROXY"] = old_http
            else:
                os.environ.pop("HTTP_PROXY", None)

    def test_multiple_servers(self, tmp_path):
        """Test loading configuration with multiple servers."""
        config_file = tmp_path / "multi-server.json"
        config_file.write_text(json.dumps({
            "servers": {
                "server1": {
                    "command": "cmd1",
                    "args": [],
                    "transport": "stdio",
                    "env": {}
                },
                "server2": {
                    "command": "cmd2",
                    "args": [],
                    "transport": "stdio",
                    "env": {}
                }
            }
        }))
        
        config = load_mcp_servers(str(config_file))
        
        assert "server1" in config
        assert "server2" in config
        assert config["server1"]["command"] == "cmd1"
        assert config["server2"]["command"] == "cmd2"
        assert "LOG_LEVEL" not in config["server1"]["env"]
        assert "LOG_LEVEL" not in config["server2"]["env"]
        
        old_http = os.environ.get("HTTP_PROXY")
        
        try:
            os.environ["HTTP_PROXY"] = "http://runtime-proxy.example.com:9999"
            config = load_mcp_servers(str(config_file))
            
            # Runtime should override
            assert config["test"]["env"]["HTTP_PROXY"] == "http://runtime-proxy.example.com:9999"
        finally:
            if old_http is not None:
                os.environ["HTTP_PROXY"] = old_http
            else:
                os.environ.pop("HTTP_PROXY", None)

    def test_file_not_found(self, tmp_path):
        """Test that FileNotFoundError is raised for non-existent config."""
        non_existent = tmp_path / "does-not-exist.json"
        
        with pytest.raises(FileNotFoundError, match="MCP servers config not found"):
            load_mcp_servers(str(non_existent))

    def test_invalid_json(self, tmp_path):
        """Test that ValueError is raised for invalid JSON."""
        config_file = tmp_path / "invalid.json"
        config_file.write_text("{ invalid json }")
        
        with pytest.raises(ValueError, match="Invalid JSON"):
            load_mcp_servers(str(config_file))

    def test_missing_servers_key(self, tmp_path):
        """Test that ValueError is raised when 'servers' key is missing."""
        config_file = tmp_path / "no-servers.json"
        config_file.write_text(json.dumps({"other_key": {}}))
        
        with pytest.raises(ValueError, match="must contain a 'servers' key"):
            load_mcp_servers(str(config_file))

    def test_servers_not_dict(self, tmp_path):
        """Test that ValueError is raised when 'servers' is not a dict."""
        config_file = tmp_path / "servers-not-dict.json"
        config_file.write_text(json.dumps({"servers": ["item1", "item2"]}))
        
        with pytest.raises(ValueError, match="'servers' .* must be a non-empty dict"):
            load_mcp_servers(str(config_file))

    def test_empty_servers(self, tmp_path):
        """Test that ValueError is raised when 'servers' is empty."""
        config_file = tmp_path / "empty-servers.json"
        config_file.write_text(json.dumps({"servers": {}}))
        
        with pytest.raises(ValueError, match="'servers' .* must be a non-empty dict"):
            load_mcp_servers(str(config_file))

    def test_server_config_not_dict(self, tmp_path):
        """Test that ValueError is raised when a server config is not a dict."""
        config_file = tmp_path / "invalid-server-config.json"
        config_file.write_text(json.dumps({
            "servers": {
                "test": "not a dict"
            }
        }))
        
        with pytest.raises(ValueError, match="Server 'test' config must be a dict"):
            load_mcp_servers(str(config_file))

    def test_multiple_servers(self, tmp_path):
        """Test loading config with multiple servers."""
        config_file = tmp_path / "multi-server.json"
        config_file.write_text(json.dumps({
            "servers": {
                "server1": {
                    "command": "cmd1",
                    "args": [],
                    "transport": "stdio",
                    "env": {}
                },
                "server2": {
                    "command": "cmd2",
                    "args": [],
                    "transport": "stdio",
                    "env": {}
                }
            }
        }))
        
        config = load_mcp_servers(str(config_file))
        
        assert "server1" in config
        assert "server2" in config
        assert config["server1"]["command"] == "cmd1"
        assert config["server2"]["command"] == "cmd2"


class TestSlugify:
    """Test suite for slugify file name helper."""

    def test_drops_provider_prefix(self):
        """Test that the provider prefix is removed."""
        assert slugify("anthropic:claude-haiku-4-5") == "claude-haiku-4-5"

    def test_replaces_remaining_separators(self):
        """Test with a model name containing an extra colon."""
        assert slugify("ollama:qwen3.5:4b") == "qwen3.5-4b"

    def test_without_prefix(self):
        """Test that a plain name is left untouched."""
        assert slugify("test_geocode") == "test_geocode"


class TestWriteAgentTrace:
    """Test suite for write_agent_trace."""

    def test_write_trace(self, tmp_path):
        """Test that the conversation is written to <reports>/<model>/<test>.txt."""
        results = [{"messages": [HumanMessage(content="Question"), AIMessage(content="Réponse")]}]

        path = write_agent_trace("anthropic:claude-haiku-4-5", "test_geocode", results,
                                 status="failed", reports_dir=tmp_path)

        assert path == tmp_path / "claude-haiku-4-5" / "test_geocode.txt"
        content = path.read_text(encoding="utf-8")
        assert "# model  : anthropic:claude-haiku-4-5" in content
        assert "# status : failed" in content
        assert "Question" in content
        assert "Réponse" in content

    def test_no_result_writes_nothing(self, tmp_path):
        """Test that nothing is written when the agent was never invoked."""
        assert write_agent_trace("anthropic:claude-haiku-4-5", "test_geocode", [], reports_dir=tmp_path) is None
        assert list(tmp_path.iterdir()) == []
