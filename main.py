from typing import Optional, List
from datetime import datetime, date
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os


# FHIR HumanName Structure
class HumanName(BaseModel):
    use: str = "official"
    given: List[str]
    family: str


# FHIR Patient Resource
class PatientCreate(BaseModel):
    given: List[str]
    family: str
    birthDate: str
    gender: str


class FHIRPatient(BaseModel):
    resourceType: str = "Patient"
    id: str
    name: List[HumanName]
    birthDate: str
    gender: str


# FHIR Observation Resource
class FHIRObservationValue(BaseModel):
    value: str
    unit: Optional[str] = None


class FHIRObservation(BaseModel):
    resourceType: str = "Observation"
    id: str
    status: str = "final"
    code: dict
    subject: dict
    effectiveDateTime: str
    value: FHIRObservationValue


app = FastAPI(
    title="API Kesehatan",
    description="API untuk data pasien dan observasi format FHIR",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Hello, World!", "status": "ok"}


@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    # contoh data pasien statis dalam format FHIR
    patients = {
        1: {
            "resourceType": "Patient",
            "id": "1",
            "name": [{"use": "official", "given": ["John"], "family": "Doe"}],
            "birthDate": "1991-05-05",
            "gender": "male"
        },
        2: {
            "resourceType": "Patient",
            "id": "2",
            "name": [{"use": "official", "given": ["Annisa"], "family": "Maulida"}],
            "birthDate": "1998-05-05",
            "gender": "female"
        },
    }
    return patients.get(patient_id, {"resourceType": "OperationOutcome", "issue": [{"severity": "error", "code": "not-found"}]})


@app.post("/patients")
def create_patient(patient: PatientCreate):
    # Membuat FHIR Patient resource baru
    new_patient = {
        "resourceType": "Patient",
        "id": "3",
        "name": [{"use": "official", "given": patient.given, "family": patient.family}],
        "birthDate": patient.birthDate,
        "gender": patient.gender,
    }
    return {"resourceType": "Patient", "message": "Patient created", "patient": new_patient}


@app.get("/patients/{patient_id}/observations")
def get_patient_observations(patient_id: int):
    # contoh data observasi statis dalam format FHIR
    observations = {
        1: [
            {
                "resourceType": "Observation",
                "id": "1",
                "status": "final",
                "code": {
                    "coding": [{"system": "http://loinc.org", "code": "55284-4", "display": "Blood pressure"}],
                    "text": "blood_pressure"
                },
                "subject": {"reference": f"Patient/{patient_id}"},
                "effectiveDateTime": "2026-05-05T09:00:00Z",
                "value": {
                    "value": "120/80",
                    "unit": "mmHg"
                }
            },
            {
                "resourceType": "Observation",
                "id": "2",
                "status": "final",
                "code": {
                    "coding": [{"system": "http://loinc.org", "code": "8867-4", "display": "Heart rate"}],
                    "text": "heart_rate"
                },
                "subject": {"reference": f"Patient/{patient_id}"},
                "effectiveDateTime": "2026-05-05T09:05:00Z",
                "value": {
                    "value": "72",
                    "unit": "bpm"
                }
            },
        ],
        2: [
            {
                "resourceType": "Observation",
                "id": "3",
                "status": "final",
                "code": {
                    "coding": [{"system": "http://loinc.org", "code": "8310-5", "display": "Body temperature"}],
                    "text": "temperature"
                },
                "subject": {"reference": f"Patient/{patient_id}"},
                "effectiveDateTime": "2026-05-05T09:10:00Z",
                "value": {
                    "value": "36.7",
                    "unit": "°C"
                }
            },
        ],
    }
    return {
        "resourceType": "Bundle",
        "type": "searchset",
        "total": len(observations.get(patient_id, [])),
        "entry": [{"resource": obs} for obs in observations.get(patient_id, [])]
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
