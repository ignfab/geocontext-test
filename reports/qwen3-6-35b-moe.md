# Test Report

*Report generated on 11-Jul-2026 at 11:03:41 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

20 tests ran in 180.86 seconds

- 3 failed
- 17 passed

## 3 failed

### test_adresse_inexistante.py

`test_adresse_inexistante` 4.09s

```
test_adresse_inexistante.py:28: in test_adresse_inexistante
    assert any(k in message_text for k in indicateurs), \
E   AssertionError: L'agent n'a pas signalé que l'adresse est introuvable: content='\n\nl\'adresse \'99999 rue inexistante, villeimaginaire\' n\'a pas été trouvée. il s\'agit visiblement d\'une adresse fictive :\n\n- le code postal 99999 n\'existe pas en france (les codes postaux français vont de 01000 à 97699)\n- "villeimaginaire" n\'est pas une ville réelle\n\nsi vous so
E   assert False
E    +  where False = any(<generator object test_adresse_inexistante.<locals>.<genexpr> at 0x794990a93ac0>)
```

### test_altitude.py

`test_altitude` 4.54s

```
test_altitude.py:24: in test_altitude
    float(match.replace(" ", "").replace(",", "."))
E   ValueError: could not convert string to float: '0.22.0'
```

### test_chaining_geocode.py

`test_chaining_geocode_altitude` 5.94s

```
test_chaining_geocode.py:62: in test_chaining_geocode_altitude
    assert re.search(r"1[\s\u202f\xa0.,]*0[\s]*3[\s]*6", message_text), \
E   AssertionError: Altitude ~1036m not found in response
E   assert None
E    +  where None = <function search at 0x794996769e40>('1[\\s\\u202f\\xa0.,]*0[\\s]*3[\\s]*6', 'content="\\n\\nL\'altitude de la mairie de Chamonix-Mont-Blanc est d\'environ **1035,89 mètres**." additional_kwargs={\'refusal\': None} response_metadata={\'token_usage\': {\'completion_tokens\': 57, \'prompt_tokens\': 5225, \'total_tokens\': 5282, \'completion_tokens_details\': None, \'prompt_tokens_details\': None}, \'model_provider\': \'openai\', \'model_name\': \'qwen3-6-35b-moe\', \'system_fingerprint\': \'vllm-0.22.0-057a257e\', \'id\': \'chatcmpl-9d40cad04c61eebc\', \'finish_reason\': \'stop\', \'logprobs\': None} id=\'lc_run--019f5069-52e2-7d42-b243-950387b86c37-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 5225, \'output_tokens\': 57, \'total_tokens\': 5282, \'input_token_details\': {}, \'output_token_details\': {}}')
E    +    where <function search at 0x794996769e40> = re.search
```

## 17 passed

### test_adminexpress.py

`test_adminexpress` 4.54s

### test_assiette_sup.py

`test_assiette_sup` 18.90s

### test_cadastre.py

`test_cadastre` 6.44s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 10.03s

### test_chaining_discovery.py

`test_chaining_discovery` 11.06s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 6.24s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 11.67s

### test_coords_hors_france.py

`test_coords_hors_france` 3.89s

### test_describe_type.py

`test_describe_type` 10.24s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.82s

### test_geocode.py

`test_geocode` 7.37s

### test_get_feature_by_id.py

`test_get_feature_by_id` 4.35s

### test_get_features.py

`test_get_features` 23.76s

### test_search_batiment.py

`test_chaining_geocode_altitude` 5.47s

### test_search_ecoles.py

`test_search_ecoles` 13.01s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 26.52s
