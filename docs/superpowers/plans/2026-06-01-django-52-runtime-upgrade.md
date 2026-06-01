# Django 5.2 Runtime Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the existing project run on Python 3.12, Django 5.2, MySQL 8.0-compatible dependencies, Bootstrap 5 availability, and ECharts 5 availability.

**Architecture:** Preserve the generated Django/Vue project structure and patch only runtime compatibility surfaces. Use `manage.py check` as the backend gate and package manifest checks as the front-end dependency gate.

**Tech Stack:** Python 3.12, Django 5.2, PyMySQL, MySQL 8.0, Vue 3, Bootstrap 5, ECharts 5.

---

### Task 1: Add Runtime Compatibility Gate

**Files:**
- Create: `tests/test_runtime_compat.py`

- [ ] Add a test that runs `django.core.management.call_command("check")` with project settings.
- [ ] Run the test and confirm it fails on the current Django 2.0/Python 3.12 environment.
- [ ] Keep the test as the migration acceptance gate.

### Task 2: Update Backend Dependencies

**Files:**
- Modify: `requirements.txt`

- [ ] Pin `Django==5.2`.
- [ ] Update `PyMySQL` and `django-cors-headers` to Django 5-compatible versions.
- [ ] Keep unrelated packages unless they block startup.

### Task 3: Patch Django Settings and URL Compatibility

**Files:**
- Modify: `dj2/settings.py`
- Modify: `dj2/urls.py`
- Modify: `dj2/__init__.py`

- [ ] Install PyMySQL as MySQLdb in `dj2/__init__.py`.
- [ ] Remove `django.conf.urls.url` import.
- [ ] Replace obsolete settings and add `DEFAULT_AUTO_FIELD`.
- [ ] Make optional Alipay key files non-fatal at import time.

### Task 4: Make Frontend Dependencies Explicit

**Files:**
- Modify: `templates/front/package.json`
- Modify: `templates/front/admin/package.json`

- [ ] Add `bootstrap` 5 dependency.
- [ ] Add `echarts` 5 dependency.
- [ ] Preserve existing build scripts.

### Task 5: Verify

**Commands:**
- `python -m pytest tests/test_runtime_compat.py -q`
- `python manage.py check`
- `npm install` and `npm run build` in each front-end package if dependencies are available.

- [ ] Fix only blockers caused by the runtime migration.
- [ ] Commit the final migration.
