from pydantic import BaseModel,ConfigDict

class WheelSpecificationOut(BaseModel):
    id: int
    wheel_number: str
    diameter: int
    condition: str
    checked_by: str

    model_config = ConfigDict(from_attributes=True)
    
