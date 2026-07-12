# Test Report

*Report generated on 12-Jul-2026 at 11:59:50 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

20 tests ran in 112.32 seconds

- 2 failed
- 18 passed

## 2 failed

### test_adresse_inexistante.py

`test_adresse_inexistante` 2.66s

```
test_adresse_inexistante.py:28: in test_adresse_inexistante
    assert any(k in message_text for k in indicateurs), \
E   AssertionError: L'agent n'a pas signalé que l'adresse est introuvable: content='je n\'ai pas pu trouver de coordonnées géographiques pour l\'adresse "99999 rue inexistante, villeimaginaire". il est probable que cette adresse n\'existe pas dans la base de données.' additional_kwargs={'refusal': none} response_metadata={'token_usage': {'completion_tokens': 50, 'prompt_to
E   assert False
E    +  where False = any(<generator object test_adresse_inexistante.<locals>.<genexpr> at 0x78509f415970>)
```

### test_coords_hors_france.py

`test_coords_hors_france` 3.07s

```
test_coords_hors_france.py:32: in test_coords_hors_france
    assert any(k in message_text for k in indicateurs), \
E   AssertionError: L'agent n'a pas signalé que les coordonnées sont hors France: content="le point de coordonnées longitude 10.0, latitude 60.0 ne semble pas se trouver sur le territoire français (les outils de recherche administrative consultés ne retournent aucun résultat pour ces coordonnées). il est situé dans la mer du nord, au large des côtes de l'allemagne et du danemark.
E   assert False
E    +  where False = any(<generator object test_coords_hors_france.<locals>.<genexpr> at 0x78509fd67370>)
```

## 18 passed

### test_adminexpress.py

`test_adminexpress` 3.23s

### test_altitude.py

`test_altitude` 2.56s

### test_assiette_sup.py

`test_assiette_sup` 18.74s

### test_cadastre.py

`test_cadastre` 4.91s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 8.09s

### test_chaining_discovery.py

`test_chaining_discovery` 10.65s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 4.81s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 4.40s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 11.78s

### test_describe_type.py

`test_describe_type` 6.34s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 0.51s

### test_geocode.py

`test_geocode` 2.76s

### test_get_feature_by_id.py

`test_get_feature_by_id` 2.87s

### test_get_features.py

`test_get_features` 7.50s

### test_search_batiment.py

`test_chaining_geocode_altitude` 3.14s

### test_search_ecoles.py

`test_search_ecoles` 5.12s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 7.27s
