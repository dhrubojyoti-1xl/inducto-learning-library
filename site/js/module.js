/* ==========================================================================
   Inducto — module page behaviour.
   Quizzes, scenario decisions, checklists, copy buttons, rail tracking and
   module completion. All state goes through Inducto.Progress.
   ========================================================================== */
(function () {
  'use strict';

  var P = window.Inducto.Progress;
  var root = document.querySelector('[data-module-id]');
  if (!root) return;

  var MODULE_ID = root.getAttribute('data-module-id');
  var SECTION_COUNT = parseInt(root.getAttribute('data-section-count'), 10) || 0;

  P.start(MODULE_ID);

  /* ---------- helpers ---------------------------------------------------- */
  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) {
    return Array.prototype.slice.call((ctx || document).querySelectorAll(sel));
  }
  function announce(msg) {
    var live = $('#live');
    if (live) { live.textContent = ''; setTimeout(function () { live.textContent = msg; }, 30); }
  }

  /* ---------- module progress bar --------------------------------------- */
  function paintProgress() {
    var pct = P.percent(MODULE_ID, SECTION_COUNT);
    var fill = $('#modbar');
    if (fill) fill.style.width = pct + '%';
    var lbl = $('#modpct');
    if (lbl) lbl.textContent = pct + '%';
    var bar = $('#modbarwrap');
    if (bar) bar.setAttribute('aria-valuenow', String(pct));
  }

  /* ---------- rail + section tracking ----------------------------------- */
  var sections = $$('section.step[id]');
  var railLinks = {};
  $$('.rail a[href^="#"]').forEach(function (a) {
    railLinks[a.getAttribute('href').slice(1)] = a;
  });

  function markSeen(id) {
    P.section(MODULE_ID, id);
    var a = railLinks[id];
    if (a && !a.classList.contains('is-done')) {
      a.classList.add('is-done');
      var t = a.querySelector('.rail__tick');
      if (t) t.textContent = '✓';
    }
    paintProgress();
  }

  P.get(MODULE_ID).sections.forEach(function (id) {
    var a = railLinks[id];
    if (a) {
      a.classList.add('is-done');
      var t = a.querySelector('.rail__tick');
      if (t) t.textContent = '✓';
    }
  });

  if ('IntersectionObserver' in window && sections.length) {
    var seenTimer = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var id = e.target.id;
        if (e.isIntersecting) {
          Object.keys(railLinks).forEach(function (k) {
            railLinks[k].classList.toggle('is-active', k === id);
          });
          // a section counts as read once it has been on screen briefly
          seenTimer[id] = setTimeout(function () { markSeen(id); }, 1200);
        } else if (seenTimer[id]) {
          clearTimeout(seenTimer[id]); delete seenTimer[id];
        }
      });
    }, { rootMargin: '-15% 0px -55% 0px', threshold: 0.01 });
    sections.forEach(function (s) { io.observe(s); });
  } else {
    sections.forEach(function (s) { markSeen(s.id); });
  }

  /* ---------- copy buttons ---------------------------------------------- */
  $$('.copybtn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var target = document.getElementById(btn.getAttribute('data-copy'));
      if (!target) return;
      var text = target.innerText;
      var done = function () {
        var old = btn.textContent;
        btn.textContent = 'Copied';
        btn.classList.add('is-done');
        announce('Copied to clipboard');
        setTimeout(function () {
          btn.textContent = old; btn.classList.remove('is-done');
        }, 1800);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { fallback(text, done); });
      } else { fallback(text, done); }
    });
  });

  function fallback(text, done) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'absolute'; ta.style.left = '-9999px';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); done(); } catch (e) {}
    document.body.removeChild(ta);
  }

  /* ---------- interactive checklists ------------------------------------ */
  var saved = P.checklistState(MODULE_ID);
  $$('.checkitem input[type="checkbox"]').forEach(function (cb) {
    var key = cb.getAttribute('data-key');
    if (saved[key]) { cb.checked = true; cb.closest('.checkitem').classList.add('is-done'); }
    cb.addEventListener('change', function () {
      cb.closest('.checkitem').classList.toggle('is-done', cb.checked);
      P.checklist(MODULE_ID, key, cb.checked);
    });
  });

  /* ---------- scenario decisions ---------------------------------------- */
  $$('[data-scenario]').forEach(function (box) {
    var opts = $$('.opt', box);
    var fb = $('.fb', box);
    opts.forEach(function (opt) {
      opt.addEventListener('click', function () {
        var tone = opt.getAttribute('data-tone');
        opts.forEach(function (o) {
          o.setAttribute('disabled', 'disabled');
          o.classList.remove('is-right', 'is-wrong');
        });
        opt.classList.add(tone === 'good' ? 'is-right' : 'is-wrong');
        fb.className = 'fb is-open ' + (tone === 'good' ? 'fb--right' : 'fb--wrong');
        fb.innerHTML =
          '<div class="fb__h">' + esc(opt.getAttribute('data-headline')) + '</div>' +
          '<p>' + esc(opt.getAttribute('data-consequence')) + '</p>' +
          '<div class="fb__remember"><b>The rule</b>' +
          esc(opt.getAttribute('data-rule')) + '</div>' +
          '<p style="margin:16px 0 0"><button class="btn btn--ghost btn--sm" ' +
          'data-retry-scenario>Try a different choice</button></p>';
        announce(opt.getAttribute('data-headline'));
        fb.scrollIntoView({ block: 'nearest' });
        var retry = $('[data-retry-scenario]', fb);
        retry.addEventListener('click', function () {
          opts.forEach(function (o) {
            o.removeAttribute('disabled');
            o.classList.remove('is-right', 'is-wrong');
          });
          fb.className = 'fb'; fb.innerHTML = '';
          opts[0].focus();
        });
      });
    });
  });

  /* ---------- knowledge check ------------------------------------------- */
  var quiz = $('[data-quiz]');
  if (quiz) {
    var questions = $$('.q', quiz);
    var answered = {};
    var PASS = 0.6;

    questions.forEach(function (q, qi) {
      var opts = $$('.opt', q);
      var fb = $('.fb', q);
      opts.forEach(function (opt) {
        opt.addEventListener('click', function () {
          var correct = opt.getAttribute('data-correct') === '1';
          if (!(qi in answered)) answered[qi] = correct;   // first answer scores
          opts.forEach(function (o) { o.setAttribute('disabled', 'disabled'); });
          opt.classList.add(correct ? 'is-right' : 'is-wrong');
          if (!correct) {
            opts.forEach(function (o) {
              if (o.getAttribute('data-correct') === '1') o.classList.add('is-right');
            });
          }
          fb.className = 'fb is-open ' + (correct ? 'fb--right' : 'fb--wrong');
          fb.innerHTML =
            '<div class="fb__h">' +
            (correct ? 'Correct — here’s why' : 'Not quite — here’s what actually happens') +
            '</div><p>' + esc(opt.getAttribute('data-why')) + '</p>' +
            '<div class="fb__remember"><b>Remember</b>' +
            esc(q.getAttribute('data-remember')) + '</div>' +
            (correct ? '' : '<p style="margin:16px 0 0">' +
              '<button class="btn btn--ghost btn--sm" data-retry>Try this question again</button></p>');
          announce(correct ? 'Correct' : 'Not quite');
          var retry = $('[data-retry]', fb);
          if (retry) {
            retry.addEventListener('click', function () {
              opts.forEach(function (o) {
                o.removeAttribute('disabled');
                o.classList.remove('is-right', 'is-wrong');
              });
              fb.className = 'fb'; fb.innerHTML = '';
              opts[0].focus();
            });
          }
          maybeScore();
        });
      });
    });

    function maybeScore() {
      if (Object.keys(answered).length !== questions.length) return;
      var score = 0;
      Object.keys(answered).forEach(function (k) { if (answered[k]) score++; });
      var passed = (score / questions.length) >= PASS;
      P.check(MODULE_ID, score, questions.length, passed);
      var box = $('#qscore');
      if (box) {
        box.hidden = false;
        box.innerHTML =
          '<div><span class="qscore__n">' + score + ' / ' + questions.length +
          '</span><div class="' + (passed ? 'chip chip--ok' : 'chip chip--warn') + '">' +
          (passed ? 'Knowledge check passed' : 'Below the 60% mark') + '</div></div>' +
          '<p style="margin:0;flex:1;min-width:220px;color:var(--grey)">' +
          (passed
            ? 'This is practice, not the formal assessment. Your score is saved to your progress.'
            : 'This is practice, so it costs you nothing. Re-read the sections above and try the questions again.') +
          '</p>';
        box.scrollIntoView({ block: 'nearest' });
      }
      paintProgress();
      announce('Knowledge check scored ' + score + ' out of ' + questions.length);
    }
  }

  /* ---------- module completion ----------------------------------------- */
  var completeBtn = $('#completeBtn');
  var doneBox = $('#doneBox');
  function paintCompletion() {
    var m = P.get(MODULE_ID);
    if (m.completedAt && doneBox) {
      doneBox.hidden = false;
      if (completeBtn) completeBtn.hidden = true;
    }
  }
  if (completeBtn) {
    completeBtn.addEventListener('click', function () {
      P.complete(MODULE_ID);
      paintProgress();
      paintCompletion();
      announce('Module marked complete');
      if (doneBox) doneBox.scrollIntoView({ block: 'center' });
    });
  }

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  paintProgress();
  paintCompletion();
})();
