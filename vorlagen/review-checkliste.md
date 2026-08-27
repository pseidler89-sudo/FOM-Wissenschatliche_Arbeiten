# Abgabe-Checkliste (Vorlage)

> Vor jeder Abgabe einmal komplett durchgehen (Phase 8, siehe
> [`anleitung/11_qualitaet-und-abgabe.md`](../anleitung/11_qualitaet-und-abgabe.md)).
> Alle Punkte sollten grün sein. Kopiere die Liste pro Arbeit und hak ab.

---

## Formalia

- [ ] Ränder, Schrift (TNR/TeX Gyre Termes 12 pt), Zeilenabstand 1,5 (Vorlage erledigt das)
- [ ] Fußnoten einzeilig, 10 pt, kleiner als der Fließtext
- [ ] Seitenzahlen vorhanden; Vorspann römisch, Textteil arabisch ab 1
- [ ] Titelblatt vollständig (Titel, Art, Modul, Hochschule, Name, Matrikelnr., Betreuer, Datum)
- [ ] Gewählter **FOM-Leitfaden in der Einleitung genannt**
- [ ] Abbildungs-/Tabellenverzeichnis aktiviert, falls Abbildungen/Tabellen vorhanden

## Struktur & roter Faden

- [ ] Jedes Kapitel (außer Einleitung) beginnt mit **2–4 Sätzen** Kapitel-Einleitung
- [ ] Jedes Kapitel-Ende leitet ins nächste über
- [ ] **Das Fazit beantwortet die Forschungsfrage aus der Einleitung**
- [ ] Gliederungstiefe ≤ 4 Ebenen; Mindestens-zwei-Regel (kein einzelnes 3.1 ohne 3.2)
- [ ] Hauptkapitel etwa ausgewogen; Grundlagen nicht aufgebläht
- [ ] Umfang im Zielbereich (Modulvorgabe / Leitfaden)

## Zitationen

- [ ] **Jede** Behauptung ist belegt
- [ ] **Jede** Zitation hat eine Seitenangabe (oder ehrlich o. S. / Rn. / Abs.)
- [ ] Direkte Zitate in `\enquote{}` ohne „Vgl.“; indirekte mit „Vgl.“
- [ ] Gesetze/Artikel im Fließtext, Kommentar-Nachweis in der Fußnote (`make check` warnt — in Gutachten wörtlich angemahnt)
- [ ] Vollbeleg bei Erstnennung, danach Kurzbeleg/ebd. (automatisch)
- [ ] `\enquote{}` statt `\glqq…\grqq` oder geraden Anführungszeichen

## BibLaTeX / Literaturverzeichnis

- [ ] Jeder Eintrag hat `langid` (ngerman/english)
- [ ] Nur `date` (ISO), kein redundantes `year`
- [ ] Korrekte Typen: Blog/Web = `@online`, Kommentar = `@incollection`, Gesetz = `@legislation`, Urteil = `@jurisdiction`
- [ ] Online-Quellen: `url` + `urldate`
- [ ] Urteile: Gericht, Datum, Aktenzeichen, Fundstelle
- [ ] Amtliche Schreiben (z. B. BMF): Datum **und** Aktenzeichen
- [ ] Literaturverzeichnis vollständig; Internetquellen separat; jede zitierte Quelle erscheint, keine Leichen

## Inhalt & Sprache

- [ ] Quellenqualität geprüft (keine Lexika/Wikipedia/Studienarbeiten als Beleg)
- [ ] Quellen-Bias geprüft: kein Quellentyp dominiert (≥ ¾), keine
      Autorenschaft mit ≥ 4 Quellen, Zeitspanne nicht auffällig eng
      (siehe [`anleitung/04_quellenrecherche.md`](../anleitung/04_quellenrecherche.md))
- [ ] Keine unbelegten Marktzahlen/Statistiken
- [ ] **Plagiats-/Paraphrase-Check** gelaufen (Prompt in
      [`recherche-prompts.md`](recherche-prompts.md), Abschnitt 10): zu nahe
      Paraphrasen neu formuliert, Definitionen/Fakten belegt, Stilbrüche
      geglättet
- [ ] Keine Ich-/Wir-/„man“-Form; Präsens; gendergerecht; keine Füllwörter
- [ ] Keine KI-typischen Floskeln (siehe Stilprofil-Verbotsliste)
- [ ] Fachbegriffe bei Erstverwendung definiert

## KI-Redlichkeit

- [ ] KI-Verzeichnis vollständig (Werkzeug, Anbieter, Version, Einsatzzweck,
      Art der Übernahme: wörtlich / angepasst / Inspiration / verworfen)
- [ ] KI-übernommene Inhalte im Text gekennzeichnet **und** mit Fachliteratur belegt
- [ ] Prompts in Kurzform im Anhang (WI) bzw. KI-Ausgaben als ZIP (JKS)
- [ ] Eigenständigkeitserklärung beachtet (Leitfaden-abhängig)

## Build & Optik

- [ ] `make pdf` / Overleaf baut **fehlerfrei**
- [ ] `make check` grün (bzw. manuell geprüft)
- [ ] PDF **visuell** geprüft: keine Schusterjungen/Hurenkinder, keine
      abgeschnittenen Tabellen, alle Abbildungen referenziert
- [ ] Abgabestand versioniert (`make release` / Git-Tag)
- [ ] Abgabeform & Frist mit dem Prüfungsamt abgeglichen
