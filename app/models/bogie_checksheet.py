from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"

    id = Column(Integer, primary_key=True, index=True)
    form_type = Column(String, nullable=False)
    workshop_name = Column(String, nullable=False)
    coach_type = Column(String, nullable=False)
    coach_number = Column(String, nullable=False)
    bogie_number = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    remarks = Column(String, nullable=True)
