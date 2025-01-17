from typing import Optional
from pydantic import BaseModel, Field
import datetime

class TodoCreate(BaseModel):
    title: str = Field(max_length=12)
    detail: str
    deadline: datetime.datetime
    status: bool
    create_date: datetime.datetime

class Todo(TodoCreate):  # TodoCreateを継承している
    id: int
    
    class Config:
        # orm_mode = True
        from_attributes = True

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    detail: Optional[str] = None
    deadline: Optional[datetime.datetime] = None
    status: Optional[bool] = None
    create_date: Optional[datetime.datetime] = None

    class Config:
        orm_mode = True