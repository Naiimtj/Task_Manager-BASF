from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from database import Base

class TaskGroup(Base):
    __tablename__ = 'taskGroup'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    # One-to-many relationship: allows access to all tasks within a group
    tasks = relationship("Task", back_populates="group")

class Task(Base):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)
    priority = Column(String, index=True)
    labels = Column(ARRAY(String), default=[])

    # Foreign key linking the task to a specific task group
    group_id = Column(Integer, ForeignKey("taskGroup.id"))
    
    # Many-to-one relationship: allows access to the group to which the task belongs
    group = relationship("TaskGroup", back_populates="tasks")

