# from sqlalchemy import Column,ForeignKey,Integer,String,DateTime
from sqlalchemy import Boolean, Column,Integer,String,DateTime
from .databes import Base

# class User(Base):
#     __tablename__ = 'users'
#     user_id = Column(Integer, primary_key=True, index=True)
#     user_name = Column(String, unique=True, index=True)

# class Room(Base):
#     __tablename__ = 'rooms'
#     room_id = Column(Integer, primary_key=True, index=True)
#     room_name = Column(String, unique=True, index=True)
#     capacity = Column(Integer)

# class Booking(Base):
#     __tablename__ = 'bookings'
#     booking_id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.user_id', ondelete='Set NUll'),nullable=False)
#     room_id = Column(Integer, ForeignKey('rooms.room_id', ondelete='Set NUll'),nullable=False)
#     booked_num = Column(Integer)
#     start_datetime = Column(DateTime,nullable=False)
#     end_datetime = Column(DateTime,nullable=False)

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    detail = Column(String)
    deadline = Column(DateTime)
    status = Column(Boolean)
    create_date = Column(DateTime)
