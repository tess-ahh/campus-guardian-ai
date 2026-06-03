import time

from ai_engine.processors.base import FramePlugin
from ai_engine.logging.event_logger import EventLogger
from ai_engine.evidence.evidence_manager import EvidenceManager


class EventEnginePlugin(FramePlugin):
    def __init__(self):
        self.first_seen = {}
        self.last_seen = {}
        self.alert_threshold = 2  # seconds (testing value)

        # Logging
        self.logger = EventLogger()

        # 📸 Evidence manager
        self.evidence_manager = EvidenceManager()

    def process(self, frame, context=None):
        if context is None:
            return frame, {}

        tracks = context.get("tracks", {})
        current_time = time.time()

        events = []

        for obj_id in tracks.keys():

            if obj_id not in self.first_seen:
                self.first_seen[obj_id] = current_time

            self.last_seen[obj_id] = current_time

            duration = (
                self.last_seen[obj_id]
                - self.first_seen[obj_id]
            )

            if duration > self.alert_threshold:

                event = {
                    "type": "LOITERING_WARNING",
                    "id": obj_id,
                    "duration": round(duration, 2)
                }

                events.append(event)

                # 💾 Log event
                try:
                    self.logger.log_event(event)
                except Exception as e:
                    print("⚠ Logger error:", e)

                # 📸 Capture evidence image
                try:
                    snapshot_path = (
                        self.evidence_manager.save_snapshot(
                            frame,
                            event["type"]
                        )
                    )

                    if snapshot_path:
                        print(
                            f"📸 Evidence saved: "
                            f"{snapshot_path}"
                        )

                except Exception as e:
                    print(
                        "⚠ Evidence capture error:",
                        e
                    )

        if events:
            print("🚨 EVENTS TRIGGERED:", events)

        context["events"] = events

        return frame, context