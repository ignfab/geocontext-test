#!/usr/bin/env python3
"""Run the pytest suite against several models and write one report per model.

Portable replacement for the old Makefile (works on Windows and Linux).

Usage:
    python scripts/run_tests.py config/models-anthropic.yaml                          # run every model in the file
    python scripts/run_tests.py config/models-ollama.yaml --list                      # show the models in the file
    python scripts/run_tests.py config/models-anthropic.yaml --model claude-haiku-4-5  # run a single model

Extra arguments after "--" are forwarded to pytest, e.g.:
    python scripts/run_tests.py config/models-anthropic.yaml -- -k geocode -x

The models to run are defined in the YAML file given as MODELS_PATH.
"""
import argparse
import os
import subprocess
from pathlib import Path

import yaml

# Repository root (this file lives in <root>/scripts/).
ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = ROOT / "reports"


def load_models(config_path: Path) -> dict[str, dict]:
    """Load the model definitions from a YAML file.

    Expected shape (key -> {model, report}):
        claude-haiku-4-5:
          model: anthropic:claude-haiku-4-5
          report: claude-haiku-4-5.md
    """
    try:
        data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Config file not found: {config_path}")
    except yaml.YAMLError as exc:
        raise SystemExit(f"Invalid YAML in {config_path}: {exc}")

    if not isinstance(data, dict) or not data:
        raise SystemExit(f"No models defined in {config_path}")

    for key, entry in data.items():
        if not isinstance(entry, dict) or "model" not in entry or "report" not in entry:
            raise SystemExit(f"Model '{key}' must define 'model' and 'report' in {config_path}")
    return data


def run_model(key: str, entry: dict, pytest_extra: list[str]) -> int:
    model_name = entry["model"]
    report_path = REPORTS_DIR / entry["report"]

    env = os.environ.copy()
    env["MODEL_NAME"] = model_name

    cmd = ["uv", "run", "pytest", "-v", "--tb=short", "--md", str(report_path), *pytest_extra]
    print(f"\n=== {key}  (MODEL_NAME={model_name}) ===", flush=True)
    print(f"$ {' '.join(cmd)}", flush=True)

    # shell=True on Windows so the "uv" launcher (uv.exe / uv.cmd) is resolved.
    completed = subprocess.run(cmd, cwd=ROOT, env=env, shell=(os.name == "nt"))
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("models_path", metavar="MODELS_PATH", type=Path,
                        help="YAML file defining the models to run.")
    parser.add_argument("--list", action="store_true", help="List available models and exit.")
    parser.add_argument("--model", metavar="KEY",
                        help="Run only this model (key from the YAML file) instead of all of them.")
    args, pytest_extra = parser.parse_known_args()

    models = load_models(args.models_path)

    if args.list:
        for key, entry in models.items():
            print(f"{key:24} {entry['model']:40} -> reports/{entry['report']}")
        return 0

    if args.model is not None:
        if args.model not in models:
            available = ", ".join(models)
            raise SystemExit(f"Unknown model '{args.model}'. Available models: {available}")
        selected = [args.model]
    else:
        selected = list(models)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    failures: dict[str, int] = {}
    for key in selected:
        code = run_model(key, models[key], pytest_extra)
        if code != 0:
            failures[key] = code

    print("\n=== Summary ===")
    for key in selected:
        status = f"FAILED ({failures[key]})" if key in failures else "ok"
        print(f"  {key:24} {status}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
