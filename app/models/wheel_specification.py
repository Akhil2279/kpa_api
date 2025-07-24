# app/models/wheel_specification.py

from sqlalchemy import Column, Integer, String
from app.database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specification"

    id = Column(Integer, primary_key=True, index=True)
    wheel_number = Column(String, nullable=False)
    diameter = Column(Integer, nullable=False)
    condition = Column(String, nullable=False)
    checked_by = Column(String, nullable=False)

