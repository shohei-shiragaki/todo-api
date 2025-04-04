from sqlalchemy import Boolean, Column,Integer,String,DateTime
from .database import Base

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    detail = Column(String)
    deadline = Column(DateTime)
    status = Column(Boolean)
    create_date = Column(DateTime)
