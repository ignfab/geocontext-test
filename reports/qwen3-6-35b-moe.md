# Test Report

*Report generated on 11-Jul-2026 at 12:00:59 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

20 tests ran in 444.11 seconds

- 3 failed
- 17 passed

## 3 failed

### test_adresse_inexistante.py

`test_adresse_inexistante` 3.68s

```
test_adresse_inexistante.py:28: in test_adresse_inexistante
    assert any(k in message_text for k in indicateurs), \
E   AssertionError: L'agent n'a pas signalé que l'adresse est introuvable: content='\n\nl\'adresse "99999 rue inexistante, villeimaginaire" n\'a pas été trouvée dans la base de données de géocodage. il s\'agit probablement d\'une adresse fictive ou erronée.\n\nsi vous souhaitez obtenir les coordonnées d\'une adresse réelle, n\'hésitez pas à me fournir une adresse valide.' 
E   assert False
E    +  where False = any(<generator object test_adresse_inexistante.<locals>.<genexpr> at 0x75c9d72eb030>)
```

### test_altitude.py

`test_altitude` 240.00s

```
.venv/lib/python3.13/site-packages/pytest_asyncio/plugin.py:569: in runtest
    super().runtest()
.venv/lib/python3.13/site-packages/pytest_asyncio/plugin.py:905: in inner
    runner.run(coro, context=context)
../../../.local/share/uv/python/cpython-3.13.12-linux-x86_64-gnu/lib/python3.13/asyncio/runners.py:118: in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
../../../.local/share/uv/python/cpython-3.13.12-linux-x86_64-gnu/lib/python3.13/asyncio/base_events.py:712: in run_until_complete
    self.run_forever()
../../../.local/share/uv/python/cpython-3.13.12-linux-x86_64-gnu/lib/python3.13/asyncio/base_events.py:683: in run_forever
    self._run_once()
../../../.local/share/uv/python/cpython-3.13.12-linux-x86_64-gnu/lib/python3.13/asyncio/base_events.py:2012: in _run_once
    event_list = self._selector.select(timeout)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
../../../.local/share/uv/python/cpython-3.13.12-linux-x86_64-gnu/lib/python3.13/selectors.py:452: in select
    fd_event_list = self._selector.poll(timeout, max_ev)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   Failed: Timeout (>240.0s) from pytest-timeout.
```

### test_chaining_geocode.py

`test_chaining_geocode_altitude` 6.04s

```
test_chaining_geocode.py:62: in test_chaining_geocode_altitude
    assert re.search(r"1[\s\u202f\xa0.,]*0[\s]*3[\s]*6", message_text), \
E   AssertionError: Altitude ~1036m not found in response
E   assert None
E    +  where None = <function search at 0x75c9dcf69e40>('1[\\s\\u202f\\xa0.,]*0[\\s]*3[\\s]*6', 'content="\\n\\nL\'altitude de la mairie de Chamonix-Mont-Blanc est de 1035,89 mètres." additional_kwargs={\'refusal\': None} response_metadata={\'token_usage\': {\'completion_tokens\': 53, \'prompt_tokens\': 5222, \'total_tokens\': 5275, \'completion_tokens_details\': None, \'prompt_tokens_details\': None}, \'model_provider\': \'openai\', \'model_name\': \'qwen3-6-35b-moe\', \'system_fingerprint\': \'vllm-0.22.0-057a257e\', \'id\': \'chatcmpl-8968dd34ddad2d5a\', \'finish_reason\': \'stop\', \'logprobs\': None} id=\'lc_run--019f509d-d56c-7890-9a6e-c31795896ab1-0\' tool_calls=[] invalid_tool_calls=[] usage_metadata={\'input_tokens\': 5222, \'output_tokens\': 53, \'total_tokens\': 5275, \'input_token_details\': {}, \'output_token_details\': {}}')
E    +    where <function search at 0x75c9dcf69e40> = re.search
```

## 17 passed

### test_adminexpress.py

`test_adminexpress` 4.33s

### test_assiette_sup.py

`test_assiette_sup` 13.67s

### test_cadastre.py

`test_cadastre` 6.35s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 45.57s

### test_chaining_discovery.py

`test_chaining_discovery` 12.39s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 6.45s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 10.45s

### test_coords_hors_france.py

`test_coords_hors_france` 4.19s

### test_describe_type.py

`test_describe_type` 16.49s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 1.84s

### test_geocode.py

`test_geocode` 3.89s

### test_get_feature_by_id.py

`test_get_feature_by_id` 5.32s

### test_get_features.py

`test_get_features` 13.11s

### test_search_batiment.py

`test_chaining_geocode_altitude` 5.32s

### test_search_ecoles.py

`test_search_ecoles` 20.69s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 22.42s
