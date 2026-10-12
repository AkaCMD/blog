#!/usr/bin/env python3
"""Print or lock the latest stable Marmite version published on crates.io."""
import argparse
import json
import re
from pathlib import Path
from urllib.request import Request, urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--update", action="store_true", help="Update the repository's .marmite-version")
    args = parser.parse_args()
    request = Request(
        "https://crates.io/api/v1/crates/marmite",
        headers={"User-Agent": "Memex-blog-build (https://github.com/AkaCMD/blog)"},
    )
    with urlopen(request, timeout=30) as response:
        version = json.load(response)["crate"]["max_stable_version"]
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise SystemExit("crates.io did not return a stable Marmite version")
    if args.update:
        lock = Path(__file__).resolve().parent.parent / ".marmite-version"
        lock.write_text(version + "\n")
        print(f"Updated {lock.name} to {version}; build and validate before committing.")
    else:
        print(version)


if __name__ == "__main__":
    main()
