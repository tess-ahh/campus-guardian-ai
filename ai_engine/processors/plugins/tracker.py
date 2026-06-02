import cv2
from ai_engine.processors.base import FramePlugin


class TrackerPlugin(FramePlugin):
    def process(self, frame, context=None):

        cv2.putText(
            frame,
            "Tracker Plugin Active",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        context["tracked"] = True
        return frame, context