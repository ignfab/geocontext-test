# Test Report

*Report generated on 11-Jul-2026 at 10:26:30 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

20 tests ran in 121.89 seconds

- 3 failed
- 17 passed

## 3 failed

### test_adresse_inexistante.py

`test_adresse_inexistante` 2.66s

```
test_adresse_inexistante.py:28: in test_adresse_inexistante
    assert any(k in message_text for k in indicateurs), \
E   AssertionError: L'agent n'a pas signalé que l'adresse est introuvable: content='je n\'ai pas pu trouver de coordonnées géographiques pour l\'adresse "99999 rue inexistante, villeimaginaire". il semble que cette adresse n\'existe pas dans la base de données.' additional_kwargs={'refusal': none} response_metadata={'token_usage': {'completion_tokens': 49, 'prompt_tokens':
E   assert False
E    +  where False = any(<generator object test_adresse_inexistante.<locals>.<genexpr> at 0x746d57725150>)
```

### test_altitude.py

`test_altitude` 2.87s

```
test_altitude.py:24: in test_altitude
    float(match.replace(" ", "").replace(",", "."))
E   ValueError: could not convert string to float: '0.23.0'
```

### test_chaining_geocode.py

`test_chaining_geocode_altitude` 5.12s

```
test_chaining_geocode.py:62: in test_chaining_geocode_altitude
    assert re.search(r"1[\s\u202f\xa0.,]*0[\s]*3[\s]*6", message_text), \
E   AssertionError: Altitude ~1036m not found in response
E   assert None
E    +  where None = <function search at 0x746d5d369e40>('1[\\s\\u202f\\xa0.,]*0[\\s]*3[\\s]*6', 'content="L\'altitude de la mairie de Chamonix-Mont-Blanc est d\'environ **1 035,89 mètres**." additional_kwargs={\'refusal\': None} response_metadata={\'token_usage\': {\'completion_tokens\': 34, \'prompt_tokens\': 4385, \'total_tokens\': 4419, \'completion_tokens_details\': None, \'prompt_tokens_details\': None}, \'model_provider\': \'openai\', \'model_name\': \'gemma4-26b-moe\', \'system_fingerprint\': \'vllm-0.23.0-fc919ceb\', \'id\': \'chatcmpl-8abec319d6b206b5\', \'finish_reason\': \'stop\', \'logprobs\': None} id=\'lc_run--019f5048-15aa-7970-af55-67f73455a4c9-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 4385, \'output_tokens\': 34, \'total_tokens\': 4419, \'input_token_details\': {}, \'output_token_details\': {}}')
E    +    where <function search at 0x746d5d369e40> = re.search
```

## 17 passed

### test_adminexpress.py

`test_adminexpress` 3.23s

### test_assiette_sup.py

`test_assiette_sup` 19.15s

### test_cadastre.py

`test_cadastre` 4.91s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 7.58s

### test_chaining_discovery.py

`test_chaining_discovery` 12.39s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 4.70s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 10.53s

### test_coords_hors_france.py

`test_coords_hors_france` 2.98s

### test_describe_type.py

`test_describe_type` 7.88s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.71s

### test_geocode.py

`test_geocode` 2.87s

### test_get_feature_by_id.py

`test_get_feature_by_id` 3.07s

### test_get_features.py

`test_get_features` 8.60s

### test_search_batiment.py

`test_chaining_geocode_altitude` 3.79s

### test_search_ecoles.py

`test_search_ecoles` 6.24s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 8.80s
