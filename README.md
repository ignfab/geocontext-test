# geocontext-test

This repository contains an integration test suite designed to validate the correct behavior of the MCP server `ignfab/geocontext` across different language models.

## Purpose

The main goal is to ensure that end-to-end interactions with `ignfab/geocontext` remain stable and consistent when switching model providers or model versions.

## What is tested

- Agent creation using a configured model name
- Real model invocation through integration scenarios
- Functional response checks for expected outputs

## Quick Start

See [CODING.md](CODING.md) for comprehensive setup instructions including:
- Environment configuration and API key setup
- Running tests with different models
- Testing a local version of geocontext
- Debugging and troubleshooting

## Reports

Generated with geocontext v0.9.8 :

- [reports/claude-haiku-4-5.md](reports/claude-haiku-4-5.md) : OK
- [reports/claude-sonnet-4-6.md](reports/claude-sonnet-4-6.md) : OK
- [reports/gemini-3.5-flash.md](reports/gemini-3.5-flash.md) : OK
- [reports/gemini-3.1-flash-lite.md](reports/gemini-3.1-flash-lite.md) : 1 test KO (`gpf_wfs_describe_type tool was not called`)
- [reports/gemma4-26b-moe.md](reports/gemma4-26b-moe.md) : 2 tests KO (ERP, `gpf_wfs_describe_type tool was not called`)
- [reports/qwen3-6-35b-moe.md](reports/qwen3-6-35b-moe.md) : 2 test KO (ERP and detailed counts for [test_count_lycees_2km_chateau_vincennes.py](test_count_lycees_2km_chateau_vincennes.py)...)
- [reports/ministral-14b-latest.md](reports/ministral-14b-latest.md) : 3 tests KO (ERP and prompt ignored for [test_geocode_address_not_found.py](test_geocode_address_not_found.py))
- [reports/mistral-small-latest.md](reports/mistral-small-latest.md) : 1 test KO (ERP)
- [reports/mistral-medium-latest.md](reports/mistral-medium-latest.md) : OK
- [reports/albert-openai-gpt-oss-120b.md](reports/albert-openai-gpt-oss-120b.md) : 2 tests KO (ERP)

> About ERP, see [gpf-schema-store#48](https://github.com/ignfab/gpf-schema-store/issues/48) and [gpf-schema-store#56](https://github.com/ignfab/gpf-schema-store/issues/56) 

Running the tests also writes the details of each conversation to `reports/<model>/<test name>.txt`
(not versioned, see [CODING.md](CODING.md)).

## Usage

### Testing with reports

```bash
export ANTHROPIC_API_KEY=YourKey

# to run with some anthropic model
uv run scripts/run_tests.py config/models-anthropic.yaml
# to rerun with a single model
uv run scripts/run_tests.py config/models-anthropic.yaml --model=claude-haiku-4-5
```

### Testing with anthropic models

```bash
export MODEL_NAME="anthropic:claude-sonnet-4-6"
export ANTHROPIC_API_KEY=YourKey

uv run pytest
```

### Testing with google models

```bash
export MODEL_NAME="google_genai:gemini-3.5-flash"
export GOOGLE_API_KEY=YourKey

uv run pytest
```

```bash
export MODEL_NAME="google_genai:gemini-3.1-flash-lite-preview"
export GOOGLE_API_KEY=YourKey

uv run pytest
```

## Tests

> Tool names are given for geocontext 0.10.x (`GEOCONTEXT_DEV=1`). With 0.9.x, `gpf_*` tools are named `gpf_wfs_*`, counts rely on `gpf_wfs_get_features` and tests using `distance` are skipped (see [config/constants.py](config/constants.py)).

### Single tool tests

| File                                                   | Tool                    | Description                                                                 |
| ------------------------------------------------------ | ----------------------- | --------------------------------------------------------------------------- |
| [test_france_capital.py](test_france_capital.py)       | none (LLM only)         | Basic test without MCP: checks that the LLM answers "Paris"                 |
| [test_tools_discovery.py](test_tools_discovery.py)     | none (tool listing)     | Checks that all the expected tools are exposed by the MCP server            |
| [test_geocode.py](test_geocode.py)                     | `geocode`               | Coordinates of 1 rue de Rivoli, Paris                                       |
| [test_altitude.py](test_altitude.py)                   | `altitude`              | Altitude at (6.87, 45.92), Chamonix area (900-1200 m)                       |
| [test_adminexpress.py](test_adminexpress.py)           | `adminexpress`          | Commune and department at (2.35, 48.85): Paris, 75                          |
| [test_cadastre.py](test_cadastre.py)                   | `cadastre`              | Cadastral parcel at 73 avenue de Paris, Saint-Mandé                         |
| [test_urbanisme.py](test_urbanisme.py)                 | `urbanisme`             | Urban planning rules at 73 avenue de Paris, Saint-Mandé                     |
| [test_assiette_sup.py](test_assiette_sup.py)           | `assiette_sup`          | Public utility easements at (4.83, 45.76), Lyon                             |
| [test_describe_type.py](test_describe_type.py)         | `gpf_describe_type`     | Attributes of the `BDTOPO_V3:batiment` table                                |
| [test_get_features.py](test_get_features.py)           | `gpf_get_features`      | BD TOPO buildings near Chamonix                                             |
| [test_get_feature_by_id.py](test_get_feature_by_id.py) | `gpf_get_feature_by_id` | `code_insee` of a commune given its `feature_id` (first commune of the WFS) |
| [test_search_batiment.py](test_search_batiment.py)     | `gpf_search_types`      | Search for tables about buildings                                           |
| [test_search_ecoles.py](test_search_ecoles.py)         | `gpf_search_types`      | Search for tables about schools                                             |

### Chaining tests (multiple tools)

| File                                                                                     | Tool chain                                                                             | Description                                                                                         |
| ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [test_chaining_geocode_altitude.py](test_chaining_geocode_altitude.py)                   | `geocode` → `altitude`                                                                 | Altitude of Chamonix town hall (900-1200 m)                                                         |
| [test_chaining_geocode_adminexpress.py](test_chaining_geocode_adminexpress.py)           | `geocode` → `adminexpress`                                                             | 1 rue de Rivoli → commune and department                                                            |
| [test_chaining_geocode_assiette_sup.py](test_chaining_geocode_assiette_sup.py)           | `geocode` → `assiette_sup`                                                             | 10 place Bellecour, Lyon → public utility easements                                                 |
| [test_chaining_cadastre_urbanisme.py](test_chaining_cadastre_urbanisme.py)               | `geocode` → `cadastre` → `urbanisme`                                                   | Address → parcel → urban planning rules                                                             |
| [test_chaining_discovery.py](test_chaining_discovery.py)                                 | `gpf_search_types` → `gpf_describe_type` → `gpf_get_features`                          | Full discovery: watercourse near the Eiffel Tower (Seine)                                           |
| [test_count_batiment_saint_mande.py](test_count_batiment_saint_mande.py)                 | `geocode` → `gpf_search_types` → `gpf_count_features`                                  | Number of buildings in Saint-Mandé (1700-1800)                                                      |
| [test_count_batiment_30m_angouleme.py](test_count_batiment_30m_angouleme.py)             | `geocode` → `gpf_search_types` → `gpf_describe_type` → `gpf_count_features`            | Number of buildings higher than 30 m in Angoulême (19)                                              |
| [test_count_lycees_2km_chateau_vincennes.py](test_count_lycees_2km_chateau_vincennes.py) | `geocode` → `gpf_search_types` → `gpf_describe_type` → `gpf_count_features`            | Number of high schools within 2 km of the Château de Vincennes (14)                                 |
| [test_chaining_geocode_distance.py](test_chaining_geocode_distance.py)                   | `geocode` → `distance`                                                                 | Walking distance between the Gare de Lyon and the Eiffel Tower (5-9 km)                             |
| [test_chaining_distance_piscine_caen.py](test_chaining_distance_piscine_caen.py)         | `geocode` → `gpf_search_types` → `gpf_describe_type` → `gpf_get_features` → `distance` | Walking time from the cinéma LUX (Caen) to the nearest swimming pool: Sivom, Mondeville (25-35 min) |

### Negative tests

| File                                                                   | Description                                                               |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [test_geocode_address_not_found.py](test_geocode_address_not_found.py) | Non-existent address: checks that the agent reports "adresse non trouvée" |

### MCP server tests (no model)

| File                                               | Description                                                                                                                                                                       |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [test_mcp_concurrency.py](test_mcp_concurrency.py) | Concurrent tool calls must not be crossed. Skipped by default until [#33](https://github.com/ignfab/geocontext-test/issues/33) is fixed (`SKIP_TEST_MCP_CONCURRENCY=0` to run it) |

## Critical cases not covered

| Case                                | Criticality | Description                                                                                       |
| ----------------------------------- | ----------- | ------------------------------------------------------------------------------------------------- |
| Ambiguous address                   | Medium      | No test with an address matching several results (e.g. "rue de la République" without a city)    |
| Overseas territories (DOM-TOM)      | Medium      | No test on overseas territories (Réunion, Guadeloupe)                                             |
| Network error / tool error recovery | Low         | No test of the agent's ability to retry after a tool error                                        |

## License

[MIT](LICENSE)

