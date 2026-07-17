# Test Report

*Report generated on 16-Jul-2026 at 14:03:33 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

48 tests ran in 577.33 seconds

- 1 failed
- 47 passed

## 1 failed

### test_cadastre.py

`test_cadastre` 4.82s

```
test_cadastre.py:9: in test_cadastre
    result = await mcp_agent.ainvoke(
.venv/lib/python3.13/site-packages/langgraph/pregel/main.py:4090: in ainvoke
    async for chunk in self.astream(
.venv/lib/python3.13/site-packages/langgraph/pregel/main.py:3440: in astream
    async for _ in runner.atick(
.venv/lib/python3.13/site-packages/langgraph/pregel/_runner.py:396: in atick
    await arun_with_retry(
.venv/lib/python3.13/site-packages/langgraph/pregel/_retry.py:744: in arun_with_retry
    return await task.proc.ainvoke(task.input, config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.13/site-packages/langgraph/_internal/_runnable.py:733: in ainvoke
    input = await asyncio.create_task(
.venv/lib/python3.13/site-packages/langgraph/_internal/_runnable.py:501: in ainvoke
    ret = await self.afunc(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.13/site-packages/langchain/agents/factory.py:1495: in amodel_node
    model_response = await _execute_model_async(request)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.13/site-packages/langchain/agents/factory.py:1467: in _execute_model_async
    output = await model_.ainvoke(messages)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.13/site-packages/langchain_core/runnables/base.py:6015: in ainvoke
    return await self.bound.ainvoke(
.venv/lib/python3.13/site-packages/langchain_core/language_models/chat_models.py:499: in ainvoke
    llm_result = await self.agenerate_prompt(
.venv/lib/python3.13/site-packages/langchain_core/language_models/chat_models.py:1860: in agenerate_prompt
    return await self.agenerate(
.venv/lib/python3.13/site-packages/langchain_core/language_models/chat_models.py:1818: in agenerate
    raise exceptions[0]
.venv/lib/python3.13/site-packages/langchain_core/language_models/chat_models.py:2151: in _agenerate_with_cache
    result = await self._agenerate(
.venv/lib/python3.13/site-packages/langchain_mistralai/chat_models.py:885: in _agenerate
    response = await acompletion_with_retry(
.venv/lib/python3.13/site-packages/langchain_mistralai/chat_models.py:286: in acompletion_with_retry
    return await _completion_with_retry(**kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.13/site-packages/tenacity/asyncio/__init__.py:193: in async_wrapped
    return await copy(fn, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.13/site-packages/tenacity/asyncio/__init__.py:112: in __call__
    do = await self.iter(retry_state=retry_state)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.13/site-packages/tenacity/asyncio/__init__.py:157: in iter
    result = await action(retry_state)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.13/site-packages/tenacity/_utils.py:111: in inner
    return call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.13/site-packages/tenacity/__init__.py:393: in <lambda>
    self._add_action_func(lambda rs: rs.outcome.result())
                                     ^^^^^^^^^^^^^^^^^^^
../../../.local/share/uv/python/cpython-3.13.12-linux-x86_64-gnu/lib/python3.13/concurrent/futures/_base.py:449: in result
    return self.__get_result()
           ^^^^^^^^^^^^^^^^^^^
../../../.local/share/uv/python/cpython-3.13.12-linux-x86_64-gnu/lib/python3.13/concurrent/futures/_base.py:401: in __get_result
    raise self._exception
.venv/lib/python3.13/site-packages/tenacity/asyncio/__init__.py:116: in __call__
    result = await fn(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
.venv/lib/python3.13/site-packages/langchain_mistralai/chat_models.py:283: in _completion_with_retry
    await _araise_on_error(response)
.venv/lib/python3.13/site-packages/langchain_mistralai/chat_models.py:245: in _araise_on_error
    raise httpx.HTTPStatusError(
E   httpx.HTTPStatusError: Error response 503 while fetching https://api.mistral.ai/v1/chat/completions: upstream connect error or disconnect/reset before headers. reset reason: remote connection failure, transport failure reason: delayed connect error: Connection refused
E   During task with name 'model' and id '5c900b26-c7d0-d34b-2796-e79b973a8267'
```

## 47 passed

### test_adminexpress.py

`test_adminexpress` 4.07s

### test_altitude.py

`test_altitude` 4.96s

### test_assiette_sup.py

`test_assiette_sup` 50.52s

### test_chaining_cadastre_urbanisme.py

`test_chaining_geocode_cadastre_urbanisme` 63.79s

### test_chaining_discovery.py

`test_chaining_discovery` 21.05s

### test_chaining_geocode_adminexpress.py

`test_chaining_geocode_adminexpress` 7.85s

### test_chaining_geocode_altitude.py

`test_chaining_geocode_altitude` 7.60s

### test_chaining_geocode_assiette_sup.py

`test_chaining_geocode_assiette_sup` 24.95s

### test_count_batiment_30m_angouleme.py

`test_count_batiment_30m_angouleme` 15.56s

### test_count_batiment_saint_mande.py

`test_count_batiment_saint_mande` 17.41s

### test_count_lycees_2km_chateau_vincennes.py

`test_count_lycees_2km_chateau_vincennes` 80.16s

### test_describe_type.py

`test_describe_type` 18.41s

### test_france_capital.py

`test_agent_creation_call_and_paris_in_response` 1.02s

### test_geocode.py

`test_geocode` 5.50s

### test_geocode_address_not_found.py

`test_geocode_address_not_found` 9.14s

### test_get_feature_by_id.py

`test_get_feature_by_id` 5.92s

### test_get_features.py

`test_get_features` 175.68s

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

`test_search_batiment` 6.46s

### test_search_ecoles.py

`test_search_ecoles` 19.46s

### test_tools_discovery.py

`test_all_tools_exposed` 0.00s

### test_urbanisme.py

`test_urbanisme` 31.26s
