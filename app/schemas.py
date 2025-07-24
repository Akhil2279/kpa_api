
from pydantic import BaseModel,ConfigDict
from datetime import date
from typing import Optional

class BogieChecksheetCreate(BaseModel):
    form_type: str
    workshop_name: str
    coach_type: str
    coach_number: str
    bogie_number: str
    date: date
    remarks: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class BogieChecksheetOut(BogieChecksheetCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


# GET API Schema
class WheelSpecificationOut(BaseModel):
    id: int
    wheel_number: str
    diameter: int
    condition: str
    checked_by: str

    model_config = ConfigDict(from_attributes=True)

