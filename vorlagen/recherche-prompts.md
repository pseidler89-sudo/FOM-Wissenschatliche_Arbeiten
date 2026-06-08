# KI-Prompts (kopierfertig)

> Erprobte Prompts für die Quellenrecherche, die Zitatextraktion und das
> Stil-Review. Ersetze die `[... PLATZHALTER ...]` durch dein Thema. Hintergrund
> und Einsatz: [`anleitung/04_quellenrecherche.md`](../anleitung/04_quellenrecherche.md),
> [`anleitung/05_grosse-texte.md`](../anleitung/05_grosse-texte.md),
> [`anleitung/07_schreiben-und-stil.md`](../anleitung/07_schreiben-und-stil.md).

> **Goldene Regel:** Jeder Treffer ist ein **unbestätigter Verdacht**, bis du
> ihn am Original geprüft hast. Diese Prompts beschleunigen die Suche – sie
> ersetzen **nicht** deine Verifikation.

---

## 0. Der Ausgabe-Block (in jeden Recherche-Prompt einbauen)

Dieser Block erzwingt direkt einsetzbares BibLaTeX. Häng ihn unten an die
Prompts 1–3 an.

```
OUTPUT-FORMAT (PFLICHT):
Gib JEDEN Treffer als fertigen BibLaTeX-Eintrag aus. Muster:

@article{nachname_JJJJ_kurzwort,
  author  = {Nachname, Vorname},
  title   = {Voller Titel},
  journal = {Zeitschrift},
  volume  = {X},
  number  = {Y},
  pages   = {1--20},
  date    = {JJJJ-MM-TT},
  doi     = {10.xxxx/xxxxx},
  langid  = {ngerman},
}

Weitere Typen:
- Buch:   @book   mit author, title, publisher, location, date, isbn
- Online: @online mit url + urldate (JJJJ-MM-TT)
- Bericht:@report mit author/institution, title, date, url+urldate
- Gesetz: @legislation mit title, date, note (Fundstelle)
- Urteil: @jurisdiction mit institution (Gericht), date, number (Aktenzeichen), note (Fundstelle)
- Kommentar/Sammelband: @incollection mit author, title, booktitle, editor, publisher, date, pages

PFLICHTFELDER auf JEDEM Eintrag: langid (ngerman/english) und date (ISO).
Bei Online-Quellen zusätzlich: url + urldate.
KEIN year-Feld (nur date). Umlaute normal ausschreiben (ä, ö, ü, ß).
URLs als reine Plain-URL (keine Markdown-Links, keine Redirects).
KEINE Quellen erfinden. Bei Unsicherheit: note = {Verifizierung empfohlen}
und einen ehrlichen Status-Kommentar davor (% STATUS: niedrige Konfidenz).
Pro Eintrag 1–2 Sätze Relevanz für die Arbeit als %-Kommentar darüber.
```

---

## 1. Normative / fachliche Grundlagen (z. B. Perplexity Deep Research)

```
ROLLE: Du bist Researcher:in mit Schwerpunkt [FACHGEBIET, z. B. deutsches
Datenschutz-/IT-Recht]. Du arbeitest mit [DATENBANKEN, z. B. EUR-Lex,
beck-online, juris, Google Scholar].

KONTEXT: Ich schreibe eine [ARBEITSTYP] zum Thema:
[FORSCHUNGSFRAGE].

AUFGABE: Recherchiere präzise, zitierfähige Quellen zu folgenden Themenfeldern:
A) [Themenfeld 1]
B) [Themenfeld 2]
C) [Themenfeld 3]

ANFORDERUNGEN:
- Priorisiere jüngere Quellen ([JAHR]–[JAHR]) und Primärquellen.
- Bei Rechtsprechung: Gericht, Datum, Aktenzeichen, Fundstelle.
- Bei amtlichen Schreiben: Aktenzeichen und Datum.
- Pro Quelle 1–2 Sätze Relevanz für die Arbeit.
- KEINE Quellen erfinden. Richtwert: [15–25] Quellen.

[HIER DEN OUTPUT-BLOCK AUS ABSCHNITT 0 EINFÜGEN]
```

---

## 2. Technische / empirische Grundlagen (z. B. Gemini)

```
ROLLE: Du bist wissenschaftliche:r Researcher:in mit Schwerpunkt
[z. B. Wirtschaftsinformatik / empirische Sozialforschung].

KONTEXT: [ARBEITSTYP] zum Thema [FORSCHUNGSFRAGE].

AUFGABE: Recherchiere mit vollständigen Quellenangaben zu:
A) [Standardwerke / Lehrbücher des Felds]
B) [Aktuelle Studien / Paper]
C) [Methoden / Modelle / Standards]
D) [Empirische Daten / Statistiken]

ANFORDERUNGEN:
- Vollständige bibliografische Angaben mit DOI/ISBN.
- Peer-reviewed vor Praxis; [JAHR]+ vor älteren.
- 2–3 Zeilen Relevanz pro Quelle.
- KEINE Halluzinationen. Richtwert: [15–25] Quellen.

[OUTPUT-BLOCK AUS ABSCHNITT 0]
```

---

## 3. Markt- / Praxisdaten (z. B. Perplexity)

```
ROLLE: Du bist Researcher:in mit Spezialisierung auf [Markt/Branche].

AUFGABE: Liefere mit Quellenangaben und Verifikationsstatus zu:
A) [Kennzahl / Marktdaten 1] – jede Zahl mit Quelle und Erhebungsdatum
B) [Trend / Entwicklung 2]
C) [Verbreitung / Praxis 3]

ANFORDERUNGEN:
- Jede Zahl mit Quelle und Erhebungsdatum.
- Markierung je Angabe: "verifiziert" / "Schätzung" / "Verifizierung empfohlen".
- Originalquellen bevorzugt. KEINE Halluzinationen. Richtwert: [10–15] Quellen.

[OUTPUT-BLOCK AUS ABSCHNITT 0]
```

---

## 4. Verifikation von Platzhalter-Quellen (z. B. Perplexity)

> Wenn du Quellen aus dem Gedächtnis als Platzhalter angelegt hast, lass sie
> gegenprüfen – statt sie blind zu glauben.

```
ROLLE: Researcher:in mit Zugriff auf [DATENBANKEN].

KONTEXT: Meine literatur.bib enthält Platzhalter, die ich aus dem Gedächtnis
rekonstruiert habe. Verifiziere ODER ersetze sie durch reale, zitierfähige
Quellen mit vollständiger Fundstelle.

ZU PRÜFEN (citekey beibehalten!):
(1) [citekey]: Annahme: [Autor, Titel, Jahr, Fundstelle].
    -> Existiert das exakt? Wenn ja: Heft/Seite/DOI bzw. Aktenzeichen/Fundstelle.
       Wenn nein: 1–3 reale Ersatzquellen (mit NEUEM citekey).
(2) [citekey]: ...

REGELN:
- citekey der Platzhalter beibehalten. Nicht auffindbar:
  "NICHT AUFFINDBAR: <citekey>" und darunter ein Ersatz mit neuem citekey.
- Pro Treffer Status-Kommentar davor:
  % STATUS: verifiziert (Quelle: [DB], abgerufen JJJJ-MM-TT)
  % URSPRUNG: ersetzt Platzhalter <citekey>
- Bei generischem Autor / fehlender Primärquelle: "% STATUS: niedrige Konfidenz".
- KEINE Halluzinationen.

[OUTPUT-BLOCK AUS ABSCHNITT 0]
```

---

## 5. Zitatextraktion aus einem Volltext → LaTeX (Gemini / Claude)

> Iterativ, **eine Quelle nach der anderen**. Du übergibst Volltext/Ausschnitt
> + BibKey, bekommst die stärksten, kopierfertigen Zitate – und **prüfst jede
> Zeile gegen das PDF**.

```
ROLLE: Du bist KI-Assistent:in für akademische Literaturarbeit und
LaTeX-Integration.

KONTEXT: Ich schreibe eine [ARBEITSTYP] zum Thema [FORSCHUNGSFRAGE].
Meine Quellen liegen als BibLaTeX-Einträge vor; die Originaltexte habe ich
als PDF-Volltext.

ARBEITSWEISE (iterativ pro Quelle): Sobald ich dir den Volltext (oder
Ausschnitt) einer Quelle und ihren BibTeX-Key gebe, führst du aus:
1) Kontext-Analyse: Gleiche den Text mit meiner Argumentationslinie ab.
2) Extraktion & Bewertung: Filtere die 5 relevantesten Belege heraus. Begründe
   je 1–2 Sätze, warum relevant und in welches Kapitel sie gehören.
3) LaTeX-Readiness: Gib zu jedem Beleg den kopierfertigen Zitierbefehl aus.

AUSGABE als Markdown-Tabelle:
| Bewertung / Zielkapitel | Seite/Rn. | Zitat / Paraphrase | LaTeX-Befehl |

REGELN:
- Direkte (wörtliche) Zitate: KEIN "Vgl.", Zitat in \enquote{...}.
- Indirekte (sinngemäße) Zitate: mit "Vgl.".
- Seitenzahl aus dem Text BELEGEN, nicht schätzen. Fehlt sie: o.\,S. / Rn. / Abs.
- Befehlsmuster: \autocite[Vgl.][S.~X]{bibkey}  bzw.  \autocite[][S.~X]{bibkey}
- Nichts hinzudichten, was nicht im übergebenen Text steht.

Bestätige kurz die Regeln und warte auf die erste Quelle.
```

---

## 6. Stil-Review / Anti-KI-Klang (Claude)

> Kapitelweise. Macht aus glattem KI-Text wieder **deinen** sachlichen Text –
> ohne die Belege zu zerstören.

```
ROLLE: Du bist erfahrene:r Lektor:in für akademische Texte. Ziel: meine fertig
strukturierte [ARBEITSTYP] sprachlich so kalibrieren, dass sie sachlich,
präzise und authentisch studentisch klingt – NICHT wie KI-generiert.

PRÜF-KRITERIEN (nach "Signs of AI writing"):
1. Keine Bot-Begeisterung ("entscheidender Meilenstein", "unterstreicht
   eindrucksvoll", "es ist wichtig anzumerken").
2. Keine künstliche Symmetrie (gleich lange Absätze, Dauer-Dreierlisten,
   "Nicht nur ..., sondern auch ..."). Satz-/Absatzlängen natürlich variieren.
3. Keine LinkedIn-/Plauder-Sprache ("Schauen wir uns nun an ...").
4. Keine moralisierenden Schluss-Sätze; sachlich bleiben.

ARBEITSAUFTRAG (iterativ, Kapitel für Kapitel):
1) Identifiziere Sätze mit KI-Mustern, Umgangssprache oder fachlichem Abdriften.
2) Ersetze sie durch sachliche, präzise, authentische Formulierungen.
3) Gib kopierfertigen LaTeX-Code zurück. ALLE \autocite-Befehle EXAKT beibehalten,
   KEINE neuen Inhalte, KEINE neuen Quellen.

Bestätige die Regeln und antworte mit: "Bereit für Kapitel 1!"
```

---

## Nach jedem Lauf: dokumentieren

Trag Werkzeug, Prompt, Trefferzahl und Übernahmen ins
[`recherche-log_VORLAGE.md`](recherche-log_VORLAGE.md) ein – das ist später die
Basis für dein KI-Verzeichnis.
