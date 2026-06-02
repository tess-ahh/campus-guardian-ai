import cv2

from ai_engine.zones.zone_editor import ZoneEditor


def main():
    editor = ZoneEditor()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Could not open webcam")
        return

    cv2.namedWindow("Zone Setup")
    cv2.setMouseCallback("Zone Setup", editor.mouse_callback)

    while True:
        success, frame = cap.read()

        if not success:
            break

        display_frame = frame.copy()

        if editor.start_point and editor.end_point:
            cv2.rectangle(
                display_frame,
                editor.start_point,
                editor.end_point,
                (0, 0, 255),
                2
            )

        cv2.putText(
            display_frame,
            "Drag mouse to create zone | Press S to save | Q to quit",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        cv2.imshow("Zone Setup", display_frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            editor.save_zone()

        elif key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()