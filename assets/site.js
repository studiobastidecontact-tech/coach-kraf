(function(){
  'use strict';
  var doux = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // l'en-tete se pose sur une bordure des qu'on quitte le haut
  var tete = document.getElementById('tete');
  if (tete) {
    var poser = function(){ tete.classList.toggle('pose', window.scrollY > 24); };
    window.addEventListener('scroll', poser, {passive:true}); poser();
  }

  // Menu mobile. Chaque bloc verifie ses elements : la page 404 n'a pas de
  // menu, et une page future pourrait ne pas en avoir non plus. Sans ce
  // garde, un seul element absent leve une TypeError qui emporte TOUT ce
  // qui suit — dont les entrees au defilement et l'envoi du formulaire.
  var burger = document.getElementById('burger'), menu = document.getElementById('menu');
  if (burger && menu) {
    var fermerMenu = function(){ menu.classList.remove('ouvert'); burger.setAttribute('aria-expanded','false'); burger.setAttribute('aria-label','Ouvrir le menu'); };
    burger.addEventListener('click', function(){
      var ouvert = menu.classList.toggle('ouvert');
      burger.setAttribute('aria-expanded', String(ouvert));
      burger.setAttribute('aria-label', ouvert ? 'Fermer le menu' : 'Ouvrir le menu');
    });
    menu.addEventListener('click', function(e){ if (e.target.tagName === 'A') fermerMenu(); });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape') fermerMenu(); });
  }

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
      // On LIT toutes les positions, PUIS on ecrit toutes les classes.
      // Melanger les deux dans un meme filter force le navigateur a
      // recalculer la mise en page a chaque tour : c'est le reflow force
      // que le profileur relevait au chargement.
      var aReveler = [], i;
      for (i = 0; i < restants.length; i++) {
        if (restants[i].getBoundingClientRect().top < seuil) aReveler.push(restants[i]);
      }
      for (i = 0; i < aReveler.length; i++) aReveler[i].classList.add('vu');
      if (aReveler.length) {
        restants = restants.filter(function(el){ return aReveler.indexOf(el) === -1; });
      }
      if (!restants.length) {
        window.removeEventListener('scroll', demander);
        window.removeEventListener('resize', demander);
        window.removeEventListener('hashchange', sauter);
        document.removeEventListener('click', surAncre);
      }
    };
    var demander = function(){ if (!enAttente) { enAttente = true; requestAnimationFrame(balayer); } };
    // un changement d'ancre est un saut par definition, meme sans evenement scroll
    var sauter = function(){ dernierY = -1e6; demander(); };
    var surAncre = function(e){
      var a = e.target.closest && e.target.closest('a[href^="#"]');
      if (a) setTimeout(sauter, 60);
    };
    // Filet : un moteur de rendu qui NE FAIT PAS defiler — Googlebot ouvre une
    // fenetre tres haute au lieu de scroller, les captures pleine page et les
    // robots de lecture ne bougent pas non plus — ne verrait JAMAIS le reste
    // de la page. Mesure du 2026-09-09 : 1 074 mots sur 1 198 restaient a
    // opacite zero. Passe ce delai, si personne n'a defile, on montre tout :
    // c'est hors ecran, donc invisible pour un humain, et present pour le reste.
    var aDefile = false;
    window.addEventListener('scroll', function(){ aDefile = true; }, {passive:true, once:true});
    setTimeout(function(){
      if (aDefile || !restants.length) return;
      for (var k = 0; k < restants.length; k++) restants[k].classList.add('vu');
      restants = [];
      window.removeEventListener('scroll', demander);
      window.removeEventListener('resize', demander);
      window.removeEventListener('hashchange', sauter);
      document.removeEventListener('click', surAncre);
    }, 2600);
    window.addEventListener('scroll', demander, {passive:true});
    window.addEventListener('resize', demander, {passive:true});
    window.addEventListener('hashchange', sauter);
    document.addEventListener('click', surAncre);
    balayer();
  }


  // envoi du message — la saisie n'est jamais perdue en cas d'echec
  var f = document.getElementById('msg');
  if (!f) return;

  // Le formulaire ne vit que sur l'accueil : les quatre autres pages y
  // renvoient. Sans ca, un parent venu de la page enfants arrive devant une
  // liste ou il doit re-choisir « Mon enfant » — il vient pourtant de passer
  // cinq minutes a le dire. On transporte le contexte dans l'adresse et on
  // pre-remplit, en silence : ?pour=Mon enfant, ?ou=Toulouse.
  (function(){
    var q = new URLSearchParams(location.search);
    var poser = function(id, valeur){
      if (!valeur) return;
      var s = document.getElementById(id);
      if (!s) return;
      for (var i = 0; i < s.options.length; i++) {
        if (s.options[i].value === valeur) { s.selectedIndex = i; return; }
      }
    };
    poser('c-qui', q.get('pour'));
    poser('c-ou', q.get('ou'));
  })();
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
        // On rend le bouton apres quelques secondes : le temps que l'accuse
        // se lise, sans enfermer celui qui veut ajouter une precision — il
        // devait sinon recharger la page pour ecrire une deuxieme fois.
        setTimeout(function(){ btn.disabled = false; btn.textContent = libelle; }, 6000);
      })
      .catch(function(){
        ko.className = 'retour ko';
        btn.disabled = false; btn.textContent = libelle;
      });
  });
})();
