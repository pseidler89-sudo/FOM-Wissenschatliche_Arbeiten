# 05 · Mit großen Volltexten arbeiten

> Du hast jetzt PDFs: Gesetzeskommentare, Studien,
> 90-seitige Verordnungen, Lehrbuchkapitel. Diese **Volltexte** mit KI
> durchzuarbeiten, ohne sich Falschzitate einzufangen, ist eine eigene
> Disziplin. Hier ist sie.

---

## Das Grundproblem: das Kontextfenster

Jede KI kann nur eine begrenzte Menge Text **gleichzeitig** „im Kopf“ behalten –
das **Kontextfenster**. Schiebst du mehr hinein, „vergisst“ sie Anfang oder
Mitte, vermischt Quellen oder erfindet Seitenzahlen. Zwei Faustregeln:

1. **Lieber wenige Quellen gründlich** als zehn PDFs auf einmal.
2. **Quelle für Quelle**, nicht „analysiere mir diese 8 PDFs zusammen“.

Moderne Modelle (besonders Gemini) haben sehr große Fenster – trotzdem gilt:
Je fokussierter die Eingabe, desto verlässlicher die Ausgabe.

---

## Drei Werkzeuge für große Texte

### NotebookLM – wenn du *deinen eigenen Quellen* Fragen stellen willst

NotebookLM (Google) ist für diese Aufgabe gebaut. Du lädst deine PDFs hoch und
fragst – die KI antwortet **nur auf Basis dieser Quellen** und **verlinkt jede
Aussage auf die Belegstelle** im Dokument. Das senkt das Halluzinationsrisiko
drastisch, weil sie kein Allgemeinwissen erfindet, sondern in deinen Texten
nachschlägt.

**Stark für:**
- „Was sagt diese Quelle zu *X*? Zeig mir die genaue Stelle.“
- Mehrere Quellen vergleichen: „Wo widersprechen sich Quelle A und B?“
- Sich einen 80-Seiten-Text erschließen, bevor man ihn liest.

**Grenze:** NotebookLM bewertet nicht und schreibt nicht deine Arbeit – es ist
ein **Befragungs-Werkzeug für deine Bibliothek.** Die Seitenzahl, die es nennt,
prüfst du trotzdem im PDF.

### Gemini – wenn ein Dokument *am Stück* analysiert werden soll

Geminis großes Kontextfenster eignet sich, um ein langes PDF komplett
einzugeben und z. B. eine strukturierte Zusammenfassung oder die stärksten
Zitate herauszuziehen.

### Claude – wenn der Kontext *über mehrere Sitzungen* halten soll

Claude „Projects“ halten Quellen, deine Forschungsfrage und dein Stilprofil
dauerhaft bereit, sodass du nicht in jeder Sitzung alles neu erklärst. Stark
fürs Schreiben und Umformulieren mit Quellenbezug.

---

## Der Kern-Workflow: Zitate Quelle für Quelle extrahieren

Das ist die Technik, mit der echte Arbeiten entstanden sind. Sie verbindet
Geschwindigkeit (KI) mit Sicherheit (Verifikation).

**Ablauf, iterativ pro Quelle:**

1. Du übergibst der KI **den Volltext (oder Ausschnitt) *einer* Quelle** und
   ihren **BibLaTeX-Key**.
2. Die KI führt drei Schritte aus:
   - **Kontext-Analyse:** Sie gleicht den Text mit deiner Argumentationslinie ab.
   - **Extraktion & Bewertung:** Sie filtert die **5 relevantesten** Belege
     heraus und begründet je 1–2 Sätze, *warum* und in *welches Kapitel* sie
     passen.
   - **LaTeX-Readiness:** Sie gibt zu jedem Beleg den **kopierfertigen
     Zitierbefehl** aus.
3. Ausgabe als **Markdown-Tabelle**:

   | Bewertung / Zielkapitel | Seite/Rn. | Zitat / Paraphrase | LaTeX-Befehl |
   |:--|:--|:--|:--|
   | [Kap. 3] stützt These, weil … | S. 12 | „…“ | `\autocite[Vgl.][S.~12]{key}` |

4. **Du prüfst jede Zeile gegen das PDF** – steht das Zitat wirklich auf S. 12,
   im behaupteten Wortlaut? – und übernimmst nur die geprüften.

Der komplette, erprobte Prompt dafür liegt in
[`vorlagen/recherche-prompts.md`](../vorlagen/recherche-prompts.md) (Abschnitt
„Zitatextraktion“).

> **Direkt vs. indirekt nicht vergessen:** Bei **wörtlichen** Zitaten **kein**
> „Vgl.“ und in `\enquote{…}` setzen; bei **sinngemäßen** Zitaten **mit**
> „Vgl.“. Fehlende Seiten: `o.\,S.`, `Abs.`, `Rn.`

---

## Seitenzahlen: die häufigste Halluzination

KI „rät“ Seitenzahlen oft erschreckend selbstbewusst. Schutzmaßnahmen:

- **PDF mit Seitenzahlen** geben; in der Anweisung verlangen, dass die KI die
  Seite aus dem Text **belegt** statt schätzt.
- Bei NotebookLM: die **verlinkte Belegstelle** anklicken und nachsehen.
- Im Zweifel die Stelle per Volltextsuche (Strg+F) im PDF gegenchecken.
- Lieber `o.\,S.` ehrlich angeben als eine erfundene Seitenzahl.

---

## Lange PDFs handhabbar machen

- **Durchsuchbar?** Gescannte PDFs ohne Textebene muss die KI „raten“. Vorher
  durch **OCR** (Texterkennung) jagen (viele PDF-Tools, auch kostenlose, können
  das).
- **Zerlegen:** Sehr lange Werke kapitel- oder abschnittsweise übergeben, jeweils
  mit Hinweis, aus welchem Teil der Ausschnitt stammt.
- **Anker mitschicken:** Wenn du nur einen Abschnitt fragst, sag, auf welchen
  Seiten er steht – dann kann die KI die Seitenzahl korrekt zuordnen.

---

## Eine ehrliche Notiz zu Zugriffsbeschränkungen

Manche Quellen (z. B. einzelne Nachrichtenportale, Bezahlschranken) lassen sich
von KI-Tools technisch **nicht** abrufen. Das heißt **nicht**, dass die Quelle
nicht existiert. Sauberer Umgang: Metadaten aus einer zweiten, zugänglichen
Quelle bestätigen, im Recherche-Log vermerken („durch Nutzerangabe gestützt,
nicht durch Tool-Volltext“) und die Stelle selbst im Original nachlesen, sobald
du Zugang hast. Transparenz schlägt Schein-Sicherheit.

---

## Woran du merkst, dass du fertig bist

- [ ] Du weißt, wann du NotebookLM (Quellen befragen), Gemini (langes Dokument)
      und Claude (dauerhafter Kontext) einsetzt.
- [ ] Du extrahierst Zitate **Quelle für Quelle** mit Seitenbeleg.
- [ ] **Jedes** Zitat ist gegen das Original geprüft, bevor es in die Arbeit geht.

---

**Nächster Schritt:** [06 · Gliederung entwerfen →](06_gliederung.md)
