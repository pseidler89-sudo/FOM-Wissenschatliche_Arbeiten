# 11 · Qualität prüfen & abgeben

> Der Inhalt steht – jetzt entscheidet die **Sorgfalt** über die Note.
> Formale Fehler, ein leeres Literaturverzeichnis oder eine vergessene
> KI-Kennzeichnung kosten leicht eine ganze Notenstufe. Dieses Kapitel ist deine
> Startbahn zur Abgabe.

---

## Zwei Review-Runden

Plane bewusst zwei Durchgänge ein:

1. **Selbst-Review** (du, gegen die Checkliste unten + `make check`).
2. **Externes Review** (optional, aber stark): 1–2 fachkundige Personen, die
   **nicht** die Zielgruppe sind. Stell **konkrete** Fragen statt „ist das gut?“
   – z. B. „Ist die Argumentation in Kapitel 3 lückenlos?“, „Versteht man die
   Forschungsfrage sofort?“. Feedback einarbeiten, jede Änderung committen.

---

## Automatische Prüfung: `make check`

Wenn du lokal mit Docker baust, prüft ein Befehl die häufigsten formalen
Stolperfallen:

```bash
make check
```

Er meldet u. a.: fehlende `langid` in der `.bib`, falsche Anführungszeichen
(`glqq` statt `\enquote`), Zitate **ohne** Seitenangabe, leere Fußnoten und
versehentliche Ich-/Wir-Form. Alles sollte „OK“ sein. (Bei Overleaf entfällt
der Befehl – arbeite dann die Checkliste manuell durch.)

---

## Die Abgabe-Checkliste

Die vollständige, abhakbare Liste liegt in
[`vorlagen/review-checkliste.md`](../vorlagen/review-checkliste.md). Die
Kernpunkte:

**Formalia**
- [ ] Ränder, Schrift, Zeilenabstand korrekt (Vorlage erledigt das)
- [ ] Seitenzahlen vorhanden, römisch→arabisch korrekt
- [ ] Titelblatt vollständig; gewählter **Leitfaden in der Einleitung genannt**
- [ ] Fußnoten einzeilig, kleiner als der Fließtext

**Struktur & roter Faden**
- [ ] Jedes Kapitel (außer Einleitung) hat **2–4 Sätze Kapitel-Einleitung**
- [ ] Jedes Kapitel-Ende führt ins nächste
- [ ] **Das Fazit beantwortet die Forschungsfrage aus der Einleitung**
- [ ] Gliederungstiefe ≤ 4, Mindestens-zwei-Regel eingehalten
- [ ] Umfang im Zielbereich

**Zitation & Literatur**
- [ ] **Jede** Behauptung belegt, jede Zitation mit Seitenangabe
- [ ] direkt/indirekt korrekt (Vgl. / kein Vgl.)
- [ ] Gesetze im Fließtext, Kommentar in der Fußnote
- [ ] jeder `.bib`-Eintrag: `langid` + `date`; Online: `url` + `urldate`
- [ ] Literaturverzeichnis vollständig, Internetquellen separat

**Sprache**
- [ ] keine Ich-/Wir-Form, Präsens, gendergerecht, keine Füllwörter
- [ ] keine KI-typischen Floskeln (siehe [07](07_schreiben-und-stil.md))

**KI-Redlichkeit** (siehe nächster Abschnitt)

**Bau & Optik**
- [ ] `make pdf` / Overleaf baut **fehlerfrei**
- [ ] PDF **visuell** geprüft: keine Schusterjungen/Hurenkinder, keine
      abgeschnittenen Tabellen, Abbildungen referenziert

---

## KI-Redlichkeit: die Abgabe-Pflichten

Wer KI genutzt hat (also fast alle), muss bei der Abgabe **sauber offenlegen**.
Was genau, sagt dein Leitfaden – die typischen Pflichten:

- **KI-Verzeichnis** ausgefüllt: alle genutzten Werkzeuge mit Anbieter, Version,
  **Einsatzzweck** (`verzeichnisse/ki_verzeichnis.tex`).
- **Lokale Kennzeichnung** im Text, wo KI-Inhalte übernommen wurden (System,
  Version, Datum) – und diese Inhalte **zusätzlich** mit Fachliteratur belegt.
- **Prompts** im Anhang – in Kurzform (WI) oder, wenn deine Prüfenden es
  verlangen, als **vollständiger Verlauf**; genutzte **KI-Ausgaben als ZIP**
  mit einreichen (JKS). Das Upload-Formular hat dafür meist ein optionales
  Feld „Zusatzdokumente“ – nutze es auch für eigene Vorarbeiten und das
  Recherche-Log.
- **Eigene Vorarbeiten** (Exposé, Vorstudie, frühere Ausarbeitung) im
  KI-Verzeichnis oder Anhang benennen – siehe [02](02_formalia.md), Abschnitt 8.
- **Eigenständigkeitserklärung** beifügen, wenn der Upload keine eigene
  abfragt – das Formular zeigt oft nur Sperrvermerk und Plagiatshinweis.
  Sie enthält die Versicherung, KI-Inhalte gekennzeichnet zu haben, **und**
  Übernahmen aus eigenen Arbeiten deklariert zu haben.

> Hier zahlt sich dein **Recherche-/KI-Log** (aus [04](04_quellenrecherche.md))
> aus: Du füllst das KI-Verzeichnis aus dem Log, statt am Abgabetag zu raten,
> was du vor sechs Wochen benutzt hast. **Ehrlichkeit schützt** – eine
> dokumentierte KI-Nutzung ist erlaubt, eine verschwiegene ist ein Risiko.

---

## Finalisieren

1. Finaler Build: `make pdf` (bzw. Overleaf Recompile).
2. PDF **am Bildschirm und – wenn möglich – ausgedruckt** durchsehen.
3. Literaturverzeichnis auf Vollständigkeit prüfen (jede zitierte Quelle taucht
   auf, keine Leichen).
4. Versionierten Stand sichern: `make release` und/oder Git-Tag
   (siehe [10](10_versionierung.md)).
5. Abgabe gemäß Prüfungsamt: meist **PDF-Upload** im Online-Campus, ggf.
   zusätzlich **gebunden** (Copyshop, Klebebindung) – Fristen und Form prüfen.

---

## Woran du merkst, dass du fertig bist

- [ ] Checkliste komplett abgehakt, `make check` grün (bzw. manuell geprüft).
- [ ] KI-Offenlegung vollständig (Verzeichnis, Kennzeichnung, Anhang/ZIP,
      Erklärung).
- [ ] PDF visuell geprüft, Abgabestand versioniert.
- [ ] Abgabeform & Frist mit dem Prüfungsamt abgeglichen.

---

🎉 **Geschafft.** Du hast eine wissenschaftliche Arbeit von der Forschungsfrage
bis zur abgabefertigen, versionierten PDF gebracht – formal sauber und mit KI
als ehrlichem Werkzeug, nicht als heimlichem Ghostwriter.

**Zurück zum:** [Überblick](00_ueberblick.md)
