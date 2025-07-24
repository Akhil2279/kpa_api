from pydantic import BaseModel,ConfigDict

class BogieChecksheetCreate(BaseModel):
    inspector_name: str
    bogie_number: str
    status: str
    remarks: str

class BogieChecksheetOut(BogieChecksheetCreate):
    id: int


model_config = ConfigDict(from_attributes=True)
    
