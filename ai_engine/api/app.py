from fastapi import FastAPI

from ai_engine.evidence.incident_query import (
    IncidentQuery
)

app = FastAPI(
    title="Campus Guardian AI",
    version="1.0.0"
)

query = IncidentQuery()


@app.get("/")
def home():
    return {
        "message": "Campus Guardian AI API Running"
    }


@app.get("/incidents")
def get_incidents():
    return query.load_incidents()