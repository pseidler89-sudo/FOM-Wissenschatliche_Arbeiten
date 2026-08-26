# Wissenschaftliche Arbeiten an der FOM – mit KI, aber richtig

**Eine vollständige, öffentliche Anleitung *plus* fertige LaTeX-Vorlage: von der
Forschungsfrage über die KI-gestützte Recherche bis zur abgabefertigen,
versionierten PDF. Gebaut so, dass es auch ohne Technikkenntnisse funktioniert.**

> Du musst kein LaTeX können, nicht programmieren und keinen teuren KI-Account
> haben. Wo es technischer wird, gibt es immer einen einfachen Weg (meist über
> [Overleaf](anleitung/09_latex-bauen.md)).

📖 **Als Website lesen (mit Suche & Navigation):**
<https://pseidler89-sudo.github.io/FOM-Wissenschatliche_Arbeiten/>

---

## Worum geht es hier?

Wissenschaftliche Arbeiten scheitern selten am Thema – sondern an **Formalia**,
an **chaotischer Quellenarbeit** und daran, dass **KI falsch eingesetzt** wird
(erfundene Quellen, KI-Klang, fehlende Kennzeichnung). Dieses Projekt nimmt dich
an die Hand und zeigt den **kompletten Prozess** – mit klarem *Warum* hinter
jeder Regel.

Es beantwortet drei Fragen vollständig:

1. **Wie baue ich eine wissenschaftliche Arbeit auf – Schritt für Schritt?**
2. **Welche Formalia gelten an der FOM, und warum?**
3. **Wie nutze ich KI (Perplexity, Gemini, NotebookLM, Claude, ChatGPT) sinnvoll
   *und* redlich – besonders bei großen Volltexten?**

---

## Für wen?

Für **alle FOM-Studierenden** mit einer Haus-, Seminar-, Projekt-, Bachelor-
oder Masterarbeit – **technisch versiert oder nicht.**

---

## Die drei Teile dieses Repos

| Ordner | Was drin ist |
|:--|:--|
| 📘 **[`anleitung/`](anleitung/00_ueberblick.md)** | Der ganze Prozess in 12 kurzen Kapiteln (das *Warum* und *Wie*) |
| 📝 **[`vorlagen/`](vorlagen/THESE_VORLAGE.md)** | Kopierfertige Hilfen: Thesenpapier, KI-Prompts (Recherche + Lektorat, Argumentation, roter Faden, Plagiats-Check), KI-Hilfe-Level, Leitfaden-Extraktion, Recherche-Log, Stilprofil, KI-Stilmerkmale-Checkliste, Abgabe-Checkliste, Formalia-Steckbrief, Gutachten-Auswertung |
| 📄 **[`template/`](template/README.md)** | Die fertige, FOM-konforme LaTeX-Vorlage – baut sofort eine saubere PDF |

---

## Schnellstart (der einfachste Weg zur PDF)

1. Repo als **ZIP herunterladen** (grüner *Code*-Button oben → *Download ZIP*).
2. Konto bei **[Overleaf](https://www.overleaf.com)** anlegen (kostenlos), den
   Ordner `template/` als ZIP hochladen.
3. In Overleaf: *Menu → Settings → Compiler →* **XeLaTeX** wählen.
4. **`skripte/meta.tex`** ausfüllen (dein Name, Titel, Modul, Datum), in
   `kapitel/` schreiben, Quellen in `literatur/literatur.bib`.
5. **Recompile** klicken → fertige PDF herunterladen.

Ausführlich (inkl. Docker- und Tectonic-Weg) in
[`anleitung/09_latex-bauen.md`](anleitung/09_latex-bauen.md).

---

## Die Anleitung – der komplette Lernpfad

Arbeite sie der Reihe nach durch, oder spring dorthin, wo du stehst:

| # | Kapitel | Inhalt |
|:--:|:--|:--|
| 00 | [Überblick](anleitung/00_ueberblick.md) | Wie alles zusammenhängt, der 9-Phasen-Prozess, Glossar |
| 01 | [Forschungsfrage](anleitung/01_forschungsfrage.md) | Thema eingrenzen, Frage schärfen, Thesenpapier |
| 02 | [Formalia](anleitung/02_formalia.md) | **Alle** FOM-Regeln – mit *Warum* und den Unterschieden je Leitfaden |
| 03 | [KI-Werkzeuge](anleitung/03_ki-werkzeuge.md) | Perplexity, Gemini, NotebookLM, Claude, ChatGPT – was wofür |
| 04 | [Quellenrecherche](anleitung/04_quellenrecherche.md) | KI-Recherche mit BibLaTeX-Ausgabe, **Verifikation**, Quellenqualität |
| 05 | [Große Volltexte](anleitung/05_grosse-texte.md) | Kontextfenster, NotebookLM, Zitate Quelle-für-Quelle extrahieren |
| 06 | [Gliederung](anleitung/06_gliederung.md) | Vom Thesenpapier zum Bauplan |
| 07 | [Schreiben & Stil](anleitung/07_schreiben-und-stil.md) | Eigenes Stilprofil, kein „KI-Klang“, FOM-Sprachregeln |
| 08 | [Zitieren](anleitung/08_zitieren.md) | Fußnotenstil, Seitenangaben, `.bib`-Typen, KI-Kennzeichnung |
| 09 | [LaTeX bauen](anleitung/09_latex-bauen.md) | Overleaf / Docker / Tectonic, Wörter zählen, Fehler beheben |
| 10 | [Versionieren](anleitung/10_versionierung.md) | Git/GitHub, datierte PDF-Stände statt nur „main.pdf“ |
| 11 | [Qualität & Abgabe](anleitung/11_qualitaet-und-abgabe.md) | Review, Checkliste, KI-Offenlegung, finalisieren |

---

## Die Leitidee zu KI

> **KI ist Zuarbeiter, niemals Autor.** Sie recherchiert, strukturiert,
> formuliert um. Aber *jede* Tatsache, *jede* Quelle, *jede* Seitenzahl prüfst
> **du** gegen das Original. So wird KI zum ehrlichen Werkzeug – nicht zum
> heimlichen Ghostwriter, der dich ein Täuschungsverfahren kostet.

KI-Nutzung ist an der FOM **erlaubt, aber kennzeichnungspflichtig**. Wie du das
sauber machst, steht in [02 · Formalia](anleitung/02_formalia.md) und
[11 · Qualität & Abgabe](anleitung/11_qualitaet-und-abgabe.md).

---

## Wichtig: die offiziellen FOM-Leitfäden

Maßgeblich für **deine** Arbeit ist immer der **aktuelle, offizielle
Leitfaden** deines Hochschulbereichs. Hol ihn dir aus dem **FOM Online-Campus** –
er ist hier aus urheberrechtlichen Gründen **nicht** mitveröffentlicht.

[Kapitel 02 · Formalia](anleitung/02_formalia.md) fasst den Stand der
einschlägigen Leitfäden (Wirtschaftsinformatik V1.4 / Jäger-Kümpel-Seng /
ifes / Bibliotheks-Leitfaden) zusammen – als Orientierung, nicht als Ersatz.
**Individuelle Vorgaben deiner Prüfer:innen haben immer Vorrang.**

---

## Weiterentwicklung

Geplant ist eine **Website** (GitHub Pages), die diese Anleitung noch
zugänglicher macht – mit Suche, „Open in Overleaf“-Knopf und Phasen-Wegweiser.
Das ausgearbeitete Konzept dazu: [`KONZEPT_WEBSITE.md`](KONZEPT_WEBSITE.md).

## Herkunft & Dank

Die LaTeX-Vorlage steht in der Tradition des
[FOM-LaTeX-Template von Andy Grunwald](https://github.com/andygrunwald/FOM-LaTeX-Template)
und wurde für FOM 2024 modernisiert (Tectonic-Build, KI-Verzeichnis,
Fußnoten-Zitierstil). Die Anleitung destilliert die Praxis aus mehreren real
geschriebenen FOM-Arbeiten.

## Lizenz

[MIT](LICENSE) – frei nutz- und anpassbar, privat wie kommerziell. Keine Gewähr
auf Vollständigkeit oder Richtigkeit; im Zweifel gilt dein offizieller
FOM-Leitfaden. Verbesserungen willkommen – siehe
[CONTRIBUTING.md](CONTRIBUTING.md).
