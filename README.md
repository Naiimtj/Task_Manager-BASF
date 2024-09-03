# Task Manager Application

## Overview

This is a simple Task Manager application designed to help users manage their tasks efficiently. The application is built using modern web technologies and is containerized using Docker. The backend uses PostgreSQL as the database.

## Features

- Create, read, update, and delete tasks.
- Categorize tasks by groups (e.g., To-Do, In Progress, Done).
- Assign priorities to tasks.
- Add labels/tags to tasks.
- Search tasks.

## Technology Stack

- **Backend:** FastApi
- **Frontend:** Node.js, Vue.js
- **Database:** PostgreSQL
- **Containerization:** Docker

## Prerequisites

- Docker installed on your local machine.
- Docker Compose installed.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Naiimtj/Task_Manager-BASF.git
cd Task_Manager-BASF
```

### 2. Set Up Environment Variables
Create a .env file in the root directory with the following content:

```bash
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=task_manager
```

### 3. Start the Application

Use Docker Compose to build and run the application:

```bash
docker-compose up --build
```

### 4. Access the Application
Once the containers are up and running, you can access the application at http://localhost:3000.

### 5. Access to Api
Once the containers are up and running, you can access the api at http://localhost:5000/docs.

### 6. Test the API

To test the API, first, enter the API container:

```bash
docker exec -it task_manager-basf-api-1 /bin/sh
```

Then, run the tests:

```bash
pytest
```
