#!/usr/bin/env python3
"""Maakt next-gen-images/changelog/index.html uit CHANGELOG.md van de pluginrepo.

Gebruik: python3 scripts/changelog.py [pad/naar/CHANGELOG.md]
Standaard wordt de laatste versie van GitHub (main) opgehaald.
"""
import html, re, sys, urllib.request, pathlib

URL = 'https://raw.githubusercontent.com/stryv-nl/wp-next-gen-images/main/CHANGELOG.md'
root = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8') if len(sys.argv) > 1 else urllib.request.urlopen(URL).read().decode('utf-8')

def inline(t):
    t = html.escape(t, quote=False)
    return re.sub(r'`([^`]+)`', r'<code>\1</code>', t)

releases, cur = [], None
for line in src.splitlines():
    m = re.match(r'^## \[([^\]]+)\] - (\d{4}-\d{2}-\d{2})', line)
    if m:
        cur = {'v': m.group(1), 'd': m.group(2), 'items': []}
        releases.append(cur)
    elif cur and line.startswith('- '):
        cur['items'].append(line[2:].strip())
    elif cur and line.strip() and cur['items']:
        cur['items'][-1] += ' ' + line.strip()

months = ['januari','februari','maart','april','mei','juni','juli','augustus','september','oktober','november','december']
def nl(d):
    y, m, dd = d.split('-'); return f'{int(dd)} {months[int(m)-1]} {y}'

body = ''
for i, r in enumerate(releases):
    lis = ''.join(f'<li>{inline(x)}</li>' for x in r['items'])
    tag = ' <span class="tag">Nieuwste</span>' if i == 0 else ''
    body += (f'<section id="v{r["v"]}"><h2>Versie {r["v"]}{tag}</h2>'
             f'<p class="date">{nl(r["d"])} · <a href="https://github.com/stryv-nl/wp-next-gen-images/releases/tag/v{r["v"]}">Download</a></p><ul>{lis}</ul></section>\n')

tpl = (root / 'scripts' / 'changelog.tpl.html').read_text(encoding='utf-8')
out = root / 'next-gen-images' / 'changelog' / 'index.html'
out.write_text(tpl.replace('{{RELEASES}}', body), encoding='utf-8')
print(f'{len(releases)} versies geschreven naar {out}')
