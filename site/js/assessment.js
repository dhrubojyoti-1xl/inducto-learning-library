/* ==========================================================================
   Inducto — formal assessment.

   Management rule implemented here: THREE attempts to pass. After three
   unsuccessful attempts the learner is told that further action requires an
   HR decision. This is the formal test, distinct from the practice
   knowledge check inside each module.

   The HR step is a front-end state only. No HR workflow is connected in
   this static build.
   ========================================================================== */
(function () {
  'use strict';

  var P = window.Inducto.Progress;
  var DATA = window.INDUCTO_DATA;
  if (!DATA || !DATA.assessment) return;

  var PASS_MARK = DATA.assessment.passMark || 0.7;
  var POOL = DATA.assessment.questions || [];
  var COUNT = Math.min(DATA.assessment.questionCount || 15, POOL.length);

  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function announce(m) {
    var l = $('#live'); if (l) { l.textContent = ''; setTimeout(function () { l.textContent = m; }, 30); }
  }

  var host = $('#assessment');
  if (!host) return;

  function shuffled(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function gate() {
    var a = P.assessment();
    var left = P.attemptsLeft();
    var ids = DATA.modules.map(function (m) { return m.id; });
    var o = P.overall(ids);

    if (a.passed) {
      host.innerHTML = panel('chip--ok', 'Assessment passed',
        'You passed on attempt ' + a.attempts.length + '. Your result is stored ' +
        'with your learning record.' +
        (o.completed === o.total
          ? ' All ' + o.total + ' modules are complete, so you are certificate eligible.'
          : ' ' + (o.total - o.completed) + ' modules are still incomplete.'),
        history(a));
      return false;
    }
    if (left === 0) {
      host.innerHTML = panel('chip--warn', 'Further action requires HR decision',
        'You have used all ' + P.ASSESSMENT_MAX_ATTEMPTS + ' attempts. Under the ' +
        'Inducto assessment rule, the next step is an HR decision. Your attempt ' +
        'history is stored with your learning record.', history(a) +
        '<p class="note" style="margin-top:16px">This build records the outcome ' +
        'only. No HR workflow is connected — the follow-up is handled outside ' +
        'this site.</p>');
      return false;
    }
    return true;
  }

  function panel(chip, title, body, extra) {
    return '<div class="card"><span class="chip ' + chip + '">' + esc(title) + '</span>' +
      '<h2 style="margin:12px 0 8px">' + esc(title) + '</h2>' +
      '<p style="max-width:66ch">' + esc(body) + '</p>' + (extra || '') +
      '<p style="margin:20px 0 0"><a class="btn btn--ghost" href="index.html">' +
      'Return to library</a></p></div>';
  }

  function history(a) {
    if (!a.attempts.length) return '';
    return '<div style="margin-top:16px"><div class="rail__title">Attempt history</div>' +
      a.attempts.map(function (x, i) {
        return '<div class="linkitem" style="cursor:default"><span>Attempt ' + (i + 1) +
          ' · ' + new Date(x.at).toLocaleDateString() + '</span><span class="chip ' +
          (x.passed ? 'chip--ok' : 'chip--warn') + '">' + x.score + '/' + x.total +
          '</span></div>';
      }).join('') + '</div>';
  }

  function startScreen() {
    var left = P.attemptsLeft();
    host.innerHTML =
      '<div class="card">' +
        '<span class="chip chip--solid">Formal assessment</span>' +
        '<h2 style="margin:12px 0 8px">Inducto final assessment</h2>' +
        '<p style="max-width:66ch">' + COUNT + ' questions drawn from across the ' +
          'library. Pass mark ' + Math.round(PASS_MARK * 100) + '%. ' +
          'You have <strong>' + left + ' of ' + P.ASSESSMENT_MAX_ATTEMPTS +
          '</strong> attempts remaining. If all three attempts are unsuccessful, ' +
          'further action requires an HR decision.</p>' +
        '<p class="note">This is not the practice knowledge check inside each ' +
          'module. Those can be retried freely and do not count here.</p>' +
        '<p style="margin-top:20px"><button class="btn" id="startBtn">' +
          'Begin attempt ' + (P.assessment().attempts.length + 1) + '</button></p>' +
        history(P.assessment()) +
      '</div>';
    $('#startBtn').addEventListener('click', run);
  }

  function run() {
    var qs = shuffled(POOL).slice(0, COUNT);
    var picked = {};
    var html = '<form id="aform" novalidate><div class="rail__title">Answer every ' +
      'question, then submit. You can change an answer before submitting.</div>';
    qs.forEach(function (q, i) {
      html += '<div class="q" data-i="' + i + '">' +
        '<div class="mcard__code">Question ' + (i + 1) + ' of ' + qs.length +
        ' · ' + esc(q.module) + '</div>' +
        '<h3 style="margin:6px 0 12px">' + esc(q.q) + '</h3>' +
        (q.stem ? '<div class="q__stem">' + esc(q.stem) + '</div>' : '') +
        '<div class="q__opts" role="group" aria-label="Options">';
      q.options.forEach(function (o, oi) {
        html += '<button type="button" class="opt" data-q="' + i + '" data-o="' + oi + '">' +
          '<span class="opt__k">' + 'ABCD'[oi] + '</span><span>' + esc(o.text) + '</span></button>';
      });
      html += '</div></div>';
    });
    html += '<div class="card" style="display:flex;gap:16px;align-items:center;' +
      'flex-wrap:wrap"><span id="acount" class="chip">0 of ' + qs.length +
      ' answered</span><button class="btn" id="submitBtn" type="submit" disabled>' +
      'Submit assessment</button></div></form>';
    host.innerHTML = html;

    $$('.opt', host).forEach(function (btn) {
      btn.addEventListener('click', function () {
        var qi = btn.getAttribute('data-q');
        picked[qi] = parseInt(btn.getAttribute('data-o'), 10);
        $$('.opt[data-q="' + qi + '"]', host).forEach(function (o) {
          o.classList.remove('is-right');
          o.setAttribute('aria-pressed', 'false');
        });
        btn.classList.add('is-right');
        btn.setAttribute('aria-pressed', 'true');
        var n = Object.keys(picked).length;
        $('#acount').textContent = n + ' of ' + qs.length + ' answered';
        $('#submitBtn').disabled = n !== qs.length;
      });
    });

    $('#aform').addEventListener('submit', function (e) {
      e.preventDefault();
      var score = 0;
      qs.forEach(function (q, i) { if (q.options[picked[i]] && q.options[picked[i]].ok) score++; });
      var passed = (score / qs.length) >= PASS_MARK;
      P.recordAttempt(score, qs.length, passed);
      result(score, qs.length, passed, qs, picked);
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
    announce('Assessment started, ' + qs.length + ' questions');
  }

  function result(score, total, passed, qs, picked) {
    var left = P.attemptsLeft();
    var review = qs.map(function (q, i) {
      var chosen = q.options[picked[i]];
      var right = q.options.filter(function (o) { return o.ok; })[0];
      var ok = chosen && chosen.ok;
      return '<div class="q"><div class="mcard__code">' + esc(q.module) + '</div>' +
        '<h3 style="margin:6px 0 10px">' + esc(q.q) + '</h3>' +
        '<div class="fb is-open ' + (ok ? 'fb--right' : 'fb--wrong') + '">' +
        '<div class="fb__h">' + (ok ? 'Correct' : 'Incorrect') + '</div>' +
        '<p><strong>Your answer:</strong> ' + esc(chosen ? chosen.text : '—') + '</p>' +
        (ok ? '' : '<p><strong>Correct answer:</strong> ' + esc(right.text) + '</p>') +
        '<p>' + esc((ok ? chosen : right).why) + '</p></div></div>';
    }).join('');

    host.innerHTML =
      '<div class="qscore" style="margin-bottom:24px">' +
        '<div><span class="qscore__n">' + score + ' / ' + total + '</span>' +
        '<div class="chip ' + (passed ? 'chip--ok' : 'chip--warn') + '">' +
        (passed ? 'Passed' : 'Not passed') + '</div></div>' +
        '<p style="margin:0;flex:1;min-width:240px;color:var(--grey)">' +
        (passed
          ? 'Recorded against your learning record.'
          : (left > 0
              ? 'You have ' + left + ' attempt' + (left === 1 ? '' : 's') + ' remaining.'
              : 'All three attempts used. Further action requires an HR decision.')) +
        '</p>' +
        (passed || left === 0 ? '' :
          '<button class="btn" id="againBtn">Try again</button>') +
        '<a class="btn btn--ghost" href="index.html">Return to library</a>' +
      '</div>' +
      '<h2>Review</h2>' + review;

    var again = $('#againBtn');
    if (again) again.addEventListener('click', function () { if (gate()) startScreen(); });
    window.scrollTo({ top: 0, behavior: 'smooth' });
    announce('Assessment scored ' + score + ' out of ' + total);
  }

  if (gate()) startScreen();
})();
