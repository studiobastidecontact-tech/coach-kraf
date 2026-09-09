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


  // Les listes longues se replient sous 760 px. Le bouton arrive `hidden`
  // du serveur et c'est CE script qui le revele : sans JS, la liste reste
  // entiere — on ne cache jamais du contenu a quelqu'un qui n'a pas le
  // moyen de le rouvrir. Rien n'est retire du document : les elements sont
  // masques, pas supprimes, donc les moteurs et les lecteurs d'ecran les
  // voient toujours.
  var replis = Array.prototype.slice.call(document.querySelectorAll('.deplier[data-deplie]'));
  if (replis.length && window.matchMedia) {
    var etroit = window.matchMedia('(max-width:760px)');
    replis.forEach(function(bouton){
      var liste = document.getElementById(bouton.getAttribute('data-deplie'));
      if (!liste) return;
      var garde = parseInt(bouton.getAttribute('data-garde'), 10) || 3;
      var caches = Array.prototype.slice.call(liste.children).slice(garde);
      if (!caches.length) return;
      var nom = bouton.getAttribute('data-nom') || 'éléments';
      var ouvert = false;
      var poser = function(){
        var replie = etroit.matches && !ouvert;
        for (var i = 0; i < caches.length; i++) caches[i].hidden = replie;
        bouton.hidden = !etroit.matches;
        bouton.setAttribute('aria-expanded', String(!replie));
        bouton.textContent = ouvert
          ? 'Masquer les ' + caches.length + ' ' + nom
          : 'Voir les ' + caches.length + ' autres ' + nom;
      };
      bouton.addEventListener('click', function(){
        ouvert = !ouvert;
        poser();
        // en repliant, on ramene la vue sur la liste : sinon le doigt se
        // retrouve devant la section suivante, sans savoir ce qui a bouge
        if (!ouvert) liste.scrollIntoView({block:'nearest'});
      });
      var surBascule = function(){ ouvert = false; poser(); };
      if (etroit.addEventListener) etroit.addEventListener('change', surBascule);
      else if (etroit.addListener) etroit.addListener(surBascule);
      poser();
    });
  }

  // Les questions se replient sous 760 px. Elles arrivent OUVERTES du
  // serveur, meme raison que les listes ci-dessus : sans JS tout se lit.
  // C'est ce script qui les referme, et jamais l'inverse. On ne touche pas
  // au reste du document : un <details> ferme garde son contenu, il n'est
  // ni retire ni masque pour les moteurs.
  var questions = Array.prototype.slice.call(document.querySelectorAll('details.qr-item'));
  if (questions.length && window.matchMedia) {
    var etroitQ = window.matchMedia('(max-width:760px)');
    var poserQ = function(){
      for (var i = 0; i < questions.length; i++) {
        if (etroitQ.matches) questions[i].removeAttribute('open');
        else questions[i].setAttribute('open', '');
      }
    };
    if (etroitQ.addEventListener) etroitQ.addEventListener('change', poserQ);
    else if (etroitQ.addListener) etroitQ.addListener(poserQ);
    poserQ();
  }

  // La barre du pouce ne double plus le bouton du heros : elle arrive quand
  // il sort du champ. On observe le BOUTON, pas une hauteur en pixels — une
  // hauteur devinee se trompe des que le titre passe sur trois lignes.
  var pouce = document.querySelector('.pouce');
  var appelHero = document.querySelector('.hero .btn-1');
  if (pouce && appelHero && 'IntersectionObserver' in window) {
    // Ici l'observateur convient : on surveille UN element, et ses deux etats
    // sont notifies. C'est un balayage qu'il faut quand on suit des sections.
    pouce.setAttribute('data-repliee', '');
    new IntersectionObserver(function(entrees){
      entrees.forEach(function(e){
        if (e.isIntersecting) pouce.setAttribute('data-repliee', '');
        else pouce.removeAttribute('data-repliee');
      });
    }, {rootMargin: '-8px 0px 0px 0px'}).observe(appelHero);
  }

  // Le rail d'ancres marque la section courante. Pas d'IntersectionObserver,
  // pour la meme raison que les entrees au defilement : il ne signale que ce
  // qu'il voit ENTRER, et sur un saut d'ancre les sections traversees ne sont
  // jamais notifiees. Un balayage ne peut pas manquer une section depassee.
  var rail = document.querySelector('.rail');
  if (rail) {
    var onglets = Array.prototype.slice.call(rail.querySelectorAll('a[href^="#"]'));
    var cibles = onglets.map(function(a){ return document.getElementById(a.getAttribute('href').slice(1)); });
    var courant = null, attente = false;
    var marquer = function(){
      attente = false;
      var repere = rail.getBoundingClientRect().bottom + 8;
      var gagnant = 0;
      for (var i = 0; i < cibles.length; i++) {
        if (cibles[i] && cibles[i].getBoundingClientRect().top <= repere) gagnant = i;
      }
      if (gagnant === courant) return;
      if (courant !== null) onglets[courant].removeAttribute('aria-current');
      courant = gagnant;
      onglets[courant].setAttribute('aria-current', 'true');
      // on fait glisser le rail pour que l'onglet actif reste visible
      var o = onglets[courant].getBoundingClientRect(), r = rail.getBoundingClientRect();
      if (o.left < r.left + 12 || o.right > r.right - 12) {
        rail.scrollTo({left: rail.scrollLeft + (o.left - r.left) - 16, behavior: doux ? 'auto' : 'smooth'});
      }
    };
    window.addEventListener('scroll', function(){
      if (!attente) { attente = true; requestAnimationFrame(marquer); }
    }, {passive:true});
    marquer();
  }

  // La modale d'ecriture. Le formulaire ne traine plus en bas de page : on
  // l'ouvre depuis l'en-tete, ou depuis le bloc de contact. Sans script, une
  // balise <dialog> ne s'ouvre pas — un <noscript> la rend alors au fil de la
  // page, et masque les boutons qui ne mèneraient nulle part.
  var modale = document.getElementById('ecrire');
  if (modale) {
    var ouvrantPrecedent = null;
    // Le declencheur porte ce que sa page sait deja du visiteur : la modale
    // s'ouvre pre-remplie. Un parent venu de la page enfants n'a pas a
    // rechoisir « Mon enfant » — il vient de passer cinq minutes a le dire.
    var poser = function(id, valeur){
      if (!valeur) return;
      var liste = modale.querySelector('#' + id);
      if (!liste) return;
      for (var i = 0; i < liste.options.length; i++) {
        if (liste.options[i].value === valeur) { liste.selectedIndex = i; return; }
      }
    };
    var ouvrir = function(depuis){
      ouvrantPrecedent = depuis || null;
      if (depuis) { poser('c-qui', depuis.getAttribute('data-pour')); poser('c-ou', depuis.getAttribute('data-ou')); }
      if (typeof modale.showModal === 'function') modale.showModal();
      else modale.setAttribute('open', '');            // navigateurs sans <dialog>
      var premier = modale.querySelector('input:not([type=hidden]):not([tabindex="-1"]), select, textarea');
      if (premier) setTimeout(function(){ premier.focus(); }, 40);
    };
    var fermer = function(){
      if (typeof modale.close === 'function') modale.close();
      else modale.removeAttribute('open');
      if (ouvrantPrecedent) ouvrantPrecedent.focus();  // on rend le focus a son point de depart
    };
    document.addEventListener('click', function(e){
      var d = e.target.closest && e.target.closest('[data-ouvre="ecrire"]');
      if (d) { e.preventDefault(); ouvrir(d); return; }
      if (e.target.closest && e.target.closest('[data-ferme]')) { fermer(); return; }
      // un clic hors du panneau ferme : la zone du <dialog> deborde son contenu
      if (e.target === modale) fermer();
    });
    modale.addEventListener('close', function(){ if (ouvrantPrecedent) ouvrantPrecedent.focus(); });
    // une adresse qui pointe la modale l'ouvre : /?...#ecrire depuis une autre page
    if (location.hash === '#ecrire') ouvrir(null);
    window.addEventListener('hashchange', function(){ if (location.hash === '#ecrire') ouvrir(null); });
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
  // Ni le telephone ni l'adresse ne sont obligatoires seuls — HTML ne sait pas
  // exprimer « l'un OU l'autre ». Quelqu'un qui ecrit plutot que d'appeler le
  // fait souvent pour ne PAS avoir a parler : lui imposer un numero contredit
  // la raison d'etre du formulaire.
  var tel = f.querySelector('[name=telephone]'), mail = f.querySelector('[name=email]');
  var joindre = function(){
    if (!tel || !mail) return;
    var vide = !tel.value.trim() && !mail.value.trim();
    var msg = vide ? 'Laissez au moins un numéro ou une adresse, sans quoi personne ne peut vous répondre.' : '';
    tel.setCustomValidity(msg); mail.setCustomValidity(msg);
  };
  if (tel && mail) {
    tel.addEventListener('input', joindre);
    mail.addEventListener('input', joindre);
    joindre();
  }

  f.addEventListener('submit', function(e){
    e.preventDefault();
    joindre();
    if (!f.checkValidity()) { f.reportValidity(); return; }
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
