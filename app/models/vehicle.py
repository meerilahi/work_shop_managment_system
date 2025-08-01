from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    issued_parts = relationship("IssuedPart", back_populates="vehicle", cascade="all, delete-orphan")
