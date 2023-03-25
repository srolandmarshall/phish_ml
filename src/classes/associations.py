# associations.py
from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

songs_tracks = Table(
    "songs_tracks",
    Base.metadata,
    Column("song_id", Integer, ForeignKey("songs.id"), primary_key=True),
    Column("track_id", Integer, ForeignKey("tracks.id"), primary_key=True),
)
