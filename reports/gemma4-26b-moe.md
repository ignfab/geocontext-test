# Test Report

*Report generated on 11-Jul-2026 at 11:00:37 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

20 tests ran in 113.37 seconds

- 4 failed
- 16 passed

## 4 failed

### test_adresse_inexistante.py

`test_adresse_inexistante` 2.87s

```
test_adresse_inexistante.py:28: in test_adresse_inexistante
    assert any(k in message_text for k in indicateurs), \
E   AssertionError: L'agent n'a pas signalé que l'adresse est introuvable: content='je n\'ai pas pu trouver de coordonnées géographiques pour l\'adresse "99999 rue inexistante, villeimaginaire". il est probable que cette adresse n\'existe pas dans la base de données.' additional_kwargs={'refusal': none} response_metadata={'token_usage': {'completion_tokens': 50, 'prompt_to
E   assert False
E    +  where False = any(<generator object test_adresse_inexistante.<locals>.<genexpr> at 0x78eee66d8ba0>)
```

### test_altitude.py

`test_altitude` 2.77s

```
test_altitude.py:24: in test_altitude
    float(match.replace(" ", "").replace(",", "."))
E   ValueError: could not convert string to float: '0.23.0'
```

### test_chaining_geocode.py

`test_chaining_geocode_altitude` 4.27s

```
test_chaining_geocode.py:62: in test_chaining_geocode_altitude
    assert re.search(r"1[\s\u202f\xa0.,]*0[\s]*3[\s]*6", message_text), \
E   AssertionError: Altitude ~1036m not found in response
E   assert None
E    +  where None = <function search at 0x78eeec26de40>('1[\\s\\u202f\\xa0.,]*0[\\s]*3[\\s]*6', 'content="L\'altitude de la mairie de Chamonix-Mont-Blanc est d\'environ **1 035,89 mètres**." additional_kwargs={\'refusal\': None} response_metadata={\'token_usage\': {\'completion_tokens\': 34, \'prompt_tokens\': 4385, \'total_tokens\': 4419, \'completion_tokens_details\': None, \'prompt_tokens_details\': None}, \'model_provider\': \'openai\', \'model_name\': \'gemma4-26b-moe\', \'system_fingerprint\': \'vllm-0.23.0-fc919ceb\', \'id\': \'chatcmpl-8e939c00fedd28ba\', \'finish_reason\': \'stop\', \'logprobs\': None} id=\'lc_run--019f5067-64a3-7f82-90ef-fce38250e424-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 4385, \'output_tokens\': 34, \'total_tokens\': 4419, \'input_token_details\': {}, \'output_token_details\': {}}')
E    +    where <function search at 0x78eeec26de40> = re.search
```

### test_coords_hors_france.py

`test_coords_hors_france` 3.37s

```
test_coords_hors_france.py:32: in test_coords_hors_france
    assert any(k in message_text for k in indicateurs), \
E   AssertionError: L'agent n'a pas signalé que les coordonnées sont hors France: content="le point de coordonnées longitude 10.0, latitude 60.0 ne semble pas se trouver sur le territoire français (les outils de recherche administrative consultés ne retournent aucun résultat pour ces coordonnées). il est situé dans la mer du nord, au large des côtes de l'allemagne et du danemark.
E   assert False
E    +  where False = any(<generator object test_coords_hors_france.<locals>.<genexpr> at 0x78eee5d89700>)
```

## 16 passed

### test_adminexpress.py

`test_adminexpress` 2.95s

### test_assiette_sup.py

`test_assiette_sup` 19.33s

### test_cadastre.py

`test_cadastre` 4.82s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 7.98s

### test_chaining_discovery.py

`test_chaining_discovery` 10.65s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 4.83s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 11.37s

### test_describe_type.py

`test_describe_type` 6.45s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.51s

### test_geocode.py

`test_geocode` 2.56s

### test_get_feature_by_id.py

`test_get_feature_by_id` 2.97s

### test_get_features.py

`test_get_features` 7.98s

### test_search_batiment.py

`test_chaining_geocode_altitude` 3.17s

### test_search_ecoles.py

`test_search_ecoles` 4.91s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 7.68s
