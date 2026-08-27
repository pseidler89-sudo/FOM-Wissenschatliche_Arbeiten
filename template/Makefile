# =============================================================================
# Makefile -- FOM LaTeX-Vorlage
#
# Die wichtigsten Befehle:
#   make            -> PDF bauen (main.pdf) via Docker (Tectonic)
#   make clean      -> Build-Hilfsdateien löschen
#   make check      -> einfache Qualitätsprüfung (vor jedem Commit)
#   make formalia-check -> prüft die Formalia gegen FORMALIA.md (vor der Abgabe)
#   make release    -> versionierte Kopie der PDF in releases/ ablegen
#   make shell      -> Shell im Docker-Container öffnen (Debugging)
#
# Wer kein Docker nutzt: siehe README.md (Overleaf oder lokales Tectonic).
# =============================================================================

.PHONY: pdf clean check formalia-check release shell all

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
	@# erklaerung.tex und sperrvermerk.tex sind ausgenommen -- die Eigenständig-
	@# keitserklärung MUSS in der Ich-Form stehen.
	@! grep -rnwiE 'ich|wir|meiner meinung|unseres erachtens' kapitel/ \
	    --exclude=erklaerung.tex --exclude=sperrvermerk.tex 2>/dev/null \
	  && echo "    OK" || echo "    Hinweis: neutrale, unpersönliche Formulierung prüfen"
	@echo "=== 6. Normverweise als Fundstelle in der Fussnote ==="
	@# Was hier gesucht wird: Faelle, in denen die NORM SELBST die Fundstelle
	@# der Fussnote ist -- \autocite[Vgl.][Art.~5 Abs.~1]{eu_ai_act}. Der
	@# Normverweis gehoert in den Fliesstext, die Fussnote traegt den
	@# bibliographischen Kurzbeleg der Literatur DAZU.
	@#
	@# Bewusst NICHT gemeldet werden Fundstellen, die zusaetzlich Rn. oder eine
	@# Seitenzahl nennen: "\S~2 Rn.~3" ist der uebliche und korrekte Beleg in
	@# einen Kommentar hinein, "Rn.~37" der korrekte Beleg in ein Urteil.
	@# Ohne diese Unterscheidung meldet die Pruefung in einer juristischen
	@# Arbeit dutzendfach richtige Zitate -- und wird dann zu Recht ignoriert.
	@T=$$(grep -rnoE '(auto|foot)cite(\[[^]]*\])?\[[^]]*(§|\\S~|Art\.)[^]]*\]' kapitel/ 2>/dev/null \
	      | grep -vE 'Rn\.|S\.~?[0-9]'); \
	 if [ -z "$$T" ]; then echo "    OK"; else \
	   echo "$$T" | sed 's|^|    |'; \
	   echo "    !! WARNUNG: $$(echo "$$T" | wc -l) Stellen -- Norm als Fundstelle der Fussnote."; \
	   echo "       Richtig: Normverweis in den Fliesstext, die Fussnote belegt die Literatur dazu."; \
	 fi
	@echo "=== 7. Quellenmix (Verteilung der Eintragstypen, nur zur Info) ==="
	@# Breite schlägt Menge: kein Warnwert, aber die Verteilung sollte nicht
	@# aus einer einzigen Kategorie bestehen (siehe ../vorlagen/gutachten-regeln.md).
	@grep -oE '^@[a-zA-Z]+' literatur/literatur.bib 2>/dev/null | sort | uniq -c | sort -rn | sed 's/^/    /' \
	  || echo "    (literatur/literatur.bib nicht gefunden)"

# Formalia-Prüfung -- vor der Abgabe. Prüft, was maschinell prüfbar ist;
# alles andere steht in ../vorlagen/review-checkliste.md.
formalia-check:
	@echo "=== 1. Umfang des Textteils (Wörter, nur kapitel/) ==="
	@SOLL=$$(grep -oE '^- \*\*Umfangsvorgabe:\*\*[^0-9]*([0-9]+)' FORMALIA.md 2>/dev/null \
	         | grep -oE '[0-9]+$$'); \
	 if [ -n "$$SOLL" ]; then python3 skripte/umfang.py --soll $$SOLL; \
	 else python3 skripte/umfang.py; fi
	@echo "=== 2. Gewählter Leitfaden in der Einleitung genannt? ==="
	@grep -qE 'formaliaLeitfadenSatz|Leitfaden' kapitel/01_einleitung.tex 2>/dev/null \
	  && echo "    OK" \
	  || echo "    !! Den gewählten Leitfaden in der Methodik-Passage nennen -- das ist selbst eine Formvorgabe (\\formaliaLeitfadenSatz)"
	@echo "=== 3. KI-Hilfsmittelverzeichnis ausgefüllt? ==="
	@if grep -qiE 'Platzhalter|TODO|Beispiel-?Eintrag|XXX' verzeichnisse/ki_verzeichnis.tex 2>/dev/null; then \
	   echo "    !! WARNUNG: Platzhaltertext im KI-Verzeichnis"; \
	 else echo "    OK"; fi
	@echo "=== 4. FORMALIA.md vorhanden und ausgefüllt? ==="
	@if [ ! -f FORMALIA.md ]; then \
	   echo "    !! FORMALIA.md fehlt -- Vorlage: ../vorlagen/FORMALIA_VORLAGE.md"; \
	 elif grep -qE '<[a-zäöü ]+>|TODO' FORMALIA.md; then \
	   echo "    !! FORMALIA.md enthält noch Platzhalter"; \
	 else echo "    OK"; fi
	@echo "=== 5. Alter des Formalia-Profils ==="
	@for f in formalia/profil_wi.tex formalia/profil_jks.tex; do \
	   D=$$(grep -oE 'Ausgewertet am[^0-9]*([0-9]{4}-[0-9]{2}-[0-9]{2})' $$f | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}'); \
	   if [ -n "$$D" ]; then \
	     A=$$(( ( $$(date +%s) - $$(date -d "$$D" +%s) ) / 86400 )); \
	     if [ $$A -gt 365 ]; then echo "    !! $$f: seit $$A Tagen nicht geprüft -- aktuelle Fassung aus dem Online-Campus holen"; \
	     else echo "    OK  $$f ($$A Tage)"; fi; \
	   fi; \
	 done
	@echo "=== 6. Kapitel-Einleitung (2-4 Sätze) vor der ersten Unterüberschrift? ==="
	@# Zwischen Kapitelüberschrift (\section) und erster \subsection stehen
	@# 2-4 einleitende Sätze (JKS Kap. 1.5.1) -- gilt nicht für die Einleitung.
	@FEHLT=0; for f in kapitel/*.tex; do \
	   case "$$f" in *einleitung*|*erklaerung*|*sperrvermerk*|*titelseite*) continue;; esac; \
	   awk -v file="$$f" ' \
	     /\\section\{/  {chap=1; body=0; next} \
	     chap && /\\subsection\{/ {if (!body) {print "    !! " file ": zwischen \\section und erster \\subsection fehlt die Kapitel-Einleitung"; exit 1} exit 0} \
	     chap && !/^[[:space:]]*($$|%)/ && !/^\\label/ {body=1} \
	   ' "$$f" || FEHLT=1; \
	 done; \
	 [ $$FEHLT -eq 0 ] && echo "    OK" || true

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
