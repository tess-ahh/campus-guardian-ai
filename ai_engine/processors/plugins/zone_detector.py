from ai_engine.processors.base import FramePlugin
from ai_engine.zones.zone_manager import ZoneManager


class ZoneDetectorPlugin(FramePlugin):
    def __init__(self):
        self.zone_manager = ZoneManager()

    def process(self, frame, context=None):
        if context is None:
            return frame, {}

        tracks = context.get("tracks", [])

        zone_events = []

        for obj_id, bbox in tracks.items():

            if self.zone_manager.check_inside(bbox, "restricted_zone"):
                zone_events.append({
                    "type": "INTRUSION",
                    "id": obj_id
                })

        context["zone_events"] = zone_events

        return frame, context