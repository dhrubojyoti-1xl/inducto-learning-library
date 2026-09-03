/* ==========================================================================
   Inducto — Learning Library (index) behaviour.
   Renders the module grid from window.INDUCTO_DATA, paints unified progress,
   drives Continue Learning, search and the glossary.
   Data is loaded as a plain script (not fetch) so the site also works when
   opened directly from disk.
   ========================================================================== */
(function () {
  'use strict';

  var P = window.Inducto.Progress;
  var DATA = window.INDUCTO_DATA;
  if (!DATA) return;

  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  var ids = DATA.modules.map(function (m) { return m.id; });

  /* ---------- overall progress ------------------------------------------ */
  function paintOverall() {
    var o = P.overall(ids);
    var fill = $('#overallBar');
    if (fill) fill.style.width = o.percent + '%';
    var wrap = $('#overallBarWrap');
    if (wrap) wrap.setAttribute('aria-valuenow', String(o.percent));
    setText('#statDone', o.completed);
    setText('#statProg', o.inProgress);
    setText('#statPct', o.percent + '%');
    var cert = P.certificateData(ids);
    var cbox = $('#certState');
    if (cbox) {
      cbox.textContent = cert.eligible
        ? 'All modules complete and assessment passed — certificate eligible.'
        : (cert.allModulesComplete
            ? 'All modules complete. Pass the final assessment to become certificate eligible.'
            : (o.total - o.completed) + ' modules still to complete before the final assessment.');
    }
  }
  function setText(sel, v) { var el = $(sel); if (el) el.textContent = v; }

  /* ---------- continue learning ----------------------------------------- */
  function paintResume() {
    var box = $('#resume');
    if (!box) return;
    var last = P.last();
    var mod = null;
    if (last.moduleId) {
      mod = DATA.modules.filter(function (m) { return m.id === last.moduleId; })[0];
      if (mod && P.status(mod.id) === 'COMPLETED') {
        var i = DATA.modules.indexOf(mod);
        mod = DATA.modules[i + 1] || mod;
      }
    }
    if (!mod) {
      mod = DATA.modules.filter(function (m) { return P.status(m.id) !== 'COMPLETED'; })[0]
            || DATA.modules[0];
    }
    var status = P.status(mod.id);
    var pct = P.percent(mod.id, mod.sectionCount);
    box.innerHTML =
      '<div class="resume__body">' +
        '<div class="resume__label">' +
          (status === 'NOT STARTED' ? 'Start here' : 'Continue learning') + '</div>' +
        '<h2 style="margin:4px 0 6px;font-size:1.3rem">' + esc(mod.title) + '</h2>' +
        '<p style="margin:0 0 12px;color:var(--grey)">' + esc(mod.summary) + '</p>' +
        '<div class="bar bar--thin" style="max-width:340px">' +
          '<div class="bar__fill" style="width:' + pct + '%"></div></div>' +
      '</div>' +
      '<a class="btn" href="' + esc(mod.href) + '">' +
        (status === 'NOT STARTED' ? 'Start module' : 'Continue') + ' →</a>';
    box.setAttribute('data-area', mod.area);
  }

  /* ---------- module grid ------------------------------------------------ */
  function card(m) {
    var status = P.status(m.id);
    var pct = P.percent(m.id, m.sectionCount);
    return '' +
      '<a class="mcard" href="' + esc(m.href) + '" data-area="' + esc(m.area) + '" ' +
         'data-status="' + status + '">' +
        '<div class="mcard__top">' +
          '<span class="mcard__code">' + esc(m.code) + '</span>' +
          '<span class="chip' + (status === 'COMPLETED' ? ' chip--ok' : '') + '">' +
            status + '</span>' +
        '</div>' +
        '<h3>' + esc(m.title) + '</h3>' +
        '<p class="mcard__desc">' + esc(m.summary) + '</p>' +
        (pct ? '<div class="bar bar--thin"><div class="bar__fill" style="width:' +
               pct + '%"></div></div>' : '') +
        '<div class="mcard__foot"><span>' + m.duration + ' min</span>' +
        '<span>' + (status === 'NOT STARTED' ? 'Start' : 'Continue') + ' →</span></div>' +
      '</a>';
  }

  function paintTracks() {
    var host = $('#tracks');
    if (!host) return;
    var html = '';
    DATA.tracks.forEach(function (t) {
      var mods = DATA.modules.filter(function (m) { return m.area === t.id; });
      var o = P.overall(mods.map(function (m) { return m.id; }));
      html += '<section class="track" data-area="' + esc(t.id) + '" id="track-' + esc(t.id) + '">' +
        '<div class="track__head"><div class="track__rule"></div>' +
        '<h2 style="margin:0">' + esc(t.name) + '</h2>' +
        '<span class="track__count">' + mods.length + ' modules · ' +
        o.completed + ' completed</span></div>' +
        '<p style="max-width:62ch;color:var(--grey);margin:-4px 0 20px">' +
        esc(t.blurb) + '</p>' +
        '<div class="grid grid--3">' + mods.map(card).join('') + '</div></section>';
    });
    host.innerHTML = html;
  }

  /* ---------- search ----------------------------------------------------- */
  var input = $('#q');
  var out = $('#qout');

  function search(term) {
    term = term.trim().toLowerCase();
    if (term.length < 2) return [];
    var words = term.split(/\s+/);
    var hits = [];
    DATA.search.forEach(function (row) {
      var hay = row.t.toLowerCase();
      var score = 0;
      for (var i = 0; i < words.length; i++) {
        var at = hay.indexOf(words[i]);
        if (at === -1) { score = 0; break; }
        score += (at === 0 ? 3 : 1) + (row.k === 'module' ? 2 : 0);
      }
      if (score) hits.push({ row: row, score: score });
    });
    hits.sort(function (a, b) { return b.score - a.score; });
    return hits.slice(0, 12).map(function (h) { return h.row; });
  }

  var KIND = { module: 'Module', lesson: 'Lesson', term: 'Glossary',
               rule: 'Key rule', toolkit: 'Toolkit' };

  function paintSearch() {
    if (!input || !out) return;
    var rows = search(input.value);
    if (!input.value.trim()) { out.classList.remove('is-open'); out.innerHTML = ''; return; }
    if (!rows.length) {
      out.classList.add('is-open');
      out.innerHTML = '<p class="note">No matches for “' + esc(input.value) +
        '”. Try a module name, a term, or a rule.</p>';
      return;
    }
    out.classList.add('is-open');
    out.innerHTML = rows.map(function (r) {
      return '<a class="sresult" href="' + esc(r.h) + '">' +
        '<span class="sresult__k">' + (KIND[r.k] || r.k) + ' · ' + esc(r.m) + '</span>' +
        '<div class="sresult__t">' + esc(r.t) + '</div>' +
        (r.s ? '<div class="sresult__s">' + esc(r.s) + '</div>' : '') + '</a>';
    }).join('');
  }

  if (input) {
    input.addEventListener('input', paintSearch);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { input.value = ''; paintSearch(); input.blur(); }
      if (e.key === 'Enter') {
        var first = $('.sresult', out);
        if (first) { e.preventDefault(); window.location.href = first.getAttribute('href'); }
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === '/' && document.activeElement !== input) {
        e.preventDefault(); input.focus();
      }
    });
  }

  /* ---------- glossary ---------------------------------------------------- */
  function paintGlossary() {
    var host = $('#glossary');
    if (!host) return;
    host.innerHTML = DATA.glossary.map(function (g) {
      return '<div class="card" style="padding:16px">' +
        '<div class="gloss__t">' + esc(g.term) + '</div>' +
        '<div class="gloss__d">' + esc(g.def) + '</div>' +
        '<div style="margin-top:8px"><a class="chip" href="' + esc(g.href) + '">' +
        esc(g.module) + '</a></div></div>';
    }).join('');
    setText('#glossCount', DATA.glossary.length);
  }

  /* ---------- reset ------------------------------------------------------- */
  var reset = $('#resetBtn');
  if (reset) {
    reset.addEventListener('click', function () {
      if (window.confirm('Clear all saved progress on this device? This cannot be undone.')) {
        P.reset(); paintAll();
      }
    });
  }

  function paintAll() { paintOverall(); paintResume(); paintTracks(); }
  paintAll();
  paintGlossary();

  if (!P.available) {
    var warn = $('#storageWarn');
    if (warn) warn.hidden = false;
  }
})();
