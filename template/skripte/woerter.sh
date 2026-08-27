#!/usr/bin/env bash
# =============================================================================
# Zaehlt die Woerter des Textteils aus der gebauten PDF.
#
#   ./skripte/woerter.sh <erste-Seite> <letzte-Seite>
#
# Gezaehlt wird so, wie manche Pruefende es vorgeben (z. B. Modul
# Wissenschaftliches Arbeiten): Fliesstext INKLUSIVE Kapitelueberschriften und
# Fussnoten. Deshalb wird aus der PDF gezaehlt und nicht aus den TeX-Quellen --
# im TeX steht der Beleg nur als \autocite-Schluessel, in der PDF steht die
# ausgeschriebene Fussnote, und die zaehlt mit.
#
# Die Seitenzahlen sind die PHYSISCHEN Seiten der PDF (Titelblatt = 1).
# Nachsehen, wo der Textteil beginnt und endet -- er ist der Bereich mit
# arabischer Seitenzahl vor dem Anhang.
# =============================================================================
set -euo pipefail
cd "$(dirname "$0")/.."

von="${1:-}"; bis="${2:-}"
if [ -z "$von" ] || [ -z "$bis" ]; then
  echo "Aufruf: ./skripte/woerter.sh <erste-Seite> <letzte-Seite>" >&2
  echo "Beispiel: ./skripte/woerter.sh 4 11" >&2
  exit 1
fi
[ -f main.pdf ] || { echo "main.pdf fehlt -- erst bauen." >&2; exit 1; }
command -v pdftotext >/dev/null || { echo "pdftotext fehlt." >&2; exit 1; }

# Kopfzeile ist die blanke Seitenzahl rechts -- die zaehlt nicht als Wort.
n=$(pdftotext -f "$von" -l "$bis" main.pdf - \
    | grep -vE '^[[:space:]]*[0-9]+[[:space:]]*$' \
    | wc -w)

printf '\n  Seiten %s-%s: %s Woerter\n' "$von" "$bis" "$n"
printf "  Rahmen laut FORMALIA.md pruefen (z. B. 2000 +/- 10%%)\n"
printf '  Wert in skripte/meta.tex bei \\myWortzahl eintragen.\n\n'

# Hinweis: skripte/umfang.py zaehlt aus den TeX-Quellen (Fliesstext plus
# Ueberschriften, Fussnoten getrennt ausgewiesen). Das ist beim Schreiben
# praktisch, unterschaetzt aber die Fussnoten -- dort steht der Beleg nur als
# \autocite-Schluessel. Massgeblich fuer die Angabe auf dem Titelblatt ist
# dieses Skript hier.
