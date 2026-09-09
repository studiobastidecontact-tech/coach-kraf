# Refonte coach-krav.fr

Chantier de refonte complète du site vitrine. Ce dossier commence par `_` :
**Jekyll ne le publie pas**, il reste invisible depuis coach-krav.fr tout en
vivant dans le dépôt (il survit donc aux sessions, et il voyage avec le code).

## Le site en une ligne

Coach particulier de Krav Maga, self-défense et boxe, à domicile ou en
extérieur, sur Toulouse et Saint-Sulpice-la-Pointe (81). Une page unique,
hébergée sur GitHub Pages, domaine `coach-krav.fr` via `CNAME`.

## Le virage de cette refonte

L'ancien site (`uber-kravmaga.jimdosite.com`) vendait **la sécurité**.
Le site actuel vend **du fitness**. On revient à la sécurité.

La cible n'est pas le pratiquant d'arts martiaux : c'est la personne qui a
peur — un adulte qui subit des incivilités, une femme qui rentre tard, un
parent dont l'enfant est harcelé, une entreprise qui doit former ses équipes.

## Le site

Cinq pages, toutes servies depuis la racine :

| Page | Rôle |
|---|---|
| `/` | L'accueil : situations, formules, déroulé, coach, tarifs, contact |
| `/enfants/` | Harcèlement scolaire — le meilleur angle commercial, absent du site précédent |
| `/toulouse/` | Lieux d'entraînement, publics et contraintes propres à la ville |
| `/saint-sulpice/` | L'espace, le rythme, les familles — le secteur de résidence |
| `/mentions/` | Mentions légales et confidentialité |

`assets/site.css` et `assets/site.js` sont communs aux cinq pages. Les blocs
(`.sit`, `.pas`, `.bien`, `.tarifs`…) ont chacun leur **variante sombre** :
posés sur `.sec--nuit` sans elle, leur gris tombe à 2,9:1.

## Les fichiers du chantier

| Fichier | Ce qu'il porte |
|---|---|
| `AUDIT.md` | L'état mesuré de l'existant, avec ses chiffres |
| `HERITAGE.md` | Ce qu'on reprend de l'ancien site, et pourquoi |
| `CONTENU.md` | La source de vérité : textes, tarifs, mentions légales, contacts |
| `MESURE-AUDIENCE.md` | La solution retenue, la procédure, et pourquoi elle attend |
| `CHECKLIST.md` | L'avancement, coché au fil de l'eau |
| `croquis/` | Les croquis validés, datés, jamais réécrits en place |
| `sources/` | Les visuels récupérés de l'ancien site, et le logo d'origine |

## Règle de travail

Un push sur `main` **met le site en ligne** — GitHub Pages sert la branche
directement, il n'y a pas d'étage intermédiaire. Rien ne part sans accord
explicite.
