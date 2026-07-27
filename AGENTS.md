# tarea_flask

## Stack

- **Framework:** Flask 3.1, Python 3.14
- **Package manager:** `uv` (see `uv.lock`, no `pip`/`poetry`)
- **Entrypoint:** `main.py` (defines `app = Flask(__name__)`, no `app.run()`)

## Running

```bash
uv sync                     # install dependencies into .venv
$env:FLASK_APP = "main"    # or set FLASK_APP=main
uv run flask --app main run --debug
```

`main.py` does **not** call `app.run()` — the app is run via `flask run`.

## Database

- **Engine:** SQLite3 via stdlib `sqlite3`
- **Location:** `instance/app.db` (Flask's instance folder, gitignored)
- **Init:** `init_db()` runs on import via `with app.app_context():`
- **Schema:** `users` table — see `main.py` for columns
- **Connection:** managed via `g` (per-request) + `teardown_appcontext`

## API

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Renders `templates/index.html` |
| `POST` | `/users` | Create user (JSON body: `dni`, `given_name`, `family_name`, `email` + optional `phone_number`, `address`) |

Responses: `201` on success, `400` if missing required fields, `409` if `dni`/`email` already exists.

## Testing & linting

None configured. No test framework, linter, or type checker is set up in `pyproject.toml`.

## Structure

```
main.py           # app definition, routes, DB init
templates/        # Jinja2 templates
instance/         # SQLite DB (gitignored)
pyproject.toml    # project metadata + deps
uv.lock           # lockfile (commit)
.python-version   # requires Python >=3.14
```

Single package, single entrypoint.
