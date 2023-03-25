from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Tour(Base):
    __tablename__ = "tours"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    starts_on = Column(Date, nullable=False)
    ends_on = Column(Date, nullable=False)
    slug = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    shows_count = Column(Integer, default=0)

    # relate to show
    shows = relationship("Show", back_populates="tour")

    def __repr__(self):
        # format is Tour Name
        return f"{self.name}"
