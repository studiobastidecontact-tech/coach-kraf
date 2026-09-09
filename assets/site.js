(function(){
  'use strict';
  var doux = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // l'en-tete se pose sur une bordure des qu'on quitte le haut
  var tete = document.getElementById('tete');
  var poser = function(){ tete.classList.toggle('pose', window.scrollY > 24); };
  window.addEventListener('scroll', poser, {passive:true}); poser();

  // menu mobile
  var burger = document.getElementById('burger'), menu = document.getElementById('menu');
  var fermerMenu = function(){ menu.classList.remove('ouvert'); burger.setAttribute('aria-expanded','false'); burger.setAttribute('aria-label','Ouvrir le menu'); };
  burger.addEventListener('click', function(){
    var ouvert = menu.classList.toggle('ouvert');
    burger.setAttribute('aria-expanded', String(ouvert));
    burger.setAttribute('aria-label', ouvert ? 'Fermer le menu' : 'Ouvrir le menu');
  });
  menu.addEventListener('click', function(e){ if (e.target.tagName === 'A') fermerMenu(); });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape') fermerMenu(); });

  // Entrees au defilement. On n'arme le masquage QUE si l'utilisateur ne
  // demande pas moins de mouvement ; sinon on ne touche a rien et le contenu
  // reste visible, exactement comme sans JS.
  //
  // Deliberement PAS d'IntersectionObserver : il ne signale que les elements
  // qu'il voit ENTRER. Sur un saut de defilement — clic sur une ancre du menu,
  // barre tiree d'un coup, touche Fin, position restauree au rechargement —
  // les blocs traverses ne sont jamais notifies et restent invisibles a vie.
  // Un balayage au defilement, lui, ne peut pas manquer un element depasse.
  if (!doux) {
    document.documentElement.classList.add('anime');
    var restants = Array.prototype.slice.call(document.querySelectorAll('.monte'));
    var enAttente = false, dernierY = window.scrollY;
    var balayer = function(){
      enAttente = false;
      var y = window.scrollY, vh = window.innerHeight;
      // Un ecart d'un ecran ou plus entre deux passages, c'est un SAUT :
      // clic sur une ancre, barre tiree, touche Fin, position restauree.
      // On revele alors largement, pour ne jamais deposer le visiteur
      // devant une section vide. En defilement normal, le seuil reste au
      // bas du viewport : l'element s'anime bien en montant.
      var saut = Math.abs(y - dernierY) >= vh;
      dernierY = y;
      var seuil = saut ? vh * 2.2 : vh;
      restants = restants.filter(function(el){
        if (el.getBoundingClientRect().top >= seuil) return true;
        el.classList.add('vu');
        return false;
      });
      if (!restants.length) {
        window.removeEventListener('scroll', demander);
        window.removeEventListener('resize', demander);
        window.removeEventListener('hashchange', sauter);
      }
    };
    var demander = function(){ if (!enAttente) { enAttente = true; requestAnimationFrame(balayer); } };
    // un changement d'ancre est un saut par definition, meme sans evenement scroll
    var sauter = function(){ dernierY = -1e6; demander(); };
    window.addEventListener('scroll', demander, {passive:true});
    window.addEventListener('resize', demander, {passive:true});
    window.addEventListener('hashchange', sauter);
    document.addEventListener('click', function(e){
      var a = e.target.closest && e.target.closest('a[href^="#"]');
      if (a) setTimeout(sauter, 60);
    });
    balayer();
  }


  // envoi du message — la saisie n'est jamais perdue en cas d'echec
  var f = document.getElementById('msg');
  if (!f) return;
  var btn = document.getElementById('c-envoi'), ok = document.getElementById('c-ok'), ko = document.getElementById('c-ko');
  var libelle = btn.textContent;
  f.addEventListener('submit', function(e){
    e.preventDefault();
    ok.className = 'retour'; ko.className = 'retour';
    btn.disabled = true; btn.textContent = 'Envoi en cours…';
    fetch(f.action, {method:'POST', body:new FormData(f), headers:{'Accept':'application/json'}})
      .then(function(r){
        if (!r.ok) throw new Error('refus');
        ok.className = 'retour ok';
        f.reset();
        btn.textContent = 'Message envoyé';
      })
      .catch(function(){
        ko.className = 'retour ko';
        btn.disabled = false; btn.textContent = libelle;
      });
  });
})();
