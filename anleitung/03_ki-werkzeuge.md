# 03 · KI-Werkzeuge auswählen und richtig bedienen

> KI kann dir bei einer wissenschaftlichen Arbeit enorm helfen – aber
> nur, wenn du das **richtige Werkzeug für die richtige Aufgabe** nimmst und die
> Ergebnisse **immer verifizierst**. Dieses Kapitel ist die Werkzeugkunde. Wie
> du damit konkret recherchierst, steht in [04](04_quellenrecherche.md) und
> [05](05_grosse-texte.md).

---

## Die eine Regel, die alles trägt

> **KI ist Zuarbeiter, nicht Autor.** Sie liefert Entwürfe, Vorschläge,
> Umformulierungen. Die fachliche Verantwortung – jede Tatsache, jede Quelle,
> jede Seitenzahl – bleibt **zu 100 % bei dir.**

Warum so streng? Weil KI-Sprachmodelle darauf trainiert sind, *plausibel*
zu klingen, nicht *wahr* zu sein. Sie erfinden Quellen, Autoren, Seitenzahlen
und Urteile, die täuschend echt aussehen (→ „Halluzination“). Wer ungeprüft
übernimmt, baut Falschzitate in eine Prüfungsleistung ein – das ist ein
Täuschungsversuch mit harten Folgen.

Daraus folgt der Arbeitsmodus dieser Anleitung: **KI schlägt vor – du prüfst
gegen das Original – erst dann übernimmst du.**

---

## Die Werkzeuge im Vergleich

Es gibt nicht „die beste KI“. Es gibt das passende Werkzeug pro Aufgabe.

| Werkzeug | Stärke | Schwäche | Am besten für |
|:--|:--|:--|:--|
| **Perplexity** | sucht live im Web, **liefert Quellen-Links** zu jeder Aussage; „Deep Research“-Modus | Tiefe begrenzt; Links müssen trotzdem geprüft werden | **Faktenrecherche & Quellensuche**, Gegenprüfung von Behörden-/Gerichtsangaben |
| **Google Gemini** | **sehr großes Kontextfenster** (lange Dokumente am Stück), gut bei Technik | manchmal überangepasst an Suchtreffer | **lange Volltexte analysieren**, Zitate aus PDFs extrahieren |
| **NotebookLM** (Google) | arbeitet **nur mit deinen hochgeladenen Quellen**, jede Antwort verlinkt auf die Belegstelle | kein Allgemeinwissen, bewusst eingeschränkt | **deine eigenen PDFs befragen**, ohne Halluzination |
| **Claude** (Anthropic) | starkes Schreiben & Argumentieren, lange Texte, „Projects“ für dauerhaften Kontext | Web-Recherche je nach Zugang eingeschränkt | **Strukturieren, Umformulieren, Gegenlesen, Stil** |
| **ChatGPT** (OpenAI) | Allrounder, breites Ökosystem | erfindet bei Quellen besonders gern | Brainstorming, Erklärungen, Code/Tabellen |

> Kostenlose Versionen reichen für vieles. Für „Deep Research“ und große
> Kontexte sind die Bezahlversionen deutlich stärker – aber **kein Werkzeug
> ist Pflicht.** Du kommst mit der kostenlosen Stufe durch eine Arbeit.

---

## Welches Werkzeug für welche Phase?

| Aufgabe | Werkzeug | Worauf es ankommt |
|:--|:--|:--|
| Forschungsfrage schärfen | Claude / ChatGPT | Sparring, Gegenrede |
| Quellen finden | Perplexity (Deep Research) | mit Links |
| Quellenangaben prüfen | Perplexity + Originalquelle (juris, beck, EUR-Lex …) | nie ohne Original |
| Lange PDFs durcharbeiten | NotebookLM / Gemini | große Texte |
| Zitate aus PDFs extrahieren | Gemini / Claude | Seite + Wortlaut |
| Gliedern & strukturieren | Claude / ChatGPT | |
| Umformulieren & Stil | Claude | Anti-KI-Klang |
| Gegenlesen / Review | Claude / Gemini | kritisch prompten |

Diese Arbeitsteilung ist kein Dogma, aber sie nutzt die jeweilige Stärke. In
echten Arbeiten hat sich genau diese Kombination bewährt: **Perplexity für die
rechtliche/empirische Recherche, Gemini für technische Volltexte und die
systematische Zitatextraktion, Claude für Struktur und Sprache.**

---

## Wie man gut promptet (4 Bausteine)

Ein schwacher Prompt bekommt eine schwache Antwort. Ein guter Prompt hat vier
Teile:

1. **Rolle** – „Du bist juristische:r Researcher:in mit Schwerpunkt
   deutsches Steuerrecht.“
2. **Kontext** – Thema, Forschungsfrage, dein Kenntnisstand, was schon existiert.
3. **Aufgabe** – präzise, ggf. nummeriert; *eine* klar umrissene Sache.
4. **Ausgabeformat** – wie das Ergebnis aussehen soll (Tabelle, BibLaTeX,
   Markdown …). Je strenger, desto brauchbarer.

**Schwach:** „Gib mir Quellen zu KI im Mittelstand.“
**Stark:** „Rolle: … Kontext: … Aufgabe: Nenne 10 zitierfähige Quellen
(2021–2026) zu X. Pro Quelle 2 Sätze Relevanz. **Ausgabe: je ein fertiger
BibLaTeX-Eintrag** mit `langid` und `date`. **Erfinde keine Quellen** – bei
Unsicherheit `note = {Verifizierung empfohlen}`.“

Fertige, erprobte Prompts für die Recherche findest du in
[`vorlagen/recherche-prompts.md`](../vorlagen/recherche-prompts.md).

---

## Drei Profi-Kniffe

**1. Format erzwingen.** Wenn die KI dir BibLaTeX, eine Markdown-Tabelle oder
nur korrigierte Einträge ausgeben soll – schreib es explizit und gib ein
Muster vor. Das spart dir später stundenlanges Nachformatieren.

**2. Kritik statt Lob anfordern.** Modelle neigen zum Bestätigen. Gegenmittel:
*„Sei ein:e strenge:r Gutachter:in. Wenn etwas schwach ist, sag es und
begründe.“* So bekommst du echtes Feedback statt Schmeichelei.

**3. Iterativ statt alles auf einmal.** Eine Quelle nach der anderen, ein
Kapitel nach dem anderen. Große „mach mir die ganze Arbeit“-Prompts erzeugen
Mittelmaß und mehr Halluzinationen. Kleine, fokussierte Schritte sind
prüfbar.

---

## Wie viel darf die KI tun? Die drei Hilfe-Level

„KI ist Zuarbeiter, nicht Autor“ sagt, **wer** verantwortlich ist – aber noch
nicht, **wie viel** Zuarbeit du zulässt. Das legst du **vor** jedem KI-Einsatz
bewusst fest, mit einem von drei Hilfe-Leveln:

| Level | Die KI darf … | Typischer Einsatz |
|:--:|:--|:--|
| **1 · Coach** | nur Fragen stellen und auf Probleme zeigen – **keinen** Text vorformulieren | Eigenleistung maximal halten, Review-Runden |
| **2 · Formulierungshilfe** | einzelne Stellen markieren und 1–2 Alternativen vorschlagen | Standard beim Überarbeiten |
| **3 · Entwurfshilfe** | ganze Absätze entwerfen oder umformulieren | Entwurfsphase, Schreibblockade – voll kennzeichnungspflichtig |

Das Level sagst du der KI **explizit** an (sonst liefert sie immer die
Maximalhilfe: fertigen Text), indem du einen kurzen Baustein an deinen Prompt
anhängst. Die drei kopierfertigen Bausteine, wann welches Level passt und was
jeweils zu kennzeichnen ist:
[`vorlagen/ki-hilfe-level.md`](../vorlagen/ki-hilfe-level.md).

Der Nebeneffekt ist prüfungsrelevant: Die Level geben dir die **Sprache für
das KI-Verzeichnis**. „Claude, Hilfe-Level 2 (Formulierungsvorschläge,
punktuell übernommen), Kapitel 3–4“ ist eine ehrliche, präzise Angabe –
„sprachliche Unterstützung“ ist keine.

---

## Datenschutz & Redlichkeit – kurz, aber wichtig

- **Keine sensiblen Daten** (echte Klarnamen aus Interviews, vertrauliche
  Unternehmensdaten) in öffentliche KI-Dienste eingeben. Anonymisieren oder
  lokal verarbeiten.
- **Eingaben können zum Training verwendet werden** – je nach Anbieter und
  Einstellung. Im Zweifel die Trainings-Nutzung in den Einstellungen abschalten.
- **Dokumentationspflicht mitdenken:** Was du an KI übernimmst, musst du später
  kennzeichnen (siehe [02 §8](02_formalia.md) und
  [11](11_qualitaet-und-abgabe.md)). Führe **von Anfang an** ein Recherche- und
  KI-Log (`vorlagen/recherche-log_VORLAGE.md`) – am Ende ist es Gold wert.

---

## Woran du merkst, dass du fertig bist

- [ ] Du weißt, welches Werkzeug du für Recherche, Volltexte, Struktur und Stil
      nutzt (und hast ggf. Accounts angelegt).
- [ ] Du hast verstanden: **alles verifizieren, nichts blind übernehmen.**
- [ ] Du weißt, mit welchem **Hilfe-Level** du arbeitest – und sagst es der KI
      in jedem Prompt an.
- [ ] Du führst ein KI-/Recherche-Log.

---

**Nächster Schritt:** [04 · Quellenrecherche mit KI →](04_quellenrecherche.md)
