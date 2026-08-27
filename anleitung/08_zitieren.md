# 08 · Richtig zitieren

> Zitieren ist der Punkt, an dem Arbeiten am
> häufigsten Note verlieren – durch Kleinigkeiten. Die gute Nachricht: Mit
> BibLaTeX machst du die Quelle **einmal** richtig, und das Literaturverzeichnis
> entsteht automatisch und korrekt. Du musst nur die paar Regeln unten kennen.

---

## Das Prinzip: einmal erfassen, überall zitieren

Du trägst jede Quelle **einmal** in `literatur/literatur.bib` ein und zitierst
sie im Text über ihren **Schlüssel**. BibLaTeX/Biber bauen daraus automatisch
die Fußnoten *und* das alphabetisch sortierte Literaturverzeichnis – richtig
formatiert, mit „ebd.“ bei Wiederholung, Internetquellen separat. **Du
formatierst keine Literaturangabe von Hand.**

---

## Der Zitierbefehl

Die Vorlage nutzt den **FOM-Fußnotenstil**. Ein Zitat erzeugst du so:

```latex
% SINNGEMÄSS (indirekt) – mit "Vgl.":
\autocite[Vgl.][S.~42]{mustermann2024}

% WÖRTLICH (direkt) – OHNE "Vgl.", Zitat in \enquote{...}:
\enquote{Wörtlich übernommener Satz.}\autocite[][S.~42]{mustermann2024}
```

Die zwei eckigen Klammern sind: `[Präfix][Seite]`. Lässt du das Präfix leer
(`[]`), erscheint kein „Vgl.“ – genau richtig fürs direkte Zitat.

### Seitenangaben (an der FOM Pflicht!)

| Fall | Schreibweise |
|:--|:--|
| eine Seite | `[Vgl.][S.~42]` |
| Seitenspanne | `[Vgl.][S.~42--45]` |
| Folgeseite(n) | `[Vgl.][S.~42\,f.]` / `[S.~42\,ff.]` |
| Online ohne Seiten | `[Vgl.][o.\,S.]` |
| Randnummer / Absatz | `[Vgl.][Rn.~12]` / `[Abs.~3]` |

> Das `~` ist ein **geschütztes Leerzeichen** – es verhindert, dass „S.“ und
> „42“ über einen Zeilenumbruch getrennt werden. Immer `S.~42`, nie `S. 42`.

---

## Die vier Regeln, die du nicht verletzen darfst

1. **Immer eine Seitenangabe** (oder ehrlich `o.\,S.`/`Rn.`/`Abs.`). Ohne Stelle
   kein gültiger Beleg – an der FOM bei *jedem* Stil.
2. **Direkt vs. indirekt:** wörtlich → in `\enquote{}`, **kein** „Vgl.“;
   sinngemäß → **mit** „Vgl.“.
3. **Gesetze & Artikel in den Fließtext, nicht in die Fußnote.** Du schreibst
   „nach Art. 5 Abs. 1 DSGVO …“ im Text; die Fußnote belegt das mit dem
   **Kommentar** (Autor, Seite/Rn.). Falsch wäre `\autocite[Art.~5]{…}`.
   *(Aus echtem Gutachter-Feedback: Paragrafen gehören nie in die Fußnote.)*
4. **`\enquote{}` für Anführungszeichen**, nie `\glqq…\grqq` und keine geraden
   `"`. `\enquote{}` setzt automatisch die richtigen deutschen „…“.

---

## Die `.bib`-Einträge: Typen & Pflichtfelder

Jede Quelle hat einen **Typ**. Den richtigen zu wählen sorgt für die korrekte
Darstellung und die automatische Trennung der Internetquellen.

| Quelle | Typ |
|:--|:--|
| Buch / Monographie | `@book` |
| Zeitschriftenaufsatz | `@article` |
| Beitrag in Sammelband / **Kommentar** | `@incollection` |
| Webseite / Blog / Behörde | `@online` |
| Studie / Bericht | `@report` |
| **Gesetz / Verordnung** | `@legislation` |
| **Gerichtsentscheidung** | `@jurisdiction` |

**Pflichtfelder auf JEDEM Eintrag:**

- `langid = {ngerman}` oder `{english}` – steuert „S.“ vs. „p.“, „u. a.“ vs.
  „et al.“ usw.
- `date = {YYYY-MM-DD}` oder `{YYYY}` im **ISO-Format** – **kein** separates
  `year`-Feld (Redundanz vermeiden).

**Zusätzlich bei Online-Quellen:** `url` **und** `urldate = {YYYY-MM-DD}`
(Zugriffsdatum).

**Gerichtsentscheidungen:** Das Gericht gehört ins Feld `author`, in doppelten
geschweiften Klammern (`author = {{Bundesgerichtshof}}`), damit es als ein
Name behandelt wird und im Kurzbeleg erscheint („Vgl. Bundesgerichtshof 2021,
S. 3125“). Steht es nur in `institution`, fehlt es in der Fußnote. Datum und
Aktenzeichen in den `title` („Urteil vom 09.09.2021 – I ZR 113/20“), die
Fundstelle in `note`; die Vorlage unterdrückt das sonst doppelt gedruckte
Datum am Ende des Eintrags.

Fertige, kommentierte Beispiel-Einträge für **jeden** Typ stehen schon in
[`template/literatur/literatur.bib`](../template/literatur/literatur.bib) – du
kopierst den passenden und füllst ihn aus.

```bibtex
@online{musterbehoerde2025,
  author  = {{Bundesamt für Sicherheit in der Informationstechnik}},
  title   = {Titel der Veröffentlichung},
  date    = {2025-03-01},
  url     = {https://www.example.org/dokument},
  urldate = {2026-01-15},
  langid  = {ngerman},
}
```

> **Institutionen als Autor** kommen in **doppelte** geschweifte Klammern:
> `author = {{Bundesamt für …}}` – sonst interpretiert BibLaTeX „Bundesamt“ als
> Vornamen.

---

## Wiederholtes Zitieren, mehrere Quellen, Erstbeleg

- **Wiederholung derselben Quelle** direkt danach → BibLaTeX setzt automatisch
  „ebd.“. Du musst nichts tun.
- **Mehrere Quellen** an einer Stelle → einfach mehrere `\autocite` hintereinander.
- **Vollbeleg bei Erstnennung, danach Kurzbeleg** – erledigt der Stil automatisch.

---

## Interne Hinweise gehören nicht in den Beleg

Korrektur-Notizen an dich selbst („Seite prüfen!“, „Werk verwechselt?“) dürfen
**weder** in den sichtbaren Zitiertext **noch** ins `note`-Feld (es kann im
Literaturverzeichnis mitgedruckt werden). Schreib sie als **LaTeX-Kommentar**
(`%`-Zeile) direkt über den `.bib`-Eintrag:

```bibtex
% TODO: Randnummer aus beck-online nachtragen
@incollection{musterkommentar2022, ... }
```

---

## KI-Nutzung kennzeichnen (kein normaler Beleg!)

KI-erzeugte Inhalte werden **gekennzeichnet**, aber nicht wie eine Fachquelle
zitiert – und die Kennzeichnung **ersetzt keine Quellenangabe**:

```latex
% überarbeitete Übernahme (mit "Vgl."), als Fußnote:
... Aussage.\footnote{Vgl. ChatGPT, Version 4 (OpenAI), Zugriff am 01.11.2025.}
```

Zusätzlich: Eintrag im **KI-Verzeichnis** und Prompt-Kurzform im **Anhang**
(beides in der Vorlage vorbereitet). Details: [02 §8](02_formalia.md) und
[11](11_qualitaet-und-abgabe.md).

---

## Anderen Stil gebraucht? (z. B. IEEE in der Informatik)

Der WI-Leitfaden erlaubt **IEEE** (nummerierte Referenzen `[12]`). Falls dein
Modul das verlangt, stellst du in `template/main.tex` den `biblatex`-Stil um –
die ursprüngliche FOM-Vorlage dokumentiert diese Umstellung. Frag im Zweifel
deine:n Dozent:in, welcher Stil gilt, **bevor** du anfängst – nachträglich
umstellen ist lästig.

---

## Woran du merkst, dass du fertig bist

- [ ] Jede Behauptung hat eine Fußnote mit **Seitenangabe**.
- [ ] Direkte vs. indirekte Zitate korrekt (Vgl. / kein Vgl.).
- [ ] Gesetze im Fließtext, Kommentar-Nachweis in der Fußnote.
- [ ] Jeder `.bib`-Eintrag hat `langid` + `date`; Online zusätzlich `url`+`urldate`.
- [ ] `make check` meldet keine fehlenden Seitenangaben / falschen Anführungszeichen.

---

**Nächster Schritt:** [09 · Das LaTeX-Dokument bauen →](09_latex-bauen.md)
