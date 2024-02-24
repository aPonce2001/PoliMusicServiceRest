from typing import List

from fastapi import APIRouter
from sqlalchemy import literal_column
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from config.db import conn
from models.song import songs
from schemas.song import Song

song = APIRouter(prefix="/songs", tags=["songs"])


@song.get("")
def get_all_songs() -> List[Song]:
    with Session(conn) as session:
        result = session.execute(songs.select()).fetchall()
        if result is None:
            return []
        return [Song(id=result[i][0], name=result[i][1], path=result[i][2], plays=result[i][3]) for i in range(len(result))]


@song.get("/{id}")
def get_song(song_id) -> Song:
    with Session(conn) as session:
        result = session.execute(songs.select().where(songs.c.ID_SONG == song_id)).fetchone()
        if result is None:
            return JSONResponse(status_code=404, content={"message": "Song not found"})
        return Song(id=result[0], name=result[1], path=result[2], plays=result[3])


@song.post("", status_code=201)
async def create_song(new_song: Song):
    song_to_insert = {
        "SONG_NAME": new_song.name,
        "SONG_PATH": new_song.path,
        "PLAYS": new_song.plays
    }
    with Session(conn) as session:
        result = session.execute(songs.insert().values(song_to_insert).returning(songs.c.ID_SONG))
        session.commit()
        new_song.id = result.scalar()
        return new_song


@song.put("/{id}")
def update_song(song_id, updated_song: Song):
    with Session(conn) as session:
        session.execute(
            songs.update()
            .where(songs.c.ID_SONG == song_id)
            .values(
                SONG_NAME=updated_song.name,
                SONG_PATH=updated_song.path,
                PLAYS=updated_song.plays
            )
        )
        session.commit()
        return updated_song


@song.delete("/{id}")
def delete_song(song_id):
    with Session(conn) as session:
        session.execute(songs.delete().where(songs.c.ID_SONG == song_id))
        session.commit()


