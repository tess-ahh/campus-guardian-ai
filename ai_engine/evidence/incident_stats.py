import json
from pathlib import Path


class IncidentStats:
    def __init__(self):
        self.incident_file = Path(
            "data/incidents/incidents.json"
        )

    def get_summary(self):
        try:
            incidents = json.loads(
                self.incident_file.read_text()
            )
        except Exception:
            incidents = []

        summary = {
            "total": len(incidents),
            "HIGH": 0,
            "MEDIUM": 0,
            "LOW": 0,
        }

        for incident in incidents:
            severity = incident.get(
                "severity",
                "LOW"
            )

            if severity in summary:
                summary[severity] += 1

        return summary