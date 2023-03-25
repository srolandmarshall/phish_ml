from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Float, JSON
from sqlalchemy.orm import relationship
from .base import Base


class Track(Base):
    __tablename__ = "tracks"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    position = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=False, default=0)
    set = Column(String, nullable=False)
    likes_count = Column(Integer, default=0)
    slug = Column(String, nullable=False)
    tags_count = Column(Integer, default=0)
    jam_starts_at_second = Column(Integer)
    audio_file_data = Column(Text)
    waveform_image_data = Column(Text)
    waveform_data = Column(JSON)
    waveform_max = Column(Float)

    # relate show to track
    show_id = Column(Integer, ForeignKey("shows.id"))
    show = relationship("Show", back_populates="tracks")

    def __repr__(self):
        return f"{self.title}"
