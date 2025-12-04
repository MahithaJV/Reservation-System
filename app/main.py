from fastapi import FastAPI
from .routers import users, tables, booking
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(tables.router)
app.include_router(booking.router)

@app.get("/")
def home():
    return {"message": "Reservation API working!"}
