# STRYV docs

Handleidingen en changelogs van de WordPress-plugins van STRYV, gepubliceerd via GitHub Pages op https://stryv-nl.github.io/docs/.

| Plugin | Handleiding | Changelog |
| --- | --- | --- |
| Next-Gen Images | [next-gen-images/](https://stryv-nl.github.io/docs/next-gen-images/) | [changelog](https://stryv-nl.github.io/docs/next-gen-images/changelog/) |

## Changelog bijwerken

De changelog wordt gemaakt uit `CHANGELOG.md` in de pluginrepo:

```
python3 scripts/changelog.py
```

Commit daarna `next-gen-images/changelog/index.html`.

## Nieuwe plugin toevoegen

Maak een map `<plugin>/` met `index.html` (handleiding) en eventueel `changelog/index.html`, en voeg een kaart toe op `index.html`.
