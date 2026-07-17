# Test Report

*Report generated on 16-Jul-2026 at 13:30:48 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 401.45 seconds

- 2 failed
- 46 passed

## 2 failed

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 138.95s

```
test_count_lycees_2km_chateau_vincennes.py:29: in test_count_lycees_2km_chateau_vincennes
    assert tool_name in tool_names_called, f"{tool_name} tool was not called"
E   AssertionError: gpf_wfs_describe_type tool was not called
E   assert 'gpf_wfs_describe_type' in {'geocode', 'gpf_wfs_search_types'}
```

### test_search_ecoles.py

`test_search_ecoles` 12.83s

```
test_search_ecoles.py:22: in test_search_ecoles
    assert fragment in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: bdtopo_v3:zone_d_activite_ou_d_interet
E   assert 'bdtopo_v3:zone_d_activite_ou_d_interet' in 'content=\'d\\\'après les recherches effectuées, il n\\\'existe pas de table nommée explicitement "écoles". cependant, vous pouvez trouver des informations relatives aux écoles dans les tables suivantes selon votre besoin :\\n\\n1.  **`bdtopo_v3:erp` (établissements recevant du public)** : les écoles étant des lieux accueillant du public, elles sont répertoriées dans cette table qui concerne les bâtiments ouverts aux personnes extérieures.\\n2.  **`bdtopo_v3:batiment`** : cette table contient l\\\'ensemble des constructions au-dessus du sol. vous pourriez y trouver les bâtiments scolaires, bien qu\\\'il faille probablement filtrer par usage ou type de bâtiment.\\n\\nsi vous recherchez des informations plus spécifiques (comme le nom de l\\\'établissement ou son type), je vous recommande d\\\'explorer la table **`bdtopo_v3:erp`** en premier.\' additional_kwargs={\'refusal\': none} response_metadata={\'token_usage\': {\'completion_tokens\': 201, \'prompt_tokens\': 6260, \'total_tokens\': 6461, \'completion_tokens_details\': none, \'prompt_tokens_details\': none}, \'model_provider\': \'openai\', \'model_name\': \'gemma4-26b-moe\', \'system_fingerprint\': \'vllm-0.23.0-fc919ceb\', \'id\': \'chatcmpl-8859317b5359628d\', \'finish_reason\': \'stop\', \'logprobs\': none} id=\'lc_run--019f6ab1-33f0-7260-b07b-2df2683f405e-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 6260, \'output_tokens\': 201, \'total_tokens\': 6461, \'input_token_details\': {}, \'output_token_details\': {}}'
```

## 46 passed

### test_adminexpress.py

`test_adminexpress` 5.42s

### test_altitude.py

`test_altitude` 3.65s

### test_assiette_sup.py

`test_assiette_sup` 49.73s

### test_cadastre.py

`test_cadastre` 8.20s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 18.19s

### test_chaining_discovery.py

`test_chaining_discovery` 17.34s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 8.34s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 6.69s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 23.62s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 17.95s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 20.09s

### test_describe_type.py

`test_describe_type` 17.52s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.65s

### test_geocode.py

`test_geocode` 3.47s

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 3.15s

### test_get_feature_by_id.py

`test_get_feature_by_id` 4.65s

### test_get_features.py

`test_get_features` 16.17s

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

`test_search_batiment` 5.70s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 16.81s
