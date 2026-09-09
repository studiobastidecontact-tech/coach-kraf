---
version: V1
kind: ui
status: valide
date: 2026-09-09
sujet: Page d'accueil — structure complète et direction visuelle
supersedes: null
---

# Page d'accueil — V1

Une seule page, comme aujourd'hui. Onze blocs, dans cet ordre.

## Le principe

La personne qui arrive **a peur de quelque chose**. Trois gestes, dans l'ordre :
la reconnaître, prouver la compétence, rendre le contact immédiat.

Tout le reste en découle — y compris le fait que le téléphone est visible dès
la première seconde, et que le formulaire arrive en dernier recours, pas en
premier canal.

## Palette

```
  Fond           #101216   anthracite froid, pas noir pur
  Surface        #181b21   cartes, bandes alternées
  Bordure        #262a32
  Texte          #f2f2f0
  Texte second   #a8a9ad   contraste 8:1  (l'actuel : 2,95:1)
  Accent         #d4622e   orange brûlé — contraste 4,9:1  (le rouge actuel : 3,2:1)
  Valeur         #c9a227   or mat, réservé aux certifications
```

L'orange brûlé remplace le rouge sang parce qu'il tient le contraste et qu'il
sort du cliché du secteur — tous les sites de sport de combat sont noir et
rouge. Le rouge franc reste disponible pour une seule chose : l'urgence.

## Typographie

Une grotesque unique, large amplitude de graisse. Titres très gros et très
serrés, corps de texte à 17 px minimum. Aucune fantaisie : la lisibilité est
la première preuve de sérieux.

---

## 1 · Header

```
┌──────────────────────────────────────────────────────────────────────────┐
│  [logo]  COACH KRAV        Cours  Coach  Tarifs  Contact   07 81 68 60 84│
│                                                            ▔▔▔▔▔▔▔▔▔▔▔▔▔ │
└──────────────────────────────────────────────────────────────────────────┘
```

Le numéro **est** le bouton principal, à droite, sur fond accent. Il ne
disparaît jamais — ni au défilement, ni sur mobile.

Mobile : le menu devient un tiroir, mais **le numéro reste dans la barre**.
C'est le défaut numéro un du site actuel, corrigé ici par construction.

```
┌────────────────────────────────┐
│ [logo]        📞 07 81 68 60 84  ☰ │
└────────────────────────────────┘
```

## 2 · Hero

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│   ── TOULOUSE · SAINT-SULPICE-LA-POINTE                                   │
│                                                                          │
│   Vous n'avez pas                                                        │
│   à subir.                            [ photo pleine hauteur,            │
│                                         dégradé vers la gauche ]         │
│   Coach particulier de Krav Maga et de self-défense.                     │
│   Je me déplace chez vous, en extérieur ou en salle.                     │
│   Des gestes simples, qui fonctionnent sous stress.                      │
│                                                                          │
│   ┌────────────────────────┐  ┌──────────────────────┐                   │
│   │  📞  07 81 68 60 84     │  │  ✉  Envoyer un SMS   │                   │
│   └────────────────────────┘  └──────────────────────┘                   │
│      Réponse dans la journée · premier échange sans engagement           │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**« Vous n'avez pas à subir »** remplace « Apprenez à vous défendre. Pour de
vrai. » — c'est la reformulation de l'accroche de l'ancien site (« l'insécurité
grandissante… prendre votre destin en main »), débarrassée du ton anxiogène.

Le hero **ne fait plus 100 vh**. Sur mobile, le site actuel ouvre sur 840 px de
photo sombre et rien d'autre : ici le titre et les deux boutons sont visibles
immédiatement, sur toutes les tailles.

Les deux boutons sont **un appel et un SMS**. Pas « Réserver un cours » qui
renvoie vers un formulaire trois écrans plus bas.

## 3 · Preuve

```
├──────────────────────────────────────────────────────────────────────────┤
│   G5 KRAV MAGA  ·  MENTION MILITAIRE ET FORCES DE L'ORDRE  ·  15 ANS      │
│   ·  À DOMICILE, EN EXTÉRIEUR OU EN SALLE  ·  TOULOUSE ET TARN            │
├──────────────────────────────────────────────────────────────────────────┤
```

Une bande fine, pas un bandeau rouge criard. Elle remplace les cinq chiffres
actuels — dont « 3 zones », qui n'est pas une statistique, et « 500+ élèves »,
qu'on ne peut pas prouver.

## 4 · Situations

```
   ── SITUATIONS
   Vous êtes probablement ici

┌────────────────────┐ ┌────────────────────┐ ┌────────────────────┐
│                    │ │                    │ │                    │
│  Vous, au          │ │  Votre enfant,     │ │  Votre équipe      │
│  quotidien         │ │  à l'école         │ │                    │
│                    │ │                    │ │                    │
│  Des incivilités   │ │  Harcèlement,      │ │  Personnel exposé  │
│  au travail. Un    │ │  racket. Il rentre │ │  au public,        │
│  trajet le soir    │ │  la tête basse et  │ │  déplacements      │
│  qui pèse. L'idée  │ │  ne dit rien.      │ │  isolés, gestion   │
│  de ne pas savoir  │ │                    │ │  d'un client       │
│  réagir.           │ │  Quelques séances  │ │  agressif.         │
│                    │ │  suffisent souvent │ │                    │
│  Apprendre à se    │ │  à ce qu'il cesse  │ │  Séminaires        │
│  dégager, à tenir  │ │  d'être une cible. │ │  entreprises et    │
│  la distance, à    │ │                    │ │  administrations.  │
│  ne plus figer.    │ │                    │ │                    │
│                    │ │                    │ │                    │
│  → Cours           │ │  → Cours enfant    │ │  → Devis           │
│    particulier     │ │                    │ │                    │
└────────────────────┘ └────────────────────┘ └────────────────────┘
```

C'est le bloc que le site actuel n'a pas, et c'est celui qui vend. Il vient
de l'ancienne page Contact — la meilleure page des deux sites.

La colonne du milieu ouvre un marché entier : les parents. Formulation revue —
on ne promet plus de rendre l'enfant « populaire », on promet qu'il cesse
d'être une cible.

## 5 · Formules

```
   ── FORMULES
   Deux façons de travailler

┌─────────────────────────────────────┐ ┌─────────────────────────────────┐
│ [photo]                             │ │ [photo]                         │
│                                     │ │                                 │
│ Cours technique                     │ │ Entraînement au combat          │
│                                     │ │                                 │
│ Les gestes pour faire face à tous   │ │ Combat souple. Les réflexes,    │
│ types d'agressions : se dégager     │ │ la résistance physique, les     │
│ d'une saisie, parer une frappe,     │ │ capacités musculaires.          │
│ porter un coup qui permet de        │ │                                 │
│ partir.                             │ │ Pour ancrer ce que la technique │
│                                     │ │ a appris.                       │
└─────────────────────────────────────┘ └─────────────────────────────────┘
```

Le découpage de l'ancien site, plus clair que les trois blocs actuels (dont
un, « Urban Training », illustré par des baskets de running).

## 6 · Bienfaits

```
   ── BIENFAITS
   Ce qui change, séance après séance

   01 Tonicité            Un renforcement musculaire complet.
   02 Souplesse           Gym douce et récupération, conscience du corps.
   03 Équilibre           Le tonus des jambes, la confiance dans les appuis.
   04 Coordination        Le mouvement des poings et des jambes, ensemble.
   05 Cardio              Une intensité qui construit du souffle.
   06 Mémoire             Les enchaînements codifiés entraînent la mémoire.
   07 Stress              L'entraînement régulier évacue le stress du quotidien.
```

Les sept de l'ancien site, contre quatre formules vagues aujourd'hui. Ils
importent moins pour leur nombre que pour ce qu'ils ouvrent : « gym douce »,
« équilibre », « mémoire » parlent à des gens qui ne veulent pas se battre.

## 7 · Coach

```
   ── LE COACH

┌───────────────────────────┐    Développement personnel, sport et
│                           │    pédagogie ont toujours été mes plus
│   [ photo de groupe,      │    grandes passions…
│     cours en extérieur,   │
│     fin de journée ]      │    « J'ai appris à être plus tolérant,
│                           │    plus apte à négocier les situations
│                           │    pour les résoudre par la non-violence
│   2000 × 1500 — la seule  │    et la parole. Car le plus difficile
│   vraie photo dont on     │    est de lutter contre soi. »
│   dispose                 │
└───────────────────────────┘    Je vous propose de vous transmettre ce
                                 savoir-être pour profiter au maximum de
                                 votre savoir-vivre.

   ┌──────────────────┬──────────────────┬──────────────────┐
   │ Instructeur      │ G5 Krav Maga     │ Ceintures noires │
   │ Krav Maga        │ Grade d'expert,  │ Karaté · Kudo    │
   │ mention militaire│ 10ᵉ niveau de    │                  │
   │ et forces de     │ l'échelle intl.  │                  │
   │ l'ordre          │                  │                  │
   ├──────────────────┼──────────────────┼──────────────────┤
   │ Savate d'argent  │ Instructeur      │ DU préparateur   │
   │ Monitorat savate │ militaire C4     │ physique         │
   │ et bâton défense │ Combat rapproché │                  │
   ├──────────────────┴──────────────────┴──────────────────┤
   │ CQP MAM — Métiers des arts martiaux                    │
   └────────────────────────────────────────────────────────┘
```

Les certifications remontent : c'est le meilleur actif du site, et il est
aujourd'hui enterré au milieu de la page.

Le G5 est **corrigé** : « grade d'expert, dixième niveau de l'échelle
internationale ». Il se vend très bien sans l'affirmation fausse qu'il serait
le plus élevé de la discipline.

## 8 · Discipline

```
   ── LA DISCIPLINE
   Le Krav Maga sacrifie l'esthétique à l'efficacité

   En hébreu, « combat rapproché ». Créé dans les années 40 par Imi
   Lichtenfeld, adopté par l'armée et la police israéliennes, enseigné
   dans de nombreuses unités de police aux États-Unis. Plus de 70 ans
   d'histoire.

   Il ne s'agit pas d'apprendre un programme figé qui correspondrait à
   des attaques codifiées. Il s'agit de savoir s'adapter.

   ┌──────────────┬──────────────┬──────────────┬──────────────┐
   │  01          │  02          │  03          │  04          │
   │  Simplicité  │  Rapidité    │  Efficacité  │  Maîtrise    │
   │              │              │              │  de soi      │
   └──────────────┴──────────────┴──────────────┴──────────────┘
```

Contenu de l'ancien site, supprimé par le site actuel. Crédibilité gratuite,
et exactement ce que les moteurs font remonter sur « krav maga toulouse ».

## 9 · Tarifs

```
   ── TARIFS
   Une séance, un prix. Sans abonnement.

   ┌────────────────────────────────┬─────────┬────────────────────────┐
   │  Cours particulier             │   50 €  │  Recommandé pour       │
   │  Une personne, suivi complet   │         │  débuter               │
   ├────────────────────────────────┼─────────┼────────────────────────┤
   │  À deux                        │   30 €  │  par personne          │
   ├────────────────────────────────┼─────────┼────────────────────────┤
   │  Petit groupe · 3 à 4          │   22 €  │  par personne          │
   ├────────────────────────────────┼─────────┼────────────────────────┤
   │  Groupe · 5 et plus            │   70 €  │  la séance             │
   └────────────────────────────────┴─────────┴────────────────────────┘
                     ▲ grille de l'ancien site — à trancher

   ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────┐
   │ Stage à thème        │ │ Entreprises et       │ │ Tarif réduit     │
   │ à la demande         │ │ administrations      │ │ pour les         │
   │                      │ │ Séminaires sur       │ │ personnes en     │
   │                      │ │ mesure               │ │ difficulté       │
   └──────────────────────┘ └──────────────────────┘ └──────────────────┘
```

Les trois cartes du bas sont les lignes perdues de l'ancien site. La dernière
en dit plus sur le coach que toute la section « Le coach ».

Les packs à crédits sont **retirés de la V1** : leur économie ne tient pas en
l'état (5 cours collectifs pour 50 € contre 18 à 25 € l'unité) et le système de
crédits n'est défini nulle part.

## 10 · Contact

```
   ── CONTACT
   Le plus simple : un appel ou un SMS

   ┌────────────────────┐ ┌────────────────────┐ ┌────────────────────┐
   │        📞          │ │        ✉           │ │        💬          │
   │   07 81 68 60 84   │ │   Envoyer un SMS   │ │     WhatsApp       │
   │      Appeler       │ │  Il rappelle dès   │ │                    │
   │                    │ │  qu'il est libre   │ │                    │
   └────────────────────┘ └────────────────────┘ └────────────────────┘

   Ou laissez-moi un message :

   ┌──────────────────────────┐ ┌──────────────────────────┐
   │ Nom                      │ │ Téléphone                │
   └──────────────────────────┘ └──────────────────────────┘
   ┌──────────────────────────┐ ┌──────────────────────────┐
   │ Pour qui ?          ▾    │ │ Où ?                ▾    │
   │  Moi / mon enfant /      │ │  Toulouse / Saint-       │
   │  mon équipe              │ │  Sulpice / autre         │
   └──────────────────────────┘ └──────────────────────────┘
   ┌─────────────────────────────────────────────────────────┐
   │ Votre situation, vos disponibilités                     │
   └─────────────────────────────────────────────────────────┘
   ☐ J'accepte que ces informations servent à me répondre.
   ┌─────────────────────────────────────────────────────────┐
   │                    ENVOYER                              │
   └─────────────────────────────────────────────────────────┘
```

Trois canaux directs **avant** le formulaire. Le champ « Pour qui ? » reprend
les trois situations du bloc 4 — David sait immédiatement à qui il répond.

Chaque `<label>` est lié à son champ par `for`/`id` : les cinq erreurs relevées
par Chrome sur le site actuel disparaissent par construction.

## 11 · Footer

```
├──────────────────────────────────────────────────────────────────────────┤
│  [logo]                    ZONES                     CONTACT             │
│  Coach particulier de      Toulouse et agglomération  07 81 68 60 84     │
│  Krav Maga et self-        Saint-Sulpice-la-Pointe    contact@coach-     │
│  défense.                  Déplacements à domicile    krav.fr            │
│                                                                          │
│  © 2026 coach-krav.fr    Mentions légales · Confidentialité               │
└──────────────────────────────────────────────────────────────────────────┘
```

## Les manques de la V1

Cinq blocs sont dessinés mais attendent une matière qui n'existe pas encore —
témoignages, photos, mentions légales complètes. L'inventaire est tenu dans le
dépôt de chantier, qui est privé.

> *Deux passages de ce croquis ont été retirés le 2026-09-09, quand le pilotage
> a quitté ce dépôt public. Le dessin, lui, n'a pas bougé.*

## Ce que la V1 corrige, mesurable

| | Aujourd'hui | V1 visée |
|---|---|---|
| Poids de la page | 1,55 Mo (742 Ko gzip) | < 60 Ko + images |
| Logo | 3,71 Mo, 6250 px | < 15 Ko, 240 px |
| Favicon | 736 Ko × 2 en base64 | < 5 Ko, fichier séparé |
| Navigation mobile | aucune | menu + téléphone permanent |
| Contraste minimum | 2,95:1 | ≥ 4,5:1 partout |
| Images cassées | 1 | 0 |
| Sections sans CSS | 1 | 0 |
| Canaux de contact | 1 | 4 |
