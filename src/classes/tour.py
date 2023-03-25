# turn this rails schema into a SQLAlchemy model
# create_table "tours", id: :serial, force: :cascade do |t|
#   t.string "name", limit: 255, null: false
#   t.date "starts_on", null: false
#   t.date "ends_on", null: false
#   t.string "slug", limit: 255, null: false
#   t.datetime "created_at", precision: nil, null: false
#   t.datetime "updated_at", precision: nil, null: false
#   t.integer "shows_count", default: 0
#   t.index ["ends_on"], name: "index_tours_on_ends_on", unique: true
#   t.index ["name"], name: "index_tours_on_name", unique: true
#   t.index ["slug"], name: "index_tours_on_slug", unique: true
#   t.index ["starts_on"], name: "index_tours_on_starts_on", unique: true
# end

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
