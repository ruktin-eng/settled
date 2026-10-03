import re, pathlib

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent / 'index.html'

PAL = {
    'K': 'var(--text)', 'B': '#0a84ff', 'D': '#0057c2', 'W': '#ffffff',
    'G': '#9aa4b2', 'L': '#d6dce6', 'Y': '#ffd400', 'R': '#ff3b30',
}

SPRITES = {
'pill': """
...KKKKKKKKKK...
..KBBBBBWWWWWK..
.KBWWBBBWWWWLLK.
.KBWBBBBWWWWWLK.
.KBBBBBBWWWWWLK.
.KDBBBBBLWWWWLK.
..KDDDDDLLLLLK..
...KKKKKKKKKK...
""",
'sparkle': """
....K....
...KYK...
...KYK...
.KKKWKKK.
KYYWWWYYK
.KKKWKKK.
...KYK...
...KYK...
....K....
""",
'mic': """
....KKKK....
...KGLWGK...
...KGGGGK...
...KLGLGK...
...KGGGGK...
...KGLGLK...
.K.KGGGGK.K.
.K..KKKK..K.
.KK......KK.
..KK....KK..
....KKKK....
.....KK.....
.....KK.....
...KKKKKK...
""",
'floppy': """
KKKKKKKKKKKKK.
KBBKLLLLLKBBBK
KBBKLLLKLKBBBK
KBBKLLLKLKBBBK
KBBKKKKKKKBBBK
KBBBBBBBBBBBBK
KBBBBBBBBBBBBK
KBWWWWWWWWWWBK
KBWKKKKKKKKWBK
KBWWWWWWWWWWBK
KBWKKKKKKWWWBK
KBWWWWWWWWWWBK
KDWWWWWWWWWWDK
KKKKKKKKKKKKKK
""",
'phone': """
.KKKKKKKK.
KGGGGGGGGK
KGKKKKKKGK
KGKBBBBKGK
KGKBWWBKGK
KGKBBBBKGK
KGKBWBBKGK
KGKBBBBKGK
KGKBBWBKGK
KGKBBBBKGK
KGKKKKKKGK
KGGGGGGGGK
KGGGKKGGGK
KGGGGGGGGK
.KKKKKKKK.
""",
'scales': """
.......K.......
......KBK......
KKKKKKKKKKKKKKK
.K.....K.....K.
.K.....K.....K.
K.K....K....K.K
K.K....K....K.K
BBB....K....BBB
.B.....K.....B.
.......K.......
......KKK......
....KKKKKKK....
""",
'mail': """
KKKKKKKKKKKKKKKK
KBKWWWWWWWWWWKBK
KWBKWWWWWWWWKBWK
KWWBKWWWWWWKBWWK
KWWWBKWWWWKBWWWK
KWWWWBKKKKBWWWWK
KWWWWWBBBBWWWWWK
KWWWWWWWWWWWWWWK
KWWWWWWWWWWWWWWK
KKKKKKKKKKKKKKKK
""",
}

def svg(name, scale):
    rows = SPRITES[name].strip('\n').split('\n')
    h, w = len(rows), max(len(r) for r in rows)
    rects = []
    for y, row in enumerate(rows):
        x = 0
        while x < len(row):
            c = row[x]
            if c == '.':
                x += 1; continue
            run = 1
            while x + run < len(row) and row[x + run] == c:
                run += 1
            rects.append(f'<rect x="{x}" y="{y}" width="{run}" height="1" style="fill:{PAL[c]}"/>')
            x += run
    size = scale * 2
    return (f'<svg class="sprite" width="{w*size}" height="{h*size}" viewBox="0 0 {w} {h}" '
            f'aria-hidden="true" focusable="false">{"".join(rects)}</svg>')

html = (HERE / 'template.html').read_text()
html = re.sub(r'\{\{(\w+):(\d)\}\}', lambda m: svg(m[1], int(m[2])), html)
assert '{{' not in html
OUT.write_text(html)
print('wrote', OUT, len(html))
