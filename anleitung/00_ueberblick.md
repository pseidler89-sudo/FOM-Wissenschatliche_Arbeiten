# 00 · Überblick: Wie diese Anleitung funktioniert

> Lies dieses Kapitel zuerst. Es erklärt, was dich erwartet, in welcher
> Reihenfolge du vorgehst und welche Grundbegriffe du brauchst. Danach
> arbeitest du dich Kapitel für Kapitel durch – oder springst gezielt dorthin,
> wo du gerade stehst.

---

## Für wen ist das hier?

Für **alle FOM-Studierenden**, die eine wissenschaftliche Arbeit schreiben –
Hausarbeit, Seminararbeit, Projektarbeit, Bachelor- oder Masterarbeit – und
dabei:

- die **Formalia einhalten** wollen (und wissen wollen, welche es überhaupt
  gibt und *warum*),
- **KI sinnvoll und redlich** einsetzen wollen (Recherche, Strukturierung,
  Sprache) – ohne sich angreifbar zu machen,
- am Ende eine **saubere PDF** abgeben wollen,
- und das alles, **auch ohne Technikkenntnisse**.

Du musst kein LaTeX können. Du musst nicht programmieren. Du brauchst keinen
teuren KI-Account. Wo etwas technischer wird, gibt es immer einen einfachen
Weg (meist über [Overleaf](09_latex-bauen.md)) und einen Profi-Weg.

---

## Die zwei Hälften dieses Projekts

```
FOM-Wissenschatliche_Arbeiten/
├── anleitung/   ← DIE ANLEITUNG  (das hier – der ganze Prozess erklärt)
├── vorlagen/    ← AUSFÜLL-HILFEN  (Forschungsfrage, Prompts, Checklisten …)
└── template/    ← DIE LATEX-VORLAGE  (fertig baubar, FOM-konform)
```

- **`anleitung/`** ist das *Warum* und *Wie*: der komplette Weg von der Idee
  bis zur abgegebenen Arbeit.
- **`vorlagen/`** sind kopierfertige Dateien zum Selbstausfüllen.
- **`template/`** ist das *Womit*: das eigentliche Dokument, das du schreibst
  und zur PDF baust.

---

## Der Prozess in 9 Phasen

Eine wissenschaftliche Arbeit entsteht nicht, indem man „losschreibt“. Sie
entsteht in Phasen, die aufeinander aufbauen. Diese Reihenfolge schützt dich
vor dem häufigsten Fehler: viel zu schreiben, bevor klar ist, *was* und *warum*.

| Phase | Was passiert | Kapitel |
|:--:|:--|:--|
| **0** | Setup: Vorlage holen, einmal eine leere PDF bauen | [09](09_latex-bauen.md) |
| **1** | Thema & **Forschungsfrage** festlegen | [01](01_forschungsfrage.md) |
| **2** | **Formalia** verstehen (welche Regeln gelten, warum) | [02](02_formalia.md) |
| **3** | **KI-Werkzeuge** auswählen und richtig bedienen | [03](03_ki-werkzeuge.md) |
| **4** | **Quellenrecherche** (mit KI, aber verifiziert) | [04](04_quellenrecherche.md) · [05](05_grosse-texte.md) |
| **5** | **Gliederung** entwerfen | [06](06_gliederung.md) |
| **6** | **Schreiben** nach eigenem Stilprofil | [07](07_schreiben-und-stil.md) · [08](08_zitieren.md) |
| **7** | **Bauen & versionieren** (PDF, nicht nur „main.pdf“) | [09](09_latex-bauen.md) · [10](10_versionierung.md) |
| **8** | **Qualität prüfen & abgeben** | [11](11_qualitaet-und-abgabe.md) |

> Phase 0 steht bewusst vor allem anderen: Bau **einmal ganz am Anfang** die
> leere Vorlage zur PDF. Wenn das klappt, weißt du, dass dein Werkzeug
> funktioniert – und musst nicht drei Tage vor Abgabe panisch ein Build-Problem
> lösen.

---

## Die wichtigste Grundregel zu KI

Diese Anleitung empfiehlt KI an vielen Stellen. Eine Regel steht über allem:

> **KI ist Zuarbeiter, niemals Autor.**
> Sie recherchiert Vorschläge, strukturiert, formuliert um. Aber *jede*
> Tatsache, *jede* Quelle, *jede* Seitenzahl prüfst **du** gegen das Original.
> KI erfindet Quellen und Seitenzahlen, die echt aussehen. Wer ungeprüft
> übernimmt, riskiert ein Täuschungsverfahren.

Mehr dazu in [03 · KI-Werkzeuge](03_ki-werkzeuge.md) und
[11 · Qualität & Abgabe](11_qualitaet-und-abgabe.md).

---

## Mini-Glossar (einmal lesen, dann nachschlagen)

| Begriff | In einem Satz |
|:--|:--|
| **LaTeX** | Ein Schriftsatz-System: Du schreibst Text + einfache Befehle, ein Programm baut daraus eine perfekt formatierte PDF. Wie „Word, aber das Layout macht der Computer fehlerfrei“. |
| **`.tex`-Datei** | Eine Textdatei mit deinem Inhalt und LaTeX-Befehlen. |
| **Kompilieren / „bauen“** | Aus den `.tex`-Dateien die fertige PDF erzeugen. |
| **Overleaf** | LaTeX im Browser, ohne Installation. Der einfachste Weg zur PDF. |
| **BibLaTeX / `.bib`** | Deine Quellendatenbank. Jede Quelle einmal eintragen, überall zitieren. |
| **Biber** | Das Hilfsprogramm, das aus der `.bib` das Literaturverzeichnis baut (läuft automatisch). |
| **Git** | Versionsverwaltung: speichert jeden Stand deiner Arbeit, nichts geht verloren. |
| **GitHub** | Git in der Cloud: Backup + Zugriff von überall. |
| **Repository („Repo“)** | Der Projektordner unter Versionsverwaltung (z. B. dieses hier). |
| **Prompt** | Die Anweisung, die du einer KI gibst. |
| **Halluzination** | Wenn eine KI etwas Falsches überzeugend erfindet (z. B. eine Quelle). |
| **Leitfaden** | Das offizielle FOM-Dokument mit den Formalia deines Bereichs. |

---

## Zwei Wege, dieselbe Arbeit

Du kannst dieses Projekt auf zwei Arten nutzen. Beide führen zur gleichen,
korrekten PDF.

**Weg „einfach“ (empfohlen, wenn du keine Technik magst):**
1. `template/`-Ordner als ZIP herunterladen.
2. Bei [Overleaf](09_latex-bauen.md) hochladen, Compiler auf **XeLaTeX** stellen.
3. In `meta.tex` deine Daten eintragen, in `kapitel/` schreiben, Quellen in
   `literatur.bib`.
4. „Recompile“ klicken → PDF herunterladen.

**Weg „voll“ (mehr Kontrolle, Backup, Versionierung):**
1. Repo auf GitHub forken/klonen.
2. Lokal mit Docker bauen (`make pdf`) – siehe [09](09_latex-bauen.md).
3. Mit Git versionieren und sichern – siehe [10](10_versionierung.md).

Du kannst jederzeit wechseln – Overleaf kann sich sogar direkt mit GitHub
verbinden.

---

**Nächster Schritt:** [01 · Forschungsfrage festlegen →](01_forschungsfrage.md)
