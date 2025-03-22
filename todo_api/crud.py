from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from todo_api import schemas
from . import models
from fastapi import HTTPException

# Todo一覧取得
def get_todos(db:Session, skip:int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

# todo_idをもとにTodoを取得
def get_todo_by_id(db: Session, todo_id: int): 
    todo = db.scalar(select(models.Todo).where(models.Todo.id == todo_id))
    if todo is None: 
        raise HTTPException(status_code=404, detail="Todo not found") 
    return todo

def update_todo(db: Session, todo_id: int, todo_update: schemas.Todo):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    # 対象データがなければ404エラーにするのが一般的です
    if db_todo is None:
        return None
    for key, value in todo_update.model_dump(exclude_unset=True).items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(
        title=todo.title,
        detail=todo.detail,
        deadline=todo.deadline,
        status=todo.status,
        create_date=todo.create_date,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todos(db: Session, todos: List[schemas.Todo]):
    todo_ids = [todo.id for todo in todos]
    db_todos = db.query(models.Todo).filter(models.Todo.id.in_(todo_ids)).all()
    if not db_todos:
        return None
    for db_todo in db_todos:
        db.delete(db_todo)
    db.commit()
    return db_todos
