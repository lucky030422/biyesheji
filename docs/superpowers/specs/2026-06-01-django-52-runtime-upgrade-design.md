# Django 5.2 Runtime Upgrade Design

## Goal

Upgrade the project runtime to Python 3.12, Django 5.2, MySQL 8.0-compatible dependencies, Bootstrap 5 availability, and ECharts 5 availability while preserving existing routes, database tables, and front-end UI behavior.

## Scope

This migration updates dependencies and compatibility code only. It does not redesign Vue pages, replace Element Plus with Bootstrap components, or alter database schema beyond what Django requires to import models.

## Backend Approach

The backend keeps the generated Django app structure and existing API endpoints. `requirements.txt` will pin Django 5.2 and update compatibility-sensitive packages such as PyMySQL and django-cors-headers. Settings will be adjusted for Django 5.2 by removing obsolete settings, using current CORS setting names, adding `DEFAULT_AUTO_FIELD`, and avoiding import-time failures when optional local secrets such as Alipay key files are absent.

URL routing will continue using `path` and `re_path`. Removed Django APIs such as `django.conf.urls.url` will be eliminated.

## Database Approach

The project will continue using MySQL through Django's MySQL backend with PyMySQL installed as the MySQLdb compatibility shim. MySQL 8.0 behavior will be targeted by keeping strict SQL mode and using the existing `config.ini` database values.

## Frontend Approach

The existing Vue 3 and Element Plus code remains unchanged visually. Bootstrap 5 and ECharts 5 will be made explicit dependencies where appropriate. Existing chart code that uses `window.echarts` remains supported by the existing page-level script loading unless a local package import is already established.

## Verification

The minimum acceptance checks are:

- `python manage.py check` passes under Python 3.12 and Django 5.2.
- Django can import settings and URL configuration.
- Front-end package manifests include Bootstrap 5 and ECharts 5 availability without breaking existing build scripts.

## Risks

`dwebsocket` may be incompatible with Django 5.2. If it fails during `manage.py check`, the migration will either replace it with a lightweight compatibility path or isolate the dependency so non-websocket startup succeeds.

The project uses generated code and many dynamic `eval` patterns. This migration will not rewrite those patterns unless they block startup under Django 5.2.
