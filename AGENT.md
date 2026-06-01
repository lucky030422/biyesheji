# AGENT.md

## Project Overview

This repository is a Django 2.0 application with MySQL persistence and two Vue 3/Vite frontends stored under `templates/front`.

The app appears to be a pet-service platform with modules for users, shop staff, pet services, foster care, adoption/sale pets, product orders, service orders, health data, forums/comments, favorites, chat, uploads, and admin management.

## Important Directories

- `dj2/`: Django project settings, root URL routing, WSGI entrypoint, and template/static serving helpers.
- `main/`: Primary Django app. Most business modules are split into `*_v.py` view files, with shared models in `models.py` and common ORM helpers in `model.py`.
- `xmiddleware/`: Request parameter normalization and token-auth middleware.
- `util/`: Shared helpers for auth, JSON encoding, SQL initialization, config reading, file encryption, HDFS/Hive/Spark helpers, messaging, and external APIs.
- `db/`: SQL seed/schema dump. `db/djangoq0l722c8.sql` is loaded by `init.py initsql`.
- `templates/front/src/`: User-facing Vue 3/Vite frontend source.
- `templates/front/admin/src/`: Admin Vue 3/Vite frontend source.
- `templates/front/dist/` and `templates/front/admin/dist/`: Built frontend output served by Django. Treat these as generated assets unless the task explicitly targets built files.
- `templates/upload/` and `media/`: Uploaded/static media assets. Avoid bulk edits here unless requested.
- `bin/`: External jar dependency.

## Backend Runtime

Python dependencies are listed in `requirements.txt`. Key packages:

- `django==2.0`
- `pymysql==1.0.2`
- `django-cors-headers==2.4.0`
- `django-threadlocals`
- `dwebsocket`
- `xlrd==1.2.0`
- `openai==1.39.0`

Database connection is read from `config.ini` via `util.configread.config_read`. Current defaults point to MySQL:

- host: `127.0.0.1`
- port: `33061`
- database: `djangoq0l722c8`
- user: `root`

Do not assume the local database is running. Commands that touch the DB can fail if MySQL is unavailable.

## Common Commands

Install and initialize on Windows using the repository's install batch file, or run the equivalent steps:

```powershell
pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
python .\init.py initdb
python .\manage.py makemigrations
python .\manage.py migrate --fake-initial
python .\init.py initsql
python .\manage.py shell -c "from django.contrib.auth.models import User;User.objects.filter(username='abo').exists() or User.objects.create_superuser('abo','abo@example.com', 'abo')"
```

Run the Django server:

```powershell
python manage.py runserver --insecure 0.0.0.0:8080 --noreload
```

Frontend user app:

```powershell
cd templates\front
npm install
npm run serve
npm run build
```

Frontend admin app:

```powershell
cd templates\front\admin
npm install
npm run serve
npm run build
```

## Routing And API Shape

`dj2/urls.py` mounts business APIs under the configured database/schema name:

```text
/<dbName>/<module>/...
```

With the current `config.ini`, API routes are typically under:

```text
/djangoq0l722c8/<module>/...
```

`main/urls.py` dynamically imports every `main/*_v.py` file except `schema_v.py` and `config_v.py`, then generates standard CRUD/list routes for each module:

- `/<table>/default`
- `/<table>/page`
- `/<table>/list`
- `/<table>/lists`
- `/<table>/query`
- `/<table>/save`
- `/<table>/add`
- `/<table>/info/<id_>`
- `/<table>/detail/<id_>`
- `/<table>/update`
- `/<table>/delete`
- `/<table>/thumbsup/<id_>`
- `/<table>/vote/<id_>`
- `/<table>/importExcel`
- `/<table>/autoSort`
- `/<table>/autoSort2`

Some tables add custom routes such as login/register/session, email login, chart aggregation, review batch updates, reminders, forum lists, websocket, uploads, and file encryption/decryption.

## Backend Coding Conventions

- Business models live in `main/models.py` and inherit from `main.model.BaseModel`.
- Model class names and table names are lower-case pinyin-style identifiers such as `yonghu`, `chongwuxinxi`, and `fuwudingdan`.
- View modules are named with capitalized table names plus `_v.py`, for example `Chongwuxinxi_v.py`.
- View function names use lower-case table prefixes, for example `chongwuxinxi_page`.
- Dynamic route generation in `main/urls.py` depends on these naming conventions. If adding a new module, keep model/table/view naming consistent.
- Request params are normalized by `xmiddleware.Xparam` and stored in `request.session["req_dict"]`.
- Authentication checks are handled by `xmiddleware.Xauth` and `util.auth.Auth`.
- Common response shape is usually:

```python
{"code": normal_code, "msg": mes.normal_code, "data": ...}
```

- `BaseModel` implements shared pagination, filtering, CRUD, aggregation, and serialization helpers. Prefer using existing helpers before adding new query plumbing.

## Frontend Notes

Both frontends use:

- Vue 3
- Vite
- Element Plus
- Pinia
- Vue Router
- Axios
- Sass

The user-facing app is in `templates/front/src`; admin is in `templates/front/admin/src`. Each has its own `package.json`, `package-lock.json`, `vite.config.js`, and `dist`.

Generated `dist` output is served by Django when present. Prefer editing `src` and rebuilding, not hand-editing files in `dist`, unless the user explicitly asks for a one-off built-output change.

## Encoding Warning

Several Python files contain mojibake in comments and string literals. Be careful when editing:

- Preserve existing file encoding and line endings where possible.
- Do not mass-reformat files just to clean comments.
- Avoid touching unrelated garbled text because some string literals may be used as behavior flags.

## Safety Notes For Agents

- This workspace has no `.git` directory, so there is no local VCS safety net.
- Make narrowly scoped edits and avoid generated/cache files such as `__pycache__`, `dist`, and uploaded media.
- Do not change `config.ini`, email credentials, payment keys, or database dumps unless explicitly requested.
- `dj2/settings.py` reads Alipay key files from `util/alipay_key/`; if those files are absent, importing settings may fail.
- Running migrations or initialization can modify the configured MySQL database. Confirm intent before destructive or reseeding operations.
- If testing backend behavior, prefer lightweight import/URL checks first, then run Django commands only when the database and key files are available.
