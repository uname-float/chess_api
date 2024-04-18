from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine

#from app.routers import chess_event
from app import schemas, models, crud
from app.schemas import Calendar

app = FastAPI()

# Funzione per ottenere una sessione di database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the Chess Events API!"}

# Definisci l'endpoint API per ottenere gli eventi di scacchi
@app.get("/events/", response_model=list[schemas.Calendar])
def read_chess_events(db: Session = Depends(get_db)):
    ##-bad#return chess_event.get_chess_events(db)
    events = jsonable_encoder(db.query(models.Calendar).all())
    return JSONResponse(content=events)

# Definisci l'endpoint API per ottenere graduatoria/ELO di scacchi
@app.get("/ratings/", response_model=list[schemas.Calendar])
def read_chess_events(db: Session = Depends(get_db)):
    ##-bad#return chess_event.get_chess_events(db)
    events = jsonable_encoder(db.query(models.Calendar).all())
    return JSONResponse(content=events)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


