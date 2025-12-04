from pydantic import BaseModel
import datetime

class UserCreate(BaseModel):
    name: str
    email: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True


class TableCreate(BaseModel):
    number: int
    capacity: int

class TableOut(BaseModel):
    id: int
    number: int
    capacity: int
    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    user_id: int
    table_id: int

class BookingOut(BaseModel):
    id: int
    user_id: int
    table_id: int
    time: datetime.datetime
    class Config:
        from_attributes = True

