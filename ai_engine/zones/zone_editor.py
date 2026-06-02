import cv2
import json
import os


class ZoneEditor:
    def __init__(self):
        self.drawing = False
        self.start_point = None
        self.end_point = None

    def mouse_callback(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.start_point = (x, y)

        elif event == cv2.EVENT_MOUSEMOVE and self.drawing:
            self.end_point = (x, y)

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            self.end_point = (x, y)

    def save_zone(self):

        if not self.start_point or not self.end_point:
            return

        x1, y1 = self.start_point
        x2, y2 = self.end_point

        zone_data = {
            "restricted_zone": {
                "bbox": [x1, y1, x2, y2],
                "color": [0, 0, 255],
                "label": "Restricted Area"
            }
        }

        os.makedirs("data", exist_ok=True)

        with open("data/zones.json", "w") as file:
            json.dump(zone_data, file, indent=4)

        print("✅ Zone saved to data/zones.json")