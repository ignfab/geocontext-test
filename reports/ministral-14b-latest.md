# Test Report

*Report generated on 16-Jul-2026 at 12:06:49 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 266.88 seconds

- 3 failed
- 45 passed

## 3 failed

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 10.90s

```
test_count_lycees_2km_chateau_vincennes.py:35: in test_count_lycees_2km_chateau_vincennes
    assert fragment.lower() in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: lycées
E   assert 'lycées' in 'content="il n\'y a aucun lycée situé dans un rayon de 2 kilomètres autour du **château de vincennes** selon les données disponibles. je peux élargir la recherche si nécessaire." additional_kwargs={} response_metadata={\'token_usage\': {\'prompt_tokens\': 8606, \'total_tokens\': 8645, \'completion_tokens\': 39, \'prompt_tokens_details\': {\'cached_tokens\': 6720}}, \'model_name\': \'ministral-14b-latest\', \'model\': \'ministral-14b-latest\', \'finish_reason\': \'stop\', \'model_provider\': \'mistralai\'} id=\'lc_run--019f6a62-ef89-7003-94c9-ed9adc3c33c6-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 8606, \'output_tokens\': 39, \'total_tokens\': 8645}'
E    +  where 'lycées' = <built-in method lower of str object at 0x723e032d05b0>()
E    +    where <built-in method lower of str object at 0x723e032d05b0> = 'lycées'.lower
```

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 3.62s

```
test_geocode_address_not_found.py:30: in test_geocode_address_not_found
    assert "adresse non trouvée" in message_text, \
E   AssertionError: L'agent n'a pas signalé 'adresse non trouvée': content="l'adresse exacte **15 avenue de paris** n'a pas été trouvée. cependant, une adresse proche est disponible :\n\n- **15 rue des ages de loray** (25390 loray)\n  **coordonnées** : longitude **6.503116**, latitude **47.144954**.\n\nsi vous cherchez une autre adresse ou précision, n'hésitez pas 
E   assert 'adresse non trouvée' in 'content="l\'adresse exacte **15 avenue de paris** n\'a pas été trouvée. cependant, une adresse proche est disponible :\\n\\n- **15 rue des ages de loray** (25390 loray)\\n  **coordonnées** : longitude **6.503116**, latitude **47.144954**.\\n\\nsi vous cherchez une autre adresse ou précision, n\'hésitez pas à me le demander." additional_kwargs={} response_metadata={\'token_usage\': {\'prompt_tokens\': 5018, \'total_tokens\': 5119, \'completion_tokens\': 101, \'prompt_tokens_details\': {\'cached_tokens\': 4928}}, \'model_name\': \'ministral-14b-latest\', \'model\': \'ministral-14b-latest\', \'finish_reason\': \'stop\', \'model_provider\': \'mistralai\'} id=\'lc_run--019f6a63-4a1a-7f30-9399-9231d843c2ad-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 5018, \'output_tokens\': 101, \'total_tokens\': 5119}'
```

### test_search_ecoles.py

`test_search_ecoles` 13.58s

```
test_search_ecoles.py:22: in test_search_ecoles
    assert fragment in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: bdtopo_v3:zone_d_activite_ou_d_interet
E   assert 'bdtopo_v3:zone_d_activite_ou_d_interet' in 'content=\'pour trouver des informations spécifiques sur les **écoles ou établissements scolaires**, les tables les plus pertinentes disponibles dans les résultats sont :\\n\\n1. **`bdtopo_v3:batiment`** :\\n   - cette table contient des informations sur les bâtiments, y compris ceux qui pourraient être des écoles. cependant, elle ne distingue pas spécifiquement les bâtiments scolaires des autres types de bâtiments. il faudra filtrer ou analyser les attributs pour identifier ceux liés à des écoles.\\n\\n2. **`bdtopo_v3:erp`** :\\n   - **établissements recevant du public (erp)** : cette table inclut des bâtiments comme les écoles, car elles accueillent du public. il est probable que les écoles y soient référencées, mais il faudra vérifier les attributs pour confirmer leur nature scolaire.\\n\\n3. **`cadastralparcels.parcellaire_express:batiment`** :\\n   - cette table contient des informations sur les bâtiments au niveau cadastral. elle pourrait inclure des écoles, mais comme pour `bdtopo_v3:batiment`, il faudra analyser les attributs pour identifier les bâtiments scolaires.\\n\\n### recommandation :\\npour obtenir des résultats précis, il est conseillé d\\\'utiliser la table **`bdtopo_v3:erp`** et de filtrer les bâtiments en fonction de leur usage (par exemple, en recherchant des attributs comme "école", "collège", "lycée", etc.). si des attributs spécifiques comme le type d\\\'établissement ou une catégorie scolaire existent, ils pourront être exploités pour affiner la recherche.\\n\\nsouhaitez-vous que je vérifie les propriétés disponibles dans **`bdtopo_v3:erp`** pour identifier comment filtrer les écoles ?\' additional_kwargs={} response_metadata={\'token_usage\': {\'prompt_tokens\': 8626, \'total_tokens\': 9001, \'completion_tokens\': 375, \'prompt_tokens_details\': {\'cached_tokens\': 4864}}, \'model_name\': \'ministral-14b-latest\', \'model\': \'ministral-14b-latest\', \'finish_reason\': \'stop\', \'model_provider\': \'mistralai\'} id=\'lc_run--019f6a63-e9d4-77c1-88c8-58ce660bc24a-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 8626, \'output_tokens\': 375, \'total_tokens\': 9001}'
```

## 45 passed

### test_adminexpress.py

`test_adminexpress` 3.88s

### test_altitude.py

`test_altitude` 3.73s

### test_assiette_sup.py

`test_assiette_sup` 39.96s

### test_cadastre.py

`test_cadastre` 6.16s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 24.65s

### test_chaining_discovery.py

`test_chaining_discovery` 12.12s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 5.73s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 4.99s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 4.79s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 15.09s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 20.46s

### test_describe_type.py

`test_describe_type` 16.55s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 1.12s

### test_geocode.py

`test_geocode` 2.62s

### test_get_feature_by_id.py

`test_get_feature_by_id` 4.49s

### test_get_features.py

`test_get_features` 22.00s

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

`test_search_batiment` 5.23s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 42.55s
