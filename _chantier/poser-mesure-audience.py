#!/usr/bin/env python3
"""Pose ou retire la mesure d'audience sur toutes les pages du site.

POURQUOI UN SCRIPT PLUTOT QU'UNE EDITION A LA MAIN. Le beacon doit etre sur
TOUTES les pages, sinon la mesure est partielle et personne ne s'en apercoit :
un compteur qui ignore la moitie du site rend des chiffres plausibles et faux.
Le site compte treize pages, et il en gagnera d'autres.

Il n'ecrit rien tant qu'on ne lui donne pas de jeton : poser un script vide
reviendrait a charger du code mort et a faire mentir la page confidentialite,
qui affirme aujourd'hui qu'aucune mesure n'est active.

    python3 _chantier/poser-mesure-audience.py --cloudflare <TOKEN>
    python3 _chantier/poser-mesure-audience.py --google <CODE>
    python3 _chantier/poser-mesure-audience.py --etat
    python3 _chantier/poser-mesure-audience.py --retirer

Le jeton Cloudflare se lit sur dash.cloudflare.com > Web Analytics > le site >
« Manage site » : c'est le `token` de l'extrait propose.

Le code Google se lit sur search.google.com/search-console, en ajoutant une
propriete « Prefixe d'URL » puis en choisissant la methode « Balise HTML » :
c'est le `content` de la balise proposee. Cette verification-la ne concerne que
l'accueil — Google n'en demande pas plus.
"""
import glob
import os
import re
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARQUE_CF = 'static.cloudflareinsights.com'
MARQUE_GG = 'google-site-verification'


def pages():
    return sorted(glob.glob(f'{R}/*.html') + glob.glob(f'{R}/*/index.html'))


def etat():
    cf = gg = 0
    total = 0
    for p in pages():
        total += 1
        s = open(p, encoding='utf-8').read()
        if MARQUE_CF in s:
            cf += 1
        if MARQUE_GG in s:
            gg += 1
    print(f'  {total} page(s)')
    print(f'  Cloudflare Web Analytics : {cf}/{total}'
          + ('' if cf in (0, total) else '  ← MESURE PARTIELLE, les chiffres seront faux'))
    print(f'  verification Google      : {gg}/{total}'
          + ('  (l\'accueil suffit)' if gg == 1 else ''))
    return 0 if cf in (0, total) else 1


def poser_cloudflare(token):
    if not re.fullmatch(r'[0-9a-f]{32}', token or ''):
        print('  Le jeton Cloudflare est une suite de 32 caracteres hexadecimaux.')
        print(f'  Recu : {token!r} ({len(token or "")} caracteres) — rien n\'a ete ecrit.')
        return 1
    bloc = ('<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
            f'data-cf-beacon=\'{{"token": "{token}"}}\'></script>\n')
    n = 0
    for p in pages():
        s = open(p, encoding='utf-8').read()
        if MARQUE_CF in s:
            continue
        if '</body>' not in s:
            print(f'  PAS DE </body> : {p[len(R)+1:]}')
            continue
        open(p, 'w', encoding='utf-8').write(s.replace('</body>', bloc + '</body>', 1))
        n += 1
    print(f'  beacon pose sur {n} page(s)')
    print('  → METTRE A JOUR /mentions/ : la section « Mesure d\'audience » affirme')
    print('    aujourd\'hui qu\'aucune mesure n\'est active. Elle deviendrait fausse.')
    return 0


def poser_google(code):
    if not code or len(code) < 20:
        print(f'  Le code de verification Google fait au moins 20 caracteres. '
              f'Recu : {code!r} — rien n\'a ete ecrit.')
        return 1
    p = os.path.join(R, 'index.html')
    s = open(p, encoding='utf-8').read()
    if MARQUE_GG in s:
        print('  une balise de verification est deja posee sur l\'accueil')
        return 0
    balise = f'<meta name="google-site-verification" content="{code}">\n'
    # Apres <head>, pas avant </head> : Google lit le debut du document, et une
    # balise posee tres bas a deja fait echouer des verifications.
    s = re.sub(r'(<head>\s*\n)', r'\1' + balise, s, count=1)
    open(p, 'w', encoding='utf-8').write(s)
    print('  balise de verification posee sur l\'accueil')
    print('  → publier, puis cliquer « Valider » dans Search Console')
    return 0


def retirer():
    n = 0
    for p in pages():
        s = open(p, encoding='utf-8').read()
        av = s
        s = re.sub(r'[ \t]*<script defer src="https://static\.cloudflareinsights\.com[^\n]*\n', '', s)
        s = re.sub(r'[ \t]*<meta name="google-site-verification"[^\n]*\n', '', s)
        if s != av:
            open(p, 'w', encoding='utf-8').write(s)
            n += 1
    print(f'  retire de {n} page(s)')
    print('  → /mentions/ doit redire qu\'aucune mesure n\'est active')
    return 0


def main():
    a = sys.argv[1:]
    if not a or '--etat' in a:
        return etat()
    if a[0] == '--cloudflare':
        return poser_cloudflare(a[1] if len(a) > 1 else None)
    if a[0] == '--google':
        return poser_google(a[1] if len(a) > 1 else None)
    if a[0] == '--retirer':
        return retirer()
    print(__doc__)
    return 1


if __name__ == '__main__':
    sys.exit(main())
