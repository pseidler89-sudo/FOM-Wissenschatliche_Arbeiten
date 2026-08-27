# 09 · Das LaTeX-Dokument bauen

> Du machst das hier zweimal: **einmal ganz am Anfang** (leere
> Vorlage zur PDF bauen – Werkzeug-Test), und **am Ende** (fertige Arbeit). Es
> gibt drei Wege. Such dir **einen** aus. Du brauchst keine LaTeX-Kenntnisse.

---

## Welcher Weg ist meiner?

| Weg | Aufwand | Für wen |
|:--|:--|:--|
| **A · Overleaf** | sehr gering, im Browser | **Empfohlen**, wenn du keine Technik magst |
| **B · Docker** | mittel, ein Befehl lokal | Wenn du lokal & offline arbeiten willst |
| **C · Tectonic lokal** | mittel | Fortgeschrittene, die kein Docker wollen |

> **Wichtig für ALLE Wege:** Diese Vorlage nutzt die Schrift *TeX Gyre Termes*
> (freier Times-New-Roman-Klon). Dafür braucht es den **XeLaTeX**- oder
> **LuaLaTeX**-Compiler – **nicht** das oft voreingestellte pdfLaTeX. Bei Docker
> und Tectonic ist das automatisch richtig; bei Overleaf stellst du es einmal um.

---

## Weg A · Overleaf (empfohlen)

[Overleaf](https://www.overleaf.com) ist LaTeX im Browser – nichts zu
installieren.

1. **Konto anlegen** (kostenlos) auf overleaf.com.
2. Den Ordner **`template/`** als **ZIP** vorbereiten (auf GitHub:
   *Code → Download ZIP*, dann den `template`-Unterordner zippen – oder das
   ganze Repo hochladen und in Overleaf den Hauptordner auf `template` zeigen
   lassen).
3. In Overleaf: **New Project → Upload Project** → ZIP hochladen.
4. **Compiler umstellen:** *Menu (oben links) → Settings → Compiler →* **XeLaTeX**.
5. **Main document** auf `main.tex` setzen (falls nicht automatisch).
6. **Recompile** klicken. Nach ein paar Sekunden erscheint rechts die PDF.
7. **Download PDF** (Symbol über der Vorschau).

Overleaf führt **Biber** (das Literaturverzeichnis-Programm) **automatisch** aus.
Wenn das Literaturverzeichnis nach der ersten Kompilierung leer ist, einfach
**noch einmal** „Recompile“ drücken.

> Overleaf kann sich direkt mit **GitHub** verbinden (*Menu → GitHub*). So hast
> du Browser-Komfort **und** Versionierung/Backup – siehe [10](10_versionierung.md).

---

## Weg B · Docker (lokal, ein Befehl)

Voraussetzung: [Docker](https://docs.docker.com/get-docker/) ist installiert und
läuft.

```bash
cd template
make pdf          # baut main.pdf  (alternativ: docker compose up --build)
```

Beim **ersten** Mal lädt Docker das Build-Image (dauert ein paar Minuten),
danach geht es schnell. Ergebnis: `template/main.pdf`.

Weitere Befehle:

```bash
make clean        # Hilfsdateien löschen (PDF bleibt)
make check        # Qualitätsprüfung (langid, Anführungszeichen, Seitenangaben …)
make release      # versionierte Kopie in releases/ ablegen (siehe Kap. 10)
make shell        # Shell im Container öffnen (Fehlersuche)
```

Das Build-Image nutzt **Tectonic**, das alle benötigten LaTeX-Pakete
automatisch beschafft – du musst nichts manuell installieren.

---

## Weg C · Tectonic lokal

Wenn du [Tectonic](https://tectonic-typesetting.github.io/) installiert hast:

```bash
cd template
tectonic -X compile main.tex
```

Tectonic lädt Pakete beim ersten Lauf selbst nach und ruft Biber automatisch
auf. Kein TeX-Live-Riesenpaket nötig.

---

## Wörter zählen

Die FOM gibt Umfänge oft in **Wörtern** an (z. B. Seminararbeit ~4.000).

- **Overleaf:** *Menu → Word Count*. Mit `%TC:ignore` … `%TC:endignore` kannst du
  Bereiche ausschließen.
- **Online:** [TeXcount](https://app.uio.no/ifi/texcount/online.php) – `.tex`
  hochladen.
- Gezählt wird der **Textteil** (Kapitel), nicht Verzeichnisse/Anhang.
- **Aus der PDF statt aus den Quellen:** `./skripte/woerter.sh <erste> <letzte Seite>`
  zählt die angegebenen PDF-Seiten – so, wie Prüfende zählen, die Überschriften
  und Fußnoten mitrechnen. In den `.tex`-Dateien steht ein Beleg nur als
  `\autocite`-Schlüssel; in der PDF steht die ausgeschriebene Fußnote, und die
  zählt dann mit. `python3 skripte/umfang.py` zählt dagegen aus den Quellen und
  weist Fußnoten getrennt aus – gut beim Schreiben, nicht für die Angabe auf
  dem Titelblatt.

---

## Wenn etwas schiefgeht – Fehlerbehandlung

LaTeX-Fehler sehen schlimm aus, sind aber meist trivial. Lies die **erste**
Fehlermeldung (nicht die letzte) – sie nennt Datei und Zeile.

| Symptom | Ursache & Lösung |
|:--|:--|
| Schrift-/Font-Fehler, „fontspec“ | Falscher Compiler. **XeLaTeX** einstellen (nicht pdfLaTeX). |
| Literaturverzeichnis **leer** | Biber lief noch nicht. Einfach **erneut** kompilieren (Overleaf) bzw. `make pdf` wiederholen. |
| `Citation 'xyz' undefined` | Schlüssel im `\autocite{xyz}` existiert nicht in `literatur.bib` (Tippfehler?). |
| `File 'bild.png' not found` | Bild fehlt in `abbildungen/` oder Dateiname stimmt nicht (Groß/Klein!). |
| `Undefined control sequence` | Tippfehler in einem `\befehl` oder Paket fehlt. Zeile aus der Meldung prüfen. |
| Umlaute kaputt | Datei muss **UTF-8** sein (Standard in Overleaf/VS Code). |
| Klammer-/`$`-Fehler | Eine `{`, `}`, `\begin{}`/`\end{}` oder `$` ist nicht geschlossen. |

> **Profi-Tipp:** Wenn ein neuer Absatz den Build bricht, kommentiere ihn
> testweise mit `%` aus und baue erneut – so grenzt du die Fehlerstelle ein.
> Und: **früh und oft bauen**, dann ist immer nur die letzte kleine Änderung
> schuld.

KI hilft auch hier: Fehlermeldung + betroffene Zeile in Claude/ChatGPT einfügen
und nach der Ursache fragen.

---

## Editor (optional, für Weg B/C)

Du kannst `.tex`-Dateien mit jedem Texteditor bearbeiten. Komfortabel ist
**VS Code** mit der Erweiterung **LaTeX Workshop** (Vorschau, Auto-Build) und
optional **LTeX** (Rechtschreib-/Grammatikprüfung für LaTeX).

---

## Woran du merkst, dass du fertig bist

- [ ] Du hast **einmal am Anfang** die leere Vorlage erfolgreich zur PDF gebaut.
- [ ] Du weißt, welcher der drei Wege deiner ist.
- [ ] Du kennst die XeLaTeX-Regel und die zwei häufigsten Fehler (Compiler,
      leeres Literaturverzeichnis).

---

**Nächster Schritt:** [10 · Versionieren & sichern →](10_versionierung.md)
