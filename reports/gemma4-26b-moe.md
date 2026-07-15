# Test Report

*Report generated on 15-Jul-2026 at 10:13:30 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 396.39 seconds

- 2 failed
- 46 passed

## 2 failed

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 59.28s

```
test_count_lycees_2km_chateau_vincennes.py:35: in test_count_lycees_2km_chateau_vincennes
    assert fragment.lower() in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: 14
E   assert '14' in 'content=\'je n\\\'ai pas pu trouver de lycées répertoriés dans la base de données des établissements recevant du public (erp) à moins de 2 km du château de vincennes. \\n\\nil est possible que ces établissements ne soient pas classés sous le type "enseignement" ou "lycée" dans cette base spécifique, ou qu\\\'ils ne soient pas enregistrés comme erp dans les données consultées.\' additional_kwargs={\'refusal\': none} response_metadata={\'token_usage\': {\'completion_tokens\': 91, \'prompt_tokens\': 12583, \'total_tokens\': 12674, \'completion_tokens_details\': none, \'prompt_tokens_details\': none}, \'model_provider\': \'openai\', \'model_name\': \'gemma4-26b-moe\', \'system_fingerprint\': \'vllm-0.23.0-fc919ceb\', \'id\': \'chatcmpl-b0af91a363ad1cef\', \'finish_reason\': \'stop\', \'logprobs\': none} id=\'lc_run--019f64d4-c831-7412-b6f7-0aefe38b7fc0-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 12583, \'output_tokens\': 91, \'total_tokens\': 12674, \'input_token_details\': {}, \'output_token_details\': {}}'
E    +  where '14' = <built-in method lower of str object at 0x73271bbd1bc0>()
E    +    where <built-in method lower of str object at 0x73271bbd1bc0> = '14'.lower
```

### test_search_ecoles.py

`test_search_ecoles` 14.12s

```
test_search_ecoles.py:22: in test_search_ecoles
    assert fragment in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: bdtopo_v3:zone_d_activite_ou_d_interet
E   assert 'bdtopo_v3:zone_d_activite_ou_d_interet' in 'content=\'d\\\'après les recherches effectuées, il n\\\'existe pas de table nommée explicitement "écoles". cependant, vous pouvez trouver des informations relatives aux écoles dans les tables suivantes :\\n\\n1.  **`bdtopo_v3:erp` (établissements recevant du public)** : les écoles étant des lieux accueillant du public, elles sont classées comme des erp. cette table est la plus susceptible de contenir des données spécifiques sur la nature de l\\\'établissement.\\n2.  **`bdtopo_v3:batiment`** : cette table répertorie les constructions physiques. vous pourriez y trouver les bâtiments scolaires, bien qu\\\'il faille probablement filtrer par usage ou fonction.\\n\\nsi vous avez un lieu précis en tête, je peux explorer ces tables pour vous afin de vérifier si des établissements scolaires y sont répertoriés.\' additional_kwargs={\'refusal\': none} response_metadata={\'token_usage\': {\'completion_tokens\': 187, \'prompt_tokens\': 6260, \'total_tokens\': 6447, \'completion_tokens_details\': none, \'prompt_tokens_details\': none}, \'model_provider\': \'openai\', \'model_name\': \'gemma4-26b-moe\', \'system_fingerprint\': \'vllm-0.23.0-fc919ceb\', \'id\': \'chatcmpl-af8408001a2d7eb5\', \'finish_reason\': \'stop\', \'logprobs\': none} id=\'lc_run--019f64d6-1eaf-7121-a74b-96253d5e7b52-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 6260, \'output_tokens\': 187, \'total_tokens\': 6447, \'input_token_details\': {}, \'output_token_details\': {}}'
```

## 46 passed

### test_adminexpress.py

`test_adminexpress` 4.88s

### test_altitude.py

`test_altitude` 3.90s

### test_assiette_sup.py

`test_assiette_sup` 54.79s

### test_cadastre.py

`test_cadastre` 7.78s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 18.17s

### test_chaining_discovery.py

`test_chaining_discovery` 21.07s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 7.81s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 7.46s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 28.55s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 47.98s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 20.97s

### test_describe_type.py

`test_describe_type` 20.80s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 1.41s

### test_geocode.py

`test_geocode` 5.01s

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 3.74s

### test_get_feature_by_id.py

`test_get_feature_by_id` 4.95s

### test_get_features.py

`test_get_features` 29.38s

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

`test_search_batiment` 8.42s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 23.53s
