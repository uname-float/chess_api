from app.models import ChessEvent
from databases import Database
from typing import List

class ChessEventService:
    def __init__(self, db: Database):
        self.db = db

    async def get_chess_events(self) -> List[ChessEvent]:
        query = "SELECT * FROM chess_events"
        return await self.db.fetch_all(query)

    async def create_chess_event(self, event: ChessEvent) -> ChessEvent:
        query = "INSERT INTO chess_events (event_name, event_location, start_date, end_date) VALUES (:event_name, :event_location, :start_date, :end_date) RETURNING *"
        values = {
            "event_name": event.event_name,
            "event_location": event.event_location,
            "start_date": event.start_date,
            "end_date": event.end_date
        }
        result = await self.db.fetch_one(query=query, values=values)
        return ChessEvent(**result)

