from typing import List
from sqlalchemy.orm import Session 
from fastapi import FastAPI,Depends,HTTPException
from todo_api import crud, models, schemas
from todo_api.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

# データベースエンジンをもとにデータベースを作成している
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 環境変数からORIGIN_URLSを取得し、カンマ区切りのリストとしてパース
origin_urls = os.getenv("ORIGIN_URLS").split(",")

# CORS設定の追加
origins = origin_urls

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos", response_model=list[schemas.Todo])
async def get_todo_all(db: Session = Depends(get_db)):
    try:
        todos = crud.get_todos(db)
        return todos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/todo/{id}", response_model=schemas.Todo) 
def get_read_todo(id: int, db: Session = Depends(get_db)): 
    try:
        todo = crud.get_todo_by_id(db, id) 
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/todo/{id}", response_model=schemas.TodoUpdate)
def update_todo(todo_update: schemas.TodoUpdate, db: Session = Depends(get_db)):
    try:
        todo = crud.update_todo(db, todo_id=todo_update.id, todo_update=todo_update)
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.post("/todo/create", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    try:
        db_todo = crud.create_todo(db=db, todo=todo)
        if db_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return db_todo
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/todos/delete", response_model=List[schemas.TodoDelete])
def delete_todos(todos: List[schemas.TodoDelete], db: Session = Depends(get_db)):
    try:
        db_todos = crud.delete_todos(db, todos=todos)
        if db_todos is None:
            raise HTTPException(status_code=404, detail="Todos not found")
        return db_todos
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
