from fastapi import FastAPI
from app import models
from app.routers import users, tables, booking
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Reservation System")

app.include_router(users.router)
app.include_router(tables.router)
app.include_router(booking.router)

@app.get("/")
def root():
    return {"message": "Reservation API Running!"}
