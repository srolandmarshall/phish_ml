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

    # relate venue to show
    venue_id = Column(Integer, ForeignKey("venues.id"))
    venue = relationship("Venue", back_populates="shows")
    # relate tour to show
    tour_id = Column(Integer, ForeignKey("tours.id"))
    tour = relationship("Tour", back_populates="shows")

    # taper notes contains the setlist in an ordered list. Extract each of these into a list
    def setlist(self):
        lines = self.taper_notes.split("\n")
        # if line starts with one or more digits and is followed by a period, it's a setlist item
        setlist = [line for line in lines if line.split(".")[0].isdigit()]
        # drop the \r and the setlist number
        return [line.split(".", 1)[1].strip() for line in setlist]

    def __repr__(self):
        # format is Date as Month DD, YYYY - Venue Name - Venue City, Venue State
        return f"{self.date.strftime('%B %d, %Y')} - {self.venue_name} - {self.venue.city}, {self.venue.state}"
