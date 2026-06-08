# =============================================================================
# Makefile -- FOM LaTeX-Vorlage
#
# Die wichtigsten Befehle:
#   make            -> PDF bauen (main.pdf) via Docker (Tectonic)
#   make clean      -> Build-Hilfsdateien löschen
#   make check      -> einfache Qualitätsprüfung (vor jedem Commit)
#   make release    -> versionierte Kopie der PDF in releases/ ablegen
#   make shell      -> Shell im Docker-Container öffnen (Debugging)
#
# Wer kein Docker nutzt: siehe README.md (Overleaf oder lokales Tectonic).
# =============================================================================

.PHONY: pdf clean check release shell all

# Standard: PDF bauen
pdf:
	docker compose up --build

# Aufräumen (PDF bleibt erhalten)
clean:
	rm -f main.aux main.log main.toc main.lof main.lot \
	      main.bbl main.bcf main.blg main.run.xml main.out \
	      main.fdb_latexmk main.fls main.synctex.gz \
	      main.acn main.acr main.alg main.glg main.glo main.gls main.ist

# Qualitätsprüfung -- alles sollte "OK" melden
check:
	@echo "=== 1. BibLaTeX: langid-Abdeckung (jeder Eintrag braucht langid) ==="
	@echo "    $$(grep -cE '^@' literatur/literatur.bib) Einträge, $$(grep -cE '^[[:space:]]*langid' literatur/literatur.bib) mit langid"
	@echo "=== 2. Falsche Anführungszeichen (glqq/grqq statt enquote) ==="
	@! grep -rn 'glqq\|grqq' kapitel/ 2>/dev/null && echo "    OK" || echo "    !! WARNUNG: \\enquote{} verwenden"
	@echo "=== 3. Zitate ohne Seitenangabe ( [...][] ) ==="
	@! grep -rnE '(auto|foot)cite\[[^]]*\]\[\]' kapitel/ 2>/dev/null && echo "    OK" || echo "    !! WARNUNG: Seitenangabe fehlt (oder bewusst o.S.)"
	@echo "=== 4. Leere Fußnoten ==="
	@! grep -rn 'footnote{}' kapitel/ 2>/dev/null && echo "    OK" || echo "    !! WARNUNG: leere Fußnote"
	@echo "=== 5. Ich-/Wir-Form (Stichprobe) ==="
	@! grep -rnwiE 'ich|wir|meiner meinung|unseres erachtens' kapitel/ 2>/dev/null && echo "    OK" || echo "    Hinweis: neutrale, unpersönliche Formulierung prüfen"

# Versionierte Kopie der fertigen PDF ablegen (statt nur "main.pdf").
# Ergebnis: releases/main_JJJJMMTT_HHMM_<commit>.pdf
release: pdf
	@mkdir -p releases
	@cp main.pdf releases/main_$$(date +%Y%m%d_%H%M)_$$(git rev-parse --short HEAD 2>/dev/null || echo nogit).pdf
	@echo "Release abgelegt: releases/main_$$(date +%Y%m%d_%H%M)_$$(git rev-parse --short HEAD 2>/dev/null || echo nogit).pdf"

# Shell im Container (für Fehlersuche)
shell:
	docker compose run --entrypoint /bin/bash latex

all: pdf
