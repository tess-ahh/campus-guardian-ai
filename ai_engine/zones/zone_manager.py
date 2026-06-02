class ZoneManager:
    def __init__(self):
        # Define restricted zones (x1, y1, x2, y2)
        self.zones = {
            "restricted_zone": (200, 100, 500, 400)
        }

    def check_inside(self, bbox, zone_name):
        zx1, zy1, zx2, zy2 = self.zones[zone_name]
        x1, y1, x2, y2 = bbox

        # simple overlap check
        return not (
            x2 < zx1 or
            x1 > zx2 or
            y2 < zy1 or
            y1 > zy2
        )