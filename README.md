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
- [reports/gemini-3.1-flash-lite.md](reports/gemini-3.1-flash-lite.md) : OK
- [reports/gemma4-26b-moe.md](reports/gemma4-26b-moe.md) : OK
- [reports/qwen3-6-35b-moe.md](reports/qwen3-6-35b-moe.md) : OK


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

### Tests directs (un seul outil)

| Test                     | Fichier                                                | Outil                       | Description                                                           |
| ------------------------ | ------------------------------------------------------ | --------------------------- | --------------------------------------------------------------------- |
| `test_france_capital`    | [test_france_capital.py](test_france_capital.py)       | aucun (LLM seul)            | Test basique sans MCP — vérifie que le LLM répond "Paris"             |
| `test_geocode`           | [test_geocode.py](test_geocode.py)                     | `geocode`                   | Coordonnées du 1 rue de Rivoli, Paris                                 |
| `test_altitude`          | [test_altitude.py](test_altitude.py)                   | `altitude`                  | Altitude au point (6.87, 45.92) — zone de Chamonix (~1000m)           |
| `test_adminexpress`      | [test_adminexpress.py](test_adminexpress.py)           | `adminexpress`              | Commune/département à partir de coordonnées (2.35, 48.85) → Paris, 75 |
| `test_cadastre`          | [test_cadastre.py](test_cadastre.py)                   | `cadastre`                  | Parcelle cadastrale au 73 av. de Paris, Saint-Mandé                   |
| `test_urbanisme`         | [test_urbanisme.py](test_urbanisme.py)                 | `urbanisme`                 | Règles d'urbanisme pour la parcelle 94067000AI0042                    |
| `test_assiette_sup`      | [test_assiette_sup.py](test_assiette_sup.py)           | `assiette_sup`              | Servitudes d'utilité publique aux coordonnées (4.83, 45.76) — Lyon    |
| `test_describe_type`     | [test_describe_type.py](test_describe_type.py)         | `gpf_wfs_describe_type`     | Attributs de la table BDTOPO_V3:batiment                              |
| `test_get_features`      | [test_get_features.py](test_get_features.py)           | `gpf_wfs_get_features`      | Bâtiments BDTOPO proches de Chamonix                                  |
| `test_get_feature_by_id` | [test_get_feature_by_id.py](test_get_feature_by_id.py) | `gpf_wfs_get_feature_by_id` | Objet commune.8952 → Aurel (INSEE 26019)                              |
| `test_search_batiment`   | [test_search_batiment.py](test_search_batiment.py)     | `gpf_wfs_search_types`      | Recherche de tables contenant des bâtiments                           |
| `test_search_ecoles`     | [test_search_ecoles.py](test_search_ecoles.py)         | `gpf_wfs_search_types`      | Recherche de tables contenant des écoles                              |

### Tests de chaînage (multi-outils)

| Test                                 | Fichier                                                                        | Chaîne d'outils                                                           | Description                                  |
| ------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------- | -------------------------------------------- |
| `test_chaining_geocode`              | [test_chaining_geocode_altitude.py](test_chaining_geocode_altitude.py)                           | `geocode` → `altitude`                                                    | Altitude de la mairie de Chamonix (~1036m)   |
| `test_chaining_geocode_adminexpress` | [test_chaining_geocode_adminexpress.py](test_chaining_geocode_adminexpress.py) | `geocode` → `adminexpress`                                                | 1 rue de Rivoli → commune/département        |
| `test_chaining_geocode_assiette_sup` | [test_chaining_geocode_assiette_sup.py](test_chaining_geocode_assiette_sup.py) | `geocode` → `assiette_sup`                                                | 10 place Bellecour, Lyon → servitudes        |
| `test_chaining_cadastre_urbanisme`   | [test_chaining_cadastre_urbanisme.py](test_chaining_cadastre_urbanisme.py)     | `geocode` → `cadastre` → `urbanisme`                                      | Adresse → parcelle → règles PLU              |
| `test_chaining_discovery`            | [test_chaining_discovery.py](test_chaining_discovery.py)                       | `gpf_wfs_search_types` → `gpf_wfs_describe_type` → `gpf_wfs_get_features` | Découverte complète : cours d'eau à Toulouse |

### Tests négatifs

| Test                       | Fichier                                                    | Description                                                                         |
| -------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `test_geocode_address_not_found` | [test_geocode_address_not_found.py](test_geocode_address_not_found.py) | Adresse fictive — vérifie que l'agent signale l'absence de résultat                 |

## Cas critiques non couverts

| Cas                                 | Criticité | Description                                                                                         |
| ----------------------------------- | --------- | --------------------------------------------------------------------------------------------------- |
| Adresse ambiguë                     | Moyenne   | Pas de test avec une adresse qui matche plusieurs résultats (ex: "rue de la République" sans ville) |
| DOM-TOM / Outre-mer                 | Moyenne   | Pas de test sur les territoires ultramarins (Réunion, Guadeloupe)                                   |
| Erreur réseau / tool error recovery | Basse     | Pas de test sur la capacité de l'agent à retenter après une erreur d'outil                          |

## License

[MIT](LICENSE)

