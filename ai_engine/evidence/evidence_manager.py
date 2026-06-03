from pathlib import Path
from datetime import datetime
import cv2


class EvidenceManager:
    def __init__(self):
        self.output_dir = Path("data/incidents")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_snapshot(self, frame, event_type):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = (
            f"{event_type.lower()}_{timestamp}.jpg"
        )

        filepath = self.output_dir / filename

        cv2.imwrite(str(filepath), frame)

        return str(filepath)