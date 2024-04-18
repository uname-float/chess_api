# app/db.py

from databases import Database

def get_database() -> Database:
    database_url = "postgres://postgres:@192.168.1.49/fide_scrapy"  # Modifica con la tua URL del database
    database = Database(database_url)
    return database
