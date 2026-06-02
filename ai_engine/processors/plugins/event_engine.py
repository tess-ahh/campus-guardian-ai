import time
from ai_engine.processors.base import FramePlugin


class EventEnginePlugin(FramePlugin):
    def __init__(self):
        self.first_seen = {}
        self.last_seen = {}   # 🆕 added for stability
        self.alert_threshold = 2  # seconds (testing value)

    def process(self, frame, context=None):
        if context is None:
            return frame, {}

        tracks = context.get("tracks", {})
        current_time = time.time()

        events = []

        for obj_id in tracks.keys():

            # 🧠 FIRST SEEN (stable memory)
            if obj_id not in self.first_seen:
                self.first_seen[obj_id] = current_time

            # 🧠 KEEP ALIVE SIGNAL (NEW)
            self.last_seen[obj_id] = current_time

            # ⏱ duration calculation (more stable now)
            duration = self.last_seen[obj_id] - self.first_seen[obj_id]

            if duration > self.alert_threshold:
                events.append({
                    "type": "LOITERING_WARNING",
                    "id": obj_id,
                    "duration": round(duration, 2)
                })

        # 🧪 Debug output
        if events:
            print("🚨 EVENTS TRIGGERED:", events)

        context["events"] = events

        return frame, context