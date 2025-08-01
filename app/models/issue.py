from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base


class IssuedPart(Base):
    __tablename__ = "issued_parts"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    spare_part_id = Column(Integer, ForeignKey("spare_parts.id"))
    quantity = Column(Integer, nullable=False)
    issued_at = Column(DateTime, default=datetime.utcnow)

    vehicle = relationship("Vehicle", back_populates="issued_parts")
    spare_part = relationship("SparePart", back_populates="issued_parts")
