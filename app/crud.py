from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def create_table(db: Session, table: schemas.TableCreate):
    new_table = models.Table(number=table.number, capacity=table.capacity)
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table

def create_booking(db: Session, booking: schemas.BookingCreate):
    new_booking = models.Booking(user_id=booking.user_id, table_id=booking.table_id)
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking
