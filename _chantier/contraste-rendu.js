/* Mesure le contraste de CHAQUE texte, sur le rendu, dans le navigateur.
 *
 * À coller dans la console d'un onglet ouvert sur une page du site.
 *
 * POURQUOI CE SCRIPT EXISTE, alors que verifier-direction.py fait déjà ce
 * contrôle. Le 2026-09-10, ce dernier annonçait « aucune paire sous son seuil »
 * pendant que l'écusson « Recommandé pour débuter » vivait à 3,91:1. Il ne
 * mentait pas : il mesurait ce qu'on lui avait dit de mesurer — des jetons
 * opaques contre des jetons opaques. Or la feuille pose aussi des aplats en
 * `rgba(var(--x-rgb), a)`, et la couleur que l'œil voit alors n'est AUCUN
 * jeton : c'est un mélange que seul le rendu connaît.
 *
 * Le garde statique a depuis appris à composer (table COMPOSEES), mais il faut
 * lui DÉCLARER chaque composition. Ce script-ci n'a rien à déclarer : il lit ce
 * qui est peint.
 *
 * DEUX PIÈGES, tous deux rencontrés le jour où ce script est né :
 *
 *   1. L'animation d'entrée. `.anime .monte{opacity:0}` passe à 1 en 0,62 s.
 *      Mesurer pendant la transition rend des couleurs partiellement mélangées :
 *      Lighthouse a signalé SIX défauts ce jour-là, cinq étaient ce mirage.
 *      D'où le `classList.add('vu')` et l'attente avant toute mesure.
 *   2. Le fond n'est pas celui de l'élément. Un texte dans une carte
 *      translucide posée sur une section colorée voit un fond COMPOSÉ. On
 *      remonte donc les parents jusqu'au premier fond opaque, puis on
 *      redescend en composant.
 */
(async () => {
  document.querySelectorAll('.monte').forEach(e => e.classList.add('vu'));
  await new Promise(r => setTimeout(r, 900));

  const lum = c => {
    const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4; };
    return .2126 * f(c[0]) + .7152 * f(c[1]) + .0722 * f(c[2]);
  };
  const rgb = s => (s.match(/[\d.]+/g) || [0, 0, 0]).slice(0, 3).map(Number);
  const alpha = s => { const m = s.match(/[\d.]+/g); return m && m.length > 3 ? +m[3] : 1; };
  const comp = (av, ar, ap) => av.map((c, i) => Math.round(c * ar + ap[i] * (1 - ar)));

  const fondEffectif = e => {
    let n = e, pile = [];
    while (n && n !== document.documentElement) {
      const b = getComputedStyle(n).backgroundColor, a = alpha(b);
      if (a > 0) { pile.push([rgb(b), a]); if (a === 1) break; }
      n = n.parentElement;
    }
    let f = [255, 255, 255];
    for (let i = pile.length - 1; i >= 0; i--) f = comp(pile[i][0], pile[i][1], f);
    return f;
  };

  const hex = c => '#' + c.map(v => v.toString(16).padStart(2, '0')).join('');
  const bas = [];
  let mesures = 0;

  document.querySelectorAll('main *, footer *, header *').forEach(e => {
    if (e.children.length || !e.textContent.trim()) return;
    const r = e.getBoundingClientRect();
    if (!r.width || !r.height || !e.checkVisibility()) return;
    const cs = getComputedStyle(e);
    if (+cs.opacity < 1) return;                 // encore en transition
    mesures++;
    const t = rgb(cs.color), f = fondEffectif(e);
    const ratio = (Math.max(lum(t), lum(f)) + .05) / (Math.min(lum(t), lum(f)) + .05);
    const px = parseFloat(cs.fontSize);
    const gras = +cs.fontWeight >= 700 || cs.fontWeight === 'bold';
    const seuil = (px >= 24 || (px >= 18.66 && gras)) ? 3 : 4.5;   // WCAG 1.4.3
    if (ratio < seuil - 0.005) bas.push({
      élément: e.tagName.toLowerCase() + (e.className ? '.' + String(e.className).split(' ')[0] : ''),
      texte: e.textContent.trim().slice(0, 30),
      ratio: +ratio.toFixed(2), seuil, px,
      couleur: hex(t), fond: hex(f)
    });
  });

  console.log(`${mesures} textes mesurés · ${bas.length} sous leur seuil`);
  if (bas.length) console.table(bas); else console.log('Aucun défaut de contraste.');
  return { mesures, sousLeSeuil: bas.length, detail: bas };
})();
