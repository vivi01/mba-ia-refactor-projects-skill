# Project Analysis Heuristics

This document provides heuristics for detecting the tech stack and architecture of a project.

## Language Detection
- **Python**: Presence of `*.py`, `requirements.txt`, `Pipfile`, `pyproject.toml`, `setup.py`.
- **JavaScript/Node.js**: Presence of `package.json`, `node_modules/`, `*.js`, `*.ts`.
- **Java**: Presence of `pom.xml`, `build.gradle`, `src/main/java`.
- **Go**: Presence of `go.mod`, `*.go`.

## Framework Detection
- **Flask (Python)**: `import flask`, `Flask(__name__)`, `flask` in `requirements.txt`.
- **Express (Node.js)**: `require('express')`, `import express`, `express` in `package.json`.
- **FastAPI (Python)**: `import fastapi`, `fastapi` in `requirements.txt`.
- **Django (Python)**: `manage.py`, `settings.py`, `django` in `requirements.txt`.

## Database Detection
- **SQLite**: Presence of `*.db`, `*.sqlite`, `sqlite3` in dependencies, connection strings using `sqlite:///`.
- **PostgreSQL**: `psycopg2`, `pg` in dependencies, connection strings with `postgresql://`.
- **MongoDB**: `pymongo`, `mongoose` in dependencies, connection strings with `mongodb://`.

## Architecture Mapping
- **Monolithic (Flat)**: Most logic in a single file or root directory (e.g., `app.py`, `server.js`).
- **MVC (Layered)**: Presence of `models/`, `views/`, `controllers/` directories.
- **Service-Oriented**: Presence of `services/`, `repositories/`, `api/` layers.
- **Legacy/Spaghetti**: Business logic mixed with route definitions and database queries in the same file.
