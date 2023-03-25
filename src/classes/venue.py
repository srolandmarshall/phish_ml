from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.orm import relationship
from src.classes.base import Base


class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    shows_count = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    abbrev = Column(String(255))

    shows = relationship("Show", back_populates="venue_shows")

    def __repr__(self):
        return f"Venue(id={self.id}, name='{self.name}', city='{self.city}', state='{self.state}', country='{self.country}', slug='{self.slug}')"
