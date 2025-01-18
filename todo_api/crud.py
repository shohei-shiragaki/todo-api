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
# # 予約一覧取得
# def get_bookings(db:Session, skip:int = 0, limit: int = 100):
#     return db.query(models.Booking).offset(skip).limit(limit).all()

# ユーザー登録
# def create_user(db:Session, user: schemas.User):
#     db_user = models.User(user_name=user.user_name)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# # 会議室登録
# def create_room(db:Session, room: schemas.Room):
#     db_room = models.Room(room_name=room.room_name, capacity=room.capacity)
#     db.add(db_room)
#     db.commit()
#     db.refresh(db_room)
#     return db_room

# # 予約登録
# def create_booking(db:Session, booking: schemas.Booking):
#     db_booked = db.query(models.Booking).\
#         filter(models.Booking.room_id == booking.room_id).\
#             filter(models.Booking.end_datetime > booking.start_datetime).\
#                 filter(models.Booking.start_datetime < booking.end_datetime).\
#                     all()
    
#     # 重複するデータがなければ登録
#     if len(db_booked) == 0:
#         db_booking = models.Booking(
#             user_id = booking.user_id,
#             room_id = booking.room_id,
#             booked_num = booking.booked_num,
#             start_datetime = booking.start_datetime,
#             end_datetime = booking.end_datetime
#         )
#         db.add(db_booking)
#         db.commit()
#         db.refresh(db_booking)
#         return db_booking
#     else:
#         raise HTTPException(status_code=404, detail="Already Booked")
