# Test Report

*Report generated on 15-Jul-2026 at 10:19:28 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 354.38 seconds

- 1 failed
- 47 passed

## 1 failed

### test_search_ecoles.py

`test_search_ecoles` 21.86s

```
test_search_ecoles.py:22: in test_search_ecoles
    assert fragment in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: bdtopo_v3:zone_d_activite_ou_d_interet
E   assert 'bdtopo_v3:zone_d_activite_ou_d_interet' in 'content="\\n\\nles informations sur les écoles se trouvent principalement dans la table **bdtopo_v3:erp** (établissements recevant du public).\\n\\ncette table contient des données sur les bâtiments dans lesquels des personnes extérieures sont admises, ce qui inclut les écoles. les propriétés pertinentes pour identifier les écoles sont :\\n- `type_principal` : qui indique la typologie principale de l\'établissement\\n- `activite_principale` : qui décrit l\'activité principale de l\'établissement\\n- `libelle` : la dénomination de l\'établissement\\n\\nles écoles sont classées comme erp (établissements recevant du public) et peuvent être identifiées grâce à ces champs qui précisent leur nature éducative." additional_kwargs={\'refusal\': none} response_metadata={\'token_usage\': {\'completion_tokens\': 249, \'prompt_tokens\': 11460, \'total_tokens\': 11709, \'completion_tokens_details\': none, \'prompt_tokens_details\': none}, \'model_provider\': \'openai\', \'model_name\': \'qwen3-6-35b-moe\', \'system_fingerprint\': \'vllm-0.22.0-057a257e\', \'id\': \'chatcmpl-bbff17fa03f8161c\', \'finish_reason\': \'stop\', \'logprobs\': none} id=\'lc_run--019f64db-715b-7810-9519-76871f2a3860-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 11460, \'output_tokens\': 249, \'total_tokens\': 11709, \'input_token_details\': {}, \'output_token_details\': {}}'
```

## 47 passed

### test_adminexpress.py

`test_adminexpress` 5.90s

### test_altitude.py

`test_altitude` 4.13s

### test_assiette_sup.py

`test_assiette_sup` 17.12s

### test_cadastre.py

`test_cadastre` 8.19s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 52.03s

### test_chaining_discovery.py

`test_chaining_discovery` 11.46s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 10.06s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 8.23s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 13.05s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 19.91s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 17.41s

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 77.34s

### test_describe_type.py

`test_describe_type` 7.14s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 2.05s

### test_geocode.py

`test_geocode` 5.38s

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 3.84s

### test_get_feature_by_id.py

`test_get_feature_by_id` 4.31s

### test_get_features.py

`test_get_features` 22.99s

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

`test_search_batiment` 5.90s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 34.09s
