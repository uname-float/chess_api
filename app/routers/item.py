from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.models import ChessEvent
from app.services.chess_event_service import ChessEventService

router = APIRouter()
chess_event_service = ChessEventService()

@router.get("/events", response_model=List[ChessEvent])
async def get_chess_events():
    return await chess_event_service.get_chess_events()

@router.post("/events", response_model=ChessEvent)
async def create_chess_event(event: ChessEvent):
    return await chess_event_service.create_chess_event(event)

