from fastapi import FastAPI, Depends
from typing import Annotated
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# < ROUTES
@app.get('/', tags=['Home'])
def home():
    return "Hi!! Check '/docs' to see routes."