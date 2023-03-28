from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from .base import Base
from .songtrack import SongTrack
from .track import Track


class Show(Base):
    __tablename__ = "shows"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    remastered = Column(Boolean, default=False)
    sbd = Column(Boolean, default=False)
    likes_count = Column(Integer, default=0)
    incomplete = Column(Boolean, default=False)
    admin_notes = Column(Text)
    duration = Column(Integer, nullable=False, default=0)
    taper_notes = Column(Text)
    tags_count = Column(Integer, default=0)
    published = Column(Boolean, nullable=False, default=False)
    venue_name = Column(String, nullable=False, default="")
    setlist = Column(Text)

    # relate venue to show
    venue_id = Column(Integer, ForeignKey("venues.id"))
    venue = relationship("Venue", back_populates="shows")

    # relate tour to show
    tour_id = Column(Integer, ForeignKey("tours.id"))
    tour = relationship("Tour", back_populates="shows")

    # relate tracks to show
    tracks = relationship("Track", back_populates="show")

    # relate songs to show via songtracks and tracks
    songs = relationship(
        "Song",
        secondary="songs_tracks",
        primaryjoin="and_(Song.id == SongTrack.song_id, "
        "SongTrack.track_id == Track.id, "
        "Track.show_id == Show.id)",
        back_populates="shows",
        viewonly=True,
    )

    # taper notes contains the setlist in an ordered list. Extract each of these into a list
    def setlist(self):
        # return an empty list if taper notes is empty
        if self.taper_notes is None:
            return []
        lines = self.taper_notes.split("\n")
        setlist = [line for line in lines if line.split(".")[0].isdigit()]
        return [line.split(".", 1)[1].strip() for line in setlist]

    def __repr__(self):
        return f"{self.date.strftime('%B %d, %Y')} - {self.venue_name} - {self.venue.city}, {self.venue.state}"
