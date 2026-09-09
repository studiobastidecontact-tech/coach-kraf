#!/usr/bin/env python3
"""Contradictions qu'aucun outil ne voit — un site peut afficher deux durées,
deux prix, ou envoyer une mention légale vers un formulaire, sans qu'un seul
validateur bronche. Ce script les cherche. Lancer avant chaque publication :
    python3 _chantier/coherence.py
"""
import re, os, sys, html, json
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ['index.html','femmes/index.html','enfants/index.html',
         'toulouse/index.html','saint-sulpice/index.html','mentions/index.html','404.html']
fautes = []

def texte(s):
    """Le texte que quelqu'un lit — y compris hors de la page. La description
    meta et les donnees structurees s'affichent dans les resultats de recherche
    et dans les apercus de partage : une contradiction y est aussi visible que
    dans le corps. Un premier jet les ignorait, et le controle negatif a
    montre qu'un defaut injecte dans la meta passait sans etre vu."""
    hors_page = ' '.join(re.findall(r'<meta[^>]+(?:name="description"|property="og:description")[^>]+content="([^"]*)"', s)
                       + re.findall(r'<meta[^>]+content="([^"]*)"[^>]+(?:name="description"|property="og:description")', s)
                       + re.findall(r'"description"\s*:\s*"([^"]*)"', s)
                       + re.findall(r'<title>(.*?)</title>', s, flags=re.S))
    corps = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', s, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', corps) + ' ' + hors_page))

for p in PAGES:
    q = os.path.join(R, p)
    if not os.path.exists(q): continue
    s = open(q, encoding='utf-8').read()
    t = texte(s)

    # 1) une seule duree de seance dans tout le site
    durees = set(re.findall(r'[Ss]éances? de (\d+\s*h(?:\s*\d+)?)', t))
    if durees - {'1 h 30'}:
        fautes.append(f"{p} : durée de séance « {', '.join(sorted(durees))} » — la seule valeur juste est 1 h 30")

    # 2) les prix affiches doivent appartenir a la grille de mai 2026
    GRILLE = {'50', '35', '25', '18', '15'}
    prix = set(re.findall(r'(\d{2,3})\s*€', t))
    if prix - GRILLE:
        fautes.append(f"{p} : prix hors grille « {', '.join(sorted(prix - GRILLE))} € » — la grille est 50/35/25/18/15")

    # 3) les liens que la loi impose doivent mener aux mentions
    n = re.search(r'<nav aria-label="Informations légales">(.*?)</nav>', s, re.S)
    if not n:
        fautes.append(f"{p} : pas de navigation légale en pied de page")
    else:
        attendu = {'Mentions légales': '/mentions/#mentions',
                   'Confidentialité': '/mentions/#confidentialite'}
        for m in re.finditer(r'<a href="([^"]+)">([^<]+)</a>', n.group(1)):
            if attendu.get(m.group(2).strip()) and m.group(1) != attendu[m.group(2).strip()]:
                fautes.append(f"{p} : « {m.group(2)} » mène à {m.group(1)} au lieu de {attendu[m.group(2).strip()]}")

    # 4) un titre qui annonce un nombre doit tenir ce nombre
    MOTS = {'deux':2,'trois':3,'quatre':4,'cinq':5,'six':6,'sept':7,'huit':8,'neuf':9,'dix':10}
    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>(.*?)(?=<h2|</section>|\Z)', s, re.S):
        titre = texte(m.group(1)).strip()
        n_annonce = next((v for mot, v in MOTS.items() if re.search(r'\b'+mot+r'\b', titre, re.I)), None)
        d = re.search(r'\b(\d+)\b', titre)
        if d: n_annonce = int(d.group(1))
        if not n_annonce or n_annonce < 2: continue
        h3 = len(re.findall(r'<h3\b', m.group(2)))
        if h3 and h3 != n_annonce:
            fautes.append(f"{p} : « {titre[:52]} » annonce {n_annonce}, en liste {h3}")

    # 5) le balisage FAQ doit citer un texte present sur la page
    for bloc in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>', s, re.S):
        try: d = json.loads(bloc)
        except Exception:
            fautes.append(f"{p} : données structurées illisibles"); continue
        for it in (d if isinstance(d, list) else [d]):
            if it.get('@type') != 'FAQPage': continue
            vis = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', re.sub(r'<(script|style)[^>]*>.*?</\1>', '', s, flags=re.S))))
            for qa in it.get('mainEntity', []):
                for quoi, val in (('question', qa['name']), ('réponse', qa['acceptedAnswer']['text'])):
                    if re.sub(r'\s+', ' ', val).strip() not in vis:
                        fautes.append(f"{p} : la {quoi} balisée « {val[:44]}… » n'est pas sur la page")

if fautes:
    print("\n".join("  ✗ " + f for f in fautes))
    print(f"\n{len(fautes)} contradiction(s).")
    sys.exit(1)
print("  Aucune contradiction sur les %d pages." % len(PAGES))
