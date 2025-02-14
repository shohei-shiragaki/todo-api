from typing import Optional
from pydantic import BaseModel, Field
import datetime

class TodoCreate(BaseModel):
    title: str = Field(max_length=50)
    detail: Optional[str]= Field(max_length=200)
    deadline: datetime.datetime
    status: bool
    create_date: datetime.datetime

    def validate_deadline(self):
        if self.deadline <= datetime.datetime.now():
            raise ValueError('締め切りは現在の日時より後でなければなりません')

class Todo(TodoCreate):  # TodoCreateを継承している
    id: int
    
    class Config:
        from_attributes = True
    
    def __init__(self, **data):
        super().__init__(**data)
        self.validate_deadline()
