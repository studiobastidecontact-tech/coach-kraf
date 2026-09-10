---
version: V2
kind: ui
status: appliquée
date: 2026-09-10
---

# Le pied de page prend un écran et demi

Remarque de William, 2026-09-10 : *« il faudrait arranger le footer qui prend
trop de hauteur »*.

## Ce qui est mesuré

| | Hauteur | En écrans |
|---|---|---|
| desktop 1440×733 | **598 px** | 0,82 |
| mobile 500×733 | **989 px** | **1,35** |

**La cause est le travail de la veille.** La colonne « Pages » est passée de
sept à dix liens le 9 septembre — `/coach-sportif/`, `/arts-martiaux/`,
`/boxe-et-mma/`. Elle fait 414 px et, en grille, impose sa hauteur aux **trois**
colonnes : celle de la marque n'a que 156 px de contenu, celle du contact 135.

```
  DESKTOP — AUJOURD'HUI, 598 px
  ┌──────────────────────────────────────────────────────────────────────┐
  │                        ↕ 64 px de padding                            │
  │  ┌─ marque 460 ──────┐ ┌─ Pages 288 ─┐ ┌─ Contact 288 ─┐             │
  │  │ coach-krav.fr     │ │ PAGES       │ │ CONTACT       │             │
  │  │ Coach sportif     │ │ Accueil     │ │ 07 81 68 60 84│             │
  │  │ particulier :     │ │ Self-défense│ │ Envoyer un SMS│             │
  │  │ Krav Maga, self-  │ │ Enfants et… │ │ kpitol@…      │             │
  │  │ défense et arts   │ │ Toulouse    │ │               │             │
  │  │ martiaux. Cours à │ │ Saint-Sulp… │ │               │             │
  │  │ domicile, en ext… │ │ Coach sport…│ │      135 px   │             │
  │  │        156 px     │ │ Arts martia…│ │               │             │
  │  │                   │ │ Boxe et MMA │ │               │             │
  │  │   ← 258 px VIDES  │ │ David       │ │  ← 279 px     │             │
  │  │                   │ │ La discipl… │ │     VIDES     │             │
  │  │                   │ │ Mentions…   │ │               │             │
  │  └───────────────────┘ └── 414 px ───┘ └───────────────┘             │
  │                        ↕ 44 px                                       │
  │  © 2026 coach-krav.fr              Mentions légales · Confidentialité │
  │                        ↕ 28 px                                       │
  └──────────────────────────────────────────────────────────────────────┘
        ▲ 537 px de vide cumulé dans deux colonnes sur trois
```

## Ce que je propose

Trois gestes, aucun ne retire un lien.

```
  DESKTOP — APRÈS, ~350 px
  ┌──────────────────────────────────────────────────────────────────────┐
  │                        ↕ 48 px                                       │
  │  ┌─ marque 400 ────┐ ┌─── Pages 384, EN DEUX ───┐ ┌─ Contact 252 ─┐  │
  │  │ coach-krav.fr   │ │ PAGES                    │ │ CONTACT       │  │
  │  │ Coach sportif   │ │ Accueil      Coach sport.│ │ 07 81 68 60 84│  │
  │  │ particulier, à  │ │ Self-défense Arts martia.│ │ Envoyer un SMS│  │
  │  │ domicile, sur   │ │ Enfants…     Boxe et MMA │ │ kpitol@…      │  │
  │  │ Toulouse et     │ │ Toulouse     David       │ │               │  │
  │  │ Saint-Sulpice.  │ │ Saint-Sulp.  La discipl. │ │               │  │
  │  │      ~110 px    │ │        ~200 px           │ │    135 px     │  │
  │  └─────────────────┘ └──────────────────────────┘ └───────────────┘  │
  │                        ↕ 32 px                                       │
  │  © 2026 coach-krav.fr              Mentions légales · Confidentialité │
  │                        ↕ 24 px                                       │
  └──────────────────────────────────────────────────────────────────────┘
```

1. **Les dix liens sur deux colonnes.** Cinq rangs au lieu de dix : la colonne
   passe de 414 à ~200 px, et c'est elle qui commandait tout. La grille se
   rééquilibre — `1.2fr 1.1fr 0.7fr` au lieu de trois parts fixes — pour que
   « Saint-Sulpice-la-Pointe » tienne sur une ligne dans une demi-colonne.
2. **La description passe de quatre lignes à deux.** Elle répétait mot pour mot
   la ligne d'identité du hero, quatre écrans plus haut.
3. **Les respirations resserrées** : 64/28 → 48/24 de padding, 44 → 32 entre
   les blocs.

## Le mobile, où le gain compte le plus

```
  AVANT, 989 px = 1,35 écran        APRÈS, ~530 px = 0,72 écran
  ┌───────────────────────┐         ┌───────────────────────┐
  │ coach-krav.fr         │         │ coach-krav.fr         │
  │ description 4 lignes  │  156    │ description 2 lignes  │  110
  ├───────────────────────┤         ├───────────────────────┤
  │ PAGES                 │         │ PAGES                 │
  │ Accueil               │         │ Accueil    Coach sp.  │
  │ Self-défense femme    │         │ Self-déf.  Arts mart. │
  │ Enfants et harcèlem.  │         │ Enfants…   Boxe/MMA   │  200
  │ Toulouse              │  414    │ Toulouse   David      │
  │ Saint-Sulpice-la-P.   │         │ St-Sulpice La discip. │
  │ Coach sportif         │         ├───────────────────────┤
  │ Arts martiaux jap.    │         │ CONTACT               │  135
  │ Boxe et MMA           │         │ 07 81 68 60 84        │
  │ David                 │         │ Envoyer un SMS        │
  │ La discipline         │         │ kpitol@laposte.net    │
  │ Mentions légales      │         └───────────────────────┘
  ├───────────────────────┤
  │ CONTACT               │  135
  └───────────────────────┘
```

Sur téléphone, la barre du pouce reste collée en bas pendant tout ce défilement :
l'utilisateur traverse un écran et demi de liens avec un bouton d'appel sous les
yeux. Réduire de moitié raccourcit la sortie de page sans lui retirer un seul
chemin.

## Ce qui a été posé, et l'écart avec ce croquis

| | Avant | Annoncé ici | **Mesuré après** |
|---|---|---|---|
| desktop 1440 | 598 px | ~350 | **379 px** — 0,52 écran |
| mobile 500 | 989 px | ~530 | **599 px** — 0,82 écran |
| mobile 360 | — | — | **712 px** — 0,91 écran |

**Deux écarts, tous deux nommés :**

1. **Le mobile n'empile plus en trois blocs.** Ce croquis les montrait l'un
   sous l'autre ; à 599 px on était encore à 0,98 écran. La marque et le
   contact sont donc passés **côte à côte**, la liste des pages dessous en
   pleine largeur — ses deux colonnes intactes. Le contact remonte, ce qui sert
   celui qui descend chercher le téléphone.
2. **Le seuil du dernier palier a été mesuré, pas supposé.** Posé d'abord à
   400 px « au cas où l'adresse e-mail ne tiendrait plus », puis mesuré à
   360 px : `kpitol@laposte.net` fait 140 px pour 146 disponibles. Le seuil est
   descendu à **340 px**, ce qui rend 85 px de plus aux téléphones de 360.

**Deux pièges rencontrés en chemin**, tous deux invisibles à la lecture :

- Une règle groupée plus bas dans la feuille — `.trio,.duo,…,.pied
  {grid-template-columns:1fr}` — remettait `.pied` à une seule colonne. Le
  placement posé plus haut y créait alors une colonne **implicite** de 140 px :
  deux colonnes inégales au lieu des deux voulues. `.pied` est sorti de ce
  groupe.
- Une première mesure a conclu que les liens légaux passaient **sous la barre
  d'appel**, `elementFromPoint` rendant « pouce ». C'était faux :
  `scroll-behavior: smooth` faisait lire une position intermédiaire. Tout en
  bas, ils sont à 26 px au-dessus de la barre et répondent au clic. **Mesurer
  après un défilement animé demande d'attendre son arrêt.**

## Ce que ça ne fait pas

Aucun lien n'est retiré. Le pied de page reste le seul endroit qui liste les
onze pages — c'est ce qui rend les trois pages du 9 septembre atteignables
depuis n'importe où.
