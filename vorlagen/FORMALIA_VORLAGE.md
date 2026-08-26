# Formalia dieser Arbeit

> Kopiere diese Datei als `FORMALIA.md` neben dein `main.tex` und fülle sie aus,
> **bevor** du mit dem Schreiben anfängst. Sie hält fest, welche Regeln für
> *diese eine* Arbeit gelten — denn die unterscheiden sich von Arbeit zu Arbeit,
> und in vier Wochen weißt du nicht mehr, was deine Prüfenden gesagt haben.
>
> `make formalia-check` liest diese Datei und prüft, was maschinell prüfbar ist.

## Die Arbeit

- **Titel:** <Titel>
- **Art:** <Hausarbeit | Seminararbeit | Projektarbeit | Bachelorarbeit | Masterarbeit>
- **Modul:** <Modulname>
- **Semester:** <z. B. WS 2026/27>
- **Prüfende:** <Name> <, Zweitgutachten: Name>
- **Abgabedatum:** <TT.MM.JJJJ>
- **Abgabeform:** <PDF-Upload im Online-Campus | zusätzlich gedruckt | …>

## Geltende Formalia

- **Leitfaden:** <WI V1.4 (03/2024) | JKS (01/2024)>
- **Fassung geprüft am:** <JJJJ-MM-TT> — hol dir die aktuelle Fassung aus dem
  Online-Campus und vergleiche. Leitfäden werden überarbeitet.
- **Overlay:** <ifes für empirische Arbeiten | keins>
- **Zitierstil:** <Fußnote | Harvard/Autor-Jahr | IEEE> — einmal festlegen, nicht wechseln.
- **Schrift:** <Times New Roman 12 pt | Arial 11 bzw. 11,5 pt>
- **Deckblatt:** <eigenes aus der Vorlage | zentraler FOM-Vordruck (bei Abschlussarbeiten Pflicht)>
- **Umfangsvorgabe:** <z. B. 4000> Wörter <bzw. Seiten> im Textteil
- **Sperrvermerk nötig?** <nein | ja, Firma: …>

Diese Werte müssen zu `template/formalia/konfig.tex` passen.

## Abweichende Vorgaben der Prüfenden

> **Vorgaben der Prüfenden schlagen den Leitfaden.** Trage sie hier ein *und*
> in `formalia/profil_eigen.tex`, damit nachvollziehbar bleibt, was Leitfaden
> ist und was Prüfervorgabe. Immer mit Datum und Quelle.

| Was | Vorgabe | Wer / wann |
|:--|:--|:--|
| — | keine Abweichungen bekannt | — |

## KI-Nachweis

- **Nachweisform:** <WI: Prompt-Kurzformen im Anhang | JKS: KI-Ausgaben als ZIP zur Abgabe>
- **Abgabeartefakte:** <PDF | + ZIP mit KI-Ausgaben | + Prompt-Anhang>

Das KI-Hilfsmittelverzeichnis ist Pflicht, sobald KI genutzt wurde — und es muss
**wahrheitsgemäß und vollständig** sein. Siehe
[`../anleitung/03_ki-werkzeuge.md`](../anleitung/03_ki-werkzeuge.md).

## Status

> Der Status gehört in diese Datei, **nicht** in einen Branch-Namen. Branches
> sind Arbeitszustand; sie werden gelöscht, und dann ist die Information weg.
> Zusätzlich pro Stufe ein Git-Tag setzen.

- [ ] **entwurf** — in Arbeit
- [ ] **abgegeben** — Tag `abgegeben-JJJJ-MM-TT`, PDF eingefroren in `abgabe/`
      inkl. SHA-256 in `abgabe/README.md`
- [ ] **bewertet** — Tag `bewertet-JJJJ-MM-TT`, Gutachten in `bewertung/`
      (Vorlage: [`bewertung_VORLAGE.md`](bewertung_VORLAGE.md))
- [ ] **ausgewertet** — verallgemeinerbare Lehren sind in
      [`gutachten-regeln.md`](gutachten-regeln.md) übernommen

Erst wenn *ausgewertet* abgehakt ist, ist die Arbeit wirklich fertig — sonst
machst du beim nächsten Mal denselben Fehler noch einmal.
