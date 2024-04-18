# schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import Dict

class Calendar(BaseModel):
    id: int
    event_name: str
    event_location: str
    start_date: str
    end_date: str


class Ratings(Calendar):
    id: int
    name: str
    fed: str
    rating: str
    byear: str
    git: str
    update: str
    image_urls: str
    images: Dict
    image_paths: str

    class Config:
        orm_mode = True
