
from sqlalchemy import Column, Integer, String, Date, Text
from app.database import Base

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"

    id = Column(Integer, primary_key=True, index=True)
    form_type = Column(String(100), nullable=False)
    workshop_name = Column(String(100), nullable=False)
    coach_type = Column(String(100), nullable=False)
    coach_number = Column(String(50), nullable=False)
    bogie_number = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    remarks = Column(Text, nullable=True)


# GET API

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    wheel_number = Column(String, nullable=False)
    diameter = Column(Integer, nullable=False)
    condition = Column(String, nullable=False)
    checked_by = Column(String, nullable=False)