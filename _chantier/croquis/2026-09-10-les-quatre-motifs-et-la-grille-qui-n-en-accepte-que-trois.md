---
version: V1
kind: ui
status: appliquée
date: 2026-09-10
---

# Les quatre motifs, et la grille qui n'en accepte que trois

Demande de William, 2026-09-10, verbatim :

> *« pour les raisons de commencer je préfère : Je dois pouvoir me défendre /
> Je souhaite améliorer mon physique et mon mental / Je veux prévenir le
> harcèlement à l'école ou au travail / Mon équipe doit gagner en confiance »*

## Ce que ça corrige

Les trois cartes en ligne sont **trois peurs** : « je ne me sens pas en
sécurité », « mon enfant est harcelé », « mon équipe est exposée ». Le motif le
plus fréquent chez un coach sportif — *je veux progresser* — n'apparaissait
nulle part en haut de page, alors que la veille on lui a ouvert une page entière
(`/coach-sportif/`), sept bienfaits et trois pages de disciplines.

Deuxième correction, plus discrète : les formulations passent d'**états subis**
à des **verbes de volonté**.

| Aujourd'hui | Proposé |
|---|---|
| Je **ne me sens pas** en sécurité | Je **dois pouvoir** me défendre |
| Mon enfant **est** harcelé | Je **veux prévenir** le harcèlement |
| Mon équipe **est exposée** | Mon équipe **doit gagner** en confiance |

Le lecteur n'est plus décrit comme une victime, il est décrit comme quelqu'un
qui décide.

## La contrainte : la grille est à trois colonnes

`.trio` fait `repeat(3,1fr)` et sert sur **neuf pages**. Une quatrième carte y
laisserait une case vide en seconde ligne — et le garde `controler_grilles()`
refuserait le commit, puisqu'il exige un multiple du nombre de colonnes.

Largeur utile du conteneur : **1124 px**. Ce que chaque option laisse au texte,
padding de carte (2 × 30) déduit :

| | Largeur de carte | Texte utile | Le titre le plus long¹ |
|---|---|---|---|
| 4 colonnes | 264 px | **204 px** | **4 lignes** |
| 3 colonnes (aujourd'hui) | 360 px | 300 px | 2 lignes |
| **2 × 2** | 551 px | **491 px** | **1 ligne** |

¹ « Je veux prévenir le harcèlement à l'école ou au travail », 54 signes à 23 px.

Quatre colonnes est écarté : un titre sur quatre lignes surmontant deux
paragraphes fait une carte étroite et très haute, illisible. **La grille
s'adapte au texte, pas l'inverse** — les formulations ne sont pas raccourcies
pour faire tenir une mise en page.

## La disposition proposée : deux par deux

Une classe dédiée `.motifs` — `.trio` n'est pas touché et continue de servir
les huit autres pages.

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  MOTIFS                                                              │
  │  Quatre raisons de commencer                                         │
  │  La plupart des gens appellent pour une raison précise. En voici     │
  │  quatre. Si la vôtre n'y est pas, elle est sans doute plus bas.      │
  │                                                                      │
  │  ┌─ 551 px ──────────────────┐  ┌─ 551 px ──────────────────┐        │
  │  │ 01                        │  │ 02                        │        │
  │  │ Je dois pouvoir me        │  │ Je souhaite améliorer mon │        │
  │  │ défendre                  │  │ physique et mon mental    │        │
  │  │                           │  │                           │        │
  │  │ Des incivilités qui       │  │ Reprendre une activité    │        │
  │  │ montent au travail. Un    │  │ sans remettre les pieds   │        │
  │  │ trajet le soir qui pèse.  │  │ dans une salle. Se        │        │
  │  │                           │  │ dépenser vraiment.        │        │
  │  │ ▸ Tenir la distance, se   │  │ ▸ Le souffle, le gainage  │        │
  │  │   dégager, ne plus figer. │  │   et le calme viennent    │        │
  │  │                           │  │   avec la technique.      │        │
  │  │ Voir les cours →          │  │ La page coach sportif →   │        │
  │  └───────────────────────────┘  └───────────────────────────┘        │
  │  ┌───────────────────────────┐  ┌───────────────────────────┐        │
  │  │ 03                        │  │ 04                        │        │
  │  │ Je veux prévenir le       │  │ Mon équipe doit gagner    │        │
  │  │ harcèlement à l'école ou  │  │ en confiance              │        │
  │  │ au travail                │  │                           │        │
  │  │                           │  │ Personnel exposé au       │        │
  │  │ Un enfant qui rentre la   │  │ public, déplacements      │        │
  │  │ tête basse et ne dit      │  │ isolés, un client qui     │        │
  │  │ rien. Un collègue qui a   │  │ monte le ton.             │        │
  │  │ pris l'habitude…          │  │                           │        │
  │  │ ▸ Une posture, un regard, │  │ ▸ Séminaires entreprises  │        │
  │  │   une voix qui portent.   │  │   et administrations.     │        │
  │  │ La page enfants →         │  │ Demander un devis →       │        │
  │  └───────────────────────────┘  └───────────────────────────┘        │
  └──────────────────────────────────────────────────────────────────────┘
```

Chaque carte est **plus large donc plus courte** qu'aujourd'hui : à 551 px le
paragraphe tient en trois lignes au lieu de quatre. Deux rangs de ~210 px
valent ~440 px contre 250 px aujourd'hui — la section grandit de 190 px, pas du
double.

Sur téléphone la grille passe à une colonne, comme `.trio` le fait déjà.

## L'ordre, et pourquoi il n'est pas discutable

Celui de William, tel quel. La défense d'abord — c'est le titre de la page et
le motif que le hero annonce. Le physique en second : c'est la porte qu'on
vient d'ouvrir, elle mérite le meilleur emplacement restant. Le harcèlement et
l'entreprise ensuite, du plus personnel au plus collectif.

## Une alternative écartée

**Trois en ligne + un en pleine largeur** — les trois motifs de particuliers en
`.trio`, l'entreprise en bandeau horizontal dessous. Le découpage est juste
(B2C / B2B) mais il **hiérarchise ce que William a donné à égalité**, et il
casse la symétrie d'une section qui gagne à se lire d'un bloc.

## Ce que ça oblige à changer ailleurs

| Fichier | Geste |
|---|---|
| `index.html` | quatre cartes, titre « Quatre raisons », chapô réécrit, eyebrow « Motifs » |
| `assets/site.css` | classe `.motifs` en deux colonnes, et sa version une colonne sous 760 px |
| `_chantier/coherence.py` | inscrire `('motifs', …, 2)` dans `GRILLES` |

L'ancre `#situations` **ne bouge pas** : quatorze liens de navigation la
visent, sous le libellé « Pour qui ».

---

## Le retour de David, une heure plus tard

Il a lu la proposition pendant qu'elle se construisait, et il a corrigé deux
choses que ni William ni moi n'avions vues.

> *« "je ne me sens pas en sécurité" fait RN. Faut éviter. »*
> *« Idem avec le harcèlement. C'est tendance mais… ce n'est pas non plus le
> fléau national. »*
> *« En revanche : je veux me débarrasser de mes craintes. »*
> *« Peut-être : une bonne raison pour débuter. Puis énumération. »*
> *« Je dois me débarrasser de mes craintes et de mes faiblesses. »*

**Le registre, pas la formulation.** « Je ne me sens pas en sécurité » n'était
pas maladroit : il était **politiquement marqué**. Un coach de self-défense qui
ouvre sur le sentiment d'insécurité emprunte un vocabulaire de campagne, et
David refuse ce terrain. Même chose pour le harcèlement : sujet porteur, donc
suspect comme accroche.

Sa solution retourne la phrase vers l'intérieur. « Je ne me sens pas en
sécurité » décrit **le monde** ; « je dois me débarrasser de mes craintes et de
mes faiblesses » décrit **soi**. Le second est un objectif d'entraînement, le
premier un constat de société.

**Sa deuxième idée règle un problème de structure.** Le titre porte
l'invitation — *Une bonne raison de débuter* — et sa phrase devient la première
ligne de l'énumération. Il n'y a plus de nombre à annoncer dans le titre, donc
plus rien à resynchroniser quand une carte s'ajoutera.

### Ce qui est en ligne

| | Proposé ici | **Livré** |
|---|---|---|
| Titre | Quatre raisons de commencer | **Une bonne raison de débuter** |
| 01 | Je dois pouvoir me défendre | **Je dois me débarrasser de mes craintes et de mes faiblesses** |
| 02 | Je souhaite améliorer mon physique et mon mental | **Je dois pouvoir me défendre** |
| 03 | Je veux prévenir le harcèlement à l'école ou au travail | **Je souhaite améliorer mon physique et mon mental** |
| 04 | Mon équipe doit gagner en confiance | inchangé |

Le motif harcèlement **disparaît de l'accueil**. La page `/enfants/` reste en
ligne, atteignable par le pied de page et les renvois de bas de section : elle
répond à qui la cherche, elle n'accroche plus personne.

Le mot « incivilités » est parti de la carte défense pour la même raison.

### Trois écarts mesurés

1. **Le titre le plus long fait deux lignes, pas une.** À 58 signes il occupe
   75 px de haut contre 50 pour les courts — le tableau de largeur plus haut
   sous-estimait la casse d'Inter à 23 px.
2. **La section fait 1 137 px, pas les ~440 annoncés pour la grille seule.**
   Deux rangs de 355 px plus le chapeau : elle a doublé, pas grandi de 190 px.
3. **La colonne de droite gardait 77 px de vide** sous son lien, les deux
   cartes paires étant plus courtes d'une ligne. Ramené à 52 px en allongeant
   les descriptions de situation — jamais les phrases qui décrivent la méthode
   de David, qui ne sont pas les miennes à étendre.

### Ce qui reste ouvert

Le vocabulaire sécuritaire subsiste ailleurs : **8 occurrences** sur
`/enfants/`, **6** sur `/la-discipline/`, **3** sur `/toulouse/`. Sur les deux
premières c'est le sujet même de la page. Sur les autres, à relire avec l'oreille
que David vient de nous prêter.
