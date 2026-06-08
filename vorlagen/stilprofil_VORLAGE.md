# Stilprofil (Vorlage)

> Dein persönliches Regelwerk für einen konsistenten, wissenschaftlichen –
> und **nicht** KI-klingenden – Text (Phase 6, siehe
> [`anleitung/07_schreiben-und-stil.md`](../anleitung/07_schreiben-und-stil.md)).
> Fülle es aus, **nachdem** du zwei Unterkapitel überarbeitet hast – dann weißt
> du, wie dein guter Stil aussieht, und schreibst die Regeln daraus ab. Gib das
> Profil der KI mit, wenn sie für dich umformuliert.

---

## 1. Tonalität

- Grundhaltung: sachlich-beschreibend, nicht essayistisch, nicht werbend.
- Wertende Adjektive nur, wenn der Beleg sie trägt. Pro Aussage höchstens eines.
- <!-- Deine Ergänzungen: -->

## 2. Satzbau & Wortwahl

- Aktiv leicht vor Passiv; konkrete Akteure benennen, wo möglich.
- Satz- und Absatzlängen bewusst **variieren** (gegen KI-Symmetrie).
- Präzise Verben statt Allerweltsverben (begründen statt liefern; verlangt
  statt will).
- <!-- Deine Ergänzungen: -->

## 3. Absatzlogik

- Dreischritt je Unterkapitel: **Begriff klären → entfalten → Folgerung & Überleitung**.
- Eine zentrale Aussage pro Unterkapitel.
- Übergang am Ende benennt die nächste Frage, ohne sie zu beantworten.

## 4. Umfang

- Wortzahl-Korridor pro Unterkapitel: **____–____ Wörter**.
- Bei größerer Abweichung: Grund notieren.

## 5. Belege

- Jeder Absatz mindestens eine Fußnote mit Seitenangabe.
- Direkt = `\enquote{}` ohne „Vgl.“; indirekt = mit „Vgl.“.

## 6. Verbotsliste (meine Anti-Patterns)

> Konkrete Wörter/Muster, die in **meinem** Text nichts zu suchen haben.

- Marketing-Sprech: „Lösung“, „innovativ“, „ganzheitlich“, „einzigartig“, …
- KI-Floskeln: „entscheidender Meilenstein“, „es ist wichtig anzumerken“,
  „unterstreicht eindrucksvoll“, „Nicht nur …, sondern auch …“, …
- Salopp/LinkedIn: „Schauen wir uns nun an …“, „In der echten Welt …“, …
- Ich-/Wir-Form, rhetorische Fragen an die Leserschaft.
- <!-- Deine Ergänzungen: -->

## 7. FOM-Sprachregeln (immer)

- [ ] Keine Ich-/Wir-/„man“-Form
- [ ] Präsens (Vergangenheit nur für Historisches)
- [ ] Gendergerechte Sprache (JKS-Pflicht)
- [ ] Keine Füllwörter („eigentlich“, „natürlich“, „sehr“ …)
- [ ] Fachbegriffe bei Erstnennung definieren

---

## Prüf-Routine vor jedem Kapitel-Commit

- [ ] Eingangssatz jedes Absatzes sachlich, ohne Wertung?
- [ ] Genau eine zentrale Aussage, Dreischritt erkennbar?
- [ ] Wortzahl im Korridor?
- [ ] Jede Behauptung belegt, jede Zitation mit Seite?
- [ ] Keine KI-Floskel aus der Verbotsliste?
- [ ] Übergang am Ende sachlich (keine rhetorische Frage)?
- [ ] Build fehlerfrei, `make check` grün?
