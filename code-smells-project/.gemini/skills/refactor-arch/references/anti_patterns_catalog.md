# Anti-Patterns Catalog

This catalog defines anti-patterns, their detection signs, and severity levels.

## 1. God Object / Fat Controller
- **Severity**: CRITICAL
- **Signs**: Classes or files with thousands of lines, handling multiple responsibilities (routing, logic, DB).
- **Impact**: Hard to test, maintain, and scale.

## 2. Hardcoded Configurations
- **Severity**: CRITICAL
- **Signs**: API keys, database credentials, or environment-specific URLs directly in the code.
- **Impact**: Security risk and deployment rigidity.

## 3. SQL Injection Vulnerability
- **Severity**: CRITICAL
- **Signs**: Building SQL queries using string concatenation with user input.
- **Impact**: Data breach and system compromise.

## 4. Business Logic in Routes/Views
- **Severity**: HIGH
- **Signs**: Complex calculations, validation, or DB queries directly inside route handlers.
- **Impact**: Lack of reusability and difficult unit testing.

## 5. Tight Coupling
- **Severity**: HIGH
- **Signs**: Direct instantiation of dependencies (e.g., `db = Database()`) instead of injection or abstraction.
- **Impact**: Difficult to mock for tests or swap implementations.

## 6. N+1 Query Problem
- **Severity**: MEDIUM
- **Signs**: Executing a query inside a loop for each item in a collection.
- **Impact**: Significant performance degradation as data grows.

## 7. Global State / Magic Numbers
- **Severity**: LOW
- **Signs**: Heavy use of global variables or numeric literals without context.
- **Impact**: Side effects and poor readability.

## 8. Deprecated APIs
- **Severity**: HIGH
- **Signs**: Use of outdated methods or libraries (e.g., `flask.escape` in Flask 3.x, `bodyParser()` in old Express).
- **Impact**: Compatibility issues, security bugs, and performance loss.
