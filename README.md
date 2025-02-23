# FastAPI Blog Project

This is a FastAPI-based blog project that includes database integration, API routing, and schema validation. It also utilizes Alembic for database migrations.

## Project Explanation
This project is a simple blog application built using FastAPI. It allows users to create, read, update, and delete blog posts. The application is designed with a modular structure, making it easy to scale and maintain. The database models define the structure of blog posts, while the Pydantic schemas handle request validation. API routes are organized within the `routers/` directory to keep the codebase clean. Alembic is used for database version control, allowing smooth migrations when updating models.

## Project Structure

```
blog/
│-- alembic/           # Database migration files
│-- alembic.ini        # Alembic configuration file
│-- database.py        # Database connection setup
│-- main.py            # Main FastAPI application
│-- models.py          # Database models
│-- routers/           # API route definitions
│-- schemas.py         # Pydantic schemas for request validation
│-- __init__.py        # Package initialization file
│-- __pycache__/       # Compiled Python files

requirements.txt      # Project dependencies
initial migration process.txt  # Notes on the initial migration process
```

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/srkthe27/Python_FastApi.git
cd blog
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# On Windows use `venv\Scripts\activate`
source venv/bin/activate  
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
Modify `database.py` with your database credentials, then apply migrations:
```bash
alembic upgrade head
```

### 5. Run the FastAPI Application
```bash
uvicorn main:app --reload
```

## API Documentation
Once the server is running, you can access API docs at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License
This project is licensed under the MIT License.

