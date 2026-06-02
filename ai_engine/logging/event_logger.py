import json
import os
from datetime import datetime


class EventLogger:
    def __init__(self, log_file="data/events_log.json"):
        self.log_file = log_file
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # initialize file if not exists
        if not os.path.exists(log_file):
            with open(log_file, "w") as f:
                json.dump([], f)

    def log_event(self, event):
        event_record = {
            "type": event.get("type"),
            "id": event.get("id"),
            "duration": event.get("duration"),
            "timestamp": datetime.now().isoformat()
        }

        with open(self.log_file, "r") as f:
            data = json.load(f)

        data.append(event_record)

        with open(self.log_file, "w") as f:
            json.dump(data, f, indent=2)