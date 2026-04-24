# GEMINI Context: task-manager-api

## Project Overview
A Python/Flask Task Manager API. While it has some initial layer separation (`models/`, `routes/`, `services/`), it is intended for architectural refactoring to fix underlying quality issues.

## Technical Stack
- **Language:** Python
- **Framework:** Flask 3.0.0
- **ORM:** Flask-SQLAlchemy 3.1.1
- **Serialization:** Marshmallow
- **Database:** SQLite (tasks.db)

## Setup & Execution
1. Install dependencies: `pip install -r requirements.txt`
2. **Crucial:** Run seed script first: `python seed.py`
3. Run application: `python app.py`
4. Port: `http://localhost:5000`

## Key Information
- Failure to run `seed.py` will result in empty lists from endpoints.
- Features separation of concerns into models, routes, services, and utils, but still requires architectural improvements.
- Part of the `refactor-arch` challenge.
