from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import declarative_base

from config.db import meta

songs = Table(
    'TBL_SONG', meta,
    Column('ID_SONG', Integer, primary_key=True),
    Column('SONG_NAME', String(50), nullable=False),
    Column('SONG_PATH', String(255), nullable=False),
    Column('PLAYS', Integer)
)
