import cv2
from ultralytics import YOLO

from ai_engine.config import YOLO_MODEL_PATH, YOLO_CONFIDENCE_THRESHOLD
from ai_engine.processors.base import FramePlugin


class DetectorPlugin(FramePlugin):
    def __init__(self):
        # 🧠 Load model once
        self.model = YOLO(YOLO_MODEL_PATH)

    def process(self, frame, context=None):
        if context is None:
            context = {}

        results = self.model(frame, verbose=False)[0]

        detections = []

        for box in results.boxes:
            conf = float(box.conf[0])

            # 🚨 filter weak detections
            if conf < YOLO_CONFIDENCE_THRESHOLD:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            label = self.model.names[cls]

            detections.append({
                "label": label,
                "confidence": conf,
                "bbox": (x1, y1, x2, y2)
            })

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f"{label} {conf:.2f}",
                (x1, y1 - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

        context["detections"] = detections

        return frame, context