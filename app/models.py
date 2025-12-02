# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
# Remove this import: from .database import Base
# Add this instead:
from app.database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    
    reservations = relationship("Reservation", back_populates="user")

class Slot(Base):
    __tablename__ = "slots"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    
    reservations = relationship("Reservation", back_populates="slot")

class Reservation(Base):
    __tablename__ = "reservations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    slot_id = Column(Integer, ForeignKey("slots.id"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    user = relationship("User", back_populates="reservations")
    slot = relationship("Slot", back_populates="reservations")