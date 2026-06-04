
import json
from pathlib import Path


class IncidentQuery:
    def __init__(self):
        self.incident_file = Path(
            "data/incidents/incidents.json"
        )

    def load_incidents(self):
        try:
            return json.loads(
                self.incident_file.read_text()
            )
        except Exception:
            return []

    def get_by_id(self, incident_id):
        incidents = self.load_incidents()

        for incident in incidents:
            if incident.get("incident_id") == incident_id:
                return incident

        return None

    def get_by_severity(self, severity):
        incidents = self.load_incidents()

        return [
            incident
            for incident in incidents
            if incident.get("severity") == severity
        ]

    def get_by_event_type(self, event_type):
        incidents = self.load_incidents()

        return [
            incident
            for incident in incidents
            if incident.get("event_type") == event_type
        ]

