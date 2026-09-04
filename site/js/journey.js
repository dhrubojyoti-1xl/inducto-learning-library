/* ==========================================================================
   Inducto — Mandatory Learning Journey behaviour.
   Handles three page shapes: a lesson stop (M-01..M-16), the integration
   exercise (M-19), and the journey map (journey.html). All state goes
   through the same Inducto.Progress store the Optional library uses.
   ========================================================================== */
(function () {
  'use strict';

  var P = window.Inducto.Progress;

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) {
    return Array.prototype.slice.call((ctx || document).querySelectorAll(sel));
  }
  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function announce(msg) {
    var live = $('#live');
    if (live) { live.textContent = ''; setTimeout(function () { live.textContent = msg; }, 30); }
  }

  var DATA = window.INDUCTO_DATA;
  var JOURNEY = DATA && DATA.journey;

  function paintTopbarPct() {
    var el = $('#jpct');
    if (!el || !JOURNEY) return;
    var ids = JOURNEY.stops.map(function (s) { return s.code; });
    var o = P.overall(ids);
    el.textContent = 'Journey ' + o.percent + '%';
  }

  /* ------------------------------------------------------------------ */
  /* LESSON STOP PAGE (M-01..M-16)                                       */
  /* ------------------------------------------------------------------ */
  var stopRoot = $('[data-journey-stop]');
  if (stopRoot) {
    var STOP_ID = stopRoot.getAttribute('data-journey-stop');
    P.start(STOP_ID);
    paintTopbarPct();

    var sections = $$('section.step[id]');
    var SECTION_COUNT = sections.length;

    function paintStopBar() {
      var pct = P.percent(STOP_ID, SECTION_COUNT);
      var fill = $('#stopbar');
      if (fill) fill.style.width = pct + '%';
      var wrap = $('#stopbarwrap');
      if (wrap) wrap.setAttribute('aria-valuenow', String(pct));
      paintTopbarPct();
    }

    if ('IntersectionObserver' in window && sections.length) {
      var seenTimer = {};
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            seenTimer[en.target.id] = setTimeout(function () {
              P.section(STOP_ID, en.target.id);
              paintStopBar();
            }, 900);
          } else if (seenTimer[en.target.id]) {
            clearTimeout(seenTimer[en.target.id]);
          }
        });
      }, { rootMargin: '-10% 0px -60% 0px', threshold: 0.01 });
      sections.forEach(function (s) { io.observe(s); });
    } else {
      sections.forEach(function (s) { P.section(STOP_ID, s.id); });
    }

    /* copy buttons */
    $$('.copybtn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var target = document.getElementById(btn.getAttribute('data-copy'));
        if (!target) return;
        var text = target.innerText;
        var done = function () {
          var old = btn.textContent;
          btn.textContent = 'Copied'; btn.classList.add('is-done');
          announce('Copied to clipboard');
          setTimeout(function () { btn.textContent = old; btn.classList.remove('is-done'); }, 1800);
        };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text, done); });
        } else { fallbackCopy(text, done); }
      });
    });

    /* checklist */
    var savedChecks = P.checklistState(STOP_ID);
    $$('.checkitem input[type="checkbox"]').forEach(function (cb) {
      var key = cb.getAttribute('data-key');
      if (savedChecks[key]) { cb.checked = true; cb.closest('.checkitem').classList.add('is-done'); }
      cb.addEventListener('change', function () {
        cb.closest('.checkitem').classList.toggle('is-done', cb.checked);
        P.checklist(STOP_ID, key, cb.checked);
      });
    });

    /* knowledge check */
    wireQuiz($('[data-quiz]'), function (score, total, passed) {
      P.check(STOP_ID, score, total, passed);
      paintStopBar();
    });

    /* completion */
    var completeBtn = $('#completeBtn');
    var doneBox = $('#doneBox');
    function paintDone() {
      var m = P.get(STOP_ID);
      if (m.completedAt && doneBox) { doneBox.hidden = false; if (completeBtn) completeBtn.hidden = true; }
    }
    if (completeBtn) {
      completeBtn.addEventListener('click', function () {
        P.complete(STOP_ID);
        paintStopBar(); paintDone();
        announce('Stop marked complete');
        if (doneBox) doneBox.scrollIntoView({ block: 'center' });
      });
    }
    paintStopBar();
    paintDone();
  }

  /* ------------------------------------------------------------------ */
  /* INTEGRATION EXERCISE PAGE (M-19)                                    */
  /* ------------------------------------------------------------------ */
  var exRoot = $('[data-exercise]');
  if (exRoot) {
    paintTopbarPct();
    var saved = P.exerciseGet();

    $$('[data-exercise-step]').forEach(function (box) {
      var id = box.getAttribute('data-exercise-step');
      var ta = $('textarea', box);
      var savedStep = saved.steps && saved.steps[id];
      if (ta && savedStep && savedStep.text) ta.value = savedStep.text;
      var timer;
      if (ta) {
        ta.addEventListener('input', function () {
          clearTimeout(timer);
          timer = setTimeout(function () { P.exerciseStep(id, ta.value); }, 500);
        });
      }
      var revealBtn = $('[data-reveal="' + id + '"]', box) || $('[data-reveal="' + id + '"]');
      var revealPanel = document.getElementById('reveal-' + id);
      if (revealBtn && revealPanel) {
        revealBtn.addEventListener('click', function () {
          revealPanel.hidden = !revealPanel.hidden;
          revealBtn.textContent = revealPanel.hidden ? 'Reveal a strong example' : 'Hide the example';
        });
      }
    });

    wireQuiz($('[data-quiz]'), function () {});

    var completeBtn = $('#completeBtn');
    var doneBox = $('#doneBox');
    function checkReady() {
      var boxes = $$('[data-exercise-step] textarea');
      return boxes.every(function (t) { return t.value.trim().length >= 15; });
    }
    if (completeBtn) {
      completeBtn.addEventListener('click', function () {
        if (!checkReady()) {
          announce('Write a short answer in every box first');
          var msg = $('#exerciseMsg');
          if (!msg) {
            msg = document.createElement('p');
            msg.id = 'exerciseMsg'; msg.className = 'note';
            msg.style.color = 'var(--alert)';
            msg.textContent = 'Write at least a short answer in every box above before marking this complete — even a rough attempt is enough.';
            completeBtn.parentNode.insertBefore(msg, completeBtn);
          }
          return;
        }
        P.exerciseComplete();
        if (doneBox) { doneBox.hidden = false; completeBtn.hidden = true; doneBox.scrollIntoView({ block: 'center' }); }
        announce('Exercise marked complete');
      });
    }
    if (saved.completedAt && doneBox) { doneBox.hidden = false; if (completeBtn) completeBtn.hidden = true; }
  }

  /* ------------------------------------------------------------------ */
  /* JOURNEY MAP PAGE (journey.html)                                      */
  /* ------------------------------------------------------------------ */
  var mapResume = $('#jResume');
  if (mapResume && JOURNEY) {
    var stopIds = JOURNEY.stops.map(function (s) { return s.code; });

    function paintMap() {
      var o = P.overall(stopIds.concat(['M-19']));
      $('#jStatDone').textContent = o.completed;
      $('#jStatPct').textContent = o.percent + '%';
      $('#jBar').style.width = o.percent + '%';
      $('#jBarWrap').setAttribute('aria-valuenow', String(o.percent));

      JOURNEY.stops.forEach(function (s) {
        var chip = document.querySelector('[data-journey-status="' + s.code + '"]');
        if (!chip) return;
        var status = P.status(s.code);
        chip.textContent = status;
        chip.classList.toggle('chip--ok', status === 'COMPLETED');
      });
      var exChip = document.querySelector('[data-journey-status="M-19"]');
      if (exChip) {
        var exDone = P.exerciseGet().completedAt;
        exChip.textContent = exDone ? 'COMPLETED' : 'NOT STARTED';
        exChip.classList.toggle('chip--ok', !!exDone);
      }

      /* resume card */
      var next = JOURNEY.stops.filter(function (s) { return P.status(s.code) !== 'COMPLETED'; })[0];
      if (!next) {
        var exStatus = P.exerciseGet().completedAt;
        if (!exStatus) {
          mapResume.innerHTML =
            '<div class="resume__body"><div class="resume__label">Almost there</div>' +
            '<h2 style="margin:4px 0 6px;font-size:1.3rem">All 16 stops complete</h2>' +
            '<p style="margin:0;color:var(--grey)">Last step: the integration exercise.</p></div>' +
            '<a class="btn" href="journey/m19.html">Start the exercise →</a>';
        } else {
          mapResume.innerHTML =
            '<div class="resume__body"><div class="resume__label">Journey complete</div>' +
            '<h2 style="margin:4px 0 6px;font-size:1.3rem">Ready for the final assessment</h2>' +
            '<p style="margin:0;color:var(--grey)">15 questions, 70% pass mark, 3 attempts.</p></div>' +
            '<a class="btn" href="assessment.html">Take the assessment →</a>';
        }
      } else {
        var status = P.status(next.code);
        mapResume.innerHTML =
          '<div class="resume__body"><div class="resume__label">' +
          (status === 'NOT STARTED' ? 'Start here' : 'Continue') + '</div>' +
          '<h2 style="margin:4px 0 6px;font-size:1.3rem">' + esc(next.code) + ' — ' + esc(next.title) + '</h2>' +
          '<p style="margin:0;color:var(--grey)">' + next.stage + ' · ' + next.minutes + ' min</p></div>' +
          '<a class="btn" href="' + esc(next.href) + '">' + (status === 'NOT STARTED' ? 'Start' : 'Continue') + ' →</a>';
      }
    }
    paintMap();
    if (!P.available) { var w = $('#storageWarn'); if (w) w.hidden = false; }
  }

  /* ------------------------------------------------------------------ */
  /* shared helpers                                                       */
  /* ------------------------------------------------------------------ */
  function fallbackCopy(text, done) {
    var ta = document.createElement('textarea');
    ta.value = text; ta.setAttribute('readonly', '');
    ta.style.position = 'absolute'; ta.style.left = '-9999px';
    document.body.appendChild(ta); ta.select();
    try { document.execCommand('copy'); done(); } catch (e) {}
    document.body.removeChild(ta);
  }

  function wireQuiz(quizRoot, onScored) {
    if (!quizRoot) return;
    var questions = $$('.q', quizRoot);
    var answered = {};
    var PASS = 0.6;

    questions.forEach(function (q, qi) {
      var opts = $$('.opt', q);
      var fb = $('.fb', q);
      opts.forEach(function (opt) {
        opt.addEventListener('click', function () {
          var correct = opt.getAttribute('data-correct') === '1';
          if (!(qi in answered)) answered[qi] = correct;
          opts.forEach(function (o) { o.setAttribute('disabled', 'disabled'); });
          opt.classList.add(correct ? 'is-right' : 'is-wrong');
          if (!correct) {
            opts.forEach(function (o) {
              if (o.getAttribute('data-correct') === '1') o.classList.add('is-right');
            });
          }
          fb.className = 'fb is-open ' + (correct ? 'fb--right' : 'fb--wrong');
          fb.innerHTML =
            '<div class="fb__h">' + (correct ? 'Correct — here’s why' : 'Not quite — here’s what actually happens') + '</div>' +
            '<p>' + esc(opt.getAttribute('data-why')) + '</p>' +
            (q.getAttribute('data-remember') ? '<div class="fb__remember"><b>Remember</b>' + esc(q.getAttribute('data-remember')) + '</div>' : '') +
            (correct ? '' : '<p style="margin:16px 0 0"><button class="btn btn--ghost btn--sm" data-retry>Try this question again</button></p>');
          announce(correct ? 'Correct' : 'Not quite');
          var retry = $('[data-retry]', fb);
          if (retry) {
            retry.addEventListener('click', function () {
              opts.forEach(function (o) { o.removeAttribute('disabled'); o.classList.remove('is-right', 'is-wrong'); });
              fb.className = 'fb'; fb.innerHTML = ''; opts[0].focus();
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
      var passed = questions.length ? (score / questions.length) >= PASS : true;
      var box = $('#qscore');
      if (box) {
        box.hidden = false;
        box.innerHTML =
          '<div><span class="qscore__n">' + score + ' / ' + questions.length + '</span>' +
          '<div class="' + (passed ? 'chip chip--ok' : 'chip chip--warn') + '">' +
          (passed ? 'Passed' : 'Below the 60% mark') + '</div></div>' +
          '<p style="margin:0;flex:1;min-width:220px;color:var(--grey)">Practice — saved to your progress, but it is not the final assessment.</p>';
        box.scrollIntoView({ block: 'nearest' });
      }
      onScored(score, questions.length, passed);
      announce('Scored ' + score + ' out of ' + questions.length);
    }
  }
})();
