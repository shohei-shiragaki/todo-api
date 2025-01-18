# from typing import List

# # from pydantic import BaseModel, Field
from typing import List
from sqlalchemy.orm import Session 
# from . import crud, models, schemas

# from fastapi import FastAPI
# from . import crud, models
# from .databes  import SessionLocal,engine
from fastapi import FastAPI,Depends,HTTPException
from todo_api import crud, models, schemas
from todo_api.databes import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

# データベースエンジンをもとにデータベースを作成している
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS設定の追加
origins = [
    "http://localhost:3000",  # フロントエンドのURL
    "https://todo-api-aa9t.onrender.com"  # 必要に応じて他のオリジンを追加
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
    db_todo = crud.update_todo(db, todo_id=todo_update.id, todo_update=todo_update)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@app.post("/todo-create", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@app.post("/todo-delete", response_model=List[schemas.Todo])
def delete_todos(todos: List[schemas.Todo], db: Session = Depends(get_db)):
    db_todos = crud.delete_todos(db, todos=todos)
    if db_todos is None:
        raise HTTPException(status_code=404, detail="Todos not found")
    return db_todos

# # Read
# @app.get("/users", response_model=List[schemas.User])
# async def read_users(skip: int = 0,limit: int = 100,db:Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip,limit=limit)
#     return users

# @app.get("/rooms", response_model=List[schemas.Room])
# async def read_rooms(skip: int = 0,limit: int = 100,db:Session = Depends(get_db)):
#     rooms = crud.get_rooms(db, skip=skip,limit=limit)
#     return rooms

# @app.get("/bookings", response_model=List[schemas.Booking])
# async def read_bookings(skip: int = 0,limit: int = 100,db:Session = Depends(get_db)):
#     bookings = crud.get_bookings(db, skip=skip,limit=limit)
#     return bookings

# # Create
# @app.post("/users", response_model=schemas.User)
# async def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):
#     return crud.create_user(db=db,user=user)

# @app.post("/rooms", response_model=schemas.Room)
# async def create_room(room: schemas.RoomCreate, db:Session = Depends(get_db)):
#     return crud.create_room(db=db,room=room)

# @app.post("/bookings", response_model=schemas.Booking)
# async def create_booking(booking: schemas.BookingCreate, db:Session = Depends(get_db)):
#     return crud.create_booking(db=db,booking=booking)
