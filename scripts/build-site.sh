#!/usr/bin/env bash
# =============================================================================
# Baut die Website. Sammelt die Inhalte aus dem Repo-Root nach docs/ (Single
# Source bleibt im Root; docs/ ist generiert und steht in .gitignore) und ruft
# mkdocs build auf.
#
# Lokal:  pip install mkdocs-material && bash scripts/build-site.sh
# CI:     siehe .github/workflows/deploy-docs.yml
# =============================================================================
set -euo pipefail
cd "$(dirname "$0")/.."

SITE_DIR="${1:-_site}"

rm -rf docs
mkdir -p docs

cp README.md          docs/index.md
cp -r anleitung       docs/anleitung
cp -r vorlagen        docs/vorlagen
cp -r template        docs/template
cp CONTRIBUTING.md    docs/CONTRIBUTING.md
cp KONZEPT_WEBSITE.md docs/KONZEPT_WEBSITE.md
cp LICENSE            docs/LICENSE

mkdocs build --site-dir "$SITE_DIR"
echo "Website gebaut nach: $SITE_DIR"
