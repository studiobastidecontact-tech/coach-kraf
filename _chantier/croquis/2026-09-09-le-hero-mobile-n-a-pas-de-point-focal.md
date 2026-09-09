---
version: V4
kind: ui
status: appliquée
---

# Le hero mobile n'a pas de point focal

Sur un téléphone, le hero fait 812 px et son contenu en occupe 545. La photo
est derrière le texte, noyée sous un voile latéral pensé pour un écran large :
on devine des silhouettes, rien de plus. **Un hero doit avoir un élément qu'on
retient ; celui-ci n'en a aucun.**

## Ce qui remplit les 545 px

| bloc | px | verdict |
|---|---|---|
| intitulé « Toulouse · Saint-Sulpice-la-Pointe » | 52 | passe sur 2 lignes à cause de l'interlettrage |
| titre | 89 | garde |
| accroche | 130 | 5 lignes, trop long pour un hero |
| deux boutons | 143 | garde |
| « Premier cours offert… » | 79 | **le meilleur argument du site** |
| « Ensuite 50 €… » | 52 | dit la même chose que le lien tarifs |

Les deux dernières lignes disent trois choses en 131 px, dont deux qui se
répètent ailleurs sur la page.

## Avant / après

```
   AVANT — 812 px, la photo est du bruit          APRÈS — 800 px, elle est un sujet

  ┌────────────────────────────────┐            ┌────────────────────────────────┐
  │ T O U L O U S E  ·  S A I N T -│            │ TOULOUSE · SAINT-SULPICE       │  1 ligne
  │ S U L P I C E - L A - P O I N T│            │                                │
  │                                │            │ Vous n'avez pas                │
  │ Vous n'avez pas                │            │ à subir.                       │
  │ à subir.                       │            │                                │
  │                                │            │ Coach particulier de Krav Maga │
  │ Coach particulier de Krav Maga │            │ et de self-défense. Je me      │
  │ et de self-défense. Je me      │            │ déplace chez vous.             │
  │ déplace chez vous, en extérieur│            │                                │
  │ ou en salle. Des gestes simples│            │ ┌────────────────────────────┐ │
  │ qui fonctionnent sous stress.  │            │ │      07 81 68 60 84        │ │
  │ Pour adultes, enfants, équipes.│            │ └────────────────────────────┘ │
  │                                │            │ ┌────────────────────────────┐ │
  │ ┌────────────────────────────┐ │            │ │      Envoyer un SMS        │ │
  │ │      07 81 68 60 84        │ │            │ └────────────────────────────┘ │
  │ └────────────────────────────┘ │            │   Comment ça se passe  →       │  ← le geste doux
  │ ┌────────────────────────────┐ │            │                                │
  │ │      Envoyer un SMS        │ │            │ ● Premier cours offert.        │
  │ └────────────────────────────┘ │            │   Ensuite 50 €, dès 15 € à     │
  │                                │            │   plusieurs. Voir les tarifs   │
  │ ● Premier cours offert. Un SMS │            │                                │
  │   suffit, je rappelle dès que  │            ├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤
  │   je suis libre. Vous préférez │            │▓▓▓▓▓▓▓ la photo respire ▓▓▓▓▓▓▓│
  │   écrire ? c'est par ici.      │            │▓▓▓▓ 190 px, voile dégradé ▓▓▓▓▓│  ← le point focal
  │                                │            │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
  │   Ensuite 50 € la séance seul, │            └────────────────────────────────┘
  │   dès 15 € par personne à      │
  │   plusieurs. Voir les tarifs   │              La photo n'est plus derrière le
  │                                │              texte : elle a sa bande, et le
  │   [ photo invisible dessous ]  │              voile passe de 94 % en haut à
  └────────────────────────────────┘              25 % en bas.
```

## Les cinq gestes

1. **L'intitulé tient sur une ligne** — l'interlettrage de 0,2 em le faisait
   passer sur deux. Il descend à 0,08 em sous 760 px. 52 → 30 px.
2. **L'accroche perd sa seconde moitié.** « en extérieur ou en salle, des gestes
   simples qui fonctionnent sous stress, pour adultes, enfants et équipes » est
   redit trois fois plus bas sur la page. 130 → 90 px.
3. **Les deux notes fusionnent.** « Un SMS suffit, je rappelle dès que je suis
   libre » double la section contact ; « Vous préférez écrire ? c'est par ici »
   double le bouton SMS. Reste ce qui ne se dit nulle part ailleurs : le
   premier cours offert, et le prix. 131 → 78 px.
4. **Un troisième geste, plus doux.** Deux boutons demandent de contacter un
   inconnu. Quelqu'un qui hésite veut d'abord comprendre : « Comment ça se
   passe → » l'amène au déroulé, sans engagement.
5. **La photo reçoit 190 px à elle**, et le voile devient vertical sur
   téléphone : opaque sous le texte, transparent sous la bande.

Sur écran large, rien ne change : le voile latéral y fonctionne déjà.
