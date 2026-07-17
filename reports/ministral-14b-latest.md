# Test Report

*Report generated on 16-Jul-2026 at 13:50:30 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 322.07 seconds

- 3 failed
- 45 passed

## 3 failed

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 14.20s

```
test_count_lycees_2km_chateau_vincennes.py:35: in test_count_lycees_2km_chateau_vincennes
    assert fragment.lower() in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: lycées
E   assert 'lycées' in 'content="il n\'y a aucun lycée situé dans un rayon de 2 kilomètres autour du **château de vincennes** selon les données disponibles. je peux élargir la recherche si nécessaire." additional_kwargs={} response_metadata={\'token_usage\': {\'prompt_tokens\': 8607, \'total_tokens\': 8646, \'completion_tokens\': 39, \'prompt_tokens_details\': {\'cached_tokens\': 4864}}, \'model_name\': \'ministral-14b-latest\', \'model\': \'ministral-14b-latest\', \'finish_reason\': \'stop\', \'model_provider\': \'mistralai\'} id=\'lc_run--019f6ac1-be2a-78e3-acea-2c8b0b20eadd-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 8607, \'output_tokens\': 39, \'total_tokens\': 8646}'
E    +  where 'lycées' = <built-in method lower of str object at 0x744ed07d83b0>()
E    +    where <built-in method lower of str object at 0x744ed07d83b0> = 'lycées'.lower
```

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 4.03s

```
test_geocode_address_not_found.py:30: in test_geocode_address_not_found
    assert "adresse non trouvée" in message_text, \
E   AssertionError: L'agent n'a pas signalé 'adresse non trouvée': content="l'adresse exacte **15 avenue de paris, loray (25390)** n'a pas été trouvée. cependant, une adresse proche est disponible :\n\n- **15 rue des ages, 25390 loray**\n  coordonnées : **longitude 6.503116**, **latitude 47.144954**.\n\nsi vous cherchez bien l'**avenue de paris**, je vous invite à 
E   assert 'adresse non trouvée' in 'content="l\'adresse exacte **15 avenue de paris, loray (25390)** n\'a pas été trouvée. cependant, une adresse proche est disponible :\\n\\n- **15 rue des ages, 25390 loray**\\n  coordonnées : **longitude 6.503116**, **latitude 47.144954**.\\n\\nsi vous cherchez bien l\'**avenue de paris**, je vous invite à vérifier l\'orthographe ou le numéro exact." additional_kwargs={} response_metadata={\'token_usage\': {\'prompt_tokens\': 5018, \'total_tokens\': 5128, \'completion_tokens\': 110, \'prompt_tokens_details\': {\'cached_tokens\': 4864}}, \'model_name\': \'ministral-14b-latest\', \'model\': \'ministral-14b-latest\', \'finish_reason\': \'stop\', \'model_provider\': \'mistralai\'} id=\'lc_run--019f6ac2-31fb-7df2-9abc-3f490b4a6bf5-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 5018, \'output_tokens\': 110, \'total_tokens\': 5128}'
```

### test_search_ecoles.py

`test_search_ecoles` 13.83s

```
test_search_ecoles.py:22: in test_search_ecoles
    assert fragment in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: bdtopo_v3:zone_d_activite_ou_d_interet
E   assert 'bdtopo_v3:zone_d_activite_ou_d_interet' in 'content="pour trouver des informations spécifiques sur les **écoles ou établissements scolaires**, les tables les plus pertinentes dans les données disponibles sont :\\n\\n1. **`bdtopo_v3:batiment`** :\\n   cette table contient des informations sur les bâtiments, y compris ceux qui pourraient être des écoles. cependant, elle ne distingue pas spécifiquement les bâtiments scolaires des autres types de bâtiments. il faudrait filtrer les bâtiments en fonction de leur usage ou de leur localisation pour identifier ceux qui sont des écoles.\\n\\n2. **`bdtopo_v3:erp`** :\\n   cette table concerne les **établissements recevant du public (erp)**, qui incluent les écoles, collèges et lycées. c\'est la table la plus adaptée pour identifier les établissements scolaires, car elle regroupe les bâtiments ouverts au public, y compris les établissements d\'enseignement.\\n\\n3. **`cadastralparcels.parcellaire_express:batiment`** :\\n   cette table contient des informations sur les bâtiments au niveau cadastral, mais elle ne cible pas spécifiquement les écoles. elle pourrait être utile pour localiser des bâtiments, mais il faudrait croiser ces données avec d\'autres sources pour confirmer leur usage scolaire.\\n\\n### recommandation :\\npour obtenir une liste précise des **écoles**, la table **`bdtopo_v3:erp`** est la plus adaptée. je peux vérifier les propriétés disponibles dans cette table pour confirmer si elle inclut des informations spécifiques sur les établissements scolaires. souhaitez-vous que je procède à cette vérification ?" additional_kwargs={} response_metadata={\'token_usage\': {\'prompt_tokens\': 8626, \'total_tokens\': 8958, \'completion_tokens\': 332, \'prompt_tokens_details\': {\'cached_tokens\': 4864}}, \'model_name\': \'ministral-14b-latest\', \'model\': \'ministral-14b-latest\', \'finish_reason\': \'stop\', \'model_provider\': \'mistralai\'} id=\'lc_run--019f6ac3-126a-7901-a32e-8be0591b5402-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 8626, \'output_tokens\': 332, \'total_tokens\': 8958}'
```

## 45 passed

### test_adminexpress.py

`test_adminexpress` 5.30s

### test_altitude.py

`test_altitude` 3.81s

### test_assiette_sup.py

`test_assiette_sup` 37.89s

### test_cadastre.py

`test_cadastre` 6.78s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 41.25s

### test_chaining_discovery.py

`test_chaining_discovery` 16.54s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 5.46s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 5.54s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 17.46s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 19.60s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 27.26s

### test_describe_type.py

`test_describe_type` 21.27s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.73s

### test_geocode.py

`test_geocode` 3.99s

### test_get_feature_by_id.py

`test_get_feature_by_id` 4.96s

### test_get_features.py

`test_get_features` 33.02s

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

`test_search_batiment` 9.90s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 27.78s
