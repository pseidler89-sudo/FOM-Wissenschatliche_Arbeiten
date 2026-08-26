#!/usr/bin/env python3
"""Zaehlt den Umfang des Textteils -- Woerter, nicht Zeichen.

Warum Woerter: Der FOM-Leitfaden Jaeger/Kuempel/Seng gibt den Umfang in
Woertern bzw. Seiten des Textteils an, nicht in Zeichen. Gezaehlt wird nur
kapitel/ -- also ohne Deckblatt, Verzeichnisse, Anhang und Literatur, genau
wie der Leitfaden es meint. Fussnoten werden getrennt ausgewiesen, weil
Pruefende unterschiedlich damit umgehen.

Aufruf:  python3 skripte/umfang.py [--soll 4000]
"""
import re, sys, glob, os

def entferne_kommentare(t):
    # % am Zeilenanfang oder nach Nicht-Backslash leitet einen Kommentar ein
    return re.sub(r'(?<!\\)%.*', '', t)

def hole_fussnoten(t):
    """Zieht \\footnote{...} heraus -- klammerbewusst, nicht per Regex."""
    fn, rest, i = [], [], 0
    while i < len(t):
        m = re.compile(r'\\footnote\s*\{').search(t, i)
        if not m:
            rest.append(t[i:]); break
        rest.append(t[i:m.start()])
        j, tiefe = m.end(), 1
        while j < len(t) and tiefe:
            if t[j] == '\\': j += 2; continue
            if t[j] == '{': tiefe += 1
            elif t[j] == '}': tiefe -= 1
            j += 1
        fn.append(t[m.end():j-1]); i = j
    return ''.join(rest), '\n'.join(fn)

ENVS = ('figure', 'table', 'lstlisting', 'tabular', 'tikzpicture', 'verbatim')

def entferne_umgebungen(t):
    """Loescht Gleitumgebungen komplett -- samt Inhalt.

    Bildunterschriften und Tabelleninhalte gehoeren nicht zum Textteil; sie
    mitzuzaehlen wuerde den Umfang kuenstlich aufblaehen.
    """
    for env in ENVS:
        t = re.sub(r'\\begin\{' + env + r'\*?\}.*?\\end\{' + env + r'\*?\}',
                   ' ', t, flags=re.S)
    return t

def zaehle(t):
    t = entferne_umgebungen(t)
    t = re.sub(r'\\caption\s*(\[[^\]]*\])?\s*\{[^{}]*\}', ' ', t)
    t = re.sub(r'\\(label|ref|cite\w*|autocite\w*|footcite\w*|input|include|acs?|acl?)\s*(\[[^\]]*\])*\s*\{[^}]*\}', ' ', t)
    t = re.sub(r'\\[a-zA-Z@]+\s*(\[[^\]]*\])?', ' ', t)   # restliche Befehle
    t = re.sub(r'[{}$&~^_\\]', ' ', t)
    return len([w for w in re.split(r'\s+', t) if re.search(r'[A-Za-zÄÖÜäöüß0-9]', w)])

def main():
    soll = None
    if '--soll' in sys.argv:
        soll = int(sys.argv[sys.argv.index('--soll') + 1])
    dateien = sorted(glob.glob('kapitel/*.tex'))
    # Nicht zum Textteil: Titelseite und Erklaerung sind Vorspann/Nachspann.
    ignorieren = {'titelseite.tex', 'erklaerung.tex', 'sperrvermerk.tex'}
    dateien = [d for d in dateien if os.path.basename(d) not in ignorieren]
    if not dateien:
        print('  keine Kapitel unter kapitel/ gefunden'); return 0

    gesamt = fussnoten = 0
    for d in dateien:
        roh = entferne_kommentare(open(d, encoding='utf-8').read())
        text, fn = hole_fussnoten(roh)
        w, wf = zaehle(text), zaehle(fn)
        gesamt += w; fussnoten += wf
        print(f'    {os.path.basename(d):<34} {w:>6} Wörter  (+{wf} in Fußnoten)')

    print(f'    {"Textteil gesamt":<34} {gesamt:>6} Wörter  (+{fussnoten} in Fußnoten)')
    print(f'    {"Richtwert Seiten (ca. 250 W/S)":<34} {gesamt/250:>6.1f}')
    if soll:
        q = gesamt / soll * 100
        lage = 'OK' if 90 <= q <= 105 else ('zu kurz' if q < 90 else 'zu lang')
        print(f'    Vorgabe {soll} Wörter -> {q:.0f} % ({lage})')
        if lage != 'OK':
            return 1
    else:
        print('    Hinweis: Umfangsvorgabe in FORMALIA.md eintragen und mit --soll prüfen.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
