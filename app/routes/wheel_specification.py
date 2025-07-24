# app/routes/wheel_specification.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import WheelSpecification
from app.schemas import WheelSpecificationOut
from app.database import get_db

router = APIRouter()

@router.get("/api/forms/wheel-specifications", response_model=list[WheelSpecificationOut])
def get_wheel_specs(db: Session = Depends(get_db)):
    wheels = db.query(WheelSpecification).all()
    return [WheelSpecificationOut.model_validate(w) for w in wheels]  # ✅ Manual validation
