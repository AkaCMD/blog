#!/usr/bin/env bash
# Use the repository's Marmite version without relying on PATH.
set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
version="$(cat "$project_root/.marmite-version")"
if [[ ! "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Invalid stable version in .marmite-version: $version" >&2
  exit 1
fi

if [[ "${1:-}" == --locked-version ]]; then
  printf '%s\n' "$version"
  exit 0
fi

marmite_root="${MARMITE_INSTALL_ROOT:-${XDG_DATA_HOME:-$HOME/.local/share}/memex-marmite}/$version"
binary="$marmite_root/bin/marmite"
if [[ ! -x "$binary" ]] || [[ "$("$binary" --version)" != "marmite $version" ]]; then
  rustup update stable --no-self-update >&2
  cargo +stable install marmite --version "$version" --locked --force --root "$marmite_root" >&2
fi
if [[ "$("$binary" --version)" != "marmite $version" ]]; then
  echo "Installed Marmite does not match .marmite-version ($version)" >&2
  exit 1
fi

if [[ "${1:-}" == --ensure ]]; then
  "$binary" --version
  exit 0
fi
exec "$binary" "$@"
