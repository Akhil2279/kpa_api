
from fastapi import FastAPI
from app.routes import wheel_specification, bogie_checksheet

app = FastAPI()

# Register routes
app.include_router(wheel_specification.router)
app.include_router(bogie_checksheet.router)

@app.get("/")
def root():
    return {"message": "API running!"}