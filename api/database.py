from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

URL_DATABASE = os.getenv("URL_DATABASE")

try:
    engine = create_engine(URL_DATABASE)
except Exception as e:
    print(f"Error creating engine: {e}")
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()