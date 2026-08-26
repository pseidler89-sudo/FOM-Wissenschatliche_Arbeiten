# Leitfaden auswerten lassen (Extraktions-Prompt)

> Dein offizieller Leitfaden ist ein langes PDF – und die Vorgaben, die du
> daraus brauchst, stehen verstreut auf Dutzenden Seiten. Dieser Prompt lässt
> eine KI (mit Dokument-Upload, z. B. Gemini, NotebookLM, Claude oder ChatGPT)
> das PDF **systematisch auswerten** und in eine feste Struktur bringen, die du
> direkt in [`template/formalia/konfig.tex`](../template/formalia/konfig.tex)
> und deine `FORMALIA.md` ([Vorlage](FORMALIA_VORLAGE.md)) überträgst.
>
> **Das Warum hinter dem Format:** Die KI muss bei **jeder** Angabe Farbe
> bekennen – ist die Vorgabe *eindeutig* (`exact`), lässt der Leitfaden dir die
> *Wahl* (`choice`), oder steht dazu *nichts* im Dokument (`missing`)? Ohne
> diesen Zwang füllt eine KI Lücken stillschweigend mit plausiblen Erfindungen.
> Mit ihm siehst du sofort, wo du selbst entscheiden oder bei deinen Prüfenden
> nachfragen musst.

> **Goldene Regel gilt auch hier:** Jede extrahierte Angabe ist ein
> unbestätigter Verdacht. Die KI liefert zu jedem Wert die Fundstelle
> (Dokument + Seite) – **schlag mindestens die Werte nach, die du in
> `konfig.tex` einträgst.**

---

## Der Prompt

Lade deinen offiziellen Leitfaden (aus dem FOM Online-Campus) und ggf. die
Modulbeschreibung hoch, dann:

```
ROLLE: Du wertest Hochschul-Leitfäden für wissenschaftliche Arbeiten aus.

AUFGABE: Analysiere die beigefügten Dokumente (Leitfaden, ggf.
Modulbeschreibung) und extrahiere alle formalen Vorgaben für eine
[ARBEITSTYP, z. B. Seminararbeit].

Antworte NUR mit einem JSON-Objekt im Format unten. Kein Text davor
oder danach.

REGELN für jedes Feld:
- Vorgabe EINDEUTIG festgelegt        -> "confidence": "exact"
- MEHRERE Optionen zugelassen         -> "confidence": "choice",
  alle Optionen in "alternativen" auflisten
- NICHT im Dokument gefunden          -> "confidence": "missing",
  "wert": null. NICHTS aus Allgemeinwissen ergänzen oder raten.
- "quelle" nennt IMMER Dokument + Seite/Abschnitt der Fundstelle.

{
  "leitfaden": {
    "name":    { "wert": "", "confidence": "", "quelle": "" },
    "fassung": { "wert": "Version/Datum", "confidence": "", "quelle": "" }
  },
  "layout": {
    "rand_links_cm":  { "wert": null, "confidence": "", "quelle": "" },
    "rand_rechts_cm": { "wert": null, "confidence": "", "quelle": "" },
    "rand_oben_cm":   { "wert": null, "confidence": "", "quelle": "" },
    "rand_unten_cm":  { "wert": null, "confidence": "", "quelle": "" },
    "schrift":        { "wert": "", "alternativen": [], "confidence": "", "quelle": "" },
    "schriftgroesse_pt": { "wert": null, "alternativen": [], "confidence": "", "quelle": "" },
    "zeilenabstand":  { "wert": null, "confidence": "", "quelle": "" }
  },
  "umfang": {
    "einheit":   { "wert": "Woerter oder Seiten", "confidence": "", "quelle": "" },
    "minimum":   { "wert": null, "confidence": "", "quelle": "" },
    "maximum":   { "wert": null, "confidence": "", "quelle": "" },
    "was_zaehlt": { "wert": "z. B. nur Textteil", "confidence": "", "quelle": "" }
  },
  "zitation": {
    "stil": { "wert": "", "alternativen": [], "confidence": "", "quelle": "" },
    "seitenangabe_pflicht": { "wert": null, "confidence": "", "quelle": "" },
    "indirekte_zitate_vgl": { "wert": null, "confidence": "", "quelle": "" }
  },
  "quellen": {
    "mindestzahl":          { "wert": null, "confidence": "", "quelle": "" },
    "nicht_zitierfaehig":   { "wert": [], "confidence": "", "quelle": "" },
    "internetquellen_separat": { "wert": null, "confidence": "", "quelle": "" }
  },
  "struktur": {
    "pflichtbestandteile_reihenfolge": { "wert": [], "confidence": "", "quelle": "" },
    "gliederungstiefe_max": { "wert": null, "confidence": "", "quelle": "" },
    "abstract_noetig":      { "wert": null, "confidence": "", "quelle": "" },
    "sperrvermerk_regeln":  { "wert": "", "confidence": "", "quelle": "" }
  },
  "ki_nutzung": {
    "ki_verzeichnis_pflicht": { "wert": null, "confidence": "", "quelle": "" },
    "nachweisform": { "wert": "z. B. Prompts im Anhang / Ausgaben als ZIP", "confidence": "", "quelle": "" }
  },
  "vorlagen_schalter": {
    "_hinweis": "Bildliche Zuordnung auf die Schalter meiner LaTeX-Vorlage. Die Vorlage baut mit XeLaTeX + biber; Dokumentklasse und Pakete stehen fest - schlage KEINE eigene LaTeX-Konfiguration vor, sondern waehle nur aus den zulaessigen Werten. Passt keiner, setze null und begruende in 'kommentar'.",
    "FormaliaLeitfaden": { "wert": "wi | jks | null", "confidence": "", "kommentar": "" },
    "FormaliaZitierstil": { "wert": "fussnote | authoryear | ieee | null", "confidence": "", "kommentar": "" },
    "FormaliaSchrift":   { "wert": "tnr | arial | null", "confidence": "", "kommentar": "" },
    "FormaliaOverlay":   { "wert": "ifes | kein", "confidence": "", "kommentar": "" }
  },
  "sonstige_auffaellige_vorgaben": [
    { "vorgabe": "", "quelle": "" }
  ]
}
```

**Falls dir deine Prüfenden individuelle Vorgaben gemacht haben** (E-Mail,
Ansage in der Vorlesung), häng diesen Block an – Prüfervorgaben schlagen den
Leitfaden, und genau das soll die KI abbilden:

```
ZUSÄTZLICHE VORGABEN MEINER PRÜFENDEN (haben VORRANG vor dem Leitfaden):
"[WORTLAUT DER VORGABE, z. B. 'Bitte Harvard statt Fußnoten.']"

Wo diese Vorgaben dem Leitfaden widersprechen, gilt die Prüfervorgabe:
setze confidence = "exact" und quelle = "Prüfervorgabe vom [DATUM]".
Liste alle so überschriebenen Felder am Ende zusätzlich unter
"pruefer_abweichungen" auf.
```

---

## So überträgst du das Ergebnis

Das JSON ist Zwischenformat, kein Selbstzweck. Es füllt drei Ziele:

| confidence | Was du tust |
|:--|:--|
| **`exact`** | Fundstelle nachschlagen → Wert in `FORMALIA.md` eintragen; die vier `vorlagen_schalter` in [`template/formalia/konfig.tex`](../template/formalia/konfig.tex) setzen. |
| **`choice`** | **Du** entscheidest dich für eine der Alternativen (einmal, dann dabei bleiben – v. a. beim Zitierstil) und hältst die Wahl in `FORMALIA.md` fest. |
| **`missing`** | Nicht raten: Modulbeschreibung prüfen, sonst **bei den Prüfenden nachfragen**. Antwort mit Datum in `FORMALIA.md` dokumentieren. |

Abweichende **Prüfervorgaben** (`pruefer_abweichungen`) trägst du doppelt ein:
in die Tabelle „Abweichende Vorgaben der Prüfenden“ der
[`FORMALIA_VORLAGE.md`](FORMALIA_VORLAGE.md) *und* – falls sie das Layout oder
die Zitation betreffen – in
[`template/formalia/profil_eigen.tex`](../template/formalia/profil_eigen.tex).
So bleibt nachvollziehbar, was Leitfaden ist und was Prüfervorgabe.

> **Grenzen der Methode:** Die KI kann Tabellen und Fußnoten im PDF falsch
> lesen, und Leitfäden werden überarbeitet. Deshalb: aktuelle Fassung aus dem
> Online-Campus verwenden, Prüfdatum in `FORMALIA.md` notieren – und die Werte,
> die in `konfig.tex` landen, selbst an der Fundstelle gegenlesen.
> Hintergrund zu allen Schaltern: [`anleitung/02_formalia.md`](../anleitung/02_formalia.md).
