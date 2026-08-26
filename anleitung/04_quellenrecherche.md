# 04 · Quellenrecherche mit KI (aber verifiziert)

> Phase 4. Jetzt baust du die Materialbasis deiner Arbeit auf: eine geprüfte
> Quellendatenbank in `literatur/literatur.bib`. KI beschleunigt das enorm –
> aber der entscheidende Schritt bleibt das **Verifizieren gegen das Original**.

---

## Der Workflow im Überblick

```
1. Suchbegriffe aus Forschungsfrage + Argumenten ableiten
2. Strukturierte KI-Recherche  (Prompt erzwingt BibLaTeX-Ausgabe)
3. JEDE Quelle gegen das Original prüfen  (existiert sie? stimmen die Daten?)
4. Geprüfte Einträge in literatur.bib übernehmen
5. Jede Suche im recherche-log dokumentieren
6. Quellen klassifizieren und ihre Qualität bewerten
```

Richtwert: **ca. 25–40 Quellen** für eine Seminar-/Bachelorarbeit (Breite *und*
Tiefe; WI nennt keine Mindestzahl, JKS sieht Qualität vor Quantität).

---

## Schritt 1: Suchbegriffe ableiten

Zerlege deine Forschungsfrage in ihre Bausteine und bilde zu jedem Synonyme und
englische Entsprechungen. Beispiel für „DSGVO-Anforderungen an KI-gestützte
Belegerkennung in KMU“:

- *DSGVO* → Datenschutz-Grundverordnung, GDPR, Art. 22, automatisierte
  Entscheidung
- *Belegerkennung* → OCR, Dokumentenklassifikation, document AI
- *KMU* → Mittelstand, small and medium enterprises

Diese Begriffe nutzt du sowohl in echten Datenbanken als auch in den
KI-Prompts.

---

## Schritt 2: Wo suchen?

KI ersetzt **nicht** die echten Fachdatenbanken – sie hilft, sie zu erschließen.
Nutze beides:

| Quelle | Wofür |
|:--|:--|
| **Google Scholar**, **BASE**, **SSRN** | Aufsätze, Preprints, Zitationszählung |
| **beck-online**, **juris** | Recht: Kommentare, Urteile (FOM-Zugang prüfen!) |
| **EUR-Lex** | EU-Recht im Volltext |
| **FOM-Bibliothek / EBSCO** | Lizenzierte Volltexte, peer-reviewed |
| Behörden (**BSI**, **BMF**, Statistisches Bundesamt) | Primärquellen, Studien |
| **Perplexity (Deep Research)** | Einstieg, Überblick, Auffinden von Kandidaten **mit Links** |

> Die **FOM-Bibliothek** gibt dir über den Online-Campus Zugang zu vielen
> kostenpflichtigen Datenbanken. Das ist oft wertvoller als jede KI.

---

## Schritt 3: Die KI-Recherche, die direkt BibLaTeX liefert

Der große Zeitgewinn entsteht, wenn die KI ihre Treffer **schon im richtigen
Format** ausgibt – als fertige BibLaTeX-Einträge, die du (nach Prüfung) direkt
in `literatur.bib` kopierst.

Erprobtes Vorgehen (drei spezialisierte Läufe):

1. **Rechtliche/normative Grundlagen** → Perplexity Deep Research
2. **Technische/empirische Grundlagen** → Gemini
3. **Marktdaten/Praxis** → Perplexity

Jeder Prompt endet mit einem **verbindlichen Ausgabeblock**, der u. a.
erzwingt:

- ein fertiger BibLaTeX-Eintrag pro Treffer,
- **Pflichtfelder** `langid` (`ngerman`/`english`) und `date` (ISO),
- bei Online-Quellen `url` + `urldate`,
- **kein** `year`-Feld (nur `date`),
- **keine erfundenen Quellen** – bei Unsicherheit `note = {Verifizierung empfohlen}`.

Die kompletten, kopierfertigen Prompts (inkl. dieses Ausgabeblocks) liegen in
[`vorlagen/recherche-prompts.md`](../vorlagen/recherche-prompts.md). Du passt
nur Rolle, Thema und Themenfelder an.

---

## Schritt 4: VERIFIZIEREN – der Schritt, den niemand auslassen darf

Behandle **jeden** KI-Treffer als unbestätigten Verdacht, bis du ihn am
Original geprüft hast.

**Prüf-Checkliste pro Quelle:**

- [ ] **Existiert** die Quelle wirklich? (Autor, Titel im Katalog/DOI auffindbar)
- [ ] Stimmen **Autor, Jahr, Titel, Zeitschrift, Band/Heft, Seiten**?
- [ ] Bei Urteilen: **Gericht, Datum, Aktenzeichen, Fundstelle** korrekt?
- [ ] Bei Online: **URL erreichbar**, Inhalt passt, `urldate` notiert?
- [ ] Sagt die Quelle **wirklich**, was die KI behauptet? (häufigster Fehler!)

Ein bewährter Verifikations-Prompt lässt die KI ihre eigenen (oder deine aus dem
Gedächtnis rekonstruierten) Einträge **gegenprüfen** und gibt pro Eintrag einen
ehrlichen **Status-Kommentar** aus:

```
% STATUS: verifiziert (Quelle: beck-online, abgerufen 2026-05-20)
% URSPRUNG: ersetzt Platzhalter neufang_2024_fzulg
@article{...}
```

Bei niedriger Konfidenz `% STATUS: niedrige Konfidenz` statt „verifiziert“.
Auch diesen Verifikations-Prompt findest du in der Vorlagen-Datei.

> **Faustregel:** Eine echte, geprüfte Seitenzahl schlägt jeden TODO-Platz-
> halter. Wenn du etwas noch nicht belegen kannst, setze einen **erkennbaren**
> Platzhalter (Werk und Norm benannt, nur Stelle offen) statt einer vagen
> unbelegten Behauptung – und ersetze ihn vor Abgabe.

---

## Schritt 5: Dokumentieren (recherche-log)

Halte **jede** Suche fest: Datum, Werkzeug/Datenbank, Suchbegriffe, Treffer,
was du übernommen hast. Das hat drei Gründe:

1. Du findest Quellen wieder und vermeidest Doppelarbeit.
2. Du kannst deine **Methodik** in der Einleitung sauber beschreiben.
3. Es ist die Grundlage für das **KI-Verzeichnis** und (bei JKS) die
   einzureichende KI-Dokumentation.

Vorlage: [`vorlagen/recherche-log_VORLAGE.md`](../vorlagen/recherche-log_VORLAGE.md).

---

## Schritt 6: Klassifizieren & Qualität bewerten

Ordne jede Quelle einer Kategorie zu – eine gute Arbeit mischt sie bewusst:

- **Primär:** Gesetze, Verordnungen, Urteile, amtliche Schreiben, Originaldaten
- **Sekundär:** Kommentare, Fachbücher, Monographien, Dissertationen – der
  Kern deiner Belegbasis (Theorie, Begriffsarbeit, Einordnung)
- **Fachartikel:** peer-reviewed Journals
- **Tertiär:** zusammenfassende Überblickswerke wie Lehrbücher – gut für den
  Einstieg und für Definitionen, **nicht** als Basis deiner Hauptargumente.
  (Lexika/Wikipedia bleiben ganz tabu, siehe unten.)
- **Graue Literatur:** nicht formal publizierte Quellen – Working Papers,
  White Papers, Unternehmensberichte. Nützlich für Aktuelles, aber
  **begründungspflichtig**: Autorität und Nachvollziehbarkeit besonders streng
  prüfen.
- **Praxis:** Behörden-Stellungnahmen, seriöse Branchenstudien, Fach-Blogs

### Bias-Schnellcheck deiner Quellenliste

Wenn die Liste steht, prüfe sie einmal als Ganzes – drei Faustregeln machen
einseitige Recherche sichtbar, bevor es die Gutachter:innen tun:

- [ ] **Dominiert ein Quellentyp** (≥ ¾ der Liste)? → Mix erweitern; nur
      Webquellen oder nur Kommentare fällt auf.
- [ ] **Stammen ≥ 4 Quellen von derselben Autorenschaft?** → Du hängst an
      einer Denkschule. Gezielt Gegenpositionen suchen.
- [ ] **Liegen (bei ≥ 8 Quellen) alle in einer Spanne von ~2 Jahren?** →
      Ältere Grundlagenwerke bzw. den aktuellen Stand ergänzen – je nach dem,
      was fehlt.

### Quellenqualität bewerten (FOM-Kriterien, KEL-Leitfaden)

Bevor du etwas zitierst, prüfe:

1. **Intention** – informierend & objektiv, oder interessengeleitet/Werbung?
2. **Autor:in** – fachliche Qualifikation, Institution, weitere Publikationen?
3. **Zielgruppe** – wissenschaftlich (peer-reviewed, mit Belegen) vs. populär
   (Spiegel, Fokus)?
4. **Umfang** – deckt die Quelle deinen Aspekt wirklich ab?
5. **Aktualität** – gerade in Recht (Gesetzesänderungen) und Informatik
   (Technikwandel) kritisch.
6. **Renommee/Kennziffern** – Journal-Ranking (VHB-JOURQUAL), Zitationszahl,
   Verlag.

**Nicht zitierfähig:** Wikipedia & andere Lexika, Vorlesungsfolien, andere
Studienarbeiten. KI-Ausgaben sind **keine** Quelle – sie werden gekennzeichnet,
aber der *Beleg* kommt aus der Fachliteratur.

Halte 2–3 Sätze Relevanz je Quelle fest (z. B. in
`vorlagen/recherche-log_VORLAGE.md` oder einer eigenen `literatur_analyse.md`).
Das ist später die Basis fürs Schreiben.

---

## Exit-Kriterium

- [ ] `literatur/literatur.bib` enthält ~25–40 **geprüfte** Einträge.
- [ ] Jeder Eintrag hat `langid` und `date`; Online-Quellen `url` + `urldate`.
- [ ] Jede Quelle ist klassifiziert und kurz auf Relevanz bewertet.
- [ ] Das Recherche-Log ist geführt.

---

**Nächster Schritt:** [05 · Mit großen Volltexten arbeiten →](05_grosse-texte.md)
