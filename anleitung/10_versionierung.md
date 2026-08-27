# 10 · Versionieren & sichern

> „Zwischenstand_final_final_v3_wirklichfinal.pdf“ kennt jeder. Es geht
> besser. Mit **Versionierung** hast du jeden Stand deiner Arbeit sicher, kannst
> jederzeit zurück und verlierst nie etwas – und du bekommst statt einer einzigen
> `main.pdf` **nachvollziehbare, datierte PDF-Stände**.

---

## Warum überhaupt versionieren?

Drei Gründe:

1. **Backup.** Eine Arbeit, die nur auf deinem Laptop liegt, ist eine Arbeit,
   die ein Kaffee zerstören kann. Versioniert + in der Cloud = sicher.
2. **Zeitreise.** „Gestern war der Absatz besser“ – mit Versionsverwaltung holst
   du ihn zurück.
3. **Nachvollziehbarkeit.** Du siehst, was du wann geändert hast – nützlich für
   die eigene Übersicht und für die Methodik-Dokumentation.

Du kannst das **einfach** (Overleaf-History) oder **voll** (Git + GitHub) haben.

---

## Variante einfach: Overleaf-History

Wenn du über [Overleaf](09_latex-bauen.md) arbeitest, versioniert es **automatisch**:

- *Menu → History* zeigt alle Stände; du kannst zu jedem zurückspringen.
- *Labels* setzen markiert wichtige Stände („Rohfassung fertig“, „nach Review“).
- Overleaf liegt in der Cloud – das Backup hast du gratis.

Das reicht für viele Studierende völlig.

---

## Variante voll: Git + GitHub

Git speichert **Schnappschüsse** („Commits“) deines Projekts. GitHub legt diese
ins Netz (Backup + Zugriff überall). Du brauchst dafür **keine** Kommandozeile:
**[GitHub Desktop](https://desktop.github.com/)** macht alles per Klick.

**Der Mini-Workflow (egal ob Klick oder Terminal):**

```bash
git add -A
git commit -m "feat: Kapitel 2 Grundlagen geschrieben"
git push
```

- **`commit`** = Schnappschuss mit Nachricht.
- **`push`** = ab in die Cloud (GitHub).
- Mach das **nach jedem fertigen Kapitel** und am Ende jedes Arbeitstags.

### Gute Commit-Nachrichten

Kurze, aussagekräftige Präfixe halten die Historie lesbar:

```
feat:  neues Kapitel / neuer Inhalt      (z.B. "feat: Kapitel 3 Analyse")
fix:   Fehler/Inkonsistenz behoben       (z.B. "fix: Zitat Kap. 2 korrigiert")
ref:   Quellen/Belege ergänzt            (z.B. "ref: 5 Quellen zu Kap. 4")
docs:  Notizen/Doku aktualisiert
chore: Aufräumen
```

### Branches (optional)

Wer experimentieren will, ohne den guten Stand zu gefährden, legt einen
**Branch** an (eine Parallelversion), schreibt dort und führt ihn zusammen, wenn
es passt. Für die meisten Arbeiten reicht aber **ein** Strang.

---

## Versionierte PDFs statt nur „main.pdf“

Genau das, was den Unterschied macht: Statt am Ende eine einzige `main.pdf` zu
haben, legst du **datierte, eindeutige** Stände ab. Das `template/` enthält
dafür einen fertigen Befehl:

```bash
make release
# → releases/main_20260115_1430_a1b2c3d.pdf
```

Der Dateiname enthält **Datum, Uhrzeit und den Git-Commit** – so weißt du
immer, welcher Quellstand zu welcher PDF gehört. Praktisch z. B. um die
„Fassung für den Reviewer“ und die „Abgabefassung“ sauber zu trennen.

> Standardmäßig wird die `main.pdf` **nicht** mit eingecheckt (steht so in der
> `.gitignore`-Logik), weil sie aus den Quellen jederzeit neu entsteht. Die
> bewusst abgelegten `releases/`-PDFs kannst du dagegen mit committen, wenn du
> Meilensteine festhalten willst.

---

## Finale Version markieren: Tags

Wenn die Arbeit abgegeben ist, markiere den exakten Stand mit einem **Tag**:

```bash
git tag -a v1.0 -m "Abgabefassung 2026-01-15"
git push origin v1.0
```

So findest du die Abgabefassung später garantiert wieder – egal, wie viel du
danach noch änderst.

> Hinweis: In manchen automatisierten Ausführungsumgebungen schlägt das
> **Pushen von Tags** mit einem Berechtigungsfehler (HTTP 403) fehl. Dann den
> Tag einfach über die **GitHub-Weboberfläche** anlegen
> (*Releases → Draft a new release → Tag erstellen*). Commits und normale
> Branch-Pushes sind davon nicht betroffen.

---

## Was gehört NICHT ins Repository?

Die mitgelieferte `.gitignore` blendet automatisch die **Build-Hilfsdateien**
aus (`.aux`, `.log`, `.bbl`, `.toc` …). Sonst gilt:

- **Keine sensiblen Daten** (echte Interviewdaten mit Klarnamen, vertrauliche
  Unternehmensunterlagen) in ein **öffentliches** Repo.
- **Keine fremden, lizenzgeschützten PDFs** (z. B. die FOM-Leitfäden selbst)
  öffentlich weiterverbreiten – verlinke/benenne sie stattdessen.

---

## Woran du merkst, dass du fertig bist

- [ ] Deine Arbeit ist versioniert (Overleaf-History **oder** Git+GitHub).
- [ ] Es gibt ein Cloud-Backup.
- [ ] Du legst wichtige Stände als `release` und/oder Tag ab.

---

**Nächster Schritt:** [11 · Qualität prüfen & abgeben →](11_qualitaet-und-abgabe.md)
