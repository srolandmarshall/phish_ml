from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from .base import Base


class Song(Base):
    __tablename__ = "songs"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    slug = Column(String, nullable=False)
    tracks_count = Column(Integer, default=0)
    lyrical_excerpt = Column(String)
    original = Column(Boolean, default=False, nullable=False)
    alias = Column(String)
    lyrics = Column(Text)
    artist = Column(String)
    instrumental = Column(Boolean, default=False, nullable=False)

    # relate to tracks
    tracks = relationship(
        "Track", secondary="songs_tracks", back_populates="song", viewonly=True
    )

    # relate to shows via songtracks and tracks
    shows = relationship(
        "Show",
        secondary="songs_tracks",
        primaryjoin="and_(Song.id == SongTrack.song_id, SongTrack.track_id == Track.id)",
        secondaryjoin="Track.show_id == Show.id",
        back_populates="songs",
        viewonly=True,
    )

    # relate to songtracks
    songtracks = relationship("SongTrack", back_populates="song", viewonly=True)

    def __repr__(self):
        return f"{self.title}"
