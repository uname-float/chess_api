from app.models import Calendar
from typing import List
from app import models, schemas

class ChessEventService:
    def __init__(self, db):
        self.db = db

    async def get_chess_events(self) -> List[Calendar]:
        # Logica per recuperare gli eventi di scacchi dal database
        query = "SELECT * FROM calendar"
        return await self.db.fetch_all(query)



