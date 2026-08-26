# KI-Hilfe-Level: Wie viel Hilfe darf es sein?

> **„KI ist Zuarbeiter, niemals Autor“** sagt, *wer* die Verantwortung trägt –
> aber noch nicht, *wie viel* Zuarbeit du zulässt. Genau das legst du mit einem
> **Hilfe-Level** fest: **vor** jedem KI-Einsatz, bewusst, pro Aufgabe. Das
> schützt dich doppelt – du rutschst nicht schleichend vom Gegenlesen ins
> Schreibenlassen, und du hast hinterher die **Sprache, um im KI-Verzeichnis
> ehrlich anzugeben, wie weit die Hilfe ging** (siehe
> [`anleitung/02_formalia.md`](../anleitung/02_formalia.md), Abschnitt 8).
>
> Einsatz: Hänge den Baustein deines Levels **unten an jeden Review- oder
> Schreib-Prompt** an – etwa an die Prompts in
> [`recherche-prompts.md`](recherche-prompts.md). Ohne diese Ansage schreibt
> dir eine KI ungefragt ganze Absätze neu, auch wenn du nur Hinweise wolltest.

---

## Die drei Level im Überblick

| Level | Name | Die KI darf … | Die KI darf nicht … | Kennzeichnung |
|:--:|:--|:--|:--|:--|
| **1** | **Coach** – nur Hinweise | Fragen stellen, auf Probleme zeigen | irgendeinen Text vorformulieren | i. d. R. nicht nachweispflichtig (keine übernommenen Inhalte), trotzdem ins Log |
| **2** | **Formulierungshilfe** – Vorschläge | einzelne Stellen markieren und 1–2 Alternativen je Stelle vorschlagen | ganze Absätze neu schreiben | übernommene Formulierungen kennzeichnen |
| **3** | **Entwurfshilfe** – komplette Entwürfe | ganze Absätze umformulieren oder entwerfen | neue Inhalte oder Quellen erfinden | voll kennzeichnungspflichtig (Text + KI-Verzeichnis, ggf. ZIP/Anhang) |

Die Level bauen aufeinander auf: je höher, desto mehr nimmt dir die KI ab –
und desto mehr musst du **kennzeichnen, prüfen und in eigene Worte fassen**.
Es gibt keinen „richtigen“ Level für alle. Es gibt den richtigen Level **für
diese eine Aufgabe, bei deinen Prüfenden, in deiner Situation.**

---

## Level 1 – Coach: nur Hinweise

> Die KI gibt **ausschließlich Feedback** – keine Textbausteine, keine
> Beispielformulierungen. Sie zeigt auf Probleme; lösen musst du sie selbst.

**Geeignet, wenn:** deine Eigenleistung maximal sichtbar bleiben soll (etwa
weil deine Prüfenden erkennbar Wert auf Selbstständigkeit legen), oder wenn du
das Formulieren bewusst selbst üben willst. Das ist der Modus mit dem
geringsten Kennzeichnungsaufwand – es werden **keine Inhalte übernommen**
(JKS verlangt den Nachweis nur für übernommene Inhalte; führe die Nutzung
trotzdem im [Recherche-Log](recherche-log_VORLAGE.md)).

**Baustein zum Anhängen:**

```
--- HILFE-LEVEL 1: NUR HINWEISE ---
Gib mir NUR Hinweise und Fragen. Schreibe KEINEN Text vor,
auch keine Beispielformulierungen.
Antworte in Stichpunkten.
Formuliere als Fragen: "Ist dir aufgefallen, dass ...?",
"Hast du bedacht, dass ...?"
Dein Ziel ist, mich zum Nachdenken zu bringen –
nicht, mir eine fertige Lösung zu liefern.
Dies ist eine wissenschaftliche Arbeit; die Verantwortung
für den Inhalt liegt bei mir.
```

---

## Level 2 – Formulierungshilfe: Vorschläge

> Die KI darf **alternative Formulierungen vorschlagen**, aber keine ganzen
> Absätze neu schreiben. Du bleibst sichtbar Autor:in jedes Satzes.

**Geeignet als:** Standard-Modus für das Überarbeiten. Guter Kompromiss aus
Tempo und Eigenleistung. Übernimmst du einen Vorschlag wörtlich, ist das eine
**übernommene Formulierung** – kennzeichnen (Log führen, im Zweifel den
Leitfaden lesen; reine Glättung eigener Sätze ist meist nicht
nachweispflichtig, siehe [07 · Schreiben & Stil](../anleitung/07_schreiben-und-stil.md)).

**Baustein zum Anhängen:**

```
--- HILFE-LEVEL 2: FORMULIERUNGSVORSCHLÄGE ---
Gib konkrete Verbesserungsvorschläge für einzelne Formulierungen.
Markiere problematische Stellen und schlage pro Stelle EINE bis ZWEI
alternative Formulierungen vor.
Schreibe NICHT den gesamten Absatz neu.
Alle \autocite-Befehle exakt beibehalten; keine neuen Inhalte,
keine neuen Quellen.
Ich entscheide selbst, welche Vorschläge ich übernehme.
Dies ist eine wissenschaftliche Arbeit; die Verantwortung
für den Inhalt liegt bei mir.
```

---

## Level 3 – Entwurfshilfe: komplette Entwürfe

> Die KI darf **ganze Absätze formulieren**, die du übernehmen oder anpassen
> kannst. Das ist die stärkste – und heikelste – Stufe.

**Geeignet bei:** Zeitdruck, Schreibblockade, oder als Inspirations-Rohstoff in
der Entwurfsphase. Aber sei ehrlich mit dir: Hier entsteht Text, den du **nicht
geschrieben hast**. Alles, was du davon übernimmst, ist **voll
kennzeichnungspflichtig** (lokal im Text *und* im KI-Verzeichnis, bei JKS
zusätzlich die KI-Ausgaben als ZIP, bei WI die Prompts in den Anhang – siehe
[02 § 8](../anleitung/02_formalia.md)). Und es klingt nach Modell, nicht nach
dir – plane die Überarbeitung gegen
[`ki-stilmerkmale.md`](ki-stilmerkmale.md) fest ein.

**Baustein zum Anhängen:**

```
--- HILFE-LEVEL 3: ENTWURFSHILFE ---
Du darfst ganze Absätze neu formulieren oder ergänzen.
Liefere einen überarbeiteten Entwurf des Abschnitts.
Markiere deine Änderungen deutlich (z. B. fett oder kursiv),
damit ich sie einzeln prüfen kann.
Alle \autocite-Befehle exakt beibehalten; KEINE neuen Inhalte,
KEINE neuen Quellen.
Ich entscheide über jede Übernahme selbst und passe sie
in eigenen Worten an.
Dies ist eine wissenschaftliche Arbeit; die Verantwortung
für den Inhalt liegt bei mir.
```

---

## Warum das funktioniert

1. **Die Entscheidung fällt vorher.** Wer erst hinterher überlegt, „wie viel
   KI das jetzt war“, redet es sich schön. Ein vorab gewähltes Level macht die
   Grenze überprüfbar – für dich und im Zweifel für deine Prüfenden.
2. **Die KI hält sich sonst nicht zurück.** Sprachmodelle liefern
   standardmäßig die maximale Hilfe: den fertigen Text. Level 1 und 2
   funktionieren nur, wenn du sie **explizit** ansagst.
3. **Das KI-Verzeichnis wird präzise.** „Claude: sprachliche Überarbeitung“
   sagt wenig. „Claude, Hilfe-Level 2 (Formulierungsvorschläge, punktuell
   übernommen), Kapitel 3–4“ sagt genau, was passiert ist – zusammen mit der
   Spalte **Übernahme** im [Recherche-Log](recherche-log_VORLAGE.md) füllt
   sich das Verzeichnis fast von selbst.

> **Übrigens:** Du darfst das Level je Aufgabe wechseln – Level 3 fürs
> Brainstorming eines Einleitungsentwurfs, Level 1 für den Argumentations-Check
> des fertigen Hauptteils. Wichtig ist nur: pro Lauf **ein** Level, bewusst
> gewählt, dokumentiert.
