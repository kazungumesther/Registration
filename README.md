# School Registration System 

A backend application built with **FastAPI** to manage a school registration system. This project has been refactored from a simple CRUD setup into a clean, **layered architecture** to ensure separation of concerns, scalability, and ease of maintainability.

## Project Description
This backend project handles full CRUD (Create, Read, Update, Delete) operations for managing core school entities, including **Students**, **Teachers**, and **Courses**. 

By decoupling the codebase into distinct layers, each entity strictly maintains its operations across independent files:
*   **Routers (API Layer):** Handles incoming HTTP requests, defines API endpoints, and manages request/response lifecycles.
*   **Services (Business Logic Layer):** Houses the core business rules and processes data before communication with the database.
*   **Repositories (Data Access Layer):** Direct database operations and raw SQL queries to fetch or persist entity data.

---

## Directory Structure

```text
Registration/
└── app/
    ├── __pycache__/
    ├── models/          # Relational database models
    ├── repositories/    # Data access layer (SQL queries)
    ├── routers/         # API endpoints and route definitions
    ├── schemas/         # Pydantic models for data validation (DTOs)
    ├── services/        # Business logic layer
    ├── database.py      # Database connection and session engine
    └── main.py          # FastAPI application entry point
```

---

## Core Entities & Features

The system supports the following entities, each containing at least 5 distinct attributes and full CRUD functionality:
*   **Students:** Manage enrollment details, personal data, and registration statuses.
*   **Teachers:** Tracking staff records, department assignments, and contact configurations.
*   **Courses:** Handling curriculum data, credit weighting, and department scheduling.

---

## Getting Started

### Prerequisites
*   Python 3.10+
*   PostgreSQL (or SQLite for local development)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Registration
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your database configuration:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/school_db
   ```

### Running the Application
Start the local development server using Uvicorn:
```bash
uvicorn app.main:app --reload
```
The server will start at `http://127.0.0.1:8000`.

---

## API Documentation & Testing

Once the server is up and running, you can interact with and test all the backend endpoints using the built-in interactive **Swagger UI**:
*   **Interactive Documentation:** [http://127.0.0](http://127.0.0)
*   **Alternative Schema Docs (ReDoc):** [http://127.0.0](http://127.0.0)
