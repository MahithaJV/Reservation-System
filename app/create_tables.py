# create_tables.py
# Make sure this is at the app root level, not inside app folder
from database import engine
from models import Base

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")