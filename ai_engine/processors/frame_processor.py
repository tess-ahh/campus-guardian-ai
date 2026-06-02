import cv2

from ai_engine.processors.plugins.detector import DetectorPlugin
from ai_engine.processors.plugins.tracker import TrackerPlugin
from ai_engine.processors.plugins.event_engine import EventEnginePlugin


class FrameProcessor:
    def __init__(self):
        # 🧠 Plugin pipeline (order matters)
        self.plugins = [
            DetectorPlugin(),
            TrackerPlugin(),
            EventEnginePlugin(),
        ]

    def process(self, frame):
        """
        Pass frame through all plugins sequentially.
        """

        context = {}

        # 🔁 Run through plugin chain
        for plugin in self.plugins:
            frame, context = plugin.process(frame, context)

        # 🧠 EVENT VISUALIZATION (NEW)
        events = context.get("events", [])

        y_offset = 160

        for event in events:
            text = f"⚠ {event['type']} | ID {event['id']} | {event['duration']}s"

            cv2.putText(
                frame,
                text,
                (20, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),  # red alert
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