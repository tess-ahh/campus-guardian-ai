import json
from pathlib import Path
from datetime import datetime


class IncidentManager:
    def __init__(self):
        self.incident_file = Path(
            "data/incidents/incidents.json"
        )

        self.incident_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.incident_file.exists():
            self.incident_file.write_text("[]")

    def get_severity(self, event_type):
        severity_map = {
            "LOITERING_WARNING": "MEDIUM",
            "INTRUSION": "HIGH",
        }

        return severity_map.get(
            event_type,
            "LOW"
        )

    def create_incident(
        self,
        event_type,
        object_id,
        evidence_image,
    ):
        try:
            incidents = json.loads(
                self.incident_file.read_text()
            )

        except Exception:
            incidents = []

        # 🆔 Generate unique incident ID
        incident_id = (
            f"INC-{len(incidents) + 1:06d}"
        )

        incident = {
            "incident_id": incident_id,
            "event_type": event_type,
            "severity": self.get_severity(event_type),
            "object_id": object_id,
            "timestamp": datetime.now().isoformat(),
            "evidence_image": evidence_image,
        }

        incidents.append(incident)

        self.incident_file.write_text(
            json.dumps(
                incidents,
                indent=4
            )
        )

        return incident