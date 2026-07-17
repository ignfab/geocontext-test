# Test Report

*Report generated on 16-Jul-2026 at 13:53:52 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 198.67 seconds

- 1 failed
- 47 passed

## 1 failed

### test_search_ecoles.py

`test_search_ecoles` 8.03s

```
test_search_ecoles.py:22: in test_search_ecoles
    assert fragment in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: bdtopo_v3:zone_d_activite_ou_d_interet
E   assert 'bdtopo_v3:zone_d_activite_ou_d_interet' in 'content=\'on peut trouver des informations sur les **écoles** dans la table **`bdtopo_v3:erp`** (établissements recevant du public).\\n\\ncette table contient des établissements comme les écoles, collèges, lycées, etc., avec des attributs comme :\\n- **`type_principal`** et **`activite_principale`** pour identifier le type d\\\'établissement (ex : "enseignement" pour les écoles).\\n- **`libelle`** pour le nom de l\\\'établissement.\\n- **`capacite_d_accueil_du_public`** pour la capacité d\\\'accueil.\\n- **`adresse_*`** pour l\\\'adresse complète.\\n- **`insee_commune`** pour le code insee de la commune.\\n\\nsi tu veux explorer les données ou faire une recherche spécifique, je peux t\\\'aider à utiliser cette table. par exemple, veux-tu chercher les écoles autour d\\\'une ville ou d\\\'un point précis ?\' additional_kwargs={} response_metadata={\'token_usage\': {\'prompt_tokens\': 8747, \'total_tokens\': 8950, \'completion_tokens\': 203, \'prompt_tokens_details\': {\'cached_tokens\': 4864}}, \'model_name\': \'mistral-small-latest\', \'model\': \'mistral-small-latest\', \'finish_reason\': \'stop\', \'model_provider\': \'mistralai\'} id=\'lc_run--019f6ac6-6bea-7d33-8b08-c92903a66be0-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 8747, \'output_tokens\': 203, \'total_tokens\': 8950}'
```

## 47 passed

### test_adminexpress.py

`test_adminexpress` 2.91s

### test_altitude.py

`test_altitude` 2.85s

### test_assiette_sup.py

`test_assiette_sup` 14.45s

### test_cadastre.py

`test_cadastre` 8.52s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 14.32s

### test_chaining_discovery.py

`test_chaining_discovery` 10.83s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 5.16s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 4.44s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 11.52s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 14.94s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 10.98s

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 22.62s

### test_describe_type.py

`test_describe_type` 8.06s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.32s

### test_geocode.py

`test_geocode` 2.32s

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 3.04s

### test_get_feature_by_id.py

`test_get_feature_by_id` 2.53s

### test_get_features.py

`test_get_features` 30.98s

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

`test_search_batiment` 3.84s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 14.54s
