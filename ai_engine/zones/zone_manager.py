class ZoneManager:
    def __init__(self):
        """
        Zone definitions for Campus Guardian AI.

        bbox format:
        (x1, y1, x2, y2)
        """

        self.zones = {
            "restricted_zone": {
                "bbox": (200, 100, 500, 400),
                "color": (0, 0, 255),  # Red (BGR)
                "label": "Restricted Area",
            }
        }

    def get_zones(self):
        """
        Return all configured zones.
        """
        return self.zones

    def check_inside(self, bbox, zone_name):
        """
        Check whether a detected object overlaps with a zone.

        Args:
            bbox: (x1, y1, x2, y2) of detected object
            zone_name: zone identifier

        Returns:
            bool
        """

        zone = self.zones[zone_name]

        zx1, zy1, zx2, zy2 = zone["bbox"]
        x1, y1, x2, y2 = bbox

        # Simple overlap check
        return not (
            x2 < zx1 or
            x1 > zx2 or
            y2 < zy1 or
            y1 > zy2
        )