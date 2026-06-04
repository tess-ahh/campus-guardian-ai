from fastapi import FastAPI

from ai_engine.evidence.incident_query import IncidentQuery
from ai_engine.evidence.incident_stats import IncidentStats

app = FastAPI(
    title="Campus Guardian AI",
    version="1.0.0"
)

query = IncidentQuery()
stats = IncidentStats()


@app.get("/")
def home():
    return {
        "message": "Campus Guardian AI API Running"
    }


@app.get("/incidents")
def get_incidents():
    return query.load_incidents()


@app.get("/incidents/severity/{severity}")
def get_incidents_by_severity(severity: str):
    return query.get_by_severity(
        severity.upper()
    )


@app.get("/incidents/type/{event_type}")
def get_incidents_by_type(event_type: str):
    return query.get_by_event_type(
        event_type.upper()
    )


@app.get("/incidents/{incident_id}")
def get_incident(incident_id: str):
    incident = query.get_by_id(
        incident_id
    )

    if incident:
        return incident

    return {
        "error": "Incident not found"
    }


@app.get("/stats")
def get_stats():
    return stats.get_summary()

