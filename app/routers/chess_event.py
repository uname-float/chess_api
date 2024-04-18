# routers/chess_event.py

from fastapi import APIRouter, Depends
from typing import List
from app.models import Calendar
from app.services.chess_event_service import ChessEventService

from app.db import get_database

router = APIRouter()

@router.get("/events", response_model=List[Calendar])
async def get_chess_events(db = Depends(get_database)):
    chess_event_service = ChessEventService(db)
    return await chess_event_service.get_chess_events()
