# 07 · Schreiben & Stil

> Jetzt entsteht der Text. Zwei Dinge entscheiden über die Qualität:
> ein **konsistenter wissenschaftlicher Stil** – und dass der Text **nicht wie
> von einer KI generiert** klingt, obwohl du KI nutzt. Beides lernst du hier.

---

## Erst Rohbau, dann Ausbau

Schreibe jedes Kapitel in **zwei Durchgängen**:

1. **Rohentwurf:** Struktur + Argumente + Belege. Hässlich ist erlaubt. Ziel ist,
   dass die *Substanz* steht.
2. **Überarbeitung:** Stil, Präzision, Übergänge, Wortwahl. Erst hier wird es
   schön.

Beginne mit **Grundlagen/Hauptteil**, nicht mit der Einleitung – die schreibst
du am Ende um, wenn du weißt, was wirklich drinsteht. Nach jedem fertigen
Kapitel: committen (siehe [10](10_versionierung.md)).

> **Faustregel: Jeder Absatz braucht mindestens eine Fußnote** mit
> Quellennachweis.
>
> **Woher das kommt:** Das ist *keine* Vorschrift aus den FOM-Leitfäden,
> sondern eine Praxisregel. Vorgeschrieben ist die **Belegpflicht**: Jeder
> fremde Gedanke muss nachgewiesen werden, egal wo er im Text steht (die
> genaue Fundstelle in deinem Leitfaden liefert dir der
> [Leitfaden-Extraktions-Prompt](../vorlagen/leitfaden-extraktion-prompt.md)).
> Die Absatz-Regel übersetzt diese Pflicht in etwas, das du beim Schreiben und
> Gegenlesen prüfen kannst: Der Absatz ist die kleinste Einheit deiner
> Argumentation (ein Gedanke pro Absatz, siehe Absatzlogik unten). Ein Absatz
> ohne Fußnote wirft beim Lesen sofort die Frage auf: *belegtes Wissen oder
> eigene Behauptung?* Kann der Absatz das nicht beantworten, wird er als
> unbelegte Behauptung gelesen – und genau so vermerken es Gutachten.
>
> **Wann die Regel nicht greift:** Absätze, die erkennbar deine Eigenleistung
> sind – eigene Analyse, Auswertung eigener Daten, Folgerungen aus bereits
> belegten Aussagen, Überleitungen. Solche Absätze sind gewollt, sie müssen
> nur sprachlich als Eigenleistung erkennbar sein („Daraus folgt …“, „Die
> Auswertung zeigt …“). Zahlen, Definitionen und Pauschalaussagen bleiben
> immer belegpflichtig.

---

## Dein Stilprofil: einmal Regeln festlegen, dann durchhalten

Der größte Hebel für einen einheitlichen Text ist ein **eigenes Stilprofil** –
ein kurzes Dokument, in dem du *deine* verbindlichen Stilregeln festhältst. Das
hat zwei Vorteile: Du schreibst konsistenter, und du kannst das Profil **der KI
mitgeben**, damit ihre Vorschläge zu deinem Ton passen.

Lege es nach [`vorlagen/stilprofil_VORLAGE.md`](../vorlagen/stilprofil_VORLAGE.md)
an. Typische Inhalte:

- **Tonalität:** sachlich-beschreibend, nicht essayistisch, nicht werbend.
- **Satzbau:** Aktiv leicht vor Passiv; konkrete Akteure benennen; variierende
  Satzlängen.
- **Wortwahl:** präzise Verben; wertende Adjektive nur, wenn der Beleg sie trägt.
- **Absatzlogik:** Dreischritt (Begriff – Entfaltung – Folgerung).
- **Wortzahl-Korridor** pro Unterkapitel (z. B. 400–700 Wörter).
- **Verbotsliste** (deine persönlichen Anti-Patterns, siehe unten).

> Das Stilprofil destillierst du am besten **aus eigenen Texten, die du gut
> findest**. Dafür musst du nicht bei null anfangen:
>
> - **Alte Arbeiten:** frühere Haus- oder Seminararbeiten, besonders die
>   Absätze, die im Gutachten gelobt wurden oder dir beim Wiederlesen selbst
>   gefallen.
> - **Andere eigene Unterlagen:** Exposés, Projektberichte, Berichte aus dem
>   Job – alles, was in deiner Stimme geschrieben ist und sachlich klingt.
> - **Neue Absätze:** Hast du noch nichts davon, schreib zwei Unterkapitel der
>   aktuellen Arbeit und überarbeite sie, bis sie sitzen.
>
> Aus diesem Material liest du die Regeln ab (Satzlänge, typische Verben,
> Absatzaufbau) und wendest sie auf den Rest an. Fremde Texte taugen dabei als
> Vergleichsmaßstab, nicht als Vorlage: Das Profil soll *deinen* Stil
> beschreiben, sonst klingt die Arbeit nach jemand anderem – ähnlich wie bei
> ungeprüftem KI-Text.

---

## Die FOM-Sprachregeln (verbindlich)

| Regel | Bedeutung |
|:--|:--|
| **Keine Ich-/Wir-Form** | dritte Person, unpersönlich. Auch „man“ vermeiden (ifes). |
| **Präsens** | Gegenwart bevorzugt; Vergangenheit nur für Historisches. |
| **Gendergerecht** | JKS verlangt geschlechtersensible Sprache („die Studierenden“, Doppelnennung, Partizip). |
| **Keine Füllwörter** | „eigentlich“, „natürlich“, „vielleicht“, „sehr“ raus. |
| **Fachbegriffe definieren** | bei Erstnennung erklären, dann konsistent nutzen. |
| **Keine rhetorischen Fragen** an die Leserschaft. |

---

## Damit der Text nicht „nach KI“ klingt

KI-Texte haben verräterische Muster. Wenn du KI zum Umformulieren nutzt, musst
du diese Muster aktiv **heraus**redigieren. Orientierung bieten die bekannten
„Signs of AI writing“ (Wikipedia) – die wichtigsten:

- **Bot-Begeisterung & Schwungvokabular:** „entscheidender Meilenstein“,
  „spielt eine zentrale Rolle“, „es ist wichtig zu bemerken“, „maßgeblich“,
  „nahtlos“, „robust“ (und die englischen Durchrutscher *delve, pivotal,
  leverage, tapestry*) → streichen oder durch das schlichte Fachwort ersetzen.
- **Vage Autoritäten:** „Experten argumentieren …“, „Studien zeigen …“ ohne
  Fundstelle → belegen oder streichen (hier sitzen oft **halluzinierte
  Quellen**).
- **Künstliche Symmetrie:** lauter gleich lange Absätze, Dauer-Dreierlisten, das
  „Nicht nur …, sondern auch …“-Muster, inhaltsleere Partizip-Anhängsel
  („…, wodurch … gewährleistet wird“) → Satz- und Absatzlängen **natürlich
  variieren**, Anhängsel streichen.
- **LinkedIn-/Plauder-Sprache:** „Schauen wir uns nun an …“, „Sicherlich!“,
  „Ich hoffe, das hilft“ → raus.
- **Copy-Paste-Artefakte:** Markdown-Reste (`**fett**`, `#`, `---`), Emoji,
  übermäßige Halbgeviertstriche und technische Spuren wie `oaicite`/`turn0…` →
  vollständig entfernen.
- **Moralisierende Schluss-Sätze**, die universelle Wahrheiten verkünden →
  sachlich bleiben.

> 📋 **Vollständige, abhakbare Liste:**
> [`vorlagen/ki-stilmerkmale.md`](../vorlagen/ki-stilmerkmale.md) – führe deinen
> Text einmal pro Kapitel dagegen (Strg+F gegen die markierten Wörter).

> **Die Falle des „Humanizers“:** Wer KI-Text einfach durch ein „mach das
> menschlicher“-Tool jagt, bekommt oft *kumpelhaft-flapsig* statt *akademisch*.
> Besser: gezielt prompten – *„Ersetze KI-typische Floskeln durch sachliche,
> präzise, studentisch-authentische Formulierungen. Behalte alle
> `\autocite`-Befehle exakt bei.“* – und danach **selbst** drüberlesen.

Der zugehörige Review-Prompt (kapitelweise, kopierfertig) liegt in
[`vorlagen/recherche-prompts.md`](../vorlagen/recherche-prompts.md), Abschnitt
„Stil-Review“. Dort findest du auch die weiterführenden Review-Prompts für den
Feinschliff: den **Lektor-Check** (Sprache, Struktur, Belege – mit
Prioritätsampel) und den **Argumentations-Check**, der gezielt nach
Zirkelschlüssen, falscher Kausalität, unzulässigen Verallgemeinerungen und
Strohmann-Argumenten sucht – und nach der Frage, wo dein Text **eigene
Analyse** liefert und wo er Quellen nur wiedergibt. Häng an jeden dieser
Prompts dein [Hilfe-Level](../vorlagen/ki-hilfe-level.md) an.

---

## So nutzt du KI beim Schreiben – richtig

**Gut:**
- *Formulierungsalternativen:* „Gib 3 sachliche Varianten dieses Absatzes,
  Niveau [Studiengang/Semester], **keine neuen Inhalte, keine neuen Quellen**,
  alle Zitierbefehle beibehalten.“
- *Kürzen/Glätten:* „Straffe diesen Absatz auf ~120 Wörter ohne Inhaltsverlust.“
- *Verständlichkeit:* „Wo ist dieser Absatz unklar oder verschachtelt?“
- *Gegenlesen:* „Prüfe diesen Abschnitt auf KI-typische Floskeln und
  unbelegte Behauptungen.“

**Tabu:**
- KI **Inhalte erfinden** lassen und ungeprüft übernehmen.
- KI **neue Quellen** in einen Absatz setzen lassen (sie halluziniert).
- Ganze Kapitel generieren lassen – das merkt man, es ist belegfrei und es ist
  nicht deine Leistung.

> **Kennzeichnungspflicht mitdenken:** Wo du KI-formulierte Inhalte übernimmst,
> kennzeichnest du das (Text + KI-Verzeichnis, siehe [02 §8](02_formalia.md)).
> Reine sprachliche Glättung deiner eigenen Sätze ist i. d. R. nicht
> nachweispflichtig – im Zweifel deinen Leitfaden lesen und ehrlich
> dokumentieren.

---

## Die häufigsten Anti-Patterns (Verbotsliste)

- Marketing-Sprech: „Lösung“, „innovativ“, „ganzheitlich“, „einzigartig“.
- Unbelegte Pauschalaussagen / Statistiken ohne Quelle.
- Wertungs-Häufung: „wichtig, zentral, entscheidend“ in einem Satz.
- Wir-/Ich-Form, „unseres Erachtens“.
- Rhetorische Fragen an die Leser:innen, auch in Übergängen.
- Wörtliche Zitate, die nur zugekleistert statt eingeordnet werden.

---

## Woran du merkst, dass du fertig bist

- [ ] Alle Kapitel sind geschrieben, jede fremde Aussage ist belegt; Absätze
      ohne Fußnote sind erkennbar Eigenleistung.
- [ ] Dein Stilprofil ist angelegt und durchgehalten.
- [ ] Der Text ist von KI-typischen Mustern bereinigt und klingt nach **dir**.
- [ ] FOM-Sprachregeln (keine Ich-Form, Präsens, gendergerecht) sind eingehalten.

---

**Nächster Schritt:** [08 · Richtig zitieren →](08_zitieren.md)
