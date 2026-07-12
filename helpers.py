import json
import os
import re
from pathlib import Path


def extract_numbers(text: str) -> list[float]:
    return [float(match) for match in re.findall(r"\d+(?:\.\d+)?", text)]


def get_mcp_servers_path(path: str | None = None) -> Path:
    """Resolve the path to MCP servers configuration file.
    
    Resolution order:
    1. Explicit path argument
    2. MCP_SERVERS_PATH environment variable
    3. Default path: config/mcp-servers.json (relative to repository root)
    
    Args:
        path: Optional explicit path to config file.
    
    Returns:
        Resolved Path object.
    """
    if path is not None:
        return Path(path)
    
    path = os.getenv("MCP_SERVERS_PATH")
    if path is not None:
        return Path(path)
    
    # Default: config/mcp-servers.json relative to repository root
    repo_root = Path(__file__).resolve().parent
    return repo_root / "config" / "mcp-servers.json"


def load_mcp_servers(path: str) -> dict:
    """Load and prepare MCP servers configuration.
    
    Loads a JSON config file and injects proxy environment variables.
    
    Args:
        path: Path to MCP servers configuration JSON file.
              Must contain a 'servers' key with server definitions.
    
    Returns:
        Dict suitable for MultiServerMCPClient with injected environment.
    
    Raises:
        FileNotFoundError: if config file not found
        ValueError: if invalid JSON, missing 'servers' key, or invalid structure
    """
    config_path = Path(path)
    
    # Load and parse JSON
    try:
        config_text = config_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"MCP servers config not found: {config_path}")
    
    try:
        config = json.loads(config_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {config_path}: {e}")
    
    # Extract and validate servers
    if not isinstance(config, dict) or "servers" not in config:
        raise ValueError(f"Config {config_path} must contain a 'servers' key with server definitions")
    
    servers = config.get("servers")
    if not isinstance(servers, dict) or not servers:
        raise ValueError(f"'servers' in {config_path} must be a non-empty dict")
    
    # Prepare proxy environment variables
    env = os.environ.copy()
    proxy_vars = ["HTTP_PROXY", "HTTPS_PROXY", "NO_PROXY", "http_proxy", "https_proxy", "no_proxy"]
    proxy_env = {var: env[var] for var in proxy_vars if var in env}
    
    # Ensure uppercase variants are set (needed by Node.js libraries)
    if "HTTP_PROXY" not in proxy_env and "http_proxy" in proxy_env:
        proxy_env["HTTP_PROXY"] = proxy_env["http_proxy"]
    if "HTTPS_PROXY" not in proxy_env and "https_proxy" in proxy_env:
        proxy_env["HTTPS_PROXY"] = proxy_env["https_proxy"]
    if "NO_PROXY" not in proxy_env and "no_proxy" in proxy_env:
        proxy_env["NO_PROXY"] = proxy_env["no_proxy"]
    
    # Inject environment into each server
    server_env = proxy_env
    
    result = {}
    allowed_transports = {"stdio", "http"}

    for server_name, server_config in servers.items():
        if not isinstance(server_config, dict):
            raise ValueError(f"Server '{server_name}' config must be a dict")

        transport = server_config.get("transport")
        if not isinstance(transport, str) or transport not in allowed_transports:
            raise ValueError(
                f"Server '{server_name}' transport must be one of {sorted(allowed_transports)}"
            )

        if transport == "stdio":
            command = server_config.get("command")
            if not isinstance(command, str) or not command.strip():
                raise ValueError(f"Server '{server_name}' with transport 'stdio' requires a non-empty 'command'")
        elif transport == "http":
            url = server_config.get("url")
            if not isinstance(url, str) or not url.strip():
                raise ValueError(f"Server '{server_name}' with transport 'http' requires a non-empty 'url'")

        # Copy server config and merge env only for stdio transport.
        # HTTP transport does not accept an `env` field in langchain_mcp_adapters.
        merged = server_config.copy()
        if transport == "stdio":
            if "env" in merged and not isinstance(merged["env"], dict):
                raise ValueError(f"Server '{server_name}' env must be a dict when provided")
            if "env" in merged and isinstance(merged["env"], dict):
                # Merge: runtime env overrides JSON env
                merged["env"] = {**merged["env"], **server_env}
            else:
                merged["env"] = server_env
        else:
            # Drop env for HTTP transport to avoid unsupported kwarg errors.
            merged.pop("env", None)
        
        result[server_name] = merged
    
    return result
