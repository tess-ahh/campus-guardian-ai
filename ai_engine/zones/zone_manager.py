import json
import os


class ZoneManager:
    def __init__(self):
        self.zone_file = "data/zones.json"
        self.zones = self.load_zones()

    def load_zones(self):
        """
        Load zones from JSON file.
        """

        if os.path.exists(self.zone_file):

            with open(self.zone_file, "r") as file:
                return json.load(file)

        print("⚠ No zones.json found. Using default zone.")

        return {
            "restricted_zone": {
                "bbox": [200, 100, 500, 400],
                "color": [0, 0, 255],
                "label": "Restricted Area",
            }
        }

    def get_zones(self):
        return self.zones

    def check_inside(self, bbox, zone_name):

        zone = self.zones[zone_name]

        zx1, zy1, zx2, zy2 = zone["bbox"]
        x1, y1, x2, y2 = bbox

        return not (
            x2 < zx1 or
            x1 > zx2 or
            y2 < zy1 or
            y1 > zy2
        )