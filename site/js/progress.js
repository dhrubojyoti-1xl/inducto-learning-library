/* ==========================================================================
   Inducto — unified learner progress model.

   ONE store for the whole learning journey. Module pages, the library and
   the final assessment all read and write this single record, so there is
   never a second, competing notion of "progress".

   Storage is localStorage for this static build. The shape is deliberately
   server-friendly: swapping load()/save() for authenticated API calls is
   the only change needed for a multi-tenant SaaS deployment.
   ========================================================================== */
(function (global) {
  'use strict';

  var KEY = 'inducto.progress.v1';

  function blank() {
    return {
      version: 1,
      updatedAt: null,
      lastModule: null,
      lastSection: null,
      modules: {},
      assessment: { attempts: [], passed: false }
    };
  }

  function blankModule() {
    return {
      startedAt: null,
      completedAt: null,
      sections: [],
      checklists: {},
      check: null           // { score, total, passed, attempts, at }
    };
  }

  var available = (function () {
    try {
      var k = '__inducto_test__';
      global.localStorage.setItem(k, '1');
      global.localStorage.removeItem(k);
      return true;
    } catch (e) { return false; }
  })();

  var memory = blank();

  function load() {
    if (!available) return memory;
    try {
      var raw = global.localStorage.getItem(KEY);
      if (!raw) return blank();
      var data = JSON.parse(raw);
      if (!data || data.version !== 1) return blank();
      if (!data.modules) data.modules = {};
      if (!data.assessment) data.assessment = { attempts: [], passed: false };
      return data;
    } catch (e) { return blank(); }
  }

  function save(state) {
    state.updatedAt = new Date().toISOString();
    if (!available) { memory = state; return state; }
    try { global.localStorage.setItem(KEY, JSON.stringify(state)); }
    catch (e) { memory = state; }
    return state;
  }

  function moduleRec(state, id) {
    if (!state.modules[id]) state.modules[id] = blankModule();
    return state.modules[id];
  }

  var P = {
    KEY: KEY,
    available: available,

    all: function () { return load(); },

    get: function (id) {
      var s = load();
      return s.modules[id] || blankModule();
    },

    status: function (id) {
      var m = this.get(id);
      if (m.completedAt) return 'COMPLETED';
      if (m.startedAt) return 'IN PROGRESS';
      return 'NOT STARTED';
    },

    /* Percentage for one module: sections seen, plus the knowledge check. */
    percent: function (id, sectionCount) {
      var m = this.get(id);
      if (m.completedAt) return 100;
      var total = (sectionCount || 0) + 1;
      var done = Math.min(m.sections.length, sectionCount || 0);
      if (m.check && m.check.passed) done += 1;
      if (!total) return 0;
      return Math.round((done / total) * 100);
    },

    start: function (id) {
      var s = load();
      var m = moduleRec(s, id);
      if (!m.startedAt) m.startedAt = new Date().toISOString();
      s.lastModule = id;
      return save(s);
    },

    section: function (id, sectionId) {
      if (!sectionId) return;
      var s = load();
      var m = moduleRec(s, id);
      if (m.sections.indexOf(sectionId) === -1) m.sections.push(sectionId);
      s.lastModule = id;
      s.lastSection = sectionId;
      return save(s);
    },

    checklist: function (id, key, checked) {
      var s = load();
      var m = moduleRec(s, id);
      m.checklists[key] = !!checked;
      return save(s);
    },

    checklistState: function (id) { return this.get(id).checklists || {}; },

    /* Practice knowledge check — retryable, never the formal assessment. */
    check: function (id, score, total, passed) {
      var s = load();
      var m = moduleRec(s, id);
      var prior = (m.check && m.check.attempts) || 0;
      m.check = {
        score: score, total: total, passed: !!passed,
        attempts: prior + 1, at: new Date().toISOString()
      };
      if (!m.startedAt) m.startedAt = m.check.at;
      s.lastModule = id;
      return save(s);
    },

    complete: function (id) {
      var s = load();
      var m = moduleRec(s, id);
      if (!m.startedAt) m.startedAt = new Date().toISOString();
      m.completedAt = new Date().toISOString();
      s.lastModule = id;
      return save(s);
    },

    reopen: function (id) {
      var s = load();
      var m = moduleRec(s, id);
      m.completedAt = null;
      return save(s);
    },

    /* ---- formal assessment: management rule is three attempts ---------- */
    ASSESSMENT_MAX_ATTEMPTS: 3,

    assessment: function () { return load().assessment; },

    attemptsLeft: function () {
      var a = this.assessment();
      if (a.passed) return 0;
      return Math.max(0, this.ASSESSMENT_MAX_ATTEMPTS - a.attempts.length);
    },

    recordAttempt: function (score, total, passed) {
      var s = load();
      s.assessment.attempts.push({
        score: score, total: total, passed: !!passed,
        at: new Date().toISOString()
      });
      if (passed) s.assessment.passed = true;
      save(s);
      return s.assessment;
    },

    /* ---- library-level roll-up ---------------------------------------- */
    overall: function (moduleIds) {
      var s = load(), done = 0, started = 0;
      moduleIds.forEach(function (id) {
        var m = s.modules[id];
        if (!m) return;
        if (m.completedAt) done += 1;
        else if (m.startedAt) started += 1;
      });
      return {
        total: moduleIds.length,
        completed: done,
        inProgress: started,
        percent: moduleIds.length
          ? Math.round((done / moduleIds.length) * 100) : 0
      };
    },

    last: function () {
      var s = load();
      return { moduleId: s.lastModule, sectionId: s.lastSection };
    },

    /* Certificate-readiness: the data a certificate would need. This is a
       front-end state only — no certificate is issued here. */
    certificateData: function (moduleIds) {
      var o = this.overall(moduleIds);
      var a = this.assessment();
      return {
        modulesCompleted: o.completed,
        modulesTotal: o.total,
        allModulesComplete: o.completed === o.total && o.total > 0,
        assessmentPassed: a.passed,
        assessmentAttempts: a.attempts.length,
        eligible: o.completed === o.total && o.total > 0 && a.passed,
        issuedBy: null,     // ORGANISATION TO CONFIRM
        certificateId: null // issued by backend, not by this build
      };
    },

    reset: function () {
      if (available) { try { global.localStorage.removeItem(KEY); } catch (e) {} }
      memory = blank();
    }
  };

  global.Inducto = global.Inducto || {};
  global.Inducto.Progress = P;
})(window);
