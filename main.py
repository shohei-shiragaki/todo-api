# from typing import List
from fastapi import FastAPI
# from fastapi import FastAPI,Depends
# # from pydantic import BaseModel, Field
# from sqlalchemy.orm import Session 
# from . import crud, models, schemas
# from .databes  import SessionLocal,engine

# データベースエンジンをもとにデータベースを作成している
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

todoList = [
        { "id": "test1", "title": "Todo 1", "detail": "Detail 1", "deadline": "2025-01-01", "status": "完了" },
        { "id": "test2", "title": "Todo 2", "detail": "Detail 2", "deadline": "2025-01-15", "status": "未完了" },
        { "id": "test3", "title": "Todo 3", "detail": "Detail 3", "deadline": "2025-01-23", "status": "未完了" },
        { "id": "test4", "title": "Todo 4", "detail": "Detail 4", "deadline": "2025-02-23", "status": "完了" },
    ]

@app.get("/")
async def get_todo_all():
    return todoList

@app.get("/updateTodo/{id}")
async def get_todo_by_id(id: str):
    todo = [todo for todo in todoList if todo["id"] == id]
    return todo[0]






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
