from fastapi import FastAPI

app = FastAPI()

visits = [
    {"visit_id": "VIS-25-0001", "patient_id": "PAT-25-001", "diagnosis": "Diabetes", "cost": 250},
    {"visit_id": "VIS-25-0002", "patient_id": "PAT-25-002", "diagnosis": "Fracture", "cost": 400},
]

billing = [
    {"billing_id": "FIN-25-0001", "visit_id": "VIS-25-0001", "status": "Paid"},
    {"billing_id": "FIN-25-0002", "visit_id": "VIS-25-0002", "status": "Pending"},
]

@app.get("/")
def root():
    return {"message": "Healthcare API is running 🚀"}

@app.get("/visits")
def get_visits():
    return visits

@app.get("/billing")
def get_billing():
    return billing
