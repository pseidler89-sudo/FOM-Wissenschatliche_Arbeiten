# Konzept: Website / GitHub Pages

> Konzept, wie aus diesem Repo eine **richtig intuitive Website** wird, die es
> FOM-Studierenden so einfach wie möglich macht, eine wissenschaftliche Arbeit
> zu schreiben. Entscheidungsreif aufbereitet – mit Empfehlung, Architektur,
> Feature-Ideen und einem Phasenplan.
>
> **Update – Stufe 1 (MVP) ist umgesetzt.** Gewählt wurde **MkDocs Material**
> (statt Just the Docs), weil der Fokus auf maximaler Lesbarkeit/„cool &
> intuitiv“ liegt und der Build vollständig automatisiert ist (GitHub Actions →
> GitHub Pages). Konfiguration im Repo-Root: `mkdocs.yml`, Build-Skript
> `scripts/build-site.sh`, Deploy-Workflow `.github/workflows/deploy-docs.yml`.
> Die Inhalte bleiben Single Source im Repo-Root und werden im Build nach
> `docs/` gesammelt. **Einmaliger Schritt durch den Inhaber:** Repo → Settings →
> Pages → Source: *GitHub Actions*. Die folgenden Stufen (Phasen-Stepper,
> Open-in-Overleaf-Knopf, eigene Domain) bleiben als Ausbau offen.

---

## 1. Ziel & Leitprinzipien

**Ziel:** Eine öffentliche Website, auf der jemand ohne Vorwissen in **5 Minuten
zur ersten PDF** kommt und Schritt für Schritt durch den ganzen Prozess geführt
wird – auf dem Handy genauso gut wie am Laptop.

**Leitprinzipien:**

1. **Inhalt bleibt Markdown.** Die Anleitung liegt schon als Markdown vor – die
   Website soll *dieselben Dateien* rendern, nicht eine zweite Inhaltsquelle
   schaffen (sonst pflegst du alles doppelt).
2. **Wartbar von Nicht-Entwickler:innen.** Du musst die Seite per
   GitHub-Web-Editor aktualisieren können; Deploy passiert automatisch.
3. **Null Hürde für Leser:innen.** Suche, Navigation, „Open in Overleaf“-Knopf,
   Copy-Buttons – die Seite nimmt Arbeit ab, statt zu erklären.
4. **Mobil & barrierearm.** Viele lesen am Handy.
5. **Kostenlos & robust.** GitHub Pages hostet statisch, kostenlos, ohne Server.

---

## 2. Zielgruppe & Randbedingungen

- **Leser:innen:** FOM-Studierende, oft wenig technikaffin, unter Zeitdruck.
- **Maintainer:** du (Patrick) – Markdown ja, aber kein Wunsch nach komplexer
  Toolchain-Pflege.
- **Inhalt:** bereits vorhanden (`anleitung/`, `vorlagen/`, `template/`).
- **Hosting:** GitHub Pages (im Repo schon „kostenlos dabei“).

---

## 3. Die Optionen im Vergleich

| Lösung | Wie es baut | UX / „cool“ | Wartung | Empfehlung |
|:--|:--|:--|:--|:--|
| **Just the Docs** (Jekyll) | nativ von GitHub Pages | gut: Suche, Seitenleiste, Dark Mode | sehr gering | ⭐ **MVP** |
| **MkDocs Material** | via GitHub Actions | exzellent: beste Suche, Tabs, Copy-Buttons, Stepper | gering (CI einmal eingerichtet) | ⭐ **Ausbau** |
| **Docsify** | kein Build (JS zur Laufzeit) | ok, aber schlechter auffindbar (SEO) | minimal | Notnagel |
| **Starlight / Astro** | Node-Build via Actions | top, aber „echtes“ Frontend | höher (npm) | Overkill |
| Plain README only | – | niedrig | null | Status quo |

**Kernabwägung:** *Just the Docs* ist von GitHub Pages nativ unterstützt
(kein eigener Build-Workflow nötig, einfach `_config.yml` + Theme) und rendert
unsere Markdown-Dateien fast unverändert. *MkDocs Material* sieht moderner aus
und hat die beste Suche/Interaktivität, braucht aber einen kleinen
GitHub-Actions-Workflow.

---

## 4. Empfehlung: zweistufig

**Stufe 1 – MVP mit *Just the Docs* (schnell live, kaum Wartung).**
Wir aktivieren GitHub Pages, legen ein `_config.yml` und pro Markdown-Datei
einen kleinen Kopf (Titel + Reihenfolge) an. Ergebnis: durchsuchbare Doku-Seite
mit Seitenleiste, Dark Mode, mobil – aus dem vorhandenen Inhalt.

**Stufe 2 – „Richtig cool“ mit *MkDocs Material* (wenn die Seite wachsen soll).**
Moderner Look, Tab-Navigation, eingebaute Copy-Buttons, bessere Suche, ein
visueller **Phasen-Stepper**, eigene Startseite mit großen Aktions-Karten
(„In 5 Minuten zur PDF“, „Open in Overleaf“, „Vorlagen herunterladen“).

> Beide nutzen denselben Markdown-Inhalt. Man kann mit Stufe 1 starten und
> später auf Stufe 2 wechseln, ohne den Inhalt neu zu schreiben.

---

## 5. Informationsarchitektur (Sitemap)

```
Startseite  ──  "In 5 Minuten zur ersten PDF" + 3 große Karten
│                (Anleitung starten · Open in Overleaf · Vorlagen)
│
├─ Schnellstart            (der kürzeste Weg, mit Overleaf-Knopf)
│
├─ Die 9 Phasen            (visueller Wegweiser / Stepper)
│   └─ verlinkt die Anleitungskapitel in Reihenfolge
│
├─ Anleitung               (= anleitung/, 12 Kapitel, durchsuchbar)
│   ├─ 00 Überblick … 11 Qualität & Abgabe
│
├─ Werkzeugkasten          (= vorlagen/)
│   ├─ Thesenpapier · KI-Prompts · Recherche-Log
│   ├─ Stilprofil · KI-Stilmerkmale · Abgabe-Checkliste
│
├─ Die LaTeX-Vorlage       (template/-Erklärung + ZIP-Download + Overleaf)
│
├─ FAQ / Troubleshooting   (häufige Build-Fehler, Zitierfragen)
│
└─ Glossar                 (aus Kapitel 00)
```

---

## 6. „Cool & intuitiv“ – die Feature-Ideen

Was die Seite über eine reine Doku hinaushebt:

- **„Open in Overleaf“-Knopf.** Ein Klick öffnet die Vorlage direkt in Overleaf.
  Technik: Button-URL `https://www.overleaf.com/docs?snip_uri=<URL-zur-template.zip>`.
  Dafür baut ein kleiner CI-Job bei jedem Release eine `template.zip` und legt
  sie als Release-Asset ab; der Knopf zeigt darauf. → Null Setup für Studierende.
- **Phasen-Stepper auf der Startseite.** Die 9 Phasen als anklickbare Schritte –
  man sieht sofort, wo man steht und was als Nächstes kommt.
- **Copy-Buttons** an allen Prompt- und Codeblöcken (in Material eingebaut). Die
  KI-Prompts sind dadurch mit einem Klick kopiert.
- **Suche** über die ganze Anleitung (beide Themes bringen sie mit).
- **Interaktive Checklisten** (die Abgabe-Checkliste zum Abhaken im Browser).
- **Download-Buttons:** Vorlagen einzeln und die ganze LaTeX-Vorlage als ZIP.
- **Dark Mode & Mobile** (beide Themes, automatisch).
- **„Automatische PDF-Vorschau“:** Ein CI-Job baut bei jedem Push die
  Beispiel-PDF der Vorlage und verlinkt sie – Beweis, dass alles baut, und
  Live-Beispiel des Ergebnisses (knüpft an `make release`/Versionierung an).
- **Callout-/Hinweis-Boxen** (Tipp/Achtung/FOM-Regel) für Scanbarkeit.

---

## 7. Wartungs-Workflow (für Nicht-Entwickler)

1. Inhalt ändern = Markdown-Datei im **GitHub-Web-Editor** bearbeiten
   (Bleistift-Symbol), „Commit“.
2. GitHub Pages / der Actions-Workflow **deployt automatisch** in ~1 Minute.
3. Fertig – kein lokales Setup, kein manuelles Hochladen.

Das ist genau dieselbe Einfachheit, die wir den Studierenden für ihre Arbeit
versprechen – nur für die Website.

---

## 8. Domain & URL

- Standard kostenlos: `https://pseidler89-sudo.github.io/FOM-Wissenschatliche_Arbeiten/`
- Optional schöner: eigene (Sub-)Domain (z. B. `fom-arbeiten.de`) per CNAME –
  einmalig DNS setzen, dann gratis über Pages.

---

## 9. Phasenplan

| Phase | Inhalt | Aufwand |
|:--|:--|:--|
| **P1 – MVP** | Pages aktivieren, *Just the Docs*, `_config.yml`, Navigation/Reihenfolge, Startseite mit Schnellstart + Overleaf-Knopf | klein (≈ halber Tag) |
| **P2 – Politur** | FAQ/Troubleshooting-Seite, Glossar-Seite, Callout-Stile, Download-Buttons, Logo/Farben | klein–mittel |
| **P3 – „cool“** | Umstieg auf *MkDocs Material* (oder Material-Features nachrüsten), Phasen-Stepper, Copy-Buttons, Suche tunen | mittel |
| **P4 – Automatik** | CI: `template.zip` als Release-Asset + automatische PDF-Vorschau; „Open in Overleaf“ verdrahten; eigene Domain | mittel |

---

## 10. Offene Entscheidungen (für dich)

1. **Theme:** mit *Just the Docs* starten (schnell, wartungsarm) oder direkt
   *MkDocs Material* (mehr „wow“, etwas mehr Setup)?
2. **Domain:** github.io-Adresse reicht, oder eigene Domain?
3. **Branding:** Name/Logo/Farben? (Aktuell neutral.)
4. **Sprache:** rein Deutsch (empfohlen, Zielgruppe) oder später zweisprachig?

---

## 11. Nächste Schritte

Sag, welche Option du willst – dann setze ich **P1 (MVP)** direkt um: Pages
aktivieren, Theme + Navigation einrichten, eine einladende Startseite mit
Schnellstart und „Open in Overleaf“-Knopf bauen, sodass die Seite live ist und
du sie nur noch mit Inhalten füllst.
