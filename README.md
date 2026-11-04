# STRYV docs

Handleidingen en changelogs van de WordPress-plugins van STRYV, gepubliceerd via GitHub Pages op https://stryv-nl.github.io/docs/.

| Plugin | Handleiding | Changelog |
| --- | --- | --- |
| Next-Gen Images | [next-gen-images/](https://stryv-nl.github.io/docs/next-gen-images/) | [changelog](https://stryv-nl.github.io/docs/next-gen-images/changelog/) |
| RankPilot Pro | [rankpilot-pro/](https://stryv-nl.github.io/docs/rankpilot-pro/) | [changelog](https://stryv-nl.github.io/docs/rankpilot-pro/changelog/) |

## Changelog bijwerken

De changelog wordt gemaakt uit `CHANGELOG.md` in de pluginrepo:

```
python3 scripts/changelog.py                # Next-Gen Images
python3 scripts/changelog.py rankpilot-pro  # RankPilot Pro
```

Commit daarna `<plugin>/changelog/index.html`.

## Stijl

De handleiding van RankPilot Pro gebruikt `assets/stryv-ds.css`, in het STRYV Plugin Design System (Calimate-koppen, inktzwarte kop, violet accent, limoenknoppen). Schermafdrukken staan in `<plugin>/img/` als WebP.

## Nieuwe plugin toevoegen

Maak een map `<plugin>/` met `index.html` (handleiding) en eventueel `changelog/index.html`, en voeg een kaart toe op `index.html`.
