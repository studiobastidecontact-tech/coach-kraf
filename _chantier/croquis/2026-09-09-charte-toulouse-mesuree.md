---
version: v3
kind: charte
status: proposée
supersedes: 2026-09-09-trois-directions-couleur.md (Terre de Toulouse)
date: 2026-09-09
---

# La charte mesurée sur 187 photographies de Toulouse

> Écrit après deux remarques de William : *« le résultat c'est maronnasse, c'est
> pas les vraies couleurs de Toulouse — Toulouse c'est pas juste brique, c'est
> des notes de bleu et de vert »* et *« on peut laisser du blanc aussi sur le
> site, pas faire que du full coloré »*.
>
> Les deux sont fondées, et la mesure ci-dessous dit **pourquoi** la première
> l'est — la faute est précise, pas une affaire de goût.

## La mesure

187 photographies de Toulouse, lues pixel par pixel dans le navigateur : place
du Capitole, Pont-Neuf et la Garonne, façades de brique, quais, toits, la
basilique Saint-Sernin, le canal du Midi, la Prairie des Filtres. **430 848
pixels classés par famille de teinte. Zéro échec de lecture.**

Deux précautions, parce que sans elles la mesure aurait menti :

- **53 fichiers écartés** parce qu'ils n'étaient pas des photographies. La
  recherche de Commons ramène des livres du XIXᵉ numérisés — un roman de Féval,
  une revue d'horticulture — dont la vignette est un `.jpg` comme les autres.
  Deux échantillons entiers n'étaient *que* des scans de livres ; sans le filtre
  sur le type réel du fichier, j'aurais fait entrer des couvertures rouges dans
  « les couleurs de Toulouse ».
- **Aucune moyenne de famille.** Une moyenne produit de la boue par
  construction : elle mélange le mur au soleil et le mur à l'ombre. Chaque
  valeur ci-dessous est la médiane de pixels **réels**, dans une bande de
  luminosité donnée.

### Ce que rendent les 430 848 pixels

| famille | part | l'échelle mesurée, de l'ombre au plein soleil |
|---|---|---|
| **pierre / pavé / ciel voilé** | **34,0 %** | `#414137` · `#6D615D` · `#84796F` · `#ABB3B8` |
| **brique** | **23,7 %** | `#352612` · `#734A2C` · `#7C5833` · `#BB8E5D` · `#CA986F` · `#DDC4AC` |
| **bleu** | **12,7 %** | `#19334E` · `#19509B` · `#449ACA` · `#6DB7E3` · `#90C5F2` |
| blanc | 8,7 % | `#FCFCFC` |
| noir | 8,5 % | `#23251F` — un noir chaud, jamais un noir pur |
| or / ocre | 6,6 % | `#48421F` · `#85843E` · `#B0A076` · `#DDD1AF` |
| **vert** | **4,8 %** | `#233313` · `#5D722E` · `#6C7835` · `#77A149` |
| rouge | 0,7 % | — |
| violet | 0,2 % | — |

## Trois faits, et le premier est ma faute

**1. La brique de Toulouse n'est pas marron. J'ai pris sa valeur à l'ombre.**

En plein jour elle mesure `#BB8E5D` et `#CA986F` : un rose sableux, chaud et
**clair**. Mon fond actuel, `#2A1A14`, tombe dans la bande la plus sombre de
l'échelle — `#352612`, la brique dans l'ombre d'une ruelle. J'ai construit tout
le site avec la couleur du mur à l'ombre, puis j'ai posé par-dessus deux
dérivés encore plus bruns (`#3B2820`, `#4C3529`). Le « maronnasse » n'est pas
une impression : c'est le nom exact de ce que j'ai fait.

**2. Le bleu n'est pas une note, c'est l'élément le plus vif du cadre.**

12,7 % des pixels, et les saturations les plus hautes de toute la mesure : 0,79
pour `#90C5F2`, 0,68 pour `#6DB7E3`. Sur la seule place du Capitole, le bleu
occupe 23,1 % de l'image. Ce n'est pas le bleu marine que j'avais essayé en
premier — c'est un bleu de ciel, clair et franc.

Et il n'est pas seulement dans le ciel : la richesse de Toulouse à la
Renaissance vient du **pastel des teinturiers**, une plante à teinture
**bleue**, dite « herbe du Lauragais ». Le pays de cocagne, c'est le triangle
Toulouse–Albi–Carcassonne — Albi est dans le Tarn, comme Saint-Sulpice. La
brique et le bleu ne sont pas deux idées qu'on rapproche : c'est le même
patrimoine.

**3. Toulouse est neutre à 42,7 %.**

Pierre 34,0 % + blanc 8,7 %. Le pavé, la pierre de taille, le crépi, le ciel
couvert. **La ville est majoritairement neutre**, et la brique y est l'accent
chaud, pas le fond. C'est la justification mesurée de la seconde remarque : le
blanc n'est pas un compromis, c'est ce que la ville est vraiment.

---

## La palette

Le renversement tient en une phrase : **le blanc devient le fond, la brique
devient l'accent, le bleu devient le signal, et le sombre ne sert plus que deux
fois dans la page.**

```
FONDS ─ ce qui occupe la surface

  #FDFCFA  ████████████████  blanc chaud     le fond par défaut de tout le site
  #F2ECE4  ████████████████  pierre pâle     une section sur deux, pour respirer
  #F7EDE3  ████████████████  brique pâle     les cartes, les encadrés
  #1C1917  ████████████████  profond         le héros et le pied. RIEN d'autre.

TEXTES

  #221E1A  ████  encre           16,14:1 sur blanc          AAA
  #6E6259  ████  pierre          5,76:1 sur blanc           AA    (secondaire)
  #FDFCFA  ████  blanc           17,06:1 sur profond        AAA
  #A79A8E  ████  estompé         6,38:1 sur profond         AA

ACCENTS ─ mesurés sur les photos, ajustés au contraste

  #9C5228  ████  brique          5,61:1 sur blanc           AA    boutons, liens
  #D9A06B  ████  brique claire   7,65:1 sur profond         AAA   sur le héros
  #1F5C8A  ████  pastel          6,93:1 sur blanc           AA    la note bleue
  #6DB7E3  ████  ciel            7,94:1 sur profond         AAA   sur le héros
  #4F6B2A  ████  olive           5,90:1 sur blanc           AA    la note verte
```

### La règle des rôles

| couleur | ce qu'elle porte | ce qu'elle ne porte jamais |
|---|---|---|
| **blanc chaud** | le fond de presque toute la page | — |
| **profond** | le héros, le pied de page | une section de contenu |
| **brique** | l'action principale, les chiffres, les liens | un fond plein |
| **pastel** | les liens de texte, les filets d'appui, les repères de lieu | un bouton d'action |
| **olive** | les marques de validation, les listes de points acquis | un titre |

Le pastel et l'olive sont des **notes** : ils apparaissent par touches — un
filet, un lien, une puce — jamais en aplat. C'est ce qui les empêche de
devenir une seconde couleur de marque et de brouiller la lecture.

---

## La page

Aujourd'hui, six sections sur huit sont en aplat sombre. Voici le renversement.

```
┌──────────────────────────────────────────────────────────────────┐
│ #FDFCFA  en-tête blanc, filet #E4DCD2 en bas                     │
│  DAVID — Krav Maga         Femmes  Enfants  Tarifs   [ Écrire ]  │
│                                        ↑ liens encre  ↑ brique   │
├──────────────────────────────────────────────────────────────────┤
│ ▓▓▓▓▓▓▓▓ #1C1917 — LE SEUL grand aplat sombre de la page ▓▓▓▓▓▓▓ │
│                                                                  │
│   ── TOULOUSE · SAINT-SULPICE-LA-POINTE        ciel #6DB7E3      │
│                                                                  │
│   Vous n'avez pas                              blanc #FDFCFA     │
│   à subir.                                     brique cl #D9A06B │
│                                                                  │
│   Coach particulier de Krav Maga…              estompé #A79A8E   │
│                                                                  │
│   ┌────────────────────┐  ┌────────────────────┐                 │
│   │▓ 07 81 68 60 84 ▓▓▓│  │  Envoyer un SMS    │                 │
│   │ fond #D9A06B       │  │  contour blanc     │                 │
│   │ texte #221E1A      │  │                    │                 │
│   └────────────────────┘  └────────────────────┘                 │
│                                                                  │
│   ● Premier cours offert. Un SMS suffit.       ciel #6DB7E3      │
├──────────────────────────────────────────────────────────────────┤
│ #FDFCFA  ← blanc. On respire, et ça dure jusqu'au pied de page.  │
│                                                                  │
│   Vous êtes probablement ici           titre encre #221E1A       │
│   ┌──────────────┐ ┌──────────────┐ ┌──────────────┐             │
│   │ #F7EDE3      │ │ #F7EDE3      │ │ #F7EDE3      │  cartes     │
│   │ filet brique │ │              │ │              │  pâles      │
│   └──────────────┘ └──────────────┘ └──────────────┘             │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│ ░░░ #F2ECE4 — pierre pâle. Une section sur deux, pour marquer    │
│     le passage sans jamais éteindre la page.                     │
│                                                                  │
│   Comment ça se passe             01 ─ 02 ─ 03  chiffres brique  │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│ #FDFCFA  blanc                                                   │
│   Tarifs        ┌──────────────┐                                 │
│                 │ ✓ olive      │  les points acquis en #4F6B2A   │
│                 │ 45 € brique  │                                 │
│                 └──────────────┘                                 │
├──────────────────────────────────────────────────────────────────┤
│ ▓▓▓ #1C1917 — le pied. Le second et dernier aplat sombre.        │
└──────────────────────────────────────────────────────────────────┘
```

**Deux aplats sombres, contre six aujourd'hui.** Le sombre redevient une
ponctuation : il ouvre et il ferme. Entre les deux, la page est claire.

---

## Ce que ça change dans le code

Quatorze valeurs dans `:root`, et **trois inversions de rôle** qui touchent le
balisage :

1. Les sections aujourd'hui marquées « sombre » passent en clair — sauf le
   héros et le pied.
2. Le texte par défaut passe de `#F4EDE4` (clair sur sombre) à `#221E1A`
   (sombre sur clair). C'est l'inverse de l'actuel : à re-vérifier bloc par
   bloc, pas globalement.
3. Les boutons d'action passent d'ambre-sur-brique à **brique-sur-blanc** dans
   le corps de page, et restent **brique-claire-sur-profond** dans le héros.

Le garde `coherence.py` interdit toute couleur écrite en dur hors de trois
valeurs tolérées : il refusera le commit si une seule valeur reste orpheline.
Les contrastes seront re-mesurés sur les 896 textes du site après application,
comme ce matin.

## Le risque

**Une page claire pardonne moins.** Sur fond sombre, une faute d'espacement se
voit à peine ; sur blanc, tout se voit. La fermeté vient alors entièrement de
la typographie et du rythme — Archivo 800, interlignes tenus, filets fins. Si
la structure mollit, une palette claire glisse vers le site de kiné.

C'est un risque de mise en œuvre, pas de direction : il se règle en regardant
chaque page après application, pas en changeant de palette.
