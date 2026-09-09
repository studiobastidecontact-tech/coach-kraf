---
version: V3
kind: charte
status: appliquée
supersedes: 2026-09-09-charte-toulouse-mesuree.md
---

# La brique est trop sombre de six points

William, en regardant le site : « les couleurs marron sont trop marron et pas
assez brique ». La mesure lui donne raison sur deux écarts distincts.

|  | teinte | saturation | clarté |
|---|---|---|---|
| `--t-brique` actuel `#9C5228` | **22°** | 59 % | **38 %** |
| brique foraine sèche `#B7603C` | 18° | 51 % | 48 % |
| brique au soleil `#C9714A` | 18° | 54 % | 54 % |
| brique lavée par la pluie `#A85436` | 16° | 51 % | 44 % |

**La clarté est la cause dominante.** Un rouge-orangé sous 44 % se lit brun,
quelle que soit sa teinte. Les 22° ajoutent une dérive de 5° vers le jaune :
jaune-ward c'est du marron, rouge-ward c'est de la brique.

**D'où vient l'erreur.** L'extraction prenait la médiane du tiers le plus
saturé, sur une bande de clarté 0,30–0,70. Une photo de mur contient autant de
brique à l'ombre que de brique au soleil : la médiane rend le mur *en lumière
moyenne*, pas la couleur de la brique. La borne basse à 0,30 laissait la moitié
ombrée peser sur la médiane.

## Le plafond, et pourquoi il existe

`--accent` porte 46 déclarations, dont une majorité de **petit texte** : liens
de 15 px, numéros de 13 px, intitulés de section de 14 px. Ils exigent 4,5:1
sur le fond le plus clair de la charte (`--t-pierre-pale #F2ECE4`).

Balayage de toutes les briques de 16° à 20°, saturation 50 à 60 % :

```
teinte  satur.  clarté max qui tienne 4,5:1     pire contraste
  16°     55%        43%   #AA5231                 4,52:1
  17°     55%        42%   #A65230                 4,62:1
  18°     55%        42%   #A65430                 4,55:1
```

**Le plafond d'un jeton unique est 42-43 % de clarté.** La brique réelle
commence à 44 et vit à 48. Un seul jeton ne peut donc pas atteindre la brique :
il n'y a pas de réglage à trouver, il y a une contrainte à lever.

## Option 1 — un jeton, la teinte corrigée

```
  --t-brique   #9C5228  →  #A9502F        22° → 16°   ·   L 38 % → 42 %

  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │   avant  ████████████  #9C5228   22°  59%  38%   « marron »  │
  │                                                              │
  │   après  ████████████  #A9502F   16°  56%  42%   « brique    │
  │                                                   sombre »   │
  │                                                              │
  │   contraste sur pierre : 4,90:1  →  4,62:1   (seuil 4,5)     │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘

  Zéro remaniement : les 46 usages suivent le jeton.
  Mais on reste à 42 %, soit six points sous la brique sèche.
```

## Option 2 — deux jetons, la brique là où l'œil la voit

Ce qui fait qu'un site « se lit brique », ce sont les **grandes formes
colorées** : le nombre de 46 px, le prix de 30 px, le mot accentué du hero, les
barres de 3 px, les icônes de 26 px. Pas les liens de 15 px. Or ces formes-là
n'ont besoin que de **3:1** (WCAG 1.4.11 pour le non-textuel, 1.4.3 pour le
grand texte) — la contrainte de 4,5 ne les concerne pas.

```
  --t-brique         #A9502F   16° 56% 42%   →  le petit texte
                                                 liens, numéros, intitulés
                                                 4,62:1 sur pierre  ✓ 4,5

  --t-brique-franche #B85C38   17° 53% 47%   →  tout le reste
                                                 hero, prix, nombres, barres,
                                                 filets, bordures, icônes
                                                 3,87:1 sur pierre  ✓ 3,0

  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │   ██████████████████████████████  #B85C38  franche  L 47 %   │
  │   ████████████                    #A9502F  texte    L 42 %   │
  │   ████████████                    #9C5228  actuelle L 38 %   │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘

  ~14 déclarations changent de jeton. La direction gagne un hexadécimal,
  les contextes un rôle. C'est exactement ce que l'architecture prévoit.
```

## Et la brique claire, sur fond sombre

`--t-brique-claire #D9A06B` est à **29°** — le jeton le plus jaune de la
charte. C'est lui qui peint le hero et le pied, les deux plus grandes surfaces
sombres du site : il tire l'ensemble vers le sable.

```
  actuelle  ████████████  #D9A06B   29° 59% 64%   7,65:1   « sable »
  proposée  ████████████  #E08A5A   21° 68% 62%   6,62:1   « brique
                                                             éclairée »
```

Contraste sur `--t-profond` : 6,62:1, très au-dessus des 4,5 requis.

## Recommandation

**Option 2, plus la brique claire.** Un seul jeton bute sur un plafond
arithmétique à 42 % ; le découpage lève la contrainte au bon endroit, sans rien
sacrifier de la lisibilité. Et corriger `--t-brique-claire` compte autant que
l'accent : les deux plus grandes surfaces du site sont sombres, et c'est ce
jeton-là qui les colore.

Le cas où l'option 1 gagne : si tu veux voir le changement de teinte seul,
avant d'engager le découpage. Un jeton, une ligne, et on regarde.
