---
version: v1
kind: structure
status: appliquée
date: 2026-09-09
---

# La page fait seize écrans sur un téléphone

> **Tranché par William le 09/09 : les trois directions, appliquées le jour
> même.** Le résultat mesuré est plus modeste que mon estimation — **12,4
> écrans, pas 9,8** — et l'écart est détaillé au bas de ce document. Les tarifs
> passent de 10,6 à 7,5 écrans.

> Écrit après une remarque de William : *« est-ce que le site est bien optimisé
> pour le téléphone ? j'ai pas l'impression »*. L'impression est juste, et la
> mesure dit où ça coince — pas là où je le croyais.

## La mesure

iPhone 390 × 844, sur le site en ligne, tout révélé.

**13 420 px de page, soit 15,9 écrans à faire défiler.** Le poids n'est pas en
cause (201 Ko, aucune image sur l'accueil au premier écran), il n'y a **aucun
débordement horizontal**, et cinq actions sont atteignables sans défiler. Deux
cibles tactiles tombaient sous le seuil AA de 24 px — corrigées le même jour.

Où l'on se trouve, en écrans :

```
 0,0 ┃ héros                    ← téléphone, SMS, prix, premier cours offert
 0,9 ┃ situations               1,8 écran   (3 cartes de 367 px)
 2,7 ┃ formules                 1,2
 3,9 ┃ déroulé                  1,3
 5,2 ┃ bienfaits                1,7 écran   (7 lignes de 143 px)
 6,8 ┃ le coach                 2,6 ÉCRANS  (7 certifications de 109 px)
 9,4 ┃ discipline               1,2
10,6 ┃ TARIFS                   1,9         ← à onze écrans du haut
12,5 ┃ contact                  2,2 écrans  (3 canaux + 4 renvois)
14,7 ┃ pied                     0,9
15,9 ┗
```

**5 037 px de grilles empilées**, soit 38 % de la page. Sur un écran large ce
sont des blocs compacts en trois colonnes ; sur un téléphone chacun devient une
échelle. Les certifications, à elles seules, font 762 px — presque un écran
entier de liste.

## Ce que le réglage ne peut pas faire

J'ai simulé les correctifs de mise en page, un par un, en direct :

| essai | hauteur | gain | écrans |
|---|---|---|---|
| état actuel | 13 420 px | — | **15,9** |
| grilles courtes en 2 colonnes | 13 228 | 192 | 15,7 |
| + marges de section 74 → 58 | 12 972 | 448 | 15,4 |
| + renvois en 2 colonnes | 12 910 | 510 | 15,3 |
| + 4 certifications repliées | 12 550 | 870 | 14,9 |
| + 4 bienfaits repliés | 11 977 | 1 443 | **14,2** |

**Les deux colonnes ne rapportent que 192 px.** À 390 px de large, deux colonnes
forcent le texte à se casser davantage : chaque cellule regrossit et le gain
s'annule presque. C'est le contraire de ce que j'attendais, et c'est pour ça que
je l'ai mesuré plutôt que supposé.

Verdict : **aucun réglage CSS ne change le ressenti.** 15,9 → 14,2 écrans, ce
n'est pas « optimisé pour le téléphone ». La longueur, c'est le contenu — huit
sections, 1 201 mots, 27 cartes — pas la mise en page.

---

## Direction 1 — Trois sections quittent l'accueil

**De 15,9 à 9,8 écrans.** La seule qui change vraiment le ressenti.

Le coach (2,6 écrans) et la discipline (1,2) partent sur leurs propres pages.
L'accueil garde ce qui fait décider : où j'en suis, ce qu'il propose, comment ça
se passe, combien, comment le joindre.

```
┌────────────────────────┐        ┌────────────────────────┐
│ AUJOURD'HUI  15,9 écr. │        │ APRÈS         9,8 écr. │
├────────────────────────┤        ├────────────────────────┤
│ héros              0,9 │        │ héros              0,9 │
│ situations         1,8 │        │ situations         1,8 │
│ formules           1,2 │        │ formules           1,2 │
│ déroulé            1,3 │        │ déroulé            1,3 │
│ bienfaits          1,7 │        │ bienfaits ▸ 3 + 4  1,0 │
│ LE COACH           2,6 │──┐     │ TARIFS             1,7 │ ← à 6,2
│ discipline         1,2 │──┼──┐  │ contact            1,9 │
│ tarifs             1,9 │  │  │  │ pied               0,9 │
│ contact            2,2 │  │  │  └────────────────────────┘
│ pied               0,9 │  │  │
└────────────────────────┘  │  │  ┌────────────────────────┐
                            └──┼─▸│ /le-coach/   page dédiée│
                               └─▸│ /la-discipline/         │
                                  └────────────────────────┘
```

Le sceptique ne perd rien : la bande de preuve sous le héros porte déjà
« INSTRUCTEUR · MENTION MILITAIRE ET FORCES DE L'ORDRE », et l'accueil renvoie
vers `/le-coach/` là où la question se pose. **Les tarifs passent de 10,6 à 6,2
écrans.**

**Ce que ça coûte** : deux pages à écrire (leur contenu existe déjà, il déménage),
le maillage interne à refaire, deux entrées de menu, le plan du site et les
données structurées à suivre. Une à deux heures.
**Le risque** : un visiteur qui ne clique pas ne verra jamais les sept
certifications. C'est le vrai arbitrage — la légitimité contre la longueur.

## Direction 2 — Les échelles se replient, la page reste entière

**De 15,9 à 14,2 écrans.** Tout reste sur l'accueil ; les deux listes longues
montrent trois éléments et proposent le reste.

```
┌──────────────────────────────────────────┐
│  Quinze ans à enseigner le Krav Maga     │
│                                          │
│  ┌────────────────────────────────────┐  │
│  │ Instructeur Krav Maga              │  │
│  │ Mention militaire et forces…       │  │
│  ├────────────────────────────────────┤  │
│  │ G5 Krav Maga                       │  │
│  │ Grade d'expert, dixième niveau     │  │
│  ├────────────────────────────────────┤  │
│  │ Ceintures noires                   │  │
│  │ Karaté · Kudo · violette de JJB    │  │
│  └────────────────────────────────────┘  │
│                                          │
│  ▸ Voir les 4 autres certifications      │
│                                          │
└──────────────────────────────────────────┘
```

Le contenu reste dans le DOM, donc lisible par les moteurs et par un lecteur
d'écran. Entier sur écran large, replié sous 760 px.

> **Écart entre le croquis et la livraison.** J'avais annoncé un `<details>`
> natif, « sans une ligne de script ». Il n'aurait pas tenu : `<details>` ne
> peut pas replier une *partie* d'une grille sans la couper en deux, ce qui
> aurait doublé le filet de séparation ; et un `<details>` au corps vide, dont
> le contenu révélé vit ailleurs, annonce « déplié » sur quelque chose qu'il ne
> contient pas — un défaut d'accessibilité. Livré avec un `<button>` portant
> `aria-expanded` et `aria-controls`. Le bouton arrive `hidden` du serveur et
> c'est le script qui le révèle : **sans JS, la liste reste entière.** On ne
> cache jamais du contenu à quelqu'un qui n'a pas le moyen de le rouvrir.

**Ce que ça coûte** : une demi-heure, aucun déménagement, aucun maillage à
refaire.
**Le risque** : ça soulage sans régler. À 14,2 écrans on scrolle encore beaucoup.

## Direction 3 — Un rail d'ancres collant

**15,9 écrans, mais on n'en traverse plus aucun.** La page ne raccourcit pas ;
on cesse d'avoir à la parcourir.

```
┌──────────────────────────────────────────┐
│ ☰  coach-krav.fr              07 81 68…  │
├──────────────────────────────────────────┤
│ ‹ Situations · Cours · Déroulé · TARIFS  │  ← rail collant sous l'en-tête,
└──────────────────────────────────────────┘     défile à l'horizontale
```

Aujourd'hui, atteindre les tarifs demande deux gestes : ouvrir le menu, choisir.
Le rail les met à un seul tapotement, en permanence, et il indique en plus où
l'on se trouve.

**Ce que ça coûte** : une heure, plus 44 px de hauteur d'écran perdus en
permanence.
**Le risque** : un deuxième bandeau collant, en plus de l'en-tête et de la barre
du pouce. Trois bandes fixes sur un écran de 844 px, ça commence à faire.

---

## Ma recommandation

**La direction 1, et la 2 avec elle.** Elle est la seule qui fasse passer la
page sous dix écrans, et c'est le seul chiffre qui répond à la remarque. Une
page d'accueil de coach local n'a pas à raconter sa biographie complète : elle
doit amener à l'appel, et tout ce qui s'interpose entre le visiteur et le prix
travaille contre elle. Les tarifs à 6,2 écrans au lieu de 10,6, c'est la moitié
du chemin en moins.

La 2 vient avec, parce qu'elle est presque gratuite et qu'elle supprime la
sensation d'échelle là où elle reste — les sept bienfaits.

**Le cas où la 3 gagne** : si tu tiens à ce que l'accueil raconte tout, parce
que le visiteur qui va au bout est celui qui appelle. Alors la longueur est un
choix et il faut la rendre traversable, pas la réduire.

**Le cas où on ne touche à rien** : si la page longue convertit. On ne le sait
pas — il n'y a aucune mesure d'audience. C'est la seule chose qui trancherait
pour de bon, et elle demande un compte à ouvrir.

---

## Le résultat, et l'écart avec mon estimation

Appliqué le 09/09. **13 420 → 10 462 px, soit 15,9 → 12,4 écrans.** Les tarifs
passent de 10,6 à **7,5 écrans**.

J'avais annoncé 9,8. L'écart tient en trois lignes, et aucune n'était une
surprise une fois posée :

| | px |
|---|---|
| le coach et la discipline retirés | **− 3 200** |
| la section de renvoi qui les remplace, que je n'avais pas comptée | **+ 847** |
| les quatre bienfaits repliés | − 513 |
| le pied, qui gagne deux liens et de l'écart entre eux | + 110 |
| les marges de section, 74 → 58 | − 224 |
| **total** | **− 2 958** |

**Les deux colonnes ont été abandonnées après mesure** : elles ne rapportaient
plus que 50 px une fois les certifications et les principes partis sur leurs
propres pages — et elles auraient fait casser le texte davantage. C'est la
deuxième fois de la journée que cette idée est démentie par la mesure.

## Le coût du rail, mesuré

Trois bandes fixes sur un écran de 844 px : **en-tête 69 + rail 52 + barre du
pouce 76 = 197 px, soit 23 % de l'écran.** Il reste 647 px utiles.

C'est le risque annoncé dans la direction 3, et il est réel. Deux atténuations
sont en place : le rail ne coiffe **pas** le héros — il est posé après la bande
de preuve, donc la première impression garde toute sa hauteur — et il n'existe
que sur l'accueil, la seule page qui ait sept sections à traverser. Les pages
courtes, `/le-coach/` à 4,9 écrans, n'en ont pas.

Si les 23 % pèsent trop à l'usage, retirer le rail est **une ligne** :
`.rail{display:none}` sans condition de largeur.

## Ce qui a été livré

- `/le-coach/` et `/la-discipline/` — le contenu déménagé, sans une ligne
  inventée. Fil d'Ariane, `BreadcrumbList`, plan du site, maillage depuis le
  menu, le pied et les renvois.
- Le repli des listes longues : **le bouton arrive `hidden` du serveur et c'est
  le script qui le révèle**. Sans JS, la liste reste entière — on ne cache
  jamais du contenu à quelqu'un qui n'a pas le moyen de le rouvrir. Rien n'est
  retiré du document : les éléments sont masqués, pas supprimés, donc les
  moteurs et les lecteurs d'écran les voient toujours. `aria-expanded` suit
  l'état, et la cible fait 350 × 45.
- Le rail d'ancres, avec marquage de la section courante par balayage — pas
  d'`IntersectionObserver`, pour la raison qui vaut déjà pour les entrées au
  défilement : il ne signale que ce qu'il voit *entrer*, et sur un saut d'ancre
  les sections traversées ne sont jamais notifiées.
- Deux cibles tactiles sous le seuil AA de 24 px, portées à 29 sans que le
  texte bouge.

**Mesure finale** : 2 219 textes sur 10 pages × 2 largeurs, 857 styles
distincts, **zéro échec de contraste, zéro débordement horizontal**.

## Ce que le garde a attrapé au passage

Trois refus de commit, dont deux vraies fautes que je venais de poser :

- le menu des deux pages neuves, hérité de Toulouse, pointait vers `#tarifs`
  — une ancre qui n'existe pas chez elles ;
- et une faute **du garde** : il lisait « dix » dans « soixante-**dix** ». La
  règle des décomptes ne voyait pas le trait d'union, que `\b` traite comme un
  séparateur de mots. Corrigée par une paire de regards `(?<![-\w])` /
  `(?![-\w])`, puis **éprouvée sur six cas dont trois adjacents** — « soixante-dix
  ans », « dix-sept ans », « Quinze ans » doivent passer ; « Trois façons »,
  « Dix effets » et « 4 principes » avec deux sous-titres doivent être refusés.
  6/6.
