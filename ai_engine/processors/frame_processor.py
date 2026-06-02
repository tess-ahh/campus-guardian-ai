import cv2


class FrameProcessor:
    def __init__(self):
        pass

    def process(self, frame):
        cv2.putText(
            frame,
            "Frame Processor Active",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
        return frame