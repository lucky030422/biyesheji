# Repository Guidelines

## Project Structure & Module Organization

This repository is a Django 5.2 project with two Vue 3/Vite frontends. `manage.py` is the Django entrypoint. `dj2/` contains project settings, root URL routing, and WSGI setup. `main/` is the primary Django app; business endpoints are split across `*_v.py` files, with shared models in `models.py` and helper ORM code in `model.py`. `util/` contains shared configuration, auth, encoding, SQL, and external-service helpers. `xmiddleware/` contains request middleware. `tests/` contains backend runtime tests. `templates/front/` is the user frontend, and `templates/front/admin/` is the admin frontend; their `dist/` folders are build outputs. `db/` stores SQL initialization data, while `media/` stores uploaded files.

## Build, Test, and Development Commands

Install Python dependencies:

```powershell
pip install -r requirements.txt
```

Run Django locally:

```powershell
python manage.py runserver --insecure 0.0.0.0:8080 --noreload
```

Run backend tests:

```powershell
python -m unittest discover tests
```

Initialize database content when a MySQL instance matching `config.ini` is available:

```powershell
python init.py initdb
python init.py initsql
```

For either frontend, run commands from `templates/front` or `templates/front/admin`:

```powershell
npm install
npm run serve
npm run build
```

## Coding Style & Naming Conventions

Use 4-space indentation for Python and keep Django code close to existing patterns. Preserve the generated module naming style in `main/`, including capitalized entity view files such as `Users_v.py` and `Chongwufuwu_v.py`. Prefer environment variables for secrets already read in `dj2/settings.py`. For Vue code, follow the existing Vite structure, use package scripts, and respect the checked-in `.prettierrc` files.

## Testing Guidelines

Backend tests use Python `unittest`; name files `test_*.py` and keep them under `tests/` for discovery. Add focused tests for runtime compatibility, settings changes, middleware behavior, or API logic touched by a change. Database-dependent tests require a valid MySQL configuration in `config.ini`; document that requirement when adding them.

## Commit & Pull Request Guidelines

Recent commits use short, scoped summaries; examples include dependency cleanup and `Upgrade runtime to Django 5.2`. Keep commit messages focused on one change. Pull requests should include a clear description, commands run, database or frontend build impact, linked issues if any, and screenshots for visible UI changes.

## Security & Configuration Tips

Do not commit real secrets, private keys, or production credentials. `config.ini` controls database access, and `dj2/settings.py` reads several credentials from environment variables. Treat `media/`, generated frontend `dist/` output, and `node_modules/` as high-churn areas; edit them only when the task specifically requires it.
