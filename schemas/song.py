from typing import Optional

from pydantic import BaseModel


class Song(BaseModel):
    id: Optional[int] = None
    name: str
    path: str
    plays: int
