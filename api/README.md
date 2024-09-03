# FastAPI Project Installation and Configuration Documentation

## Prerequisites

Before starting, make sure you have the following installed on your system:

### Windows
1. **Python**: Download and install Python from [python.org](https://www.python.org/downloads/). Be sure to select the "Add Python to PATH" option during installation.
2. **Git** Git (optional but recommended): Install Git from [git-scm.com](https://git-scm.com/downloads) to clone repositories and manage versions.

### macOS
1. **Python**: You can install Python using Homebrew with the following command:
   ```bash
   brew install python
    ```
2. **Git** (optional but recommended): Install Git using Homebrew with:
   ```bash
   brew install git
    ```
## Virtual Environment Setup
### 1. Create the Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment

#### En Windows:

```bash
.\.venv\Scripts\activate
```
#### En macOS:

```bash
source .venv/bin/activate
```
## Dependency Installation
With the virtual environment activated, install the necessary dependencies with pip:
```bash
pip install fastapi uvicorn sqlalchemy asyncpg psycopg2-binary python-dotenv logging httpx pytest
```
## Project Configuration
1. **.env File**: (opcional):  If you use environment variables, create a .env file at the root of the project to store configurations such as the database URL. An example .env file could be:

```bash
DATABASE_URL=postgresql://user:password@localhost:5432/your_database
```
1. **Data Base**: Ensure your database is set up and accessible. The database.py file should be configured to connect to your PostgreSQL database.

## Running the FastAPI Server
To start the FastAPI development server, use the following command:

```bash
uvicorn main:app --port 5000 --reload
```
- `main`: This is the name of the Python file that contains the FastAPI instance (without the ".py" extension).
- `app`: This is the name of the FastAPI instance in your main.py file.
- `--port 5000`: Specifies the port on which the server will run (you can change the port number if needed).
- `--reload`: Enables auto-reload for development, which will restart the server when code changes are made.

## Accessing the Application
Once the server is running, you can access the API at:

```bash
http://localhost:5000
```
The interactive API documentation will be available at:

```bash
http://localhost:5000/docs
```
Or an alternative interface (Swagger UI) at:

```bash
http://localhost:5000/redoc
```

## Testing
```bash
pytest
```
