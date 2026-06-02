import cv2
from ai_engine.processors.base import FramePlugin


import numpy as np
from ai_engine.processors.base import FramePlugin


class TrackerPlugin(FramePlugin):
    def __init__(self):
        # store tracked objects
        self.tracks = {}
        self.next_id = 0

    def iou(self, box1, box2):
        x1, y1, x2, y2 = box1
        x1_p, y1_p, x2_p, y2_p = box2

        xi1 = max(x1, x1_p)
        yi1 = max(y1, y1_p)
        xi2 = min(x2, x2_p)
        yi2 = min(y2, y2_p)

        inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)

        box1_area = (x2 - x1) * (y2 - y1)
        box2_area = (x2_p - x1_p) * (y2_p - y1_p)

        union_area = box1_area + box2_area - inter_area

        if union_area == 0:
            return 0

        return inter_area / union_area

    def process(self, frame, context=None):
        if context is None:
            return frame, {}

        detections = context.get("detections", [])

        updated_tracks = {}

        for det in detections:
            box = det["bbox"]
            matched_id = None

            # 🔍 match with existing tracks
            for track_id, track_box in self.tracks.items():
                if self.iou(box, track_box) > 0.3:
                    matched_id = track_id
                    break

            # 🆕 new object
            if matched_id is None:
                matched_id = self.next_id
                self.next_id += 1

            updated_tracks[matched_id] = box

            # 🎯 draw ID
            x1, y1, x2, y2 = box
            import cv2

            cv2.putText(
                frame,
                f"ID {matched_id}",
                (x1, y2 + 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 0, 0),
                2
            )

        self.tracks = updated_tracks

        context["tracks"] = self.tracks

        return frame, context