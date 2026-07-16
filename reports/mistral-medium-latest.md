# Test Report

*Report generated on 16-Jul-2026 at 09:57:49 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 454.87 seconds

- 1 failed
- 47 passed

## 1 failed

### test_search_ecoles.py

`test_search_ecoles` 28.07s

```
test_search_ecoles.py:22: in test_search_ecoles
    assert fragment in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: bdtopo_v3:zone_d_activite_ou_d_interet
E   assert 'bdtopo_v3:zone_d_activite_ou_d_interet' in 'content=\'les informations sur les **écoles** peuvent être trouvées dans la table **`bdtopo_v3:erp`**.\\n\\ncette table contient des données sur les **établissements recevant du public (erp)**, qui incluent les écoles. voici quelques propriétés pertinentes pour identifier les écoles :\\n- **`type_principal`** : peut indiquer le type d\\\'établissement (ex. : "enseignement").\\n- **`activite_principale`** : peut préciser l\\\'activité principale (ex. : "école maternelle", "école primaire", "collège", "lycée", etc.).\\n- **`libelle`** : nom de l\\\'établissement (ex. : "école primaire jean jaurès").\\n- **`public`** : indique si l\\\'établissement est public ou privé.\\n- **`adresse_numero`**, **`adresse_nom_1`**, **`code_postal`**, **`insee_commune`** : informations d\\\'adresse et de localisation.\\n\\npour filtrer spécifiquement les écoles, vous pouvez utiliser des requêtes sur les champs **`type_principal`** ou **`activite_principale`** avec des valeurs comme **"enseignement"** ou **"école"**.\' additional_kwargs={} response_metadata={\'token_usage\': {\'prompt_tokens\': 11415, \'total_tokens\': 11684, \'completion_tokens\': 269, \'prompt_tokens_details\': {\'cached_tokens\': 0}}, \'model_name\': \'mistral-medium-latest\', \'model\': \'mistral-medium-latest\', \'finish_reason\': \'stop\', \'model_provider\': \'mistralai\'} id=\'lc_run--019f69ee-313f-7ea2-a10a-0db0f7849c50-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 11415, \'output_tokens\': 269, \'total_tokens\': 11684}'
```

## 47 passed

### test_adminexpress.py

`test_adminexpress` 5.67s

### test_altitude.py

`test_altitude` 4.32s

### test_assiette_sup.py

`test_assiette_sup` 57.51s

### test_cadastre.py

`test_cadastre` 6.85s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 33.05s

### test_chaining_discovery.py

`test_chaining_discovery` 26.33s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 8.01s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 10.51s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 27.67s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 16.67s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 22.47s

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 44.42s

### test_describe_type.py

`test_describe_type` 29.86s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 1.26s

### test_geocode.py

`test_geocode` 4.32s

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 6.17s

### test_get_feature_by_id.py

`test_get_feature_by_id` 4.09s

### test_get_features.py

`test_get_features` 91.38s

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

`test_search_batiment` 4.29s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 20.38s
