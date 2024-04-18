#crud.py
from sqlalchemy.orm import Session
import models, schemas

def get_calendar(db: Session):
    return db.query(models.Calendar).all()
