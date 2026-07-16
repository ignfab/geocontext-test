# Test Report

*Report generated on 16-Jul-2026 at 09:50:11 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 239.74 seconds

- 2 failed
- 46 passed

## 2 failed

### test_search_batiment.py

`test_search_batiment` 2.47s

```
test_search_batiment.py:25: in test_search_batiment
    assert fragment in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: cadastralparcels.parcellaire_express:batiment
E   assert 'cadastralparcels.parcellaire_express:batiment' in "content='on peut trouver des informations sur les bâtiments dans la table **`bdtopo_v3:batiment`** (bâtiment).\\n\\nsi tu veux explorer les propriétés disponibles dans cette table ou interroger des données spécifiques, fais-le-moi savoir !' additional_kwargs={} response_metadata={'token_usage': {'prompt_tokens': 5194, 'total_tokens': 5245, 'completion_tokens': 51, 'prompt_tokens_details': {'cached_tokens': 4864}}, 'model_name': 'mistral-small-latest', 'model': 'mistral-small-latest', 'finish_reason': 'stop', 'model_provider': 'mistralai'} id='lc_run--019f69e7-2105-74b1-8a3a-e476ef252449-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 5194, 'output_tokens': 51, 'total_tokens': 5245}"
```

### test_search_ecoles.py

`test_search_ecoles` 8.84s

```
test_search_ecoles.py:22: in test_search_ecoles
    assert fragment in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: bdtopo_v3:zone_d_activite_ou_d_interet
E   assert 'bdtopo_v3:zone_d_activite_ou_d_interet' in 'content=\'on peut trouver des informations sur les **écoles** dans la table **`bdtopo_v3:erp`** (établissements recevant du public).\\n\\ncette table contient des établissements comme les écoles, collèges, lycées, etc., avec des attributs comme :\\n- **`type_principal`** et **`types_secondaires`** (pour identifier les écoles),\\n- **`activite_principale`** (ex : "enseignement primaire", "enseignement secondaire"),\\n- **`libelle`** (nom de l\\\'établissement),\\n- **`capacite_d_accueil_du_public`** (nombre de places),\\n- **`adresse_*`** (adresse complète),\\n- **`insee_commune`** (code insee de la commune),\\n- et bien d\\\'autres informations utiles.\\n\\nsi tu veux explorer les données disponibles ou effectuer une recherche spécifique, fais-le-moi savoir !\' additional_kwargs={} response_metadata={\'token_usage\': {\'prompt_tokens\': 8747, \'total_tokens\': 8944, \'completion_tokens\': 197, \'prompt_tokens_details\': {\'cached_tokens\': 0}}, \'model_name\': \'mistral-small-latest\', \'model\': \'mistral-small-latest\', \'finish_reason\': \'stop\', \'model_provider\': \'mistralai\'} id=\'lc_run--019f69e7-3faa-78a3-86ae-0150ec2bae3e-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 8747, \'output_tokens\': 197, \'total_tokens\': 8944}'
```

## 46 passed

### test_adminexpress.py

`test_adminexpress` 2.87s

### test_altitude.py

`test_altitude` 3.69s

### test_assiette_sup.py

`test_assiette_sup` 20.75s

### test_cadastre.py

`test_cadastre` 8.44s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 12.18s

### test_chaining_discovery.py

`test_chaining_discovery` 9.22s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 4.67s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 4.40s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 19.52s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 12.13s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 10.52s

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 62.35s

### test_describe_type.py

`test_describe_type` 7.80s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.33s

### test_geocode.py

`test_geocode` 2.35s

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 3.02s

### test_get_feature_by_id.py

`test_get_feature_by_id` 2.73s

### test_get_features.py

`test_get_features` 20.91s

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

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 18.69s
