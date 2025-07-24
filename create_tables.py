from app.database import  engine,Base
from app.models.wheel_specification import WheelSpecification
#from app.models.bogie_checksheet import BogieChecksheet

Base.metadata.drop_all(bind=engine)

Base.metadata.create_all(bind=engine)

print("✅ Tables dropped and re-created successfully.")