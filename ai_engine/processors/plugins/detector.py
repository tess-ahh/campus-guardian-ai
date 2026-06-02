import cv2
from ultralytics import YOLO
from ai_engine.processors.base import FramePlugin


class DetectorPlugin(FramePlugin):
    def __init__(self):
        # 🧠 Load model ONCE (critical for performance)
        self.model = YOLO("yolov8n.pt")

    def process(self, frame, context=None):
        if context is None:
            context = {}

        # 🚀 Run YOLO inference
        results = self.model(frame, verbose=False)[0]

        detections = []

        # 📦 Parse results
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = self.model.names[cls]

            detections.append({
                "label": label,
                "confidence": conf,
                "bbox": (x1, y1, x2, y2)
            })

            # 🎯 Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
            cv2.putText(
                frame,
                f"{label} {conf:.2f}",
                (x1, y1 - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 255),
                2
            )

        # 📡 Pass data to next plugins
        context["detections"] = detections

        return frame, context