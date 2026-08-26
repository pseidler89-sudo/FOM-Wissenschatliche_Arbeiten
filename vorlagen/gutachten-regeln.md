# Gutachten-Regeln

> **Was in Gutachten immer wieder angemerkt wird — und wie man es vermeidet.**
>
> Diese Sammlung wächst mit jeder bewerteten Arbeit. Sie ist der Grund, warum
> sich der Aufwand lohnt, ein Gutachten nach der Rückgabe noch einmal
> durchzuarbeiten: Was hier steht, kostet dich beim nächsten Mal keine Punkte
> mehr.
>
> **Entpersonalisiert.** Keine Prüfernamen, keine Noten, keine identifizierenden
> Modulangaben — nur Fachgebiet und Semester. Was aus einem konkreten Gutachten
> stammt, gehört privat in die eigene `bewertung/GUTACHTEN.md`; hier steht nur
> die verallgemeinerte Regel.
>
> **Etwas beizutragen?** Siehe [`../CONTRIBUTING.md`](../CONTRIBUTING.md). Regeln
> aus anderen Fachbereichen sind ausdrücklich willkommen — die FOM-Leitfäden
> unterscheiden sich, die Praxis der Prüfenden erst recht.

---

## Zitation

### Paragraphen und Artikel gehören in den Fließtext, nicht in die Fußnote

Normverweise (§, Art., Abs., Rn.) nennt man im Satz. Die Fußnote enthält **nur**
den bibliografischen Kurzbeleg — also den Kommentar oder Aufsatz mit Seitenzahl,
nicht die Norm selbst.

**Falsch**

```latex
\autocite[Vgl.][Art.~5 Abs.~1]{eu_ai_act}
```

**Richtig**

```latex
Art.~5 Abs.~1 \ac{KI-VO}\autocite[Vgl.][S.~73]{hilgendorf_haertlein_2025}
```

*Rechtsnahe Fächer, ab SS 2026. Deckt sich mit der stilübergreifenden FOM-Regel
in [`../anleitung/02_formalia.md`](../anleitung/02_formalia.md), Abschnitt 6.*

### Seitenangabe ist immer Pflicht

Bei jedem Zitierstil, auch bei IEEE, wo sie international oft entfällt. Ohne
Seite kein Beleg. Bei Onlinequellen ohne Paginierung: `o. S.`, `Abs.`, `Rn.`

*Prüfbar: `make check` meldet Zitate ohne Seitenangabe.*

---

## Aufbau

### Zwischen Kapitelüberschrift und erster Unterüberschrift stehen 2–4 Sätze

Sie fassen zusammen, was das Kapitel leistet, und stellen den roten Faden zum
vorherigen Kapitel her. Gilt nicht für die Einleitung selbst.

*Quelle: Leitfaden Jäger/Kümpel/Seng, Kap. 1.5.1, Fußnote 2.*

### Den verwendeten Leitfaden in der Einleitung nennen

Am Ende der Methodik-Passage. Das ist selbst eine Formvorgabe — und sie wird
regelmäßig vergessen. Die Vorlage stellt dafür `\formaliaLeitfadenSatz` bereit,
der den in `formalia/konfig.tex` eingestellten Leitfaden einsetzt.

*Prüfbar: `make formalia-check`, Prüfung 2.*

---

## Quellen

### Breite schlägt Menge

Belohnt wird ein Mix, nicht eine hohe Zahl:

- **Primärquellen** — Gesetze, Verordnungen, Urteile, amtliche Statistiken
- **Sekundärquellen** — Kommentare, Fachbücher, Monographien
- **Fachartikel** — begutachtete Journals
- **Praxisquellen** — Behördenstellungnahmen, Fachblogs (begründungspflichtig)

Wer nur eine dieser Kategorien nutzt, fällt auf. Als Faustzahl für eine
Seminararbeit: ~25–30 Quellen, aber die Verteilung zählt mehr als die Summe.

*Rechtsnahe Fächer, ab SS 2026.*

---

## Wie du diese Liste erweiterst

Nach jeder bewerteten Arbeit: `bewertung/GUTACHTEN.md` ausfüllen (Vorlage:
[`bewertung_VORLAGE.md`](bewertung_VORLAGE.md)), dann prüfen, welcher Punkt
**über die eigene Arbeit hinaus** gilt. Nur der kommt hierher — entpersonalisiert
und mit dem Hinweis, ob er sich maschinell prüfen lässt. Lässt er sich prüfen,
gehört er zusätzlich in `make check` oder `make formalia-check`.
