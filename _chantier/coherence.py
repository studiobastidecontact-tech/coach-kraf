#!/usr/bin/env python3
"""Contradictions qu'aucun outil ne voit — un site peut afficher deux durées,
deux prix, ou envoyer une mention légale vers un formulaire, sans qu'un seul
validateur bronche. Ce script les cherche. Lancer avant chaque publication :
    python3 _chantier/coherence.py
"""
import re, os, sys, html, json, struct
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = sorted(
    os.path.relpath(os.path.join(rep, f), R)
    for rep, _, fichiers in os.walk(R)
    for f in fichiers
    if f.endswith('.html')
    and '_chantier' not in rep
    and '/.git' not in rep
)
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
        # Un numeral COMPOSE n'annonce pas un decompte : « soixante-dix ans
        # d'histoire » ne promet pas dix elements, et « dix-sept » n'en promet
        # pas dix non plus. Le trait d'union est une frontiere que \b ne voit
        # pas — il la considere comme un separateur de mots.
        n_annonce = next((v for mot, v in MOTS.items()
                          if re.search(r'(?<![-\w])' + mot + r'(?![-\w])', titre, re.I)), None)
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

    # 7) titre et description dans les bornes que Google affiche.
    #    Au-dela, il tronque : la fin de la phrase n'existe plus pour personne.
    #    Les bornes viennent de l'audit SEO du 09/09, ou les six pages d'alors
    #    ont ete ramenees a 49-53 et 138-143. Deux pages creees le jour meme en
    #    sont ressorties — un titre a 70, une description a 163 — parce que
    #    RIEN ne les mesurait. Les pages en noindex sont hors sujet : elles ne
    #    paraissent dans aucun resultat.
    if 'noindex' not in (re.search(r'<meta name="robots" content="([^"]*)"', s) or type('', (), {'group': lambda *a: ''})).group(1):
        titre = re.search(r'<title>(.*?)</title>', s, re.S)
        if not titre:
            fautes.append(f"{p} : pas de <title>")
        elif len(titre.group(1).strip()) > 60:
            fautes.append(f"{p} : titre de {len(titre.group(1).strip())} caracteres — Google en affiche 60")
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        if not desc:
            fautes.append(f"{p} : pas de meta description")
        elif len(desc.group(1)) > 160:
            fautes.append(f"{p} : description de {len(desc.group(1))} caracteres — Google en affiche 160")

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

BORNES = ('/* @charte:direction-debut */',
          '/* @charte:contextes-debut */',
          '/* @charte:contextes-fin */')

def sans_commentaires(s):
    """Un commentaire bien ecrit cite les valeurs qu'il explique, et une sonde
    qui ne le retire pas trouve ce qu'elle cherche DANS SA PROPRE PROSE. Les
    adresses de donnees partent aussi : leur SVG porte une couleur de trait
    qui n'est pas une couleur de charte."""
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.S)
    return re.sub(r'data:image/svg\+xml[^"\')]*', '', s)

def controler_charte(fautes):
    q = os.path.join(R, 'assets', 'site.css')
    if not os.path.exists(q):
        fautes.append("assets/site.css introuvable"); return
    brut = open(q, encoding='utf-8').read()

    # ── Les bornes AVANT tout le reste ────────────────────────────────────
    # Un repere introuvable rend -1, et brut[a:-1] lit alors presque tout le
    # fichier sans lever la moindre erreur : le controle passerait au vert en
    # ne mesurant rien. On refuse donc de decouper tant que les trois bornes
    # ne sont pas la, uniques, et dans l'ordre.
    postes = []
    for b in BORNES:
        n = brut.count(b)
        if n != 1:
            fautes.append(f"assets/site.css : la borne « {b} » apparait {n} fois, il en faut exactement une")
            return
        postes.append(brut.index(b))
    if not (postes[0] < postes[1] < postes[2]):
        fautes.append("assets/site.css : les bornes @charte ne sont pas dans l'ordre")
        return

    direction = brut[postes[0]:postes[1]]
    contextes = brut[postes[1]:postes[2]]
    corps     = brut[:postes[0]] + brut[postes[2]:]
    direction_p, contextes_p, corps_p = map(sans_commentaires, (direction, contextes, corps))

    # ── 1) l'echelle typographique et les rayons ──────────────────────────
    for t in sorted({float(x) for x in re.findall(r'font-size:\s*([\d.]+)px', corps_p)}):
        if t not in ECHELLE:
            fautes.append(f"assets/site.css : {t:g}px hors de l'echelle typographique ({sorted(ECHELLE)})")
    for r in sorted({x.strip() for x in re.findall(r'border-radius:\s*([^;}]+)', corps_p)}):
        if r not in RAYONS:
            fautes.append(f"assets/site.css : rayon « {r} » hors charte — attendus : {sorted(RAYONS)}")

    # ── 2) aucune couleur hors du bloc de direction ───────────────────────
    # C'est l'invariant qui rend la charte remplacable : si une seule valeur
    # vit ailleurs, changer de direction ne la suit pas.
    for zone, nom in ((corps_p, 'le corps de la feuille'), (contextes_p, 'la couche des contextes')):
        for c in sorted({x.lower() for x in re.findall(r'#[0-9a-fA-F]{3,8}\b', zone)}):
            if c not in COULEURS_TOLEREES:
                fautes.append(f"assets/site.css : couleur {c} ecrite dans {nom} — elle doit vivre dans le bloc de direction")
        for c in sorted({re.sub(r'\s+', '', x) for x in re.findall(r'rgba?\(\s*\d[^)]*\)', zone)}):
            fautes.append(f"assets/site.css : transparence {c} ecrite dans {nom} — deriver de --*-rgb")

    # ── 3) le corps ne cite jamais un jeton de direction ──────────────────
    # Un --t-* dans le corps court-circuite la couche des contextes : la regle
    # cesse alors de basculer entre fond clair et fond profond, en silence.
    for j in sorted(set(re.findall(r'var\((--t-[a-z0-9-]+)\)', corps_p))):
        fautes.append(f"assets/site.css : {j} cite hors des contextes — le corps ne connait que les roles")

    # ── 4) chaque triplet doit valoir son hexadecimal ─────────────────────
    # La duplication est assumee (rgba ne lit pas un hexadecimal) mais elle
    # ne doit pas deriver.
    hexa = dict(re.findall(r'(--t-[a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})\s*;', direction_p))
    for nom, trio in re.findall(r'(--t-[a-z0-9-]+)-rgb:\s*(\d+,\s*\d+,\s*\d+)\s*;', direction_p):
        h = hexa.get(nom)
        if not h:
            fautes.append(f"assets/site.css : {nom}-rgb existe sans {nom}")
            continue
        attendu = tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
        reel = tuple(int(x) for x in trio.replace(' ', '').split(','))
        if attendu != reel:
            fautes.append(f"assets/site.css : {nom}-rgb vaut {reel} alors que {nom} vaut {h} = {attendu}")

    # ── 5) le chevron du <select> suit la couleur de texte secondaire ─────
    # Il vit dans une adresse de donnees, ou aucune variable n'entre : c'est
    # la seule couleur du fichier qui ne peut pas etre un renvoi.
    ch = re.search(r"--t-chevron:.*?stroke='%23([0-9A-Fa-f]{6})'", direction, re.S)
    if not ch:
        fautes.append("assets/site.css : --t-chevron introuvable ou sans couleur de trait")
    elif '#' + ch.group(1).upper() != (hexa.get('--t-pierre') or '').upper():
        fautes.append(f"assets/site.css : le chevron trace en #{ch.group(1)} alors que --t-pierre vaut {hexa.get('--t-pierre')}")

    # ── 6) tout var(--x) doit renvoyer a un --x defini quelque part ───────
    # Une faute de frappe dans un nom de jeton ne casse rien : la declaration
    # est simplement ignoree, et l'element se peint avec la valeur heritee.
    definis = set(re.findall(r'(--[a-z0-9-]+)\s*:', sans_commentaires(brut)))
    for j in sorted(set(re.findall(r'var\((--[a-z0-9-]+)\)', sans_commentaires(brut)))):
        if j not in definis:
            fautes.append(f"assets/site.css : {j} est utilise mais n'est defini nulle part")

controler_charte(fautes)

if fautes:
    print("\n".join("  ✗ " + f for f in fautes))
    print(f"\n{len(fautes)} contradiction(s).")
    sys.exit(1)
print("  Aucune contradiction sur les %d pages." % len(PAGES))
