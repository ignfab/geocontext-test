# Test Report

*Report generated on 17-Jul-2026 at 10:45:09 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 557.22 seconds

- 2 failed
- 46 passed

## 2 failed

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 175.26s

```
test_count_lycees_2km_chateau_vincennes.py:35: in test_count_lycees_2km_chateau_vincennes
    assert fragment.lower() in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: 14
E   assert '14' in 'content="\\n\\nd\'après mes recherches, j\'ai identifié les lycées situés à proximité du château de vincennes (coordonnées : 2.435792, 48.842681).\\n\\nen calculant les distances approximatives, **3 lycées** sont situés à moins de 2 km du château de vincennes :\\n\\n1. **lycée hector berlioz** (vincennes) - environ 736 m\\n2. **lycée gregor mendel** (vincennes) - environ 918 m  \\n3. **lycée saint-michel de picpus** (saint-mandé) - environ 1 334 m\\n\\nles autres lycées identifiés dans les communes voisines (nogent-sur-marne, le perreux-sur-marne) se situent au-delà de 2 km du château de vincennes.\\n\\n**réponse : il y a 3 lycées situés à 2 km du château de vincennes.**" additional_kwargs={\'refusal\': none} response_metadata={\'token_usage\': {\'completion_tokens\': 2595, \'prompt_tokens\': 27176, \'total_tokens\': 29771, \'completion_tokens_details\': none, \'prompt_tokens_details\': none}, \'model_provider\': \'openai\', \'model_name\': \'qwen3-6-35b-moe\', \'system_fingerprint\': \'vllm-0.22.0-057a257e\', \'id\': \'chatcmpl-a4a61db7425ac17f\', \'finish_reason\': \'stop\', \'logprobs\': none} id=\'lc_run--019f6f3c-9f83-7511-a9f7-34b0021ecf69-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 27176, \'output_tokens\': 2595, \'total_tokens\': 29771, \'input_token_details\': {}, \'output_token_details\': {}}'
E    +  where '14' = <built-in method lower of str object at 0x7959de5c2820>()
E    +    where <built-in method lower of str object at 0x7959de5c2820> = '14'.lower
```

### test_search_ecoles.py

`test_search_ecoles` 32.97s

```
test_search_ecoles.py:22: in test_search_ecoles
    assert fragment in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: bdtopo_v3:zone_d_activite_ou_d_interet
E   assert 'bdtopo_v3:zone_d_activite_ou_d_interet' in 'content="\\n\\nil n\'existe pas de table spécifique dédiée uniquement aux écoles dans les données géospatiales disponibles. cependant, les écoles peuvent être trouvées dans les tables suivantes :\\n\\n1. **bdtopo_v3:erp** (établissements recevant du public) - c\'est la table la plus pertinente pour trouver des écoles. les écoles sont classées comme erp et peuvent être identifiées via les propriétés `type_principal` ou `activite_principale` qui indiquent leur fonction éducative.\\n\\n2. **bdtopo_v3:batiment** - contient les bâtiments en général, mais sans information sur leur usage spécifique (donc pas possible de filtrer uniquement les écoles).\\n\\nla table **bdtopo_v3:erp** est donc la plus adaptée pour trouver des informations sur les écoles, car elle contient des données sur les établissements recevant du public avec des informations sur leur activité principale et leur type." additional_kwargs={\'refusal\': none} response_metadata={\'token_usage\': {\'completion_tokens\': 457, \'prompt_tokens\': 18795, \'total_tokens\': 19252, \'completion_tokens_details\': none, \'prompt_tokens_details\': none}, \'model_provider\': \'openai\', \'model_name\': \'qwen3-6-35b-moe\', \'system_fingerprint\': \'vllm-0.22.0-057a257e\', \'id\': \'chatcmpl-9aa497195351ac77\', \'finish_reason\': \'stop\', \'logprobs\': none} id=\'lc_run--019f6f3f-0662-7640-a6a4-798aee41bf32-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 18795, \'output_tokens\': 457, \'total_tokens\': 19252, \'input_token_details\': {}, \'output_token_details\': {}}'
```

## 46 passed

### test_adminexpress.py

`test_adminexpress` 5.35s

### test_altitude.py

`test_altitude` 3.88s

### test_assiette_sup.py

`test_assiette_sup` 18.26s

### test_cadastre.py

`test_cadastre` 8.61s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 48.49s

### test_chaining_discovery.py

`test_chaining_discovery` 11.53s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 8.80s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 6.29s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 12.84s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 17.87s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 15.74s

### test_describe_type.py

`test_describe_type` 7.61s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.96s

### test_geocode.py

`test_geocode` 4.61s

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 3.89s

### test_get_feature_by_id.py

`test_get_feature_by_id` 4.31s

### test_get_features.py

`test_get_features` 82.01s

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

`test_search_batiment` 8.76s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 76.69s
