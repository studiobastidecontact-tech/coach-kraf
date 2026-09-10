#!/usr/bin/env python3
"""Éprouve une direction graphique AVANT de la poser sur le site.

Changer de direction, c'est remplacer le bloc `@charte:direction` de
`assets/site.css`. Ce script lit ce bloc, résout les rôles dans les trois
contextes, et mesure chaque paire texte/fond que la feuille emploie
réellement. Il rend un tableau et refuse la direction si une seule paire
tombe sous son seuil.

    python3 _chantier/verifier-direction.py                # la direction en place
    python3 _chantier/verifier-direction.py <fichier.css>  # une candidate

La candidate peut être un fichier ne contenant QUE le bloc de direction :
les contextes sont alors repris de la feuille du site, puisqu'ils ne
changent pas d'une direction à l'autre — c'est tout l'intérêt de la couche.
"""
import re, os, sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = os.path.join(R, 'assets', 'site.css')
BORNES = ('/* @charte:direction-debut */',
          '/* @charte:contextes-debut */',
          '/* @charte:contextes-fin */')


def sans_commentaires(s):
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.S)
    return re.sub(r'data:image/svg\+xml[^"\')]*', '', s)


def decouper(brut):
    """Refuse de découper si un repère manque : `index` lèverait, mais
    `find` rendrait -1 et la tranche lirait le fichier entier sans rien
    signaler. On tranche donc explicitement."""
    p = []
    for b in BORNES:
        if brut.count(b) != 1:
            raise SystemExit(f"✗ la borne « {b} » apparait {brut.count(b)} fois dans la feuille")
        p.append(brut.index(b))
    if not (p[0] < p[1] < p[2]):
        raise SystemExit("✗ les bornes @charte ne sont pas dans l'ordre")
    return brut[p[0]:p[1]], brut[p[1]:p[2]]


def lire_direction(txt):
    return {n: h.upper() for n, h in
            re.findall(r'(--t-[a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})\s*;', sans_commentaires(txt))}


def lire_contextes(txt):
    """Rend {nom_du_contexte: {role: jeton}}. Le contexte PIERRE n'écrase
    que ce qu'il déclare : le reste vient du contexte clair."""
    txt = sans_commentaires(txt)
    blocs = re.findall(r'([^{}]+)\{([^}]*)\}', txt)
    ctx = {}
    for sel, corps in blocs:
        sel = ' '.join(sel.split())
        roles = dict(re.findall(r'(--[a-z0-9-]+):\s*var\((--t-[a-z0-9-]+)\)', corps))
        if not roles:
            continue
        ctx.setdefault(sel, {}).update(roles)
    clair = ctx.get(':root', {})
    hors = ctx.get(':root', {})  # les rôles non contextuels vivent aussi sur :root
    return {
        'clair':   dict(clair),
        'pierre':  {**clair, **ctx.get('.sec--pierre', {})},
        'profond': {**clair, **ctx.get('.hero,footer,.pouce', {})},
    }


def lum(h):
    def c(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * c(r) + 0.7152 * c(g) + 0.0722 * c(b)


def ratio(a, b):
    x, y = lum(a), lum(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


def composer(voile, alpha, fond):
    """La couleur REELLEMENT vue quand un voile translucide est pose sur un fond.

    Ce script ne mesurait que des couleurs opaques — des jetons contre des
    jetons. Or la feuille pose des aplats en `rgba(var(--x-rgb), a)`, et ce que
    l'oeil voit alors n'est AUCUN jeton : c'est un melange. L'ecusson
    « Recommande pour debuter » vivait a 3,91:1 pendant que ce script annoncait
    « aucune paire sous son seuil » — il ne regardait simplement pas la.
    """
    v = [int(voile[i:i + 2], 16) for i in (1, 3, 5)]
    f = [int(fond[i:i + 2], 16) for i in (1, 3, 5)]
    return '#' + ''.join(f'{round(v[i] * alpha + f[i] * (1 - alpha)):02X}' for i in range(3))


# Ce que la feuille pose réellement : un texte, sur un fond, à quel seuil.
# 4,5 = texte courant (WCAG AA) · 3,0 = contour de composant (WCAG 1.4.11)
# 1,2 = un filet doit se voir, ce n'est pas une exigence WCAG mais une
#       exigence de dessin : en dessous, la ligne disparaît.
FONDS = ('--fond', '--fond-2', '--fond-carte', '--survol')
#       --accent-franc ne porte QUE du non-textuel et du grand texte
#       (filets, barres, icônes, chiffres de 30 et 46 px) : son seuil est
#       3,0, et c'est précisément ce qui lui permet d'être plus clair que
#       --accent. Il a été ajouté ici le jour où il est né — cette liste
#       est en dur, donc un rôle qu'on n'y inscrit pas n'est JAMAIS mesuré
#       et le verdict reste vert sans avoir rien regardé.
PAIRES = ([(t, f, 4.5) for t in ('--sur', '--sur-2', '--accent', '--note', '--acquis', '--alerte') for f in FONDS]
          + [(t, f, 3.0) for t in ('--contour', '--focus', '--accent-franc') for f in FONDS]
          + [(t, f, 1.2) for t in ('--filet',) for f in FONDS]
          + [('--accent-sur', '--accent', 4.5)]
          # LE BOUTON D'APPEL, qui ne suit plus le contexte depuis le
          # 2026-09-09 : deux briques différentes pour le même bouton, et
          # William l'a vu du premier coup d'œil. Deux paires, et il faut les
          # DEUX — la première seule laisserait passer un bouton illisible,
          # la seconde seule un bouton invisible sur son fond.
          #
          #   · son LIBELLÉ sur son aplat : 4,5, le seuil du texte courant.
          #     Il valait 3,0 tant que la brique rendait 4,43 avec le blanc —
          #     une dette gagée sur une taille de 19 px, que la barre du pouce
          #     violait à 15 px sans que rien ne le dise (la règle 7 de
          #     coherence.py avait une liste blanche qui couvrait ce cas
          #     précis). La brique a baissé d'un point de clarté ; le seuil
          #     remonte, et la dette n'existe plus.
          #   · sa FORME contre le fond de chaque contexte : 3,0, WCAG 1.4.11.
          #     C'est cette seconde exigence qui a désigné #B85C38 : 3,87:1
          #     sur la pierre claire, 3,85:1 sur le fond profond.
          + [('--accent-aplat-sur', '--accent-aplat', 4.5)]
          + [('--accent-aplat', f, 3.0) for f in ('--fond', '--fond-2')])

# Ce que la feuille pose en TRANSPARENCE, et le texte qui vit dessus.
# Chaque entree : (texte, voile, alpha, fond sous le voile, seuil).
# Releve le 2026-09-10, quand Lighthouse a signale un ecusson a 3,91:1 que ce
# script declarait conforme. L'alpha se lit dans la feuille, il ne se devine
# pas : `grep 'rgba(var(--accent-rgb)' assets/site.css`.
# Le dernier champ borne les CONTEXTES ou la composition existe reellement.
# Sans lui, ce script mesurait un aplat d'accent pose sur le fond profond du
# hero — une combinaison qui n'apparait sur AUCUNE des treize pages, et qui
# faisait crier le garde a 1,90:1 sur du vide. Un garde qui refuse ce qui
# n'existe pas finit contourne, et emporte avec lui les refus qui comptaient.
# L'unique ecusson du site vit dans une `.sec`, en fond clair : verifie par
# `grep -c 'class="ecusson"'` sur les treize pages, un seul, jamais en profond.
COMPOSEES = [
    ('--accent-sur-aplat', '--accent', 0.13, f, 4.5, ('clair', 'pierre'))
    for f in ('--fond', '--fond-2', '--fond-carte', '--survol')
]


def main():
    brut = open(CSS, encoding='utf-8').read()
    dir_txt, ctx_txt = decouper(brut)
    if len(sys.argv) > 1:
        cand = open(sys.argv[1], encoding='utf-8').read()
        dir_txt = decouper(cand)[0] if BORNES[0] in cand else cand
        print(f"Direction candidate : {sys.argv[1]}\n")
    else:
        print("Direction en place dans assets/site.css\n")

    teintes = lire_direction(dir_txt)
    contextes = lire_contextes(ctx_txt)
    if not teintes:
        raise SystemExit("✗ aucune teinte lue — le bloc de direction est vide ou mal formé")

    echecs, mesures, manquants = [], 0, set()
    for nom, roles in contextes.items():
        lignes = []
        for texte, fond, seuil in PAIRES:
            jt, jf = roles.get(texte), roles.get(fond)
            if not jt or not jf:
                manquants.add((nom, texte if not jt else fond)); continue
            ht, hf = teintes.get(jt), teintes.get(jf)
            if not ht or not hf:
                manquants.add((nom, jt if not ht else jf)); continue
            k = ratio(ht, hf); mesures += 1
            ok = k >= seuil
            if not ok:
                echecs.append(f"{nom} : {texte} {ht} sur {fond} {hf} → {k:.2f}:1 (seuil {seuil})")
            lignes.append(f"  {'ok ' if ok else 'ECHEC'} {texte:<14} {ht} sur {fond:<13} {hf}  {k:6.2f}:1  seuil {seuil}")
        # `ou` et non `contextes` : ce nom-la porte deja le dictionnaire des
        # trois contextes, et l'ecraser ici faisait rendre au rapport final
        # « sur 2 contextes » — la longueur du tuple, pas le nombre reel.
        for texte, voile, alpha, fond, seuil, ou in COMPOSEES:
            if nom not in ou:
                continue
            jt, jv, jf = roles.get(texte), roles.get(voile), roles.get(fond)
            if not (jt and jv and jf):
                manquants.add((nom, texte if not jt else (voile if not jv else fond))); continue
            ht, hv, hf = teintes.get(jt), teintes.get(jv), teintes.get(jf)
            if not (ht and hv and hf):
                manquants.add((nom, jt if not ht else (jv if not hv else jf))); continue
            compose = composer(hv, alpha, hf)
            k = ratio(ht, compose); mesures += 1
            ok = k >= seuil
            if not ok:
                echecs.append(f"{nom} : {texte} {ht} sur {voile} a {alpha:.0%} pose sur {fond} = {compose} → {k:.2f}:1 (seuil {seuil})")
            lignes.append(f"  {'ok ' if ok else 'ECHEC'} {texte:<14} {ht} sur {voile}@{alpha:.0%}/{fond:<9} {compose}  {k:6.2f}:1  seuil {seuil}")

        print(f"── contexte {nom.upper()} ──")
        print('\n'.join(lignes)); print()

    for c, j in sorted(manquants):
        echecs.append(f"{c} : {j} n'est defini nulle part")

    print(f"{mesures} paires mesurees sur {len(contextes)} contextes.")
    if echecs:
        print("\n" + "\n".join("  ✗ " + e for e in echecs))
        print(f"\n{len(echecs)} paire(s) sous leur seuil — direction REFUSEE.")
        return 1
    print("Aucune paire sous son seuil — direction VALIDE.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
