# Test Report

*Report generated on 11-Jul-2026 at 11:53:32 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

20 tests ran in 356.55 seconds

- 2 failed
- 18 passed

## 2 failed

### test_adresse_inexistante.py

`test_adresse_inexistante` 9.28s

```
test_adresse_inexistante.py:28: in test_adresse_inexistante
    assert any(k in message_text for k in indicateurs), \
E   AssertionError: L'agent n'a pas signalé que l'adresse est introuvable: content='je n\'ai pas pu trouver de coordonnées géographiques pour l\'adresse "99999 rue inexistante, villeimaginaire". il est probable que cette adresse n\'existe pas dans la base de données.' additional_kwargs={'refusal': none} response_metadata={'token_usage': {'completion_tokens': 50, 'prompt_to
E   assert False
E    +  where False = any(<generator object test_adresse_inexistante.<locals>.<genexpr> at 0x783016beb030>)
```

### test_chaining_geocode.py

`test_chaining_geocode_altitude` 9.83s

```
test_chaining_geocode.py:62: in test_chaining_geocode_altitude
    assert re.search(r"1[\s\u202f\xa0.,]*0[\s]*3[\s]*6", message_text), \
E   AssertionError: Altitude ~1036m not found in response
E   assert None
E    +  where None = <function search at 0x78301c86de40>('1[\\s\\u202f\\xa0.,]*0[\\s]*3[\\s]*6', 'content="L\'altitude de la mairie de Chamonix-Mont-Blanc est d\'environ **1 035,89 mètres**." additional_kwargs={\'refusal\': None} response_metadata={\'token_usage\': {\'completion_tokens\': 34, \'prompt_tokens\': 4385, \'total_tokens\': 4419, \'completion_tokens_details\': None, \'prompt_tokens_details\': None}, \'model_provider\': \'openai\', \'model_name\': \'gemma4-26b-moe\', \'system_fingerprint\': \'vllm-0.23.0-fc919ceb\', \'id\': \'chatcmpl-b0b905d2856c379a\', \'finish_reason\': \'stop\', \'logprobs\': None} id=\'lc_run--019f5097-05ee-76a2-88b5-03d18d3e6969-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 4385, \'output_tokens\': 34, \'total_tokens\': 4419, \'input_token_details\': {}, \'output_token_details\': {}}')
E    +    where <function search at 0x78301c86de40> = re.search
```

## 18 passed

### test_adminexpress.py

`test_adminexpress` 10.29s

### test_altitude.py

`test_altitude` 9.06s

### test_assiette_sup.py

`test_assiette_sup` 56.12s

### test_cadastre.py

`test_cadastre` 20.48s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 57.65s

### test_chaining_discovery.py

`test_chaining_discovery` 73.22s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 6.14s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 25.60s

### test_coords_hors_france.py

`test_coords_hors_france` 4.40s

### test_describe_type.py

`test_describe_type` 17.10s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.81s

### test_geocode.py

`test_geocode` 4.10s

### test_get_feature_by_id.py

`test_get_feature_by_id` 4.34s

### test_get_features.py

`test_get_features` 14.19s

### test_search_batiment.py

`test_chaining_geocode_altitude` 6.04s

### test_search_ecoles.py

`test_search_ecoles` 8.91s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 17.09s
