# 02 · Formalia verstehen (und warum es sie gibt)

> Phase 2. Hier lernst du **alle** formalen Regeln der FOM kennen – und vor
> allem das *Warum* dahinter. Die gute Nachricht: Die Vorlage in
> [`template/`](../template/README.md) hat fast alles davon schon korrekt eingebaut. Du
> musst die Regeln also nicht *umsetzen* – aber du solltest sie *kennen*, denn
> formale Fehler kosten Note, und manche Vorgaben musst du selbst beachten.

---

## Die wichtigste Meta-Regel zuerst

An der FOM gibt es **nicht den einen** Leitfaden, sondern mehrere – je nach
Hochschulbereich. Daraus folgen drei Grundsätze, die über allem stehen:

1. **Wähle einen Leitfaden und wende ihn konsequent an.** Nicht mischen.
2. **Nenne den gewählten Leitfaden in der Einleitung** (am Ende des
   Methodik-Abschnitts). Das ist selbst eine Formvorgabe.
3. **Individuelle Vorgaben deiner Prüfer:innen / deiner Prüfungsordnung haben
   immer Vorrang** vor dem Leitfaden. Weicht dein:e Erstgutachter:in ab, gilt
   die Abweichung.

### Den Leitfaden in der Vorlage einstellen

Weil es mehrere Leitfäden gibt, hat die Vorlage einen Schalter. Du stellst
einmal ein, welcher für dich gilt — Ränder, Schrift, Zitierstil und die
leitfadenspezifischen Sonderregeln setzen sich dann automatisch richtig.

In [`template/formalia/konfig.tex`](../template/formalia/konfig.tex):

```latex
\def\FormaliaLeitfaden{jks}        % wi | jks
\def\FormaliaZitierstil{fussnote}  % fussnote | authoryear | ieee
\def\FormaliaSchrift{tnr}          % tnr | arial
\def\FormaliaOverlay{kein}         % ifes | kein
```

Drei Dinge dazu:

1. **Den Zitierstil legst du einmal fest und wechselst ihn nicht mehr.** Der
   Schalter ändert nur die *Ausgabe*, nicht den Sinn der bereits gesetzten
   `\autocite`-Befehle. Ein später Wechsel von Fußnote auf Harvard schiebt alle
   Belege in den Fließtext — das musst du dann sprachlich nacharbeiten.
2. **Unzulässige Kombinationen brechen den Build ab**, mit einer erklärenden
   Meldung. `ieee` zusammen mit `jks` etwa geht nicht: JKS erlaubt nur Chicago
   in Fußnoten oder Harvard im Text.
3. **Vorgaben deiner Prüfenden gehören nicht in `konfig.tex`**, sondern in
   [`template/formalia/profil_eigen.tex`](../template/formalia/profil_eigen.tex).
   Die Datei wird zuletzt geladen und überschreibt alles. So bleibt
   nachvollziehbar, was Leitfaden ist und was Prüfervorgabe.

Was für *deine* Arbeit gilt, hältst du zusätzlich in einer `FORMALIA.md` fest
(Vorlage: [`../vorlagen/FORMALIA_VORLAGE.md`](../vorlagen/FORMALIA_VORLAGE.md)).
`make formalia-check` prüft vor der Abgabe, was maschinell prüfbar ist: Umfang
in Wörtern, ob der Leitfaden in der Einleitung genannt ist, ob das
KI-Verzeichnis ausgefüllt ist und ob dein Profil noch aktuell ist.

> **Leitfaden-PDF per KI auswerten:** Das Übertragen der Vorgaben aus deinem
> offiziellen Leitfaden in `konfig.tex` und `FORMALIA.md` kannst du dir
> erleichtern: Ein strukturierter Prompt lässt die KI das PDF auswerten und
> bei **jeder** Angabe offenlegen, ob sie eindeutig ist, Wahlfreiheit lässt
> oder im Dokument fehlt – inklusive Fundstelle zum Nachschlagen. Prompt und
> Übertrag: [`vorlagen/leitfaden-extraktion-prompt.md`](../vorlagen/leitfaden-extraktion-prompt.md).

> **Hol dir die *aktuelle* Fassung deines Leitfadens aus dem FOM Online-Campus.**
> Leitfäden werden überarbeitet. Diese Anleitung fasst den Stand der FOM-Leit-
> fäden Wirtschaftsinformatik (V1.4, März 2024) und Jäger/Kümpel/Seng
> (Januar 2024) zusammen – maßgeblich ist immer dein offizielles Dokument.

Die vier in dieser Anleitung ausgewerteten Leitfäden:

| Kürzel | Leitfaden | Für wen v. a. |
|:--|:--|:--|
| **WI** | Gestaltung wiss. Arbeiten, V1.4 (3/2024) | Wirtschaftsinformatik & Ingenieurwesen |
| **JKS** | Formale Gestaltung (Jäger/Kümpel/Seng, 1/2024) | allgemeiner FOM-Standard (Wirtschaft & Recht u. a.) |
| **KEL** | Kritische Evaluation von Literatur | Quellenbewertung (alle) |
| **ifes** | Empirische Arbeiten (Gansser u. a.) | empirische Arbeiten |

---

## 1. Seitenlayout · *warum: Lesbarkeit & Korrekturrand*

Der breite linke Rand ist kein Zufall – er ist der **Platz für Korrektur-
anmerkungen** und (bei gedruckter Abgabe) für die Bindung.

| Maß | Wert | Anmerkung |
|:--|:--|:--|
| Papier | DIN A4, Hochformat | |
| Rand oben | 4 cm | Kopfzeile 2 cm vom Rand |
| Rand unten | 2 cm | Fußzeile 2 cm vom Rand |
| Rand **links** | **4 cm** | breiter Korrektur-/Bindungsrand |
| Rand rechts | 2 cm | (ifes abweichend: mind. 1 cm) |

✅ **Schon in der Vorlage** (`main.tex`, `geometry`-Paket). WI nennt die Maße
„ungefähr“, JKS als „Richtwerte“ – die Vorlage trifft die strengere Lesart.

---

## 2. Schrift & Zeilenabstand · *warum: Vergleichbarkeit des Umfangs*

Einheitliche Schrift und Zeilenabstand sorgen dafür, dass „20 Seiten“ bei allen
ungefähr gleich viel Text bedeuten.

| Element | Vorgabe |
|:--|:--|
| Fließtext | **Times New Roman 12 pt**, **1,5-zeilig** (Alternative Arial: WI 11 pt / JKS 11,5 pt) |
| Fußnoten | einzeilig, **10 pt** (Arial 9,5 pt), oft linksbündig |
| Absatz | vor 0 pt, nach 6 pt, **Blocksatz**, Silbentrennung an |
| Richtwert WI | ca. 37 Zeilen × ca. 60 Zeichen ≈ 2.200 Zeichen/Seite |

✅ **Schon in der Vorlage.** Statt der lizenzpflichtigen Schrift *Times New
Roman* nutzt sie *TeX Gyre Termes* – einen **metrisch identischen, freien
Klon**. Das Ergebnis ist optisch dasselbe. (Deshalb braucht die Vorlage den
**XeLaTeX**-Compiler, siehe [09](09_latex-bauen.md).)

---

## 3. Umfang · *warum: Fairness & Fokus*

Nur **JKS** nennt konkrete Zahlen:

- **Seminararbeit / Assignment:** laut Modulbeschreibung, **z. B. 4.000 Wörter**
- **Bachelor-Thesis:** **40–60 Seiten**
- **Master-Thesis:** **60–80 Seiten**

Gemeint ist der **Textteil** – ohne Deckblatt, Verzeichnisse, Abbildungen,
Tabellen, Anhang. **WI verzichtet bewusst** auf eine feste Seiten- oder
Mindestquellenzahl. **ifes** verlangt nur: der **empirische Teil > 50 %** der
Arbeit.

> **Immer mit der Modulbeschreibung / den Prüfenden abgleichen** – der genaue
> Umfang wird dort festgelegt. Wörter zählen: siehe [09](09_latex-bauen.md).

---

## 4. Aufbau & Gliederung · *warum: roter Faden*

### Reihenfolge der Bestandteile (JKS)

```
Titelblatt
→ Inhaltsverzeichnis
→ Abbildungs- / Tabellen- / Abkürzungsverzeichnis  (wenn vorhanden)
→ ggf. Symbol-/Formelverzeichnis, ggf. Sperrvermerk
→ TEXTTEIL  (Einleitung → Hauptteil → Schluss)
→ ggf. Anhang
→ Literaturverzeichnis  (Internetquellen separat am Ende)
→ ggf. Rechtsprechungs-/Quellenverzeichnis
→ KI-Hilfsmittelverzeichnis
```

WI denkt funktional in sechs Bereichen: **Vorspann → Einleitung → Grundlagen →
Umsetzung → Schluss → Nachspann**.

### Gliederungstiefe

- **Dekadisch** nummerieren: 1, 1.1, 1.1.1 …
- **Maximal 4 Ebenen** (darüber hinaus ohne Nummer).
- **Mindestens-zwei-Regel:** Wer 3.1 hat, braucht auch 3.2. Eine einzelne
  Unterüberschrift ist verboten – logisch, denn man teilt nichts in „ein Teil“.
- **Kapitel-Einleitung:** Zwischen einer Kapitelüberschrift und der ersten
  Unterüberschrift stehen **2–4 einleitende Sätze** (JKS). Gilt nicht für die
  Einleitung selbst.
- Hauptkapitel etwa gleich umfangreich; Grundlagen nicht aufblähen, Hauptteil
  nicht zu kurz.

✅ Gliederungstiefe (`secnumdepth`/`tocdepth` = 4) ist in der Vorlage gesetzt.
⚠️ Die **2–4 Sätze Kapitel-Einleitung** musst **du** schreiben – die
Chapter-Skelette der Vorlage zeigen, wo.

---

## 5. Verzeichnisse & Seitenzahlen · *warum: Auffindbarkeit*

**Pflichtverzeichnisse:** Inhalt + Literatur immer. Abbildungs-,
Tabellen-, Abkürzungsverzeichnis, **sobald** es Abbildungen / Tabellen /
fachspezifische Abkürzungen gibt. **KI-Verzeichnis**, sobald KI genutzt wurde.

**Seitennummerierung (JKS, detailliert):**

- Titelblatt zählt mit, **trägt aber keine Seitenzahl**.
- Alle Verzeichnisse vor dem Textteil: **römisch** (II, III, …).
- **Textteil: arabisch, neu beginnend mit 1.**
- Seitenzahl **oben** in der Kopfzeile.
- Das Inhaltsverzeichnis listet sich nicht selbst; Eigenständigkeits­erklärung
  und Titelblatt stehen nicht im Inhaltsverzeichnis.

✅ Der römisch→arabisch-Wechsel und die Verzeichnislogik sind in der Vorlage
eingebaut. Abbildungs-/Tabellenverzeichnis sind **auskommentiert** und werden
erst eingeschaltet, wenn du Abbildungen/Tabellen hast (Hinweis steht in
`main.tex`).

⚠️ **Achtung Detail-Widerspruch:** Beim **Sperrvermerk** unterscheiden sich die
Leitfäden – WI: keine Seitenzahl, nicht im Inhaltsverzeichnis; JKS: römische
Seitenzahl, **im** Inhaltsverzeichnis. Richte dich nach *deinem* Leitfaden.

---

## 6. Zitation · *der wichtigste Unterschied zwischen den Leitfäden*

Hier liegt die größte Divergenz – **welcher Zitierstil gilt, hängt von deinem
Bereich ab.** Details und LaTeX-Befehle in [08 · Zitieren](08_zitieren.md);
hier die formale Landkarte.

| Leitfaden | Zulässige Stile |
|:--|:--|
| **WI** | offen: Fußnote, **IEEE** (`[12]`, in Informatik üblich), Harvard, APA – **nicht mischen** |
| **JKS** | **Chicago in Fußnoten** *oder* **Harvard im Text** (Kurzbeleg mit Stichwort) |
| **ifes** | Harvard im Satz *oder* Fußnote |

Drei Regeln gelten **stilübergreifend an der FOM**:

1. **Seitenangabe ist immer Pflicht** – bei *jedem* Stil, auch bei IEEE (wo das
   international oft entfällt). Ohne Seite kein Beleg. Online ohne Seiten:
   `o. S.`, `Abs.`, `Rn.`
2. **Indirekte (sinngemäße) Zitate** mit **„Vgl.“** kennzeichnen; **direkte
   (wörtliche)** Zitate in Anführungszeichen **ohne** „Vgl.“.
3. **Gesetze/Artikel im Fließtext** nennen (z. B. „§ 433 Abs. 2 BGB“,
   „Art. 5 DSGVO“) – **nicht** in die Fußnote. Die Fußnote enthält nur den
   bibliografischen Kurzbeleg (z. B. den Kommentar mit Seitenzahl).

✅ Die Vorlage ist auf den **FOM-Fußnotenstil** (`ext-authoryear-ibid`)
vorkonfiguriert – passend für die meisten FOM-Bereiche. Wie du auf IEEE
umstellst, steht in [08](08_zitieren.md).

> ⚠️ **Echter Widerspruch zwischen den Leitfäden:** Bei selbst erstellten
> Abbildungen/Tabellen verlangt **JKS** den Vermerk *„Quelle: Eigene
> Darstellung“*, **WI** verbietet ihn ausdrücklich. → Nach *deinem* Leitfaden
> richten.

---

## 7. Literaturverzeichnis · *warum: Nachprüfbarkeit*

- **Alphabetisch** nach Familienname des Erstautors (Ausnahme IEEE: nummeriert).
- **Internetquellen** kommen bei JKS **separat ans Ende** unter „Internetquellen“.
- JKS-Feinheiten: Angaben enden **ohne Punkt**, akademische Titel werden **nicht**
  genannt, ab 2. Zeile 1 cm einrücken.
- Je Quellentyp die passenden Felder (Autor, Titel, in:, Hrsg., Auflage, Ort,
  Verlag, Jahr, Seiten, ISBN/DOI, URL + Zugriffsdatum).
- **Nicht zitierfähig:** Skripte, andere Studienarbeiten, Vorlesungsfolien,
  Lexika/Wikipedia (Tertiärliteratur). Publikumspresse (Spiegel, Handelsblatt)
  nur sparsam. → Quellenqualität bewerten: [04](04_quellenrecherche.md), Abschnitt KEL.

✅ Die Vorlage trennt **automatisch** in „Literaturverzeichnis“ und
„Internetquellen“ (über den Quellentyp `@online`). Sortierung und Formatierung
erledigt BibLaTeX – **du musst nichts per Hand formatieren**, wenn die
`.bib`-Einträge korrekt sind.

---

## 8. KI-Nutzung kennzeichnen · *Pflicht seit 2024*

Sowohl WI als auch JKS verlangen ein eigenes **KI-Verzeichnis**. Die
Kennzeichnung erfolgt **zweistufig**:

**a) Lokal im Text** – wo KI-erzeugte Inhalte übernommen wurden, mit
**System, ggf. Version, Datum**. Beispiel (überarbeitete Übernahme, mit „Vgl.“):
*„… Aussage.“ (Vgl. ChatGPT, Version 4, Zugriff am 01.11.2025)*

**b) Summarisch im KI-Verzeichnis** – alle Werkzeuge mit Einsatzzweck, direkt
nach dem Literaturverzeichnis.

Wichtige Feinheiten:

- **KI-Kennzeichnung ersetzt KEINE Quellenangabe.** KI-gestützte Aussagen
  zusätzlich mit Fachliteratur belegen.
- **JKS:** Nachweis nur für *übernommene Inhalte* (Textgenerierung,
  Paraphrase, Übersetzung) – **nicht** für reine Ideenfindung/Methodenwahl oder
  Literatursuche. JKS verlangt zusätzlich, die genutzten **KI-Ausgaben als ZIP
  (PDF-Ausdrucke)** mit einzureichen.
- **WI:** Kurzform der **Prompts** in den Anhang.
- **Nicht** ins Verzeichnis gehören Rechtschreibprüfung oder Taschenrechner.

✅ Die Vorlage hat `verzeichnisse/ki_verzeichnis.tex` und einen Anhang-Abschnitt
für Prompts. ⚠️ **Inhalt füllst du selbst** – ehrlich und vollständig.
Mehr: [11 · Qualität & Abgabe](11_qualitaet-und-abgabe.md).

---

## 9. Deckblatt · *Pflichtangaben*

Titel der Arbeit (größter Schriftgrad), Untertitel (optional), Art der Arbeit,
Modul, Hochschule + Studiengang + Studienort, Name + Matrikelnummer,
Erstbetreuer:in, Abgabedatum. **Keine** Privatadresse/Kontaktdaten.

> Für **Abschlussarbeiten** stellt die FOM das Titelblatt **zentral im
> Online-Campus** bereit – dann dieses verwenden. Für Seminararbeiten erstellst
> du es selbst.

✅ Alles in der Vorlage – du füllst nur `skripte/meta.tex` aus.

---

## 10. Sprache & Stil · *warum: Wissenschaftlichkeit*

| Regel | Inhalt |
|:--|:--|
| Keine Ich-/Wir-Form | dritte Person, unpersönlich. ifes verbietet auch die „man“-Form |
| Tempus | **Präsens** bevorzugt; Vergangenheit nur für historische Sachverhalte |
| Gendergerechte Sprache | **JKS: Pflicht** (z. B. „die Studierenden“, Doppelnennung, Partizip) |
| Keine Füllwörter | „eigentlich“, „vielleicht“, „natürlich“, „sehr“ vermeiden |
| Fachbegriffe | präzise, einheitlich, bei Erstnennung definieren |
| Abkürzungen | sparsam; vor Erstnennung einführen; eigene Abkürzungen verboten |
| Vorwort/Danksagung | WI erlaubt Vorwort; **ifes verbietet** Danksagung in der Abgabe (kein Dank an Notengeber!) |

Diese Stilregeln vertieft [07 · Schreiben & Stil](07_schreiben-und-stil.md) –
inklusive der Frage, wie du verhinderst, dass dein Text wie von einer KI
generiert klingt.

---

## Die Widersprüche auf einen Blick

Wo sich die Hauptleitfäden unterscheiden – **richte dich nach deinem Bereich**:

| Punkt | WI | JKS |
|:--|:--|:--|
| IEEE-Zitation | erlaubt | nicht vorgesehen |
| „Eigene Darstellung“ | **verboten** | **Pflicht** |
| Arial-Größe | 11 pt | 11,5 pt |
| Sperrvermerk-Seitenzahl | nein | ja (römisch, im IV) |
| Eigenständigkeitserklärung | beifügen | nicht beifügen (bei Anmeldung bestätigt) |
| KI-Verzeichnis: Zusatz | Prompts im Anhang | KI-Ausgaben als ZIP |

---

## Was die Vorlage dir abnimmt – und was nicht

| ✅ Erledigt die Vorlage | ⚠️ Machst du selbst |
|:--|:--|
| Ränder, Schrift, Zeilenabstand, Blocksatz | Leitfaden in der Einleitung nennen |
| Seitenzahlen römisch→arabisch | 2–4 Sätze Kapitel-Einleitung je Kapitel |
| Fußnoten-Zitierstil, Literaturverzeichnis | korrekte `.bib`-Einträge pflegen |
| Trennung Internetquellen | Inhalt des KI-Verzeichnisses |
| KI-Verzeichnis-Gerüst, Deckblatt-Layout | gendergerechte Sprache, Präsens, keine Ich-Form |

---

**Nächster Schritt:** [03 · KI-Werkzeuge auswählen →](03_ki-werkzeuge.md)
