# LaTeX-Vorlage (FOM)

Dies ist die **fertige, baubare LaTeX-Vorlage**. Sie ist FOM-konform
vorkonfiguriert (Seitenränder, Schrift, Zeilenabstand, Fußnoten-Zitation,
KI-Verzeichnis). Du musst LaTeX **nicht** verstehen, um sie zu nutzen.

> Die ausführliche Schritt-für-Schritt-Erklärung – von der Forschungsfrage
> über die KI-gestützte Recherche bis zur fertigen PDF – steht in
> [`../anleitung/`](../anleitung/00_ueberblick.md). Diese Datei hier ist die Kurzanleitung
> nur zur Vorlage.

---

## In 5 Schritten zur PDF

1. **Diesen `template/`-Ordner kopieren** (oder das ganze Repo als ZIP laden).
2. **`skripte/meta.tex` öffnen** und deine Daten eintragen (Titel, Name,
   Matrikelnummer, Modul, Datum). Das ist die einzige Datei mit deinen
   persönlichen Angaben.
3. **In `kapitel/` schreiben.** Jede `.tex`-Datei ist ein Kapitel. Fang in
   `01_einleitung.tex` an. `main.tex` musst du nur anfassen, um ein **neues**
   Kapitel einzubinden.
4. **Quellen in `literatur/literatur.bib`** eintragen (Beispiele für jeden
   Quellentyp sind schon drin).
5. **PDF bauen** – siehe unten. Ergebnis ist `main.pdf`.

> ℹ️ **Die Kapitel sind nur ein Beispielgerüst.** `01_einleitung`,
> `02_grundlagen`, `03_hauptteil`, `04_fazit` zeigen Aufbau und Befehle – sie
> sind **kein Pflicht-Schema**. Lösche, benenne um oder ergänze Kapitel, wie es
> deine Forschungsfrage verlangt (z. B. eigene Analyse- und Fallstudien-Kapitel,
> oder bei empirischen Arbeiten Methoden/Ergebnisse). Welche Struktur zu welchem
> Arbeitstyp passt, erklärt
> [`../anleitung/06_gliederung.md`](../anleitung/06_gliederung.md). Beim
> Hinzufügen/Entfernen nur die `\input{...}`-Zeilen in `main.tex` anpassen.

---

## PDF bauen – drei Wege

### Weg A: Overleaf (empfohlen, kein Technikwissen nötig)

1. Konto auf [overleaf.com](https://www.overleaf.com) anlegen (kostenlos).
2. *New Project → Upload Project* → den `template/`-Ordner als ZIP hochladen.
3. **Wichtig:** *Menu → Settings → Compiler* auf **XeLaTeX** stellen
   (die Vorlage nutzt die Schrift *TeX Gyre Termes* und braucht XeLaTeX,
   nicht das voreingestellte pdfLaTeX).
4. Auf **Recompile** klicken. Fertig. PDF rechts herunterladen.

Overleaf kümmert sich automatisch um das Literaturverzeichnis (Biber).

### Weg B: Docker (ein Befehl, lokal, reproduzierbar)

Voraussetzung: [Docker](https://docs.docker.com/get-docker/) ist installiert.

```bash
make pdf      # oder:  docker compose up --build
```

### Weg C: Tectonic lokal (für Fortgeschrittene)

```bash
tectonic -X compile main.tex
```

Details und Fehlerbehandlung: [`../anleitung/09_latex-bauen.md`](../anleitung/09_latex-bauen.md).

---

## Was steckt wo? (Datei-Landkarte)

| Aufgabe | Datei |
|:--|:--|
| Titel, Name, Matrikelnummer, Datum ändern | `skripte/meta.tex` |
| Kapitel schreiben | `kapitel/01_einleitung.tex` … |
| Neues Kapitel einbinden | `kapitel/XX_name.tex` + Zeile in `main.tex` |
| Quelle hinzufügen | `literatur/literatur.bib` |
| Abkürzung definieren | `abkuerzungen/acronyms.tex` |
| KI-Werkzeuge offenlegen (Pflicht!) | `verzeichnisse/ki_verzeichnis.tex` |
| KI-Prompts dokumentieren | `anhang/anhang.tex` |
| Bild ablegen | `abbildungen/` + Verweis im Kapitel |
| Layout/Pakete (selten anfassen) | `main.tex` |

---

## Zitieren in einem Satz

```latex
% sinngemäß (indirekt) – mit "Vgl.":
\autocite[Vgl.][S.~42]{mustermann2024}
% wörtlich (direkt) – ohne "Vgl.", Zitat in \enquote{...}:
\enquote{Wörtliches Zitat.}\autocite[][S.~42]{mustermann2024}
```

Seitenangabe ist an der FOM **Pflicht**. Online-Quellen ohne Seiten:
`[o.\,S.]`, `[Abs.~3]` oder `[Rn.~5]`.

---

## Versionierte PDF statt nur „main.pdf“

Statt am Ende nur eine `main.pdf` zu haben, kannst du nummerierte Stände
sichern:

```bash
make release   # legt releases/main_JJJJMMTT_HHMM_<commit>.pdf ab
```

So bleibt jeder Zwischenstand nachvollziehbar. Mehr dazu in
[`../anleitung/10_versionierung.md`](../anleitung/10_versionierung.md).

---

## Qualität prüfen vor der Abgabe

```bash
make check     # prüft langid, Anführungszeichen, fehlende Seitenangaben u.a.
```

Die vollständige Abgabe-Checkliste:
[`../vorlagen/review-checkliste.md`](../vorlagen/review-checkliste.md).

---

## Formalia einstellen

An der FOM gilt nicht ein einziger Leitfaden. Welcher für dich gilt, stellst du
in [`formalia/konfig.tex`](formalia/konfig.tex) ein — Ränder, Schrift,
Zitierstil und die leitfadenspezifischen Sonderregeln setzen sich dann selbst.

| Datei | Wofür |
|:--|:--|
| `formalia/konfig.tex` | **Hier stellst du ein.** Leitfaden, Zitierstil, Schrift, Overlay |
| `formalia/profil_wi.tex`, `profil_jks.tex` | die belegten Werte je Leitfaden — normalerweise nicht anfassen |
| `formalia/profil_eigen.tex` | **Abweichende Vorgaben deiner Prüfenden.** Wird zuletzt geladen, überschreibt alles |
| `formalia/laden.tex` | die Mechanik — nichts zu ändern |

Zwei Befehle, die dir die Profile bereitstellen:

- `\formaliaQuellenvermerk` — unter selbst erstellte Abbildungen setzen. JKS
  verlangt „Quelle: Eigene Darstellung", WI verbietet es; der Befehl macht je
  nach Profil das Richtige.
- `\formaliaLeitfadenSatz` — nennt den gewählten Leitfaden. Gehört ans Ende der
  Methodik-Passage in der Einleitung; das ist selbst eine Formvorgabe.

Für häufige Abkürzungen gibt es `skripte/textbausteine.tex`: `\zb`, `\dah`,
`\ua`, `\vgl`, `\os` setzen das schmale geschützte Leerzeichen, das „z. B."
korrekt macht und den Zeilenumbruch mitten in der Abkürzung verhindert.

Braucht deine Arbeit einen Sperrvermerk, bindest du `kapitel/sperrvermerk.tex`
vor dem Inhaltsverzeichnis ein und setzt `\myFirma` in `skripte/meta.tex`.

---

## Formalia prüfen vor der Abgabe

```bash
make formalia-check
```

Prüft Umfang (in **Wörtern**, nur `kapitel/` — Fußnoten getrennt ausgewiesen),
ob der Leitfaden in der Einleitung genannt ist, ob das KI-Verzeichnis ausgefüllt
ist, ob deine `FORMALIA.md` vollständig ist und ob dein Formalia-Profil noch
aktuell ist. Die Umfangsvorgabe liest der Check aus `FORMALIA.md`
(Vorlage: [`../vorlagen/FORMALIA_VORLAGE.md`](../vorlagen/FORMALIA_VORLAGE.md)).

---

## Herkunft

Diese Vorlage geht auf das
[FOM-LaTeX-Template von Andy Grunwald](https://github.com/andygrunwald/FOM-LaTeX-Template)
zurück (MIT, Copyright © 2020 Andreas Grunwald & contributors). Sie wurde
seither eigenständig weiterentwickelt: Umstellung auf `scrartcl` und einen
Tectonic-Build, Layout nach FOM-Leitfaden V1.4 (03/2024) und Jäger/Kümpel/Seng
(01/2024), Fußnoten-Zitierstil, KI-Hilfsmittelverzeichnis, `make check`.
Beide Copyright-Vermerke stehen in der [LICENSE](../LICENSE).
