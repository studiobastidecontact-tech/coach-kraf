# L'atelier de coach-krav.fr

Ce dossier commence par `_` : **Jekyll ne le publie pas**, il reste invisible
depuis coach-krav.fr tout en vivant dans le dépôt. Il porte l'outillage du site
et sa direction visuelle — les deux gardes, les croquis datés, les images
sources.

> **Le pilotage n'est plus ici.** Depuis le 2026-09-09, tout ce qui décrit la
> *prestation* — la source de vérité du contenu, l'inventaire de ce qui est
> sourcé, les questions au client, l'avancement — vit dans un dépôt **privé** :
> `wdelpech-mediane/coach-kraf-chantier`.
>
> Ce dépôt-ci est **public**, et un fichier d'un dépôt public est lisible par
> qui en connaît le chemin, `_` ou pas. La frontière tient en une phrase :
> **ce qui décrit le site reste ici, ce qui décrit la prestation est là-bas.**
> En cas de doute, là-bas.

## Le site

Coach particulier de Krav Maga, self-défense et boxe, à domicile ou en
extérieur, sur Toulouse et Saint-Sulpice-la-Pointe (81). Hébergé sur GitHub
Pages, domaine `coach-krav.fr` via `CNAME`.

Il s'adresse à qui a peur, pas au pratiquant d'arts martiaux : un adulte qui
subit des incivilités, une femme qui rentre tard, un parent dont l'enfant est
harcelé, une entreprise qui doit former ses équipes.

Cinq pages, toutes servies depuis la racine :

| Page | Rôle |
|---|---|
| `/` | L'accueil : situations, formules, disciplines, déroulé, coach, tarifs, contact |
| `/enfants/` | Harcèlement scolaire — le meilleur angle commercial, absent du site précédent |
| `/toulouse/` | Lieux d'entraînement, publics et contraintes propres à la ville |
| `/saint-sulpice/` | L'espace, le rythme, les familles — le secteur de résidence |
| `/mentions/` | Mentions légales et confidentialité |

`assets/site.css` et `assets/site.js` sont communs aux cinq pages. Les blocs
(`.sit`, `.pas`, `.bien`, `.tarifs`…) ont chacun leur **variante sombre** :
posés sur `.sec--nuit` sans elle, leur gris tombe à 2,9:1.

## Les deux gardes

| Garde | Rôle |
|---|---|
| `coherence.py` | Refuse le commit si le site se contredirait en ligne — prix, durées, ancres, contraste, et la frontière ci-dessus |
| `verifier-direction.py` | Mesure chaque paire texte/fond de la charte et refuse une direction dont une paire tombe sous son seuil |

Le premier tourne au `pre-commit`. Installation :
`bash _chantier/hooks/installer.sh`.

## La direction visuelle

| Dossier | Rôle |
|---|---|
| `croquis/` | Les croquis validés, datés, jamais réécrits en place |
| `charte.html` | La charte rendue, à ouvrir dans un navigateur |
| `directions/` | Les directions candidates, à passer au second garde |
| `sources/` | Les visuels récupérés de l'ancien site, et le logo d'origine |

## Règle de travail

Un push sur `main` **met le site en ligne** — GitHub Pages sert la branche
directement, il n'y a pas d'étage intermédiaire. Rien ne part sans accord
explicite.
