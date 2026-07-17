# Test Report

*Report generated on 16-Jul-2026 at 13:41:22 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 113.58 seconds

- 1 failed
- 47 passed

## 1 failed

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 8.63s

```
test_count_batiment_saint_mande.py:31: in test_count_batiment_saint_mande
    assert tool_name in tool_names_called, f"{tool_name} tool was not called"
E   AssertionError: gpf_wfs_describe_type tool was not called
E   assert 'gpf_wfs_describe_type' in {'adminexpress', 'geocode', 'gpf_wfs_get_features', 'gpf_wfs_search_types'}
```

## 47 passed

### test_adminexpress.py

`test_adminexpress` 2.71s

### test_altitude.py

`test_altitude` 3.24s

### test_assiette_sup.py

`test_assiette_sup` 4.47s

### test_cadastre.py

`test_cadastre` 5.71s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 5.36s

### test_chaining_discovery.py

`test_chaining_discovery` 9.91s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 4.90s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 4.40s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 5.65s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 13.13s

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 9.72s

### test_describe_type.py

`test_describe_type` 3.72s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.48s

### test_geocode.py

`test_geocode` 2.56s

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 2.47s

### test_get_feature_by_id.py

`test_get_feature_by_id` 3.86s

### test_get_features.py

`test_get_features` 7.02s

### test_helpers.py

`TestExtractNumbers.test_extract_integers` 0.00s

`TestExtractNumbers.test_extract_floats` 0.00s

`TestExtractNumbers.test_extract_mixed_numbers` 0.00s

`TestExtractNumbers.test_no_numbers` 0.00s

`TestExtractNumbers.test_empty_string` 0.00s

`TestGetMcpServersPath.test_explicit_path` 0.00s

`TestGetMcpServersPath.test_env_var_path` 0.00s

`TestGetMcpServersPath.test_default_path` 0.00s

`TestGetMcpServersPath.test_explicit_overrides_env` 0.00s

`TestGetMcpServersPath.test_env_overrides_default` 0.00s

`TestLoadMcpServers.test_load_valid_config` 0.00s

`TestLoadMcpServers.test_load_default_config` 0.00s

`TestLoadMcpServers.test_load_http_transport_config` 0.00s

`TestLoadMcpServers.test_file_not_found` 0.00s

`TestLoadMcpServers.test_invalid_json` 0.00s

`TestLoadMcpServers.test_missing_servers_key` 0.00s

`TestLoadMcpServers.test_servers_not_dict` 0.00s

`TestLoadMcpServers.test_empty_servers` 0.00s

`TestLoadMcpServers.test_server_config_not_dict` 0.00s

`TestLoadMcpServers.test_http_transport_requires_url` 0.00s

`TestLoadMcpServers.test_stdio_transport_requires_command` 0.00s

`TestLoadMcpServers.test_invalid_transport` 0.00s

`TestLoadMcpServers.test_proxy_variables_injected` 0.00s

`TestLoadMcpServers.test_existing_env_is_preserved` 0.00s

`TestLoadMcpServers.test_runtime_env_overrides_json_env` 0.00s

`TestLoadMcpServers.test_multiple_servers` 0.00s

### test_search_batiment.py

`test_search_batiment` 3.26s

### test_search_ecoles.py

`test_search_ecoles` 4.81s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 5.02s
