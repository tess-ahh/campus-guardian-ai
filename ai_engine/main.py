import argparse
import cv2

from ai_engine.config import VideoPipelineConfig, parse_camera_source
from ai_engine.pipelines.video_stream import (
    VideoStream,
    VideoStreamError,
    draw_frame_overlay,
)

# ✅ NEW: import FrameProcessor
from ai_engine.processors.frame_processor import FrameProcessor


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Campus Guardian AI video pipeline")

    parser.add_argument(
        "--source",
        default=None,
        help="Camera index, video file path, RTSP URL, or IP camera URL.",
    )

    parser.add_argument(
        "--display",
        action="store_true",
        help="Show the video stream in an OpenCV window.",
    )

    parser.add_argument(
        "--max-frames",
        type=int,
        default=0,
        help="Stop after this many frames. Use 0 to run until the stream ends.",
    )

    parser.add_argument(
        "--snapshot-every",
        type=int,
        default=0,
        help="Save one snapshot every N frames. Use 0 to disable snapshots.",
    )

    return parser


def main() -> int:
    args = build_parser().parse_args()
    config = VideoPipelineConfig.from_env()

    if args.source is not None:
        config = VideoPipelineConfig(
            camera_source=parse_camera_source(args.source),
            snapshot_dir=config.snapshot_dir,
            output_dir=config.output_dir,
            window_name=config.window_name,
        )

    stream = VideoStream(config)

    # ✅ NEW: initialize processor
    processor = FrameProcessor()

    try:
        stream.open()
        print(f"Opened video source: {config.camera_source!r}")

        while True:
            success, frame, packet = stream.read()

            if not success or packet is None:
                print("Video stream ended or frame could not be read.")
                break

            # 1️⃣ existing overlays (FPS, frame index etc.)
            frame = draw_frame_overlay(frame, packet)

            # 2️⃣ NEW: frame processor layer
            frame = processor.process(frame)

            # 3️⃣ snapshot logic
            if args.snapshot_every and packet.frame_index % args.snapshot_every == 0:
                path = stream.save_snapshot(frame)
                print(f"Saved snapshot: {path}")

            # 4️⃣ display
            if args.display:
                cv2.imshow(config.window_name, frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

            # 5️⃣ max frames limit
            if args.max_frames and packet.frame_index >= args.max_frames:
                print(f"Stopped after {packet.frame_index} frames.")
                break

    except VideoStreamError as error:
        print(f"Video pipeline error: {error}")
        return 1

    finally:
        stream.release()
        if args.display:
            cv2.destroyAllWindows()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())