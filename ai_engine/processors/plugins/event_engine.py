import time
from ai_engine.processors.base import FramePlugin
from ai_engine.logging.event_logger import EventLogger


class EventEnginePlugin(FramePlugin):
    def __init__(self):
        self.first_seen = {}
        self.last_seen = {}
        self.alert_threshold = 2  # seconds (testing value)

        # 🧠 persistent logger (NEW)
        self.logger = EventLogger()

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

            # 🧠 KEEP ALIVE SIGNAL
            self.last_seen[obj_id] = current_time

            # ⏱ duration calculation
            duration = self.last_seen[obj_id] - self.first_seen[obj_id]

            if duration > self.alert_threshold:

                event = {
                    "type": "LOITERING_WARNING",
                    "id": obj_id,
                    "duration": round(duration, 2)
                }

                events.append(event)

                # 💾 SAVE EVENT TO FILE (NEW)
                try:
                    self.logger.log_event(event)
                except Exception as e:
                    print("⚠ Logger error:", e)

        # 🧪 Debug output
        if events:
            print("🚨 EVENTS TRIGGERED:", events)

        context["events"] = events

        return frame, context