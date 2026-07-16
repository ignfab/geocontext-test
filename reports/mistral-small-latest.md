# Test Report

*Report generated on 16-Jul-2026 at 11:19:14 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 217.89 seconds

- 2 failed
- 46 passed

## 2 failed

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 26.74s

```
test_count_lycees_2km_chateau_vincennes.py:35: in test_count_lycees_2km_chateau_vincennes
    assert fragment.lower() in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: 14
E   assert '14' in "content='il y a **2 lycées** situés à moins de 2 km du château de vincennes.' additional_kwargs={} response_metadata={'token_usage': {'prompt_tokens': 18473, 'total_tokens': 18496, 'completion_tokens': 23, 'prompt_tokens_details': {'cached_tokens': 4864}}, 'model_name': 'mistral-small-latest', 'model': 'mistral-small-latest', 'finish_reason': 'stop', 'model_provider': 'mistralai'} id='lc_run--019f6a37-cc04-7d70-9c60-c0baebaa39b1-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 18473, 'output_tokens': 23, 'total_tokens': 18496}"
E    +  where '14' = <built-in method lower of str object at 0x729ae88be610>()
E    +    where <built-in method lower of str object at 0x729ae88be610> = '14'.lower
```

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 3.73s

```
test_geocode_address_not_found.py:30: in test_geocode_address_not_found
    assert "adresse non trouvée" in message_text, \
E   AssertionError: L'agent n'a pas signalé 'adresse non trouvée': content="les coordonnées géographiques du **15 avenue de paris à loray (25390)** ne sont pas directement disponibles dans les résultats.\n\ncependant, voici les coordonnées des adresses les plus proches trouvées :\n- **15 rue des ages de loray** : longitude `6.503116`, latitude `47.144954`\n- **15 r
E   assert 'adresse non trouvée' in 'content="les coordonnées géographiques du **15 avenue de paris à loray (25390)** ne sont pas directement disponibles dans les résultats.\\n\\ncependant, voici les coordonnées des adresses les plus proches trouvées :\\n- **15 rue des ages de loray** : longitude `6.503116`, latitude `47.144954`\\n- **15 rue des ages** : longitude `6.50319`, latitude `47.145048`\\n- **15 grande rue** : longitude `6.495587`, latitude `47.153689`\\n\\nsi tu cherches spécifiquement l\'**avenue de paris**, l\'adresse n\'a pas été trouvée. souhaites-tu que je vérifie une autre orthographe ou une autre localisation ?" additional_kwargs={} response_metadata={\'token_usage\': {\'prompt_tokens\': 5156, \'total_tokens\': 5341, \'completion_tokens\': 185, \'prompt_tokens_details\': {\'cached_tokens\': 4864}}, \'model_name\': \'mistral-small-latest\', \'model\': \'mistral-small-latest\', \'finish_reason\': \'stop\', \'model_provider\': \'mistralai\'} id=\'lc_run--019f6a37-fea9-7ce0-9d20-3e4083ea8014-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 5156, \'output_tokens\': 185, \'total_tokens\': 5341}'
```

## 46 passed

### test_adminexpress.py

`test_adminexpress` 3.01s

### test_altitude.py

`test_altitude` 2.63s

### test_assiette_sup.py

`test_assiette_sup` 13.67s

### test_cadastre.py

`test_cadastre` 8.52s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 14.78s

### test_chaining_discovery.py

`test_chaining_discovery` 13.72s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 5.09s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 4.49s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 16.39s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 12.44s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 10.52s

### test_describe_type.py

`test_describe_type` 7.20s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.45s

### test_geocode.py

`test_geocode` 2.44s

### test_get_feature_by_id.py

`test_get_feature_by_id` 2.62s

### test_get_features.py

`test_get_features` 23.03s

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

`test_search_batiment` 3.88s

### test_search_ecoles.py

`test_search_ecoles` 21.77s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 19.30s
