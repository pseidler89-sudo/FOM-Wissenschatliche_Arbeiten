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

Diese Regel ist inzwischen wörtlich belegt — als Anmerkung im Block „Formales“
eines Gutachtens:

> „Ohne Beanstandung - allein darauf achten, dass §§ nie in Fußnoten gehören“

Stärker kann ein Beleg in dieser Sammlung nicht werden: Das ist keine
Leitfaden-Auslegung, sondern der Satz, den die Prüfenden selbst unter die
Bewertung schreiben.

*Rechtsnahe Fächer, WS 2025/26. Deckt sich mit der stilübergreifenden FOM-Regel
in [`../anleitung/02_formalia.md`](../anleitung/02_formalia.md), Abschnitt 6.*

*Prüfbar: `make check`, Prüfung 6 warnt bei §, Art., Abs. oder Rn. innerhalb
der Fußnoten-Argumente von `\autocite`/`\footcite`. Warnung statt Abbruch —
`Abs.`/`Rn.` als Fundstelle einer Quelle ohne Seitenzahlen bleibt legitim
(siehe nächste Regel).*

### Seitenangabe ist immer Pflicht

Bei jedem Zitierstil, auch bei IEEE, wo sie international oft entfällt. Ohne
Seite kein Beleg. Bei Onlinequellen ohne Paginierung: `o. S.`, `Abs.`, `Rn.`

*Prüfbar: `make check`, Prüfung 3 meldet Zitate mit leerem Seiten-Argument.*

---

## Formales

### Auch eine inhaltlich herausragende Arbeit verliert ihre Punkte an der Form

Aus der Notenverteilung eines Gutachtens (rechtsnahes Fach, WS 2025/26): Die
inhaltliche Darstellung wurde als „extrem tiefgreifend“ und deutlich über dem
Durchschnitt liegend bewertet — Methoden, Argumentation, Literaturnutzung,
alles ohne Abzug. Abzüge gab es trotzdem, und zwar ausschließlich bei zwei
Kriterien, beide im Block „Formales“:

- **Gestaltung** (gemäß Leitfaden zur formalen Gestaltung von Seminar- und
  Abschlussarbeiten)
- **Zitierweise in Text und Fußnoten** (Einheitlichkeit, Korrektheit)

Die Lehre daraus: Wenn der Inhalt sitzt, entscheidet die Form darüber, was
übrig bleibt. Sie ist zugleich der Teil, der sich am billigsten absichern
lässt, weil er zu großen Teilen maschinell prüfbar ist. Konkret:

- **Gestaltung**: vor der Abgabe die Formvorgaben systematisch gegen den
  eigenen Leitfaden abgleichen (`FORMALIA.md` ausfüllen, `make formalia-check`
  laufen lassen, PDF visuell prüfen) — nicht aus der Erinnerung.
- **Zitierweise**: einen eigenen Durchgang nur für die Zitation einplanen —
  Einheitlichkeit von Kurzbelegen, „Vgl.“, Seitenangaben und Normverweisen
  (siehe die Regeln unter [Zitation](#zitation)). `make check` deckt die
  maschinell greifbaren Fälle ab.

*Rechtsnahe Fächer, WS 2025/26.*

*Teilweise prüfbar: `make check` (Zitierweise, Prüfungen 2–4 und 6) und
`make formalia-check` (Gestaltung, soweit maschinell greifbar). Der Rest steht
in der [`review-checkliste.md`](review-checkliste.md), Abschnitte „Formalia“
und „Zitationen“.*

---

## Aufbau

### Zwischen Kapitelüberschrift und erster Unterüberschrift stehen 2–4 Sätze

Sie fassen zusammen, was das Kapitel leistet, und stellen den roten Faden zum
vorherigen Kapitel her. Gilt nicht für die Einleitung selbst.

*Quelle: Leitfaden Jäger/Kümpel/Seng, Kap. 1.5.1, Fußnote 2.*

*Prüfbar: `make formalia-check`, Prüfung 6 meldet Kapitel, in denen auf die
Kapitelüberschrift direkt die erste Unterüberschrift folgt.*

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

*Rechtsnahe Fächer, WS 2025/26.*

*Teilweise prüfbar: `make check`, Prüfung 7 zeigt die Verteilung der
BibLaTeX-Eintragstypen im Literaturverzeichnis — ohne Warnwert, denn ob der
Mix zum Thema passt, bleibt eine inhaltliche Entscheidung.*

---

## Wie du diese Liste erweiterst

Nach jeder bewerteten Arbeit: `bewertung/GUTACHTEN.md` ausfüllen (Vorlage:
[`bewertung_VORLAGE.md`](bewertung_VORLAGE.md)), dann prüfen, welcher Punkt
**über die eigene Arbeit hinaus** gilt. Nur der kommt hierher — entpersonalisiert
und mit dem Hinweis, ob er sich maschinell prüfen lässt. Lässt er sich prüfen,
gehört er zusätzlich in `make check` oder `make formalia-check`.
