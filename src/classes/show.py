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
from src.classes.base import Base
from src.classes.venue import Venue


class Show(Base):
    __tablename__ = "shows"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    remastered = Column(Boolean, default=False)
    sbd = Column(Boolean, default=False)
    venue_id = Column(Integer, ForeignKey("venues.id"))
    venue = relationship("Venue", back_populates="venue_shows")
    tour_id = Column(Integer, ForeignKey("tours.id"))
    likes_count = Column(Integer, default=0)
    incomplete = Column(Boolean, default=False)
    admin_notes = Column(Text)
    duration = Column(Integer, nullable=False, default=0)
    taper_notes = Column(Text)
    tags_count = Column(Integer, default=0)
    published = Column(Boolean, nullable=False, default=False)
    venue_name = Column(String, nullable=False, default="")

    def __repr__(self):
        # format is Date as Month DD, YYYY - Venue Name
        return f"{self.date.strftime('%B %d, %Y')} - {self.venue_name}"
