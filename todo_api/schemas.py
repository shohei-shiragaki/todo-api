from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime, timezone

class TodoCreate(BaseModel):
    title: str = Field(max_length=50)
    detail: Optional[str]= Field(max_length=200)
    deadline: datetime
    status: bool
    create_date: Optional[datetime] = None

    def validate_deadline(self):
        if not self.deadline.tzinfo:
            self.deadline = self.deadline.replace(tzinfo=timezone.utc)
        
        if self.deadline <= datetime.now(timezone.utc):
            raise ValueError('締め切りは現在の日時より後でなければなりません')

class TodoUpdate(BaseModel):
    id: int
    title: str = Field(max_length=50)
    detail: Optional[str]= Field(max_length=200)
    deadline: datetime
    status: bool
    create_date: Optional[datetime] = None

    def validate_deadline(self):
        if not self.deadline.tzinfo:
            self.deadline = self.deadline.replace(tzinfo=timezone.utc)


class Todo(TodoCreate):  # TodoCreateを継承している
    id: int
    
    class Config:
        from_attributes = True
    
    def __init__(self, **data):
        super().__init__(**data)
        self.validate_deadline()
