#!/usr/bin/env bash
# Build and validate using the same entry point locally and in CI.
set -euo pipefail
project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_root"
bash scripts/marmite.sh . site "$@"
python3 - <<'PY'
import json
from pathlib import Path

expected = Path(".marmite-version").read_text().strip()
actual = json.loads(Path("site/marmite.json").read_text())["marmite_version"]
if actual != expected:
    raise SystemExit(f"Built site uses Marmite {actual}, expected {expected}")
print(f"Verified site Marmite version: {actual}")
PY
python3 scripts/check_site.py site
