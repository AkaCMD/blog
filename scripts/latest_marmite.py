#!/usr/bin/env python3
"""Print the latest stable Marmite version published on crates.io."""
import json
import re
from urllib.request import Request, urlopen


def main():
    request = Request(
        "https://crates.io/api/v1/crates/marmite",
        headers={"User-Agent": "Memex-blog-build (https://github.com/AkaCMD/blog)"},
    )
    with urlopen(request, timeout=30) as response:
        version = json.load(response)["crate"]["max_stable_version"]
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise SystemExit("crates.io did not return a stable Marmite version")
    print(version)


if __name__ == "__main__":
    main()
