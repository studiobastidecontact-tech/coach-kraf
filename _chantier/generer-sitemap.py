#!/usr/bin/env python3
"""Regenere sitemap.xml depuis les pages du depot et leur dernier commit.

POURQUOI CE SCRIPT EXISTE. Le sitemap etait ecrit a la main. Le 2026-09-10, ses
onze `lastmod` annoncaient le 9 septembre alors que les onze pages avaient ete
modifiees le 10 : une journee entiere de travail que les moteurs n'avaient
aucune raison de venir relire. Un fichier tenu a la main se perime le jour ou
l'on oublie de le tenir, et personne ne s'en apercoit — rien ne casse.

La date vient de `git log`, pas de l'horodatage du fichier : un `git clone`
donne a tous les fichiers la date du clone, et une page jamais touchee
paraitrait alors fraiche.

Une page nouvelle entre ici toute seule. Sa PRIORITE, elle, se declare dans
PRIORITES : c'est un jugement editorial, pas un fait mesurable.

    python3 _chantier/generer-sitemap.py           ecrit sitemap.xml
    python3 _chantier/generer-sitemap.py --verifier  rend 1 si perime
"""
import datetime
import glob
import os
import re
import subprocess
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://coach-krav.fr'

# Ce qui ne s'indexe pas : les pages en noindex le declarent elles-memes, on ne
# tient pas une seconde liste qui pourrait diverger de la premiere.
PRIORITES = {
    '/': '1.0',
    '/femmes/': '0.9',
    '/enfants/': '0.9',
    '/toulouse/': '0.9',
    '/saint-sulpice/': '0.9',
    '/le-coach/': '0.8',
    '/la-discipline/': '0.8',
    '/coach-sportif/': '0.8',
    '/arts-martiaux/': '0.8',
    '/boxe-et-mma/': '0.8',
    '/mentions/': '0.3',
}
DEFAUT = '0.7'


def derniere_date(chemin_relatif):
    """Date de publication de ce fichier, au format AAAA-MM-JJ.

    PIEGE TEMPOREL, et il rendrait ce script inutilisable au pre-commit. Une
    page qu'on s'apprete a commiter n'a pas encore sa date : `git log` rendrait
    celle du commit PRECEDENT, et le sitemap serait perpetuellement en retard
    d'un commit — le garde refuserait a chaque fois, sans qu'aucune
    regeneration ne le satisfasse.

    Une page modifiee dans l'arbre de travail ou dans l'index est donc datee
    d'AUJOURD'HUI : c'est bien le jour ou elle part en ligne.
    """
    modifiee = subprocess.run(['git', '-C', R, 'status', '--porcelain', '--', chemin_relatif],
                              capture_output=True, text=True).stdout.strip()
    if modifiee:
        return datetime.date.today().isoformat()
    r = subprocess.run(['git', '-C', R, 'log', '-1', '--format=%cs', '--', chemin_relatif],
                       capture_output=True, text=True)
    return r.stdout.strip() or None


def pages():
    """Les pages publiables, dans l'ordre de PRIORITES puis alphabetique."""
    trouvees = []
    for p in sorted(glob.glob(f'{R}/*.html') + glob.glob(f'{R}/*/index.html')):
        rel = p[len(R) + 1:]
        s = open(p, encoding='utf-8').read()
        if re.search(r'<meta name="robots"[^>]*noindex', s, re.I):
            continue
        url = '/' + rel.replace('index.html', '')
        if url == '/index.html':
            url = '/'
        trouvees.append((url, rel))
    ordre = list(PRIORITES)
    return sorted(trouvees, key=lambda t: (ordre.index(t[0]) if t[0] in ordre else 999, t[0]))


def composer():
    lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    inconnues = []
    for url, rel in pages():
        d = derniere_date(rel)
        if d is None:
            # Jamais commitee : elle n'est pas encore en ligne, elle n'a rien
            # a faire dans un sitemap qui dit aux moteurs quoi aller lire.
            continue
        if url not in PRIORITES:
            inconnues.append(url)
        lignes += ['  <url>',
                   f'    <loc>{SITE}{url}</loc>',
                   f'    <lastmod>{d}</lastmod>',
                   '    <changefreq>monthly</changefreq>',
                   f'    <priority>{PRIORITES.get(url, DEFAUT)}</priority>',
                   '  </url>']
    lignes.append('</urlset>')
    return '\n'.join(lignes) + '\n', inconnues


def main():
    verifier = '--verifier' in sys.argv
    neuf, inconnues = composer()
    q = os.path.join(R, 'sitemap.xml')
    actuel = open(q, encoding='utf-8').read() if os.path.exists(q) else ''

    for u in inconnues:
        print(f'  ! {u} n\'a pas de priorite declaree, elle prend {DEFAUT} — '
              f'l\'inscrire dans PRIORITES de generer-sitemap.py')

    if actuel == neuf:
        print(f'  sitemap a jour ({neuf.count("<url>")} URL)')
        return 0
    if verifier:
        # Nommer CE qui differe : un « perime » sans detail envoie relire tout
        # le fichier pour trouver une date.
        av = dict(zip(re.findall(r'<loc>([^<]+)</loc>', actuel),
                      re.findall(r'<lastmod>([^<]+)</lastmod>', actuel)))
        ap = dict(zip(re.findall(r'<loc>([^<]+)</loc>', neuf),
                      re.findall(r'<lastmod>([^<]+)</lastmod>', neuf)))
        for u in sorted(set(av) | set(ap)):
            if av.get(u) != ap.get(u):
                print(f'  ✗ {u}  sitemap dit {av.get(u, "absent")}, '
                      f'le depot dit {ap.get(u, "absent")}')
        print('  → python3 _chantier/generer-sitemap.py')
        return 1
    open(q, 'w', encoding='utf-8').write(neuf)
    print(f'  sitemap regenere ({neuf.count("<url>")} URL)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
