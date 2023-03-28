from .base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class SongTrack(Base):
    __tablename__ = "songs_tracks"
    song_id = Column(Integer, ForeignKey("songs.id"), primary_key=True)
    track_id = Column(Integer, ForeignKey("tracks.id"), primary_key=True)

    song = relationship("Song", back_populates="songtracks")
    track = relationship("Track", back_populates="songtracks")
