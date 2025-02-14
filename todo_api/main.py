from typing import List
from sqlalchemy.orm import Session 
from fastapi import FastAPI,Depends,HTTPException
from todo_api import crud, models, schemas
from todo_api.databes import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

# データベースエンジンをもとにデータベースを作成している
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS設定の追加
origins = [
    "http://localhost:3000/",  # 開発環境
    "https://todo-app-nextjs-git-main-shiragaki-shoheis-projects.vercel.app/",  # 本番環境1
    "https://todo-app-nextjs-omega.vercel.app/"  # 本番環境2
]

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

@app.get("/", response_model=list[schemas.Todo])
async def get_todo_all(db: Session = Depends(get_db)):
    try:
        todos = crud.get_todos(db)
        return todos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/todos/{id}", response_model=schemas.Todo) 
def get_read_todo(id: int, db: Session = Depends(get_db)): 
    todo = crud.get_todo_by_id(db, id) 
    return todo

@app.put("/todos/{id}", response_model=schemas.Todo)
def update_todo(todo_update: schemas.Todo, db: Session = Depends(get_db)):
    todo = crud.update_todo(db, todo_id=todo_update.id, todo_update=todo_update)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.post("/todo-create", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@app.post("/todo-delete", response_model=List[schemas.Todo])
def delete_todos(todos: List[schemas.Todo], db: Session = Depends(get_db)):
    db_todos = crud.delete_todos(db, todos=todos)
    if db_todos is None:
        raise HTTPException(status_code=404, detail="Todos not found")
    return db_todos
