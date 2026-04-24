# MVC Architecture Guidelines

Rules for the target MVC structure.

## 1. Models (Data Layer)
- **Responsibility**: Define data structure (schemas), database interactions, and core business entities.
- **Rules**:
  - No routing or HTTP logic.
  - No HTML/View rendering.
  - Business logic related to data integrity belongs here.

## 2. Views / Routes (Interface Layer)
- **Responsibility**: Handle incoming requests and outgoing responses (JSON or HTML).
- **Rules**:
  - Should only delegate to Controllers.
  - Minimal logic (only request parsing and response formatting).
  - Define URL patterns and HTTP methods.

## 3. Controllers (Logic Layer)
- **Responsibility**: Orchestrate the flow between Models and Views.
- **Rules**:
  - Contains application-specific business logic.
  - Validates input from the View before passing to the Model.
  - Fetches data from Models and prepares it for the View.

## 4. General Principles
- **Separation of Concerns**: Each layer should only know about the layer directly below it.
- **Centralized Error Handling**: Use middleware or decorators to catch and format errors consistently.
- **Configuration**: All settings must come from environment variables or a dedicated config service.
