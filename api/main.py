from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import List, Annotated, Optional
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import logging

# Logging config

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the database and create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.title="BASF - Task Api"
app.version="1.0.0"

# Dependency to get the session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]  


# Config CORS
origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request bodies
class TaskGroupSchema(BaseModel):
    name: str = Field(min_length=3, max_length=20)

class TaskSchemaCreate(BaseModel):
    title: str = Field(min_length=3, max_length=20)
    description: str = Field(max_length=40)
    completed: bool = Field(default=False)
    priority: str = Field(default='Low')
    labels: List[str]
    group_id: int = Field(ge=0)

class TaskSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[str] = None
    labels: Optional[List[str]] = None
    group_id: Optional[int] = None

# Mount a folder to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/', tags=['Home'], include_in_schema=False)
async def home():
    return "Hi!! Check '/docs' to see routes."

# FAVICON
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

# < ROUTES
# * SEARCH
@app.get('/tasks/search', tags=['Tasks'], response_model=List[TaskSchema])
async def search_tasks( db:db_dependency, title: Optional[str] = Query(None, description="Search by title")):
    query = db.query(models.Task)
    if title is None or title == "":
        return []

    if title.lower() == "alltasks":
        results = query.all()
    else:
        query = query.filter(models.Task.title.ilike(f'%{title}%'))
        results = query.all()
    
    if not results:
        raise HTTPException(status_code=404, detail="No title tasks found")

    return results

# - GET
# TASKS
@app.get("/tasks", tags=['Tasks'])
async def get_all_tasks(db:db_dependency):
    tasks = db.query(models.Task).all()
    return tasks

@app.get("/tasks/{id}", tags=['Tasks'])
async def get_detail_task(id: int, db:db_dependency):
    task = db.query(models.Task).filter(models.Task.id == id).all()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# TASKS GROUPS
@app.get("/task-groups/{group_id}/tasks", tags=['Task Group'])
async def get_tasks_by_group(group_id: int, db:db_dependency):
    tasks = db.query(models.Task).filter(models.Task.group_id == group_id).all()
    return tasks

@app.get("/task-groups", tags=['Task Group'])
async def get_all_task_groups(db:db_dependency):
    task_groups = db.query(models.TaskGroup).all()
    return task_groups

@app.get("/task-groups/{group_id}", tags=['Task Group'])
async def get_name_group(group_id: int, db:db_dependency):
    tasks = db.query(models.TaskGroup).filter(models.TaskGroup.id == group_id).all()
    if not task_group:
        raise HTTPException(status_code=404, detail="Task Group not found")
    return task_group

# . POST
# TASKS
@app.post('/tasks', tags=['Tasks'])
async def create_task(task:TaskSchemaCreate, db:db_dependency):
    task_group = db.query(models.TaskGroup).filter(models.TaskGroup.id == task.group_id).first()
    if not task_group:
        raise HTTPException(status_code=400, detail="Task Group not found")

    new_task = models.Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        priority=task.priority,
        labels=task.labels,
        group_id=task.group_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# TASKS GROUPS
@app.post("/task-groups", tags=['Task Group'])
async def create_task_group(group:TaskGroupSchema, db:db_dependency):
    new_group = models.TaskGroup(name=group.name)
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group

# * PUT
# TASKS
@app.put('/tasks/{id}', tags=['Tasks'])
async def update_task(id: int, task: TaskSchema, db: db_dependency):
    task_to_update = db.query(models.Task).filter(models.Task.id == id).first()

    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.group_id:
        task_group = db.query(models.TaskGroup).filter(models.TaskGroup.id == task.group_id).first()
        if not task_group:
            raise HTTPException(status_code=400, detail="Task Group not found")

    if task.title is not None:
        task_to_update.title = task.title
    if task.description is not None:
        task_to_update.description = task.description
    if task.completed is not None:
        task_to_update.completed = task.completed
    if task.priority is not None:
        task_to_update.priority = task.priority
    if task.labels is not None:
        task_to_update.labels = task.labels
    if task.group_id is not None:
        task_to_update.group_id = task.group_id

    db.commit()
    db.refresh(task_to_update)

    return task_to_update

# TASKS GROUPS
@app.put('/tasks-groups/{id}', tags=['Task Group'])
async def update_task_group(id: int, group: TaskGroupSchema, db: db_dependency):
    task_group_update = db.query(models.TaskGroup).filter(models.TaskGroup.id == id).first()
    if not task_group_update:
        raise HTTPException(status_code=400, detail="Task Group not found")
    
    task_group_update.name = group.name
    
    db.commit()
    db.refresh(task_group_update)
    
    return task_group_update

# ! DELETE
# TASKS
@app.delete('/tasks/{id}', tags=['Tasks'])
async def delete_task(id: int, db: db_dependency):
    task_to_delete = db.query(models.Task).filter(models.Task.id == id).first()
    
    if not task_to_delete:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task_to_delete)
    db.commit()
    
    return {"message": "Task deleted successfully"}

@app.delete('/tasks', tags=['Tasks'])
async def delete_all_tasks(db: db_dependency):
    # Fetch all tasks to delete
    tasks_to_delete = db.query(models.Task).all()

    if not tasks_to_delete:
        return {"message": "No tasks found to delete"}
    
    # Delete each task individually
    for task in tasks_to_delete:
        db.delete(task)
    
    db.commit()
    
    return {"message": "All tasks deleted successfully"}

# TASKS GROUPS
@app.delete('/task-groups/{id}', tags=['Task Group'])
async def delete_task_group(id: int, db: db_dependency):
    task_group_to_delete = db.query(models.TaskGroup).filter(models.TaskGroup.id == id).first()
    
    if not task_group_to_delete:
        raise HTTPException(status_code=404, detail="Task Group not found")

    tasks = db.query(models.Task).filter(models.Task.group_id == id).all()
    for task in tasks:
        db.delete(task)
    
    db.delete(task_group_to_delete)
    db.commit()
    
    return {"message": "Task Group deleted successfully"}

@app.delete('/task-groups', tags=['Task Group'])
async def delete_all_task_groups(db: db_dependency):
    task_groups_to_delete = db.query(models.TaskGroup).all()
    if not task_groups_to_delete:
        return {"message": "No tasks groups found to delete"}    
    for task_group in task_groups_to_delete:
        db.delete(task_group)
    db.commit()    
    return {"message": "All tasks groups deleted successfully"}