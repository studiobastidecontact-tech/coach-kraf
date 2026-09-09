#!/usr/bin/env python3
"""Contradictions qu'aucun outil ne voit — un site peut afficher deux durées,
deux prix, ou envoyer une mention légale vers un formulaire, sans qu'un seul
validateur bronche. Ce script les cherche. Lancer avant chaque publication :
    python3 _chantier/coherence.py
"""
import re, os, sys, html, json, struct
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

def dimensions_jpeg(chemin):
    """Lit la taille dans l'en-tete du fichier — pas de dependance, et ca ne
    ment pas, contrairement a ce que le HTML declare."""
    d = open(chemin, 'rb').read()
    i = 2
    while i < len(d) - 9:
        if d[i] != 0xFF:
            i += 1; continue
        if d[i+1] in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack('>HH', d[i+5:i+9]); return w, h
        i += 2 + struct.unpack('>H', d[i+2:i+4])[0]
    return None

ANCRES = {f: set(re.findall(r'\sid="([^"]+)"', open(os.path.join(R, f), encoding='utf-8').read()))
          for f in PAGES if os.path.exists(os.path.join(R, f))}

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

    # 5) l'image de partage doit exister et mesurer ce qu'on annonce.
    #    Elle est passee de 800 a 1400 px sans que les dimensions declarees
    #    suivent : les reseaux dessinent la carte d'apres ces chiffres.
    img = re.search(r'og:image" content="https://coach-krav\.fr/([^"]+)"', s)
    if img:
        chemin = os.path.join(R, img.group(1))
        if not os.path.exists(chemin):
            fautes.append(f"{p} : image de partage introuvable — {img.group(1)}")
        else:
            w = re.search(r'og:image:width" content="(\d+)"', s)
            h = re.search(r'og:image:height" content="(\d+)"', s)
            reel = dimensions_jpeg(chemin)
            if not (w and h):
                fautes.append(f"{p} : image de partage sans dimensions declarees")
            elif reel and (int(w.group(1)), int(h.group(1))) != reel:
                fautes.append(f"{p} : image de partage declaree {w.group(1)}x{h.group(1)}, reelle {reel[0]}x{reel[1]}")

    # 6) les ancres internes doivent mener quelque part
    for href in set(re.findall(r'href="([^"]*#[^"]+)"', s)):
        chemin_h, _, frag = href.partition('#')
        base = chemin_h.split('?')[0].strip('/')
        cible = (base + '/index.html') if base else ('index.html' if chemin_h.startswith('/') else p)
        if chemin_h == '': cible = p
        if cible in ANCRES and frag not in ANCRES[cible]:
            fautes.append(f"{p} : l'ancre {href} ne mene nulle part")

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

# ── La charte, telle qu'elle est reellement appliquee ────────────────────
# Ces trois listes ne decrivent pas une intention : elles sont relevees sur la
# feuille, et le controle refuse tout ce qui en sort. Sans ca, la charte
# derive — il y avait huit rayons pour trois familles d'objets, et quatre
# tailles de titre pour une seule fonction.
ECHELLE = {13, 14, 15, 16, 17, 19, 20, 23, 26, 30, 46}
RAYONS  = {'var(--r-controle)', 'var(--r-surface)', 'var(--r-focus)', '50%'}
# Le noir et le blanc purs de la feuille d'impression sont voulus : sur du
# papier, l'encre n'a pas de teinte de marque.
COULEURS_TOLEREES = {'#fff', '#000', '#444'}

def controler_charte(fautes):
    q = os.path.join(R, 'assets', 'site.css')
    if not os.path.exists(q):
        fautes.append("assets/site.css introuvable"); return
    brut = open(q, encoding='utf-8').read()
    fin_racine = brut.index('}', brut.index(':root{')) + 1
    racine, corps = brut[:fin_racine], brut[fin_racine:]
    corps = re.sub(r'/\*.*?\*/', '', corps, flags=re.S)
    corps = re.sub(r'data:image/svg\+xml[^"\')]*', '', corps)

    for t in sorted({float(x) for x in re.findall(r'font-size:\s*([\d.]+)px', corps)}):
        if t not in ECHELLE:
            fautes.append(f"assets/site.css : {t:g}px hors de l'echelle typographique ({sorted(ECHELLE)})")
    for r in sorted({x.strip() for x in re.findall(r'border-radius:\s*([^;}]+)', corps)}):
        if r not in RAYONS:
            fautes.append(f"assets/site.css : rayon « {r} » hors charte — attendus : {sorted(RAYONS)}")
    for c in sorted({x.lower() for x in re.findall(r'#[0-9a-fA-F]{3,8}\b', corps)}):
        if c not in COULEURS_TOLEREES:
            fautes.append(f"assets/site.css : couleur {c} ecrite en dur — elle doit passer par un jeton")
    for c in sorted({re.sub(r'\s+', '', x) for x in re.findall(r'rgba?\(\s*\d[^)]*\)', corps)}):
        fautes.append(f"assets/site.css : transparence {c} ecrite en dur — deriver de --*-rgb")

controler_charte(fautes)

if fautes:
    print("\n".join("  ✗ " + f for f in fautes))
    print(f"\n{len(fautes)} contradiction(s).")
    sys.exit(1)
print("  Aucune contradiction sur les %d pages." % len(PAGES))
