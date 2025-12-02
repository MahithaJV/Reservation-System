from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User

app = FastAPI(title="Reservation System")

@app.get("/")
def root(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {"users_count": len(users)}