from app.database import SessionLocal
from app.models.wheel_specification import WheelSpecification

# Create DB session
db = SessionLocal()

# Create one sample entry
sample = WheelSpecification(
    wheel_number="W003",
    diameter=852,
    condition="Not Good",
    checked_by="Inspector 2"
)

# Add and commit
db.add(sample)
db.commit()
db.close()

print("Sample data inserted.")
