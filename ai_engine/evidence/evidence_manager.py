from pathlib import Path
from datetime import datetime
import cv2
import time


class EvidenceManager:
    def __init__(self):
        self.output_dir = Path("data/incidents")
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Prevent repeated captures for the same event type
        self.last_capture = {}
        self.cooldown_seconds = 10

    def save_snapshot(self, frame, event_type):
        current_time = time.time()

        # Cooldown check
        if event_type in self.last_capture:
            elapsed = current_time - self.last_capture[event_type]

            if elapsed < self.cooldown_seconds:
                return None

        self.last_capture[event_type] = current_time

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = (
            f"{event_type.lower()}_{timestamp}.jpg"
        )

        filepath = self.output_dir / filename

        cv2.imwrite(str(filepath), frame)

        return str(filepath)