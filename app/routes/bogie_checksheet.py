
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import BogieChecksheetCreate, BogieChecksheetOut
from app.models import BogieChecksheet
from app.database import get_db

router = APIRouter()

@router.post("/api/forms/bogie-checksheet", response_model=BogieChecksheetOut, status_code=status.HTTP_201_CREATED)
def create_bogie_checksheet(form_data: BogieChecksheetCreate, db: Session = Depends(get_db)):
    try:
        print("Received data:", form_data.dict())
        new_entry = BogieChecksheet(**form_data.dict())
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        print("Inserted entry:", new_entry)
        return new_entry
    except Exception as e:
        print("🔥 ERROR:", e)  # Print full error
        raise HTTPException(status_code=500, detail="Internal Server Error")
