# geocontext-test

This repository contains an integration test suite designed to validate the correct behavior of the MCP server `ignfab/geocontext` across different language models.

## Purpose

The main goal is to ensure that end-to-end interactions with `ignfab/geocontext` remain stable and consistent when switching model providers or model versions.

## What is tested

- Agent creation using a configured model name
- Real model invocation through integration scenarios
- Functional response checks for expected outputs

## Usage

### Testing with anthropic models

```bash
export MODEL_NAME="anthropic:claude-sonnet-4-6"
export ANTHROPIC_API_KEY=YourKey

uv run pytest
```

### Testing with google models

```bash
export MODEL_NAME="google_genai:gemini-2.5-flash"
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

| Test | Fichier | Outil | Description |
|------|---------|-------|-------------|
| `test_france_capital` | [test_france_capital.py](test_france_capital.py) | aucun (LLM seul) | Test basique sans MCP — vérifie que le LLM répond "Paris" |
| `test_geocode` | [test_geocode.py](test_geocode.py) | `geocode` | Coordonnées du 1 rue de Rivoli, Paris |
| `test_altitude` | [test_altitude.py](test_altitude.py) | `altitude` | Altitude au point (6.87, 45.92) — zone de Chamonix (~1000m) |
| `test_adminexpress` | [test_adminexpress.py](test_adminexpress.py) | `adminexpress` | Commune/département à partir de coordonnées (2.35, 48.85) → Paris, 75 |
| `test_cadastre` | [test_cadastre.py](test_cadastre.py) | `cadastre` | Parcelle cadastrale au 73 av. de Paris, Saint-Mandé |
| `test_urbanisme` | [test_urbanisme.py](test_urbanisme.py) | `urbanisme` | Règles d'urbanisme pour la parcelle 94067000AI0042 |
| `test_assiette_sup` | [test_assiette_sup.py](test_assiette_sup.py) | `assiette_sup` | Servitudes d'utilité publique aux coordonnées (4.83, 45.76) — Lyon |
| `test_describe_type` | [test_describe_type.py](test_describe_type.py) | `gpf_wfs_describe_type` | Attributs de la table BDTOPO_V3:batiment |
| `test_get_features` | [test_get_features.py](test_get_features.py) | `gpf_wfs_get_features` | Bâtiments BDTOPO proches de Chamonix |
| `test_get_feature_by_id` | [test_get_feature_by_id.py](test_get_feature_by_id.py) | `gpf_wfs_get_feature_by_id` | Objet commune.8952 → Aurel (INSEE 26019) |
| `test_search_batiment` | [test_search_batiment.py](test_search_batiment.py) | `gpf_wfs_search_types` | Recherche de tables contenant des bâtiments |
| `test_search_ecoles` | [test_search_ecoles.py](test_search_ecoles.py) | `gpf_wfs_search_types` | Recherche de tables contenant des écoles |

### Tests de chaînage (multi-outils)

| Test | Fichier | Chaîne d'outils | Description |
|------|---------|----------------|-------------|
| `test_chaining_geocode` | [test_chaining_geocode.py](test_chaining_geocode.py) | `geocode` → `altitude` | Altitude de la mairie de Chamonix (~1036m) |
| `test_chaining_geocode_adminexpress` | [test_chaining_geocode_adminexpress.py](test_chaining_geocode_adminexpress.py) | `geocode` → `adminexpress` | 1 rue de Rivoli → commune/département |
| `test_chaining_geocode_assiette_sup` | [test_chaining_geocode_assiette_sup.py](test_chaining_geocode_assiette_sup.py) | `geocode` → `assiette_sup` | 10 place Bellecour, Lyon → servitudes |
| `test_chaining_cadastre_urbanisme` | [test_chaining_cadastre_urbanisme.py](test_chaining_cadastre_urbanisme.py) | `geocode` → `cadastre` → `urbanisme` | Adresse → parcelle → règles PLU |
| `test_chaining_discovery` | [test_chaining_discovery.py](test_chaining_discovery.py) | `gpf_wfs_search_types` → `gpf_wfs_describe_type` → `gpf_wfs_get_features` | Découverte complète : cours d'eau à Toulouse |

### Tests négatifs

| Test | Fichier | Description |
|------|---------|-------------|
| `test_coords_hors_france` | [test_coords_hors_france.py](test_coords_hors_france.py) | Coordonnées en Norvège (10.0, 60.0) — vérifie que l'agent signale le hors périmètre |
| `test_adresse_inexistante` | [test_adresse_inexistante.py](test_adresse_inexistante.py) | Adresse fictive — vérifie que l'agent signale l'absence de résultat |

## Derniers résultats de tests

**Date** : 29 June 2026
**Modèle** : `anthropic:claude-haiku-4-5`
**Serveur MCP** : `geocontext@0.9.8`
**Nombre de tests** : 20

### Run — 20/20 passed (2 min 11 s)

| Test | Résultat | Détail |
|------|----------|--------|
| test_adminexpress | ✅ PASSED | |
| test_altitude | ✅ PASSED | |
| test_assiette_sup | ✅ PASSED | |
| test_adresse_inexistante | ✅ PASSED | |
| test_cadastre | ✅ PASSED | |
| test_chaining_geocode_altitude | ✅ PASSED | |
| test_chaining_geocode_cadastre_urbanisme | ✅ PASSED | |
| test_chaining_geocode_adminexpress | ✅ PASSED | |
| test_chaining_discovery | ✅ PASSED | |
| test_coords_hors_france | ✅ PASSED | |
| test_agent_creation_call_and_paris_in_response | ✅ PASSED | |
| test_chaining_geocode_assiette_sup | ✅ PASSED | |
| test_geocode | ✅ PASSED | |
| test_get_feature_by_id | ✅ PASSED | |
| test_describe_type | ✅ PASSED | |
| test_chaining_geocode_altitude | ✅ PASSED | |
| test_search_ecoles | ✅ PASSED | |
| test_get_features | ✅ PASSED | |
| test_all_tools_exposed | ✅ PASSED | |
| test_urbanisme | ✅ PASSED | |

### Observations

- **20 tests sur 20 sont passés**
- Les 10 outils MCP sont tous couverts.
## Couverture des outils MCP

| Outil | Test direct | Test en chaînage | Couvert |
|-------|------------|-----------------|---------|
| `geocode` | `test_geocode` | 5 tests de chaînage | ✅ |
| `altitude` | `test_altitude` | `test_chaining_geocode` | ✅ |
| `adminexpress` | `test_adminexpress` | `test_chaining_geocode_adminexpress` | ✅ |
| `cadastre` | `test_cadastre` | `test_chaining_cadastre_urbanisme` | ✅ |
| `urbanisme` | `test_urbanisme` | `test_chaining_cadastre_urbanisme` | ✅ |
| `assiette_sup` | `test_assiette_sup` | `test_chaining_geocode_assiette_sup` | ✅ |
| `gpf_wfs_search_types` | `test_search_batiment`, `test_search_ecoles` | `test_chaining_discovery` | ✅ |
| `gpf_wfs_describe_type` | `test_describe_type` | `test_chaining_discovery` | ✅ |
| `gpf_wfs_get_features` | `test_get_features` | `test_chaining_discovery` | ✅ |
| `gpf_wfs_get_feature_by_id` | `test_get_feature_by_id` | — | ✅ |

## Cas critiques non couverts

| Cas | Criticité | Description |
|-----|-----------|-------------|
| Adresse ambiguë | Moyenne | Pas de test avec une adresse qui matche plusieurs résultats (ex: "rue de la République" sans ville) |
| DOM-TOM / Outre-mer | Moyenne | Pas de test sur les territoires ultramarins (Réunion, Guadeloupe) |
| Erreur réseau / tool error recovery | Basse | Pas de test sur la capacité de l'agent à retenter après une erreur d'outil |

## License

[MIT](LICENSE)

