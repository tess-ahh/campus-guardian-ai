import cv2
from ai_engine.processors.base import FramePlugin


class DetectorPlugin(FramePlugin):
    def process(self, frame, context=None):

        cv2.putText(
            frame,
            "Detector Plugin Active",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )

        context["detected"] = True
        return frame, context