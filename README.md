# 🚆 KPA Form API - FastAPI + PostgreSQL Project

This project is a backend API for managing **Bogie Checksheet** and **Wheel Specifications** forms, built with **FastAPI**, **SQLAlchemy**, **Pydantic v2**, and **PostgreSQL**.

---

## 📌 Features

- ✅ Create and retrieve **Bogie Checksheet** data
- ✅ Retrieve **Wheel Specification** data
- ✅ PostgreSQL database integration
- ✅ Pydantic v2 support with `model_config = ConfigDict(from_attributes=True)`
- ✅ Environment variables loaded using `python-dotenv`
- ✅ Modular structure with models, schemas, routes

---

## 🚀 Tech Stack

| Component      | Technology             |
|----------------|------------------------|
| Framework      | FastAPI                |
| ORM            | SQLAlchemy             |
| Validation     | Pydantic v2            |
| Database       | PostgreSQL             |
| Server         | Uvicorn                |
| Env Management | python-dotenv          |

---

## 🏗️ Project Structure


kpa_api/
├── app/
│ ├── models/
│ │ ├── init.py
│ │ ├── bogie_checksheet.py
│ │ └── wheel_specification.py
│ │
│ ├── routes/
│ │ ├── init.py
│ │ ├── bogie_checksheet.py
│ │ └── wheel_specification.py
│ │
│ ├── schemas/
│ │ ├── init.py
│ │ ├── bogie_checksheet.py
│ │ └── wheel_specification.py
│ │
│ ├── database.py
│ ├── models.py # Optional aggregator (if used)
│ └── schemas.py # Optional aggregator (if used)
│
├── btmdj1/ # Virtual environment (local)
│
├── .env # Environment variables
├── create_tables.py # Script to create all tables
├── seed_data.py # Optional: for inserting sample data
├── main.py # App entry point
├── requirements.txt
└── README.md




📫 API Endpoints

🔸 Wheel Specification - GET

GET /api/forms/wheel-specifications

✅ Response


[
  {
    "id": 1,
    "wheel_number": "W1234",
    "diameter": 840,
    "condition": "Good",
    "checked_by": "John Doe"
  }
]


🔸 Bogie Checksheet - POST

POST /api/forms/bogie-checksheet

{
  "form_type": "Initial",
  "workshop_name": "XYZ Workshop",
  "coach_type": "Sleeper",
  "coach_number": "S12",
  "bogie_number": "B123",
  "date": "2025-07-22",
  "remarks": "All good"
}


## 📬 Postman Collection

You can test the implemented APIs using the Postman collection:

🔗 [Download Postman Collection](https://drive.google.com/file/d/1lrg5rcAaegg8Sv_uKo-R3eBLBW2AyZTI/view?usp=drive_link)

Includes:
- ✅ GET: /api/forms/wheel-specifications
- ✅ POST: /api/forms/bogie-checksheet
- 📌 Sample responses and payloads



🧠 Important Notes

Pydantic v2 uses model_config = ConfigDict(from_attributes=True) instead of Config: orm_mode = True.

Make sure PostgreSQL is installed and running.

Tables must be created manually or using Alembic migrations (not covered here).



✅ Dependencies


fastapi
uvicorn
sqlalchemy
pydantic>=2.0,<3.0
python-dotenv
psycopg[binary]


📞 Contact
If you have any questions or need help, feel free to reach out!

Phone : 63029949922


