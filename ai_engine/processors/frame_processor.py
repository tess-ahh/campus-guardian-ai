import cv2

from ai_engine.processors.plugins.detector import DetectorPlugin
from ai_engine.processors.plugins.tracker import TrackerPlugin


class FrameProcessor:
    def __init__(self):
        # 🧠 Plugin pipeline (order matters)
        self.plugins = [
            DetectorPlugin(),
            TrackerPlugin(),
        ]

    def process(self, frame):
        """
        Pass frame through all plugins sequentially.
        """

        context = {}

        # 🔁 Run through plugin chain
        for plugin in self.plugins:
            frame, context = plugin.process(frame, context)

        # 🟢 Optional global overlay (kept from earlier stage)
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