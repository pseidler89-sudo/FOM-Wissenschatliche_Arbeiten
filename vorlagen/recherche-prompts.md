# KI-Prompts (kopierfertig)

> Erprobte Prompts für die Quellenrecherche, die Zitatextraktion und die
> Review-Runden (Stil, Lektorat, Argumentation, roter Faden, Plagiatsrisiko).
> Ersetze die `[... PLATZHALTER ...]` durch dein Thema. Hintergrund
> und Einsatz: [`anleitung/04_quellenrecherche.md`](../anleitung/04_quellenrecherche.md),
> [`anleitung/05_grosse-texte.md`](../anleitung/05_grosse-texte.md),
> [`anleitung/07_schreiben-und-stil.md`](../anleitung/07_schreiben-und-stil.md).

> **Goldene Regel:** Jeder Treffer ist ein **unbestätigter Verdacht**, bis du
> ihn am Original geprüft hast. Diese Prompts beschleunigen die Suche – sie
> ersetzen **nicht** deine Verifikation.

> **Hilfe-Level nicht vergessen:** An die Review-Prompts (6–10) gehört unten
> immer der Baustein deines [KI-Hilfe-Levels](ki-hilfe-level.md) – er legt
> fest, ob die KI nur Hinweise geben, Formulierungen vorschlagen oder Entwürfe
> liefern darf. Ohne diese Ansage schreibt sie ungefragt um.

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

## 7. Lektor-Check: 5 Kategorien mit Prioritätsampel (Claude / ChatGPT)

> Der Stil-Review (Prompt 6) prüft die **Sprache**. Dieser Prompt prüft
> zusätzlich **Inhalt, Logik und Belege** – kapitelweise, mit einer Ampel, die
> dir sagt, was zuerst dran ist. Die Ampel ist der eigentliche Gewinn: Ohne sie
> bekommst du 30 gleichrangige Anmerkungen und weißt nicht, wo anfangen.

```
ROLLE: Du bist erfahrene:r wissenschaftliche:r Lektor:in für deutschsprachige
Hochschularbeiten. Sei streng und konkret – Lob hilft mir nicht.

KONTEXT: [ARBEITSTYP], Kapitel "[KAPITELTITEL]". Zitierstil: [Fußnote (FOM) /
Harvard / IEEE]. Es gilt: JEDER Beleg braucht eine Seitenangabe
(bzw. o. S. / Rn. / Abs.).

AUFGABE: Prüfe den Text unten auf genau diese fünf Kategorien und gib zu
jeder Feedback:

1. WISSENSCHAFTLICHE SPRACHE
   - sachlich, präzise, keine Umgangssprache?
   - unpersönlich, wo angebracht (keine Ich-/Wir-Form)?
   - Fachbegriffe korrekt und einheitlich verwendet?
2. ARGUMENTATION & LOGIK
   - nachvollziehbar und schlüssig? Brüche, unbegründete Behauptungen?
   - werden Gegenargumente berücksichtigt?
3. STRUKTUR & ABSÄTZE
   - hat jeder Absatz einen klaren Kerngedanken?
   - sinnvolle Übergänge zwischen den Absätzen? logische Reihenfolge?
4. BELEGE & QUELLEN
   - ist jede Behauptung belegt? Wo fehlen Belege?
   - direkt vs. indirekt korrekt (wörtlich in \enquote{...} ohne "Vgl.",
     sinngemäß mit "Vgl.")?
   - hat jeder Beleg eine Seitenangabe?
5. VERSTÄNDLICHKEIT & LESBARKEIT
   - Sätze zu lang oder verschachtelt? Redundanzen?
   - auch für fachfremde Prüfende verständlich?

AUSGABEFORMAT: Nummerierte Liste, gruppiert nach Kategorie. Pro Fund:
- die betroffene Stelle (kursiv zitiert)
- was das Problem ist (ein Satz)
- Priorität: 🔴 hoch (kostet Punkte) / 🟡 mittel / 🟢 Feinschliff

REGELN: Alle \autocite-Befehle EXAKT beibehalten. KEINE neuen Inhalte,
KEINE neuen Quellen.

[HILFE-LEVEL-BAUSTEIN ANHÄNGEN – siehe ki-hilfe-level.md]

---
ZU PRÜFENDER TEXT:
[KAPITELTEXT]
```

---

## 8. Argumentations-Check: Logikfehler finden (Claude / ChatGPT)

> Der Lektor-Check streift die Argumentation; dieser Prompt seziert sie. Er
> sucht gezielt nach den klassischen Fehlschlüssen, die Gutachten anstreichen –
> und nach der Frage, die über die Note entscheidet: **Wo ist eigene Analyse,
> wo nur Wiedergabe?** Einsatz: pro Hauptteil-Kapitel, sobald der Rohentwurf
> steht (siehe [07 · Schreiben & Stil](../anleitung/07_schreiben-und-stil.md)).

```
ROLLE: Du bist Expert:in für wissenschaftliche Argumentation und kritisches
Denken. Prüfe hart – ich will die Schwächen vor meinen Gutachter:innen finden.

KONTEXT: [ARBEITSTYP], Kapitel "[KAPITELTITEL]".
Forschungsfrage: "[FORSCHUNGSFRAGE]"

AUFGABE: Analysiere die Argumentationsstruktur des Textes unten auf:

1. ARGUMENTATIONSKETTE
   - folgen die Argumente logisch aufeinander?
   - gibt es Sprünge oder fehlende Zwischenschritte?
   - wird jede These begründet?
2. LOGISCHE FEHLER
   - Zirkelschlüsse (die Behauptung begründet sich selbst)?
   - falsche Kausalität (Korrelation ≠ Kausalität)?
   - unzulässige Verallgemeinerungen (vom Einzelfall aufs Ganze)?
   - Strohmann-Argumente (verzerrte Gegenposition widerlegt)?
3. ROTER FADEN
   - trägt jeder Absatz zur Beantwortung der Forschungsfrage bei?
   - gibt es Exkurse, die nicht zurückgeführt werden?
   - ist die Gewichtung der Argumente angemessen?
4. WISSENSCHAFTLICHE REDLICHKEIT
   - werden Gegenargumente anerkannt und diskutiert?
   - wird zwischen Fakten, Meinungen und Interpretationen unterschieden?
   - werden Limitationen benannt?
5. EIGENLEISTUNG
   - wo ist eigene Analyse, wo reine Wiedergabe von Quellen?
   - werden Quellen kritisch eingeordnet oder nur aufgelistet?
   - gibt es eigene Schlussfolgerungen?

AUSGABEFORMAT: Pro Fund:
- 📍 Stelle im Text (kursiv zitiert)
- 🔍 Art des Problems (z. B. "Zirkelschluss", "reine Wiedergabe")
- 💡 wie sich das beheben lässt
- Priorität: 🔴 kritisch / 🟡 wichtig / 🟢 Feinschliff

REGELN: Alle \autocite-Befehle EXAKT beibehalten. KEINE neuen Inhalte,
KEINE neuen Quellen.

[HILFE-LEVEL-BAUSTEIN ANHÄNGEN – siehe ki-hilfe-level.md]

---
ZU PRÜFENDER TEXT:
[KAPITELTEXT]
```

---

## 9. Roter-Faden-Check über die ganze Arbeit (Claude / Gemini)

> Die Prompts 7 und 8 prüfen **ein** Kapitel. Dieser prüft das, was kein
> Einzel-Check sehen kann: ob die **Kapitel zusammen** eine Linie ergeben, die
> von der Einleitung zur Beantwortung der Forschungsfrage führt. Er lohnt sich
> **zweimal**: früh gegen die nackte Gliederung
> (siehe [06 · Gliederung](../anleitung/06_gliederung.md)) und spät noch einmal
> über die geschriebenen Kapitel. Bei langen Arbeiten: pro Kapitel Titel plus
> erster und letzter Absatz (oder eine 5-Zeilen-Zusammenfassung) reichen –
> genau dort sitzt der rote Faden.

```
ROLLE: Du bist erfahrene:r wissenschaftliche:r Gutachter:in.

AUFGABE: Prüfe den roten Faden dieser [ARBEITSTYP]: Bauen die Kapitel logisch
aufeinander auf und führen sie konsequent zur Beantwortung der
Forschungsfrage hin?

THEMA: "[THEMA]"
FORSCHUNGSFRAGE: "[FORSCHUNGSFRAGE]"
ZIEL DER ARBEIT: "[FORSCHUNGSZIEL, optional]"

KAPITELSTRUKTUR MIT INHALT:
### 1. [Kapiteltitel] ([Wortzahl] Wörter)
[erster + letzter Absatz oder Kurzzusammenfassung; bei leeren Kapiteln:
"(noch kein Inhalt)"]
### 2. [Kapiteltitel] ...
[...]

PRÜFE DIESE ASPEKTE:

1. LOGISCHER AUFBAU
   - baut jedes Kapitel auf dem vorherigen auf?
   - gibt es Sprünge? ist die Reihenfolge sinnvoll?
2. FOKUS AUF DIE FORSCHUNGSFRAGE
   - trägt jedes Kapitel zur Beantwortung bei?
   - gibt es Exkurse, die nicht zurückgeführt werden?
3. ÜBERGÄNGE
   - leiten die Kapitel ineinander über, oder gibt es harte Brüche?
4. GEWICHTUNG
   - sind die Kapitel proportional zu ihrer Bedeutung? ist eines
     unverhältnismäßig lang oder kurz (Grundlagen aufgebläht)?
5. KOHÄRENZ
   - werden die in der Einleitung aufgeworfenen Fragen im Hauptteil
     beantwortet? greift das Fazit die Einleitung auf?
   - gibt es Widersprüche zwischen Kapiteln?

AUSGABEFORMAT:
## Gesamtbewertung: [🟢 tragfähiger roter Faden | 🟡 Verbesserungsbedarf |
🔴 kein erkennbarer roter Faden] + eine Begründung in 2–3 Sätzen
## Kapitel für Kapitel: je 2–3 Sätze, was das Kapitel zum roten Faden
beiträgt – oder wo es ihn verliert
## Empfehlungen: nummeriert, nach Priorität sortiert

[HILFE-LEVEL-BAUSTEIN ANHÄNGEN – siehe ki-hilfe-level.md]
```

---

## 10. Plagiats- & Paraphrase-Check (Claude / ChatGPT)

> **Ehrliche Vorbemerkung, die im Prompt bleibt:** Eine KI ist **kein
> Plagiatsdetektor** – sie kann nicht gegen die Datenbanken prüfen, die deine
> Hochschule benutzt. Was sie kann: die **Muster** erkennen, die in echten
> Plagiatsverfahren auffallen – zu nahe Paraphrasen, unbelegte Fakten,
> Stilbrüche. Das ersetzt keine Software-Prüfung, fängt aber die Fälle ab, die
> aus Schlamperei entstehen statt aus Absicht. Der zugehörige Haken steht in
> der [Abgabe-Checkliste](review-checkliste.md).

```
ROLLE: Du bist Expert:in für wissenschaftliche Integrität und
Plagiatsprävention.

WICHTIG: Du bist KEIN Plagiatsdetektor – du kannst nicht gegen Datenbanken
abgleichen. Aber du kannst typische Muster erkennen, die auf Probleme
hindeuten. Genau das ist deine Aufgabe.

KONTEXT: [ARBEITSTYP], Kapitel "[KAPITELTITEL]".

PRÜFE AUF:

1. ZU NAHE PARAPHRASIERUNG
   - Stellen, die wie leicht umformulierte Originaltexte wirken
   - "Patchwork": aneinandergesetzte Sätze aus verschiedenen Quellen
2. FEHLENDE QUELLENANGABEN
   - Behauptungen, die offensichtlich nicht eigenes Wissen sind
   - fachspezifische Fakten und Zahlen ohne Beleg
   - Definitionen ohne Quellenangabe
3. STILBRÜCHE
   - plötzlicher Wechsel im Schreibstil (deutet auf Copy-Paste hin)
   - uneinheitliche Terminologie
   - Passagen, die deutlich "professioneller" klingen als der Rest
4. KI-GENERIERTE TEXTANTEILE
   - typische KI-Muster (übermäßig ausgewogene Formulierungen,
     Dauer-Aufzählungen, generische Aussagen ohne Substanz)
   - Hinweis: KI-Nutzung ist nicht verboten, muss aber gekennzeichnet
     sein – markiere solche Stellen, damit ich die Kennzeichnung prüfe
5. ZITIERTECHNIK
   - direktes Zitat vs. indirektes Zitat vs. eigene Aussage sauber
     unterschieden?
   - "Vgl." bei sinngemäßer Wiedergabe korrekt gesetzt?

AUSGABEFORMAT: Pro problematischer Stelle:
- 📍 Textstelle (kursiv zitiert)
- Art des Problems
- 🛠️ Vorschlag zur Behebung (z. B. "neu paraphrasieren + Beleg", "Quelle
  ergänzen", "als direktes Zitat kennzeichnen")
- Risiko: 🔴 hoch / 🟡 mittel / 🟢 niedrig
Am Ende: Gesamteinschätzung in 2–3 Sätzen.

REGELN: Alle \autocite-Befehle EXAKT beibehalten. KEINE neuen Inhalte,
KEINE neuen Quellen.

[HILFE-LEVEL-BAUSTEIN ANHÄNGEN – siehe ki-hilfe-level.md]

---
ZU PRÜFENDER TEXT:
[KAPITELTEXT]
```

> **Was du mit den Funden machst:** Zu nahe Paraphrasen **neu in eigenen
> Worten** schreiben (Quelle zuklappen, aus dem Gedächtnis formulieren, dann
> gegenprüfen) – nicht nur drei Wörter tauschen. Unbelegte Fakten belegen oder
> streichen. Unkenntlich gewordene KI-Passagen kennzeichnen oder ersetzen.

---

## Nach jedem Lauf: dokumentieren

Trag Werkzeug, Prompt, Trefferzahl und Übernahmen ins
[`recherche-log_VORLAGE.md`](recherche-log_VORLAGE.md) ein – das ist später die
Basis für dein KI-Verzeichnis.
