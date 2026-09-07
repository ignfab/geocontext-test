# Test Report

*Report generated on 07-Sep-2026 at 09:59:52 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

54 tests ran in 516.40 seconds

- 2 failed
- 52 passed

## 2 failed

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 232.93s

```
test_count_lycees_2km_chateau_vincennes.py:37: in test_count_lycees_2km_chateau_vincennes
    assert fragment.lower() in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: lycées
E   assert 'lycées' in "content='après avoir géocodé le château de vincennes (lon\\u202f=\\u202f2.439144\\u202f; lat\\u202f=\\u202f48.844676) et interrogé le jeu de données «\\u202ferp\\u202f» (établissements recevant du public) de la bd\\u202ftopo pour les objets dont le champ **type_principal** correspond à «\\u202flycée\\u202f» dans un rayon de\\u202f2\\u202fkm, aucune entité n’a été retournée\\u202f:\\n\\n* nombre d’objets trouvés\\u202f=\\u202f0\\n\\nle catalogue de données géographiques disponible ne comporte donc aucun lycée situé à moins de 2\\u202fkm du château de vincennes. (il est possible que les établissements d’enseignement ne soient pas couverts par le jeu de données erp\\u202f; dans ce cas, les données correspondantes ne sont tout simplement pas présentes dans la source consultée.)' additional_kwargs={'refusal': none} response_metadata={'token_usage': {'completion_tokens': 178, 'prompt_tokens': 0, 'total_tokens': 178, 'completion_tokens_details': none, 'prompt_tokens_details': none, 'cost': 0.0, 'carbon': {'kwh': {'min': 0.0001226622100995581, 'max': 0.0001226622100995581}, 'kgco2eq': {'min': 1.0913670201394316e-05, 'max': 1.0913670201394316e-05}}, 'impacts': {'kwh': 0.0001226622100995581, 'kgco2eq': 1.0913670201394316e-05}, 'requests': 1}, 'model_provider': 'openai', 'model_name': 'openai/gpt-oss-120b', 'system_fingerprint': none, 'id': 'chatcmpl-880c413497aea11a', 'finish_reason': 'stop', 'logprobs': none} id='lc_run--01a07adf-ce1f-7c51-aef9-2773669f7702-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 0, 'output_tokens': 178, 'total_tokens': 178, 'input_token_details': {}, 'output_token_details': {}}"
E    +  where 'lycées' = <built-in method lower of str object at 0x764800c950b0>()
E    +    where <built-in method lower of str object at 0x764800c950b0> = 'lycées'.lower
```

### test_search_ecoles.py

`test_search_ecoles` 16.97s

```
test_search_ecoles.py:22: in test_search_ecoles
    assert fragment in message_text, f"Expected fragment not found in response: {fragment}"
E   AssertionError: Expected fragment not found in response: bdtopo_v3:zone_d_activite_ou_d_interet
E   assert 'bdtopo_v3:zone_d_activite_ou_d_interet' in "content='les informations relatives aux établissements scolaires sont disponibles dans la table **`bdtopo_v3:erp`** (erp\\u202f=\\u202f«\\u202fétablissements recevant du public\\u202f»).  \\n\\ncette couche recense tous les erp\\u202f: commerces, administrations, établissements de santé, **écoles**, etc. elle comporte notamment\\u202f:\\n\\n* le libellé de l’établissement (`libelle`);\\n* le type principal et les types secondaires (`type_principal`, `types_secondaires`);\\n* la catégorie de l’erp (1\\u202fà\\u202f5) qui, pour les écoles, correspond généralement à la catégorie\\u202f3\\u202fou\\u202f4\\u202fselon la capacité d’accueil\\u202f;\\n* l’adresse détaillée (`adresse_numero`, `adresse_nom_1`, `code_postal`, `insee_commune`);\\n* la capacité d’accueil du public (`capacite_d_accueil_du_public`);\\n* le statut d’ouverture (`ouvert`) et d’appartenance au domaine public/privé (`public`);\\n* la date d’apparition ou de mise à jour, ainsi que les sources d’information.\\n\\nen interrogeant ce type wfs (`bdtopo_v3:erp`) vous pourrez donc récupérer l’ensemble des écoles situées sur le territoire français, avec leurs attributs et leur géométrie (point).' additional_kwargs={'refusal': none} response_metadata={'token_usage': {'completion_tokens': 267, 'prompt_tokens': 0, 'total_tokens': 267, 'completion_tokens_details': none, 'prompt_tokens_details': none, 'cost': 0.0, 'carbon': {'kwh': {'min': 0.00014751050264933717, 'max': 0.00014751050264933717}, 'kgco2eq': {'min': 7.99876204896806e-06, 'max': 7.99876204896806e-06}}, 'impacts': {'kwh': 0.00014751050264933717, 'kgco2eq': 7.99876204896806e-06}, 'requests': 1}, 'model_provider': 'openai', 'model_name': 'openai/gpt-oss-120b', 'system_fingerprint': none, 'id': 'chatcmpl-b7d6b12c8ad8b3d2', 'finish_reason': 'stop', 'logprobs': none} id='lc_run--01a07ae0-e83a-7fe3-926f-5b44bc77bf7b-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 0, 'output_tokens': 267, 'total_tokens': 267, 'input_token_details': {}, 'output_token_details': {}}"
```

## 52 passed

### test_adminexpress.py

`test_adminexpress` 4.17s

### test_altitude.py

`test_altitude` 2.36s

### test_assiette_sup.py

`test_assiette_sup` 28.41s

### test_cadastre.py

`test_cadastre` 5.03s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 45.65s

### test_chaining_discovery.py

`test_chaining_discovery` 15.89s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 15.72s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 7.22s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 19.88s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 29.72s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 7.22s

### test_describe_type.py

`test_describe_type` 7.31s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.87s

### test_geocode.py

`test_geocode` 2.90s

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 4.34s

### test_get_feature_by_id.py

`test_get_feature_by_id` 6.07s

### test_get_features.py

`test_get_features` 17.20s

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

`TestSlugify.test_drops_provider_prefix` 0.00s

`TestSlugify.test_replaces_remaining_separators` 0.00s

`TestSlugify.test_without_prefix` 0.00s

`TestWriteAgentTrace.test_write_trace` 0.00s

`TestWriteAgentTrace.test_no_result_writes_nothing` 0.00s

### test_mcp_concurrency.py

`test_concurrent_tool_calls_are_not_crossed` 4.25s

### test_search_batiment.py

`test_search_batiment` 5.14s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 34.34s
