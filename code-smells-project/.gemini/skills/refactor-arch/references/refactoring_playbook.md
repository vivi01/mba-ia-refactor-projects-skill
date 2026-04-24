# Refactoring Playbook

Transformation patterns for common anti-patterns.

## 1. Extract Business Logic to Controller
**Before:**
```python
@app.route('/order')
def process_order():
    user = db.get_user(session['id'])
    items = request.json['items']
    total = sum(i['price'] for i in items) # Business Logic
    db.save_order(user, items, total)
    return jsonify(success=True)
```
**After:**
```python
# controllers/order_controller.py
def handle_process_order(user_id, items):
    user = model.get_user(user_id)
    total = calculation_service.calculate_total(items)
    return model.save_order(user, items, total)

# routes.py
@app.route('/order')
def process_order():
    result = order_controller.handle_process_order(session['id'], request.json['items'])
    return jsonify(result)
```

## 2. Replace Hardcoded Config with Environment Variables
**Before:** `DB_URL = "sqlite:///prod.db"`
**After:** `DB_URL = os.getenv("DATABASE_URL", "sqlite:///dev.db")`

## 3. Parametrize SQL Queries
**Before:** `cursor.execute("SELECT * FROM users WHERE name = '" + name + "'")`
**After:** `cursor.execute("SELECT * FROM users WHERE name = ?", (name,))`

## 4. Centralize Error Handling
**Before:** Every route has a `try/except` block.
**After:** Global error handler (e.g., `@app.errorhandler(Exception)`) that logs and returns standard JSON.

## 5. Implement Dependency Injection (Simple)
**Before:** `self.db = SQLiteDatabase()` inside a constructor.
**After:** `def __init__(self, database_service): self.db = database_service`

## 6. Fix N+1 Query (Eager Loading)
**Before:** `for user in users: get_profile(user.id)`
**After:** `users = db.query(User).options(joinedload(User.profile)).all()`

## 7. Replace Magic Numbers with Constants
**Before:** `if status == 3: ...`
**After:** `STATUS_SHIPPED = 3; if status == STATUS_SHIPPED: ...`

## 8. Update Deprecated APIs
**Before (Flask):** `from flask import escape` (deprecated in some contexts for `markupsafe`)
**After:** `from markupsafe import escape`
