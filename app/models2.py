# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, JSON, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Calendar(Base):
    __tablename__ = 'calendar'

    id = Column(Integer, primary_key=True, server_default=text("nextval('calendar_id_seq'::regclass)"))
    event_name = Column(String)
    event_location = Column(String)
    start_date = Column(String)
    end_date = Column(String)


class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, server_default=text("nextval('ratings_id_seq'::regclass)"))
    name = Column(String)
    fed = Column(String)
    rating = Column(String)
    byear = Column(String)
    git = Column(String)
    update = Column(DateTime)
    image_urls = Column(String)
    images = Column(JSON)
    image_paths = Column(String)
