# FAQ – Häufige Fragen

Kurze Antworten auf die häufigsten Fragen. Tiefer geht es in der
[Anleitung](anleitung/00_ueberblick.md).

## Einstieg & Technik

??? question "Brauche ich LaTeX-Kenntnisse?"
    Nein. Der einfachste Weg läuft komplett im Browser über
    [Overleaf](anleitung/09_latex-bauen.md): ZIP hochladen, Daten in
    `skripte/meta.tex` eintragen, in `kapitel/` schreiben, **Recompile**. Du
    fasst nur Text an, das Layout macht die Vorlage.

??? question "Die PDF baut nicht / Schrift-Fehler. Was tun?"
    Fast immer der **falsche Compiler**. Die Vorlage braucht **XeLaTeX**
    (Overleaf: *Menu → Settings → Compiler → XeLaTeX*). Weitere Fehlerbilder und
    Lösungen: [LaTeX bauen → Fehlerbehandlung](anleitung/09_latex-bauen.md).

??? question "Mein Literaturverzeichnis ist leer."
    Beim ersten Durchlauf läuft das Literaturprogramm (Biber) noch nicht mit.
    Einfach **nochmal kompilieren** – dann erscheint es.

??? question "Wie zähle ich Wörter?"
    Overleaf: *Menu → Word Count*. Oder
    [TeXcount](https://app.uio.no/ifi/texcount/online.php). Gezählt wird der
    Textteil, nicht Verzeichnisse/Anhang.

??? question "Kann ich die Kapitelstruktur ändern?"
    Ja – die vier Kapitel der Vorlage sind nur ein **Beispielgerüst**. Lösche,
    benenne um oder ergänze frei; passe die `\input{...}`-Zeilen in `main.tex`
    an. Welche Struktur passt: [Gliederung](anleitung/06_gliederung.md).

## Formalia

??? question "Welchen Zitierstil soll ich nehmen?"
    Das hängt von **deinem** Hochschulbereich/Leitfaden ab (Fußnotenstil,
    Harvard oder IEEE). Die Vorlage ist auf den FOM-Fußnotenstil vorkonfiguriert.
    Im Zweifel mit der/dem Dozent:in abklären. Details:
    [Zitieren](anleitung/08_zitieren.md).

??? question "Wie viele Quellen / wie viele Seiten?"
    Richtwert ~25–40 Quellen. Umfang laut Leitfaden (z. B. Seminararbeit
    ~4.000 Wörter, Bachelor 40–60 Seiten) – immer mit der Modulbeschreibung
    abgleichen. Mehr: [Formalia](anleitung/02_formalia.md).

??? question "Wie zitiere ich Gesetze und Urteile?"
    Paragraphen/Artikel kommen in den **Fließtext** (z. B. „§ 433 BGB"), der
    Beleg (Kommentar mit Seite) in die **Fußnote**. Urteile mit Gericht, Datum,
    Aktenzeichen, Fundstelle. Siehe [Zitieren](anleitung/08_zitieren.md).

??? question "Muss jede Aussage belegt sein?"
    Ja. Jeder Absatz braucht mindestens eine Fußnote mit Seitenangabe. Ohne
    Stellenangabe kein gültiger Beleg.

## KI

??? question "Darf ich überhaupt KI benutzen?"
    Ja – an der FOM **erlaubt, aber kennzeichnungspflichtig**. Du legst die
    genutzten Werkzeuge im KI-Verzeichnis offen und kennzeichnest übernommene
    Inhalte im Text. Verschweigen ist das Risiko, nicht die Nutzung.
    Siehe [Formalia §8](anleitung/02_formalia.md) und
    [Qualität & Abgabe](anleitung/11_qualitaet-und-abgabe.md).

??? question "Wie verhindere ich, dass mein Text „nach KI" klingt?"
    Mit der Checkliste [KI-Stilmerkmale](vorlagen/ki-stilmerkmale.md): typische
    Floskeln, vage Autoritäten, Markdown-Reste und Copy-Paste-Artefakte gezielt
    heraussuchen und entfernen.

??? question "Kann ich KI die Quellen suchen lassen?"
    Als Startpunkt ja – aber **jede** Quelle gegen das Original prüfen. KI
    erfindet überzeugend aussehende Quellen und Seitenzahlen. Vorgehen:
    [Quellenrecherche](anleitung/04_quellenrecherche.md).

## Sichern & Abgeben

??? question "Wie sichere ich Zwischenstände?"
    Über Overleaf-History oder Git/GitHub. Statt nur „main.pdf" kannst du mit
    `make release` datierte PDF-Stände ablegen.
    Siehe [Versionieren](anleitung/10_versionierung.md).

??? question "Was muss ich vor der Abgabe prüfen?"
    Die [Abgabe-Checkliste](vorlagen/review-checkliste.md) Punkt für Punkt –
    Formalia, roter Faden, Zitate, KI-Offenlegung, sauberer Build.

---

Frage nicht dabei? [Eröffne ein Issue](https://github.com/pseidler89-sudo/FOM-Wissenschatliche_Arbeiten/issues/new) –
siehe auch [Mitmachen](CONTRIBUTING.md).
