import cv2

from ai_engine.processors.plugins.detector import DetectorPlugin
from ai_engine.processors.plugins.tracker import TrackerPlugin
from ai_engine.processors.plugins.event_engine import EventEnginePlugin
from ai_engine.processors.plugins.zone_detector import ZoneDetectorPlugin


class FrameProcessor:
    def __init__(self):
        # 🧠 Plugin pipeline (order matters)
        self.plugins = [
            DetectorPlugin(),
            TrackerPlugin(),
            EventEnginePlugin(),
            ZoneDetectorPlugin(),   # 🔥 ADDED
        ]

    def process(self, frame):
        """
        Pass frame through all plugins sequentially.
        """

        context = {}

        # 🔁 Run through plugin chain
        for plugin in self.plugins:
            frame, context = plugin.process(frame, context)

        # 🧠 EVENT VISUALIZATION (includes loitering + intrusion)
        events = context.get("events", [])

        y_offset = 160

        for event in events:
            # handle both event types safely
            event_type = event.get("type", "EVENT")
            obj_id = event.get("id", "UNKNOWN")
            duration = event.get("duration", None)

            if duration is not None:
                text = f"⚠ {event_type} | ID {obj_id} | {duration}s"
            else:
                text = f"⚠ {event_type} | ID {obj_id}"

            cv2.putText(
                frame,
                text,
                (20, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

            y_offset += 30

        # 🟢 base overlay
        cv2.putText(
            frame,
            "Frame Processor Active",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        return frame