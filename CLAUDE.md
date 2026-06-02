# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```powershell
# Backend
pip install -r requirements.txt
python manage.py runserver --insecure 0.0.0.0:8080 --noreload
python manage.py test <app>              # Django test runner
python init.py initdb                    # Create MySQL database
python init.py initsql                   # Load SQL dump into database
python manage.py makemigrations
python manage.py migrate --fake-initial

# Frontend (user-facing)
cd templates/front
npm install
npm run serve        # Vite dev on port 8082
npm run build

# Frontend (admin)
cd templates/front/admin
npm install
npm run serve        # Vite dev on port 8081
npm run build
```

No linting/formatting tools are configured.

## Project Architecture

**Stack**: Django 5.2 + MySQL + two independent Vue 3/Vite SPAs (user-facing + admin panel).

### Directory Layout

| Directory | Role |
|-----------|------|
| `dj2/` | Django project settings, root URL routing, WSGI, static file serving |
| `main/` | Primary Django app — ORM models (`models.py`), base model (`model.py`), 30+ `*_v.py` view modules |
| `xmiddleware/` | Custom middleware: parameter normalization (`xparam.py`), token auth (`xauth.py`), Hive support |
| `util/` | Shared helpers: auth, codes, JSON encoder, file encryption, Baidu AI API, HDFS/Hive/Spark/MapReduce connectors |
| `db/` | MySQL schema/seed dump (`djangoq0l722c8.sql`) |
| `templates/front/` | User-facing Vue 3 SPA source (`src/`) and build output (`dist/`) |
| `templates/front/admin/` | Admin Vue 3 SPA source and build output |
| `templates/upload/` | Uploaded files |
| `media/` | Static media assets |

### API Pattern

Routes are auto-generated from `main/*_v.py` files (except `schema_v.py` and `config_v.py`):
`/<dbName>/<tableName>/<action>` where actions include `page`, `list`, `save`, `add`, `update`, `delete`, `info/<id>`, `detail/<id>`, `thumbsup/<id>`, `vote/<id>`, `importExcel`, `autoSort`.

Extra endpoints (login, register, chart aggregation, websocket, upload/encrypt) are added per-module.

### View Convention

- Each `*_v.py` covers one business domain (e.g., `Yonghu_v.py`, `Chongwuxinxi_v.py`).
- View functions are named `<lowercase_table>_<action>` (e.g., `yonghu_page`, `chongwuxinxi_save`).
- Request params arrive via `request.session["req_dict"]` (normalized by `xparam` middleware).
- Auth via Base64-encoded token in `HTTP_TOKEN` header (handled by `xauth` middleware + `util/auth.py`).
- Response shape: `{"code": <int>, "msg": <str>, "data": <any>}`.

### Model Convention

- All business models in `main/models.py` inherit from `main.model.BaseModel`.
- Model/table names are pinyin-style lower-case (e.g., `yonghu`, `chongwuxinxi`, `fuwudingdan`).
- Feature flags on model classes: `__tablename__`, `__loginUser__`, `__authTables__`, `__foreEndList__`.

### Frontend

Both SPAs use Vue 3 + Vite + Element Plus + Pinia + Vue Router + Axios + Sass. They share no components; each is self-contained. `dist/` directories are generated — edit `src/` then rebuild; do not hand-edit `dist/`.

### Business Domains (from models)

users, shop staff, pet info, pet services, pet orders, pet products, pet interaction, service orders, foster care, foster orders, adoption pets, adoption applications, for-sale pets, health data, redemption gifts, forum posts/comments, discuss tables, favorites, chat, chat orders, product orders, shipping records, refund requests, news, system intro, email verification codes.

### Big Data Layer

HDFS, Hive, Spark, and MapReduce integration helpers live in `util/`. Database-to-Hive DDL conversion, query execution, and a CLI bootstrapper (`init.py`) support running analytics on Hadoop clusters alongside the primary MySQL database.

## Key Constraints

- `config.ini` stores DB/Redis credentials (gitignored). Commands requiring the database may fail if MySQL isn't running.
- `util/alipay_key/` contains payment keys (gitignored). `dj2/settings.py` reads them at import time.
- Several Python files contain mojibake in comments/strings — preserve encoding, do not mass-reformat.
- The `AGENT.md` file exists but still references Django 2.0; the project now runs Django 5.2.
- `.understand-anything/` contains knowledge graph analysis output from the Understand-Anything plugin.
