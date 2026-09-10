---
version: v2
kind: charte
status: appliquée
supersedes: charte.html (Bleu de garde)
date: 2026-09-09
---

# Trois directions de couleur

> **Tranché par William le 09/09 : direction 1, Terre de Toulouse. Appliquée
> le jour même.** Les valeurs finales et les contrastes mesurés sont dans
> `charte.html`. Les deux autres directions restent ici, écrites, au cas où la
> conversation se rouvre.

> Écrit après une réaction de William : *« je ne suis pas convaincu par les
> choix de couleur »*. Réaction fondée — la mesure ci-dessous le dit crûment.

## Le défaut de la palette actuelle, mesuré

Le bleu `#0E1A2B` que j'ai choisi est à une **distance de 3,3** du `slate-900`
de Tailwind. C'est-à-dire : le même. Les autres bleus sombres du web courant
(Stripe, GitHub, Bootstrap, Notion) sont tous à moins de 25.

**Le problème n'est pas qu'il soit laid — il est irréprochable. Le problème est
qu'il n'appartient à personne.** J'ai pris le contrepied du noir/rouge en
allant vers le froid institutionnel, et le froid institutionnel est le réglage
par défaut de tout site sérieux depuis 2018.

Deux conséquences que je n'avais pas assez pesées :

- **Le bleu marine est la couleur de l'administration** — police, gendarmerie,
  assurance, banque. Pour un instructeur à mention forces de l'ordre ce n'était
  pas absurde, mais ça
  parle de l'institution, pas de l'homme qui vient chez vous.
- **`#F0B429` est un jaune de signalisation.** Panneau, gilet, bandeau
  d'alerte. Sur un site qui parle de sécurité, il évoque le danger autant que
  la protection.

**L'argument central du site est « je me déplace chez vous ».** C'est une
palette d'intérieur qu'il faut, pas une palette de dojo ni de guichet.

---

## Direction 1 — Terre de Toulouse

**Fond `#2A1A14` brique brûlée · chaux `#F4EDE4` · ambre `#E9A03C`**

Toulouse est la ville rose. La brique foraine est *littéralement* la couleur du
lieu où il exerce. Personne d'autre ne l'a, et elle ancre le site
géographiquement — ce qui sert aussi le référencement local, où l'on se bat
sur « krav maga toulouse ».

La brique est le **mur**, pas le panneau : elle devient le fond, et l'ambre
chaud marque l'action. C'est ce qui évite de retomber sur le rouge qu'on
voulait fuir.

```
┌────────────────────────────────────────────────────────────┐
│ ▓▓▓▓▓ #2A1A14 — brique brûlée, presque noir mais chaud     │
│                                                            │
│  ── TOULOUSE · SAINT-SULPICE-LA-POINTE      (ambre #E9A03C)│
│                                                            │
│  Vous n'avez pas                            crème #F4EDE4  │
│  à subir.                                   ambre #E9A03C  │
│                                                            │
│  Coach particulier de Krav Maga…            estompé #C0A997│
│                                                            │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │▓▓ 07 81 68 60 84 ▓▓▓▓│  │  Envoyer un SMS      │        │
│  │  ambre, texte brique │  │  contour crème       │        │
│  └──────────────────────┘  └──────────────────────┘        │
│                                                            │
│  ● Premier cours offert. Un SMS suffit.                    │
├────────────────────────────────────────────────────────────┤
│ ░░░ #F4EDE4 — chaux. Le blanc du sud, pas le blanc d'écran │
│                                                            │
│   Vous êtes probablement ici          encre #2A1A14        │
│   ┌───────────┐ ┌───────────┐ ┌───────────┐                │
│   │ carte     │ │ carte     │ │ carte     │  #E8DDCF       │
│   └───────────┘ └───────────┘ └───────────┘                │
└────────────────────────────────────────────────────────────┘
```

| | | contraste |
|---|---|---|
| crème sur brique | `#F4EDE4` / `#2A1A14` | **14,39:1** AAA |
| ambre sur brique | `#E9A03C` / `#2A1A14` | **7,61:1** AAA |
| bouton : brique sur ambre | `#2A1A14` / `#E9A03C` | **7,61:1** AAA |
| secondaire sur chaux | `#6B5648` / `#F4EDE4` | **5,93:1** AA |

**Ce qu'elle dit** : le sud, la terre battue, l'extérieur, la chaleur.
**Le risque** : sans la fermeté typographique actuelle (Archivo 800, tracking
serré), elle glisserait vers le studio de yoga. La structure doit rester dure.

---

## Direction 2 — Vert de garde

**Fond `#12261F` sapin profond · os `#F1F0E8` · laiton `#D9A441`**

Le vert est **la couleur que personne n'utilise en sport de combat**, et c'est
précisément pourquoi elle serait mémorable. Elle dit le calme et le dehors —
or ses cours se donnent en extérieur, et son message est « la violence est la
dernière option ».

Attention au piège : ce n'est **pas** le kaki militaire, qui est le cliché du
secteur. C'est un vert forêt, profond et froid-chaud, tirant vers le sapin.

```
┌────────────────────────────────────────────────────────────┐
│ ▓▓▓▓▓ #12261F — sapin profond                              │
│                                                            │
│  ── TOULOUSE · SAINT-SULPICE-LA-POINTE     (laiton #D9A441)│
│                                                            │
│  Vous n'avez pas                             os #F1F0E8    │
│  à subir.                                   laiton #D9A441 │
│                                                            │
│  Coach particulier de Krav Maga…          estompé #9BB0A4  │
│                                                            │
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │▓▓ 07 81 68 60 84 ▓▓▓▓│  │  Envoyer un SMS      │        │
│  │  laiton, texte sapin │  │  contour os          │        │
│  └──────────────────────┘  └──────────────────────┘        │
├────────────────────────────────────────────────────────────┤
│ ░░░ #F1F0E8 — os. Plus chaud qu'un blanc, moins qu'un beige│
└────────────────────────────────────────────────────────────┘
```

| | | contraste |
|---|---|---|
| os sur sapin | `#F1F0E8` / `#12261F` | **13,89:1** AAA |
| laiton sur sapin | `#D9A441` / `#12261F` | **7,06:1** AAA |
| secondaire sur os | `#4F5B52` / `#F1F0E8` | **6,23:1** AA |

**Ce qu'elle dit** : la maîtrise, le dehors, le calme.
**Le risque** : à un cheveu du kaki. Si la teinte dérive vers le jaune, on
retombe sur le treillis — exactement ce que la charte voulait éviter.

---

## Direction 3 — Ardoise chaude

**Fond `#211F1D` gris-brun · calcaire `#F3F1EC` · ambre `#E09A2B`**

La plus proche de l'existant : même logique, même contraste, juste **débarrassée
du bleu**. Le fond passe d'un marine identifiable à un gris-brun neutre, chaud,
sans marque. C'est la direction du risque minimal.

```
┌────────────────────────────────────────────────────────────┐
│ ▓▓▓▓▓ #211F1D — gris-brun. Ni bleu, ni noir : sans marque  │
│                                                            │
│  ── TOULOUSE · SAINT-SULPICE-LA-POINTE      (ambre #E09A2B)│
│  Vous n'avez pas / à subir.        calcaire #F3F1EC + ambre│
│  ┌──────────────────────┐  ┌──────────────────────┐        │
│  │▓▓ 07 81 68 60 84 ▓▓▓▓│  │  Envoyer un SMS      │        │
│  └──────────────────────┘  └──────────────────────┘        │
├────────────────────────────────────────────────────────────┤
│ ░░░ #F3F1EC — calcaire                                     │
└────────────────────────────────────────────────────────────┘
```

| | | contraste |
|---|---|---|
| calcaire sur ardoise | `#F3F1EC` / `#211F1D` | **14,55:1** AAA |
| ambre sur ardoise | `#E09A2B` / `#211F1D` | **6,90:1** AA |
| secondaire sur calcaire | `#5C5651` / `#F3F1EC` | **6,40:1** AA |

**Ce qu'elle dit** : rien de particulier — et c'est son défaut comme sa force.
Neutre, chaude, sans connotation.
**Le risque** : on corrige le symptôme (le bleu générique) sans gagner
d'identité. À six mois, on aura la même conversation.

---

## Ce que ça coûte à changer

**Une heure, quelle que soit la direction.** Les couleurs sont toutes passées
en jetons ce matin — il n'en reste aucune écrite en dur, transparences
comprises. Changer de palette, c'est réécrire quatorze valeurs dans `:root`
puis mesurer les contrastes sur les 728 textes du site.

La photo du héros — un cours au coucher du soleil, dominante orangée — s'accorde
**mieux** avec les directions 1 et 3 qu'avec le bleu actuel, où elle jure
légèrement.

## Ma recommandation

**La direction 1.** Parce qu'elle est la seule qui dise *où* il exerce, et que
c'est le seul avantage qu'un site de coach local puisse avoir sur un site de
coach générique. La brique de Toulouse n'est pas une idée de designer : c'est
ce que les gens voient par la fenêtre.

**Le cas où la 2 gagne** : si l'axe qu'on veut tenir est « la violence est la
dernière option » plutôt que l'ancrage local. Le vert porte cette idée mieux
que n'importe quelle autre couleur.

**Le cas où la 3 gagne** : si l'inconfort porte sur le bleu lui-même et pas sur
le manque d'identité. Elle règle ça en une heure et sans débat.
