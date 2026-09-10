---
version: V1
kind: ui
status: appliquée
date: 2026-09-10
---

# Le Krav Maga tient en trois lignes sur la page qui le vend

Remarque de William, 2026-09-10 :

> *« "Les disciplines / Karaté, boxe anglaise, boxe thaï, MMA" → du coup c'est
> les autres disciplines non ? Et est-ce qu'on a un bandeau avant pour parler
> juste du Krav Maga et ses vertus ? »*

Les deux observations sont justes, et la seconde désigne un trou de structure.

## Le déséquilibre, en chiffres

| | Place sur l'accueil |
|---|---|
| Karaté, boxe anglaise, boxe thaï, MMA | **une section entière, 4 cartes**, position 4 sur 9 |
| **Krav Maga** | **une demi-carte, 3 lignes**, position 7, à côté de celle sur David |

Le texte intégral consacré à la discipline principale :

> « "Combat rapproché" en hébreu. Créé dans les années 1940, adopté par l'armée
> et la police israéliennes. Quatre principes, aucune figure. »

Rien d'autre. `#formules` explique comment on le travaille **avant** d'avoir dit
ce que c'est ; `#bienfaits` arrive après les autres disciplines. **Un visiteur
qui ignore ce qu'est le Krav Maga ne l'apprend nulle part sur l'accueil** — et
c'est le premier mot du nom de domaine.

Le libellé « Les disciplines » est corrigé séparément en **« Les autres
disciplines »** : il annonçait plus que sa section ne contient.

## La section proposée

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  LE KRAV MAGA                                          fond PIERRE   │
  │                                                                      │
  │  Quatre règles, aucune figure                                        │
  │                                                                      │
  │  « Combat rapproché » en hébreu. Né dans la rue et non dans un       │
  │  dojo, adopté par l'armée et la police israéliennes dans les         │
  │  années 1940. Ce n'est pas un sport de combat : aucune règle,        │
  │  aucune compétition.                                                 │
  │                                                                      │
  │  ┌──────────┬──────────┬──────────┬──────────┐                       │
  │  │ 01       │ 02       │ 03       │ 04       │                       │
  │  │ Simpli-  │ Rapidité │ Effica-  │ Maîtrise │                       │
  │  │ cité     │          │ cité     │ de soi   │                       │
  │  │          │          │          │          │                       │
  │  │ Un geste │ Une      │ Le but   │ Savoir   │                       │
  │  │ qu'on ne │ agression│ n'est pas│ se       │                       │
  │  │ peut pas │ dure     │ de       │ défendre │                       │
  │  │ faire en │ quelques │ dominer, │ n'auto-  │                       │
  │  │ tremblant│ secondes │ c'est de │ rise     │                       │
  │  │ ne sert  │ : la     │ créer    │ rien.    │                       │
  │  │ à rien.  │ réponse  │ l'ouver- │ La       │                       │
  │  │          │ part du  │ ture qui │ réponse  │                       │
  │  │          │ réflexe. │ permet   │ reste    │                       │
  │  │          │          │ de partir│ propor-  │                       │
  │  │          │          │          │ tionnée. │                       │
  │  └──────────┴──────────┴──────────┴──────────┘                       │
  │                                        Lire la page discipline →     │
  └──────────────────────────────────────────────────────────────────────┘
```

Grille `.princ`, la même que `/la-discipline/` emploie **pour ces quatre mêmes
règles** : un visiteur qui suit le lien retrouve la structure qu'il vient de
lire. Le garde `controler_grilles` la connaît déjà (4 cartes sur 4 colonnes), et
la règle du nombre annoncé compte les quatre `<h3>` derrière « Quatre règles ».

Les textes **condensent** ceux de `/la-discipline/`, ils ne les inventent pas.
Aucune des quatre règles n'est de moi : elles sont la doctrine canonique de la
méthode, et la page les porte déjà.

## Où elle se place, et la cascade qu'elle déclenche

Entre `#situations` et `#formules`. L'ordre devient celui d'une explication :
**pourquoi vous venez → ce qu'on apprend → comment on le travaille → les autres
options.** Aujourd'hui la troisième arrive avant la deuxième.

```
  AVANT                          APRÈS
  clair   situations             clair   situations
                                 PIERRE  krav-maga      ← nouvelle
  PIERRE  formules               clair   formules       ← bascule
  clair   disciplines            PIERRE  disciplines    ← bascule
  PIERRE  bienfaits              clair   bienfaits      ← bascule
  clair   deroule                PIERRE  deroule        ← bascule
  PIERRE  fond                   clair   fond           ← bascule
  clair   tarifs                 PIERRE  tarifs         ← bascule
  clair   contact                clair   contact        ← inchangé
```

**La cascade ne coûte presque rien** : `.sec--pierre` ne redéfinit que trois
jetons de rôle (`--fond`, `--fond-carte`, `--survol`), et tous les blocs s'y
adaptent seuls. Une classe se déplace, aucun composant n'est touché.

Elle **améliore** au passage ce qui existe : aujourd'hui `#tarifs` et `#contact`
sont deux sections claires consécutives en fin de page. Après, l'alternance est
régulière du premier au dernier écran, et les tarifs gagnent l'aplat qui les
détache.

## Les deux sections voisines, et pourquoi elles ne bougent pas

`#formules` (« Deux façons de travailler ») garde son contenu : elle décrit le
cours technique et l'entraînement au combat, ce qui est le niveau **en dessous**
des quatre règles. Elle suit naturellement.

`#fond` garde ses deux cartes, David et le renvoi vers la discipline. Retirer
la seconde laisserait une carte seule dans une grille à deux colonnes — que le
garde refuserait — et le renvoi reste utile à qui descend sans avoir lu le
milieu de la page.

## Le prix : un écran de plus

La page gagne un écran. Elle en compte déjà huit ; c'est le prix de dire ce
qu'on vend avant d'énumérer ce qu'on vend d'autre.

---

## Les quatre défauts trouvés en construisant

Trois défauts trouvés en posant la section, tous **antérieurs** à elle.

**Le menu basculait en burger 340 px trop tard.** Ses trois blocs — marque
(135), navigation (668), bouton d'appel (194) — réclament **997 px** côte à
côte, mais le seuil était à 760. Sur toute la plage 761-1050 px (tablette en
paysage, petit portable) la navigation passait donc **sur deux lignes**. Mesuré
dans les deux états, avec et sans l'entrée « Krav Maga » : le défaut existait
déjà à six entrées (517 px), la septième l'a seulement élargi à 591. Seuil
porté à **1100 px**, frontière éprouvée à 1120 (menu sur une ligne) et 1080
(burger, menu qui s'ouvre et se referme).

**Le numéro disparaissait de l'en-tête sur téléphone**, et la barre du pouce ne
prend le relais qu'une fois le bouton du héros sorti du champ : en haut de page,
l'appel n'était joignable nulle part. Demande de William le même jour. Il reste
désormais, compacté — 16 px au lieu de 19, marge intérieure réduite — et sous
375 px la marque se réduit à son glyphe pour lui laisser la place.

**Le burger tombait à 32 px**, sous le minimum tactile de WCAG 2.5.5, dès que
le numéro revenait à côté : le flex le comprimait. `flex-shrink:0` sur les deux.

**Une troisième navigation existait**, que ni le croquis ni la première passe
n'avaient vue : le rail d'ancres mobile, sous l'en-tête, propre à l'accueil.
Une capture d'écran l'a montrée — aucune mesure ne l'aurait désignée. Son JS
lit ses liens dynamiquement, donc l'entrée s'y intègre seule ; vérifié en
défilant, il marque bien « Krav Maga » puis « Cours ».

## L'alternance obtenue

```
  clair    situations     PIERRE   krav-maga
  clair    formules       PIERRE   disciplines
  clair    bienfaits      PIERRE   deroule
  clair    fond           PIERRE   tarifs
  clair    contact
```

Stricte du premier au dernier écran, ce qu'elle n'était pas avant.

## Le doublon, tranché

Sur téléphone, le numéro est apparu **deux fois en même temps** : dans l'en-tête
fixe et dans la barre du pouce. William a laissé l'arbitrage.

**Les deux points de contact restent, la répétition part.** Ils ne font pas le
même travail : l'en-tête porte l'**information** — à qui l'on parle, il est
joignable, voici son numéro — et la barre porte l'**action**, sous le pouce.
Le défaut n'était pas d'avoir deux points d'appel, c'était d'afficher deux fois
les mêmes chiffres au même instant.

La barre passe donc à deux **verbes** : **Appeler** et **SMS**. Elle y gagne
une symétrie qu'elle n'avait pas — un long numéro face à un sigle de trois
lettres, sur deux boutons de largeur égale, se lisait de travers. Le lien garde
`aria-label="Appeler le 07 81 68 60 84"` : rien ne se perd pour un lecteur
d'écran.

Appliqué aux **treize** pages. Deux d'entre elles ont une barre différente —
`/404/` et `/merci/` offrent « Accueil » plutôt que le SMS — et `merci/`
portait le motif deux fois, donc a demandé un ciblage dans sa barre seule.
