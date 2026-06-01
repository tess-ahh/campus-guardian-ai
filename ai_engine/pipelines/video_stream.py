from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from time import perf_counter
from typing import Optional

import cv2

from ai_engine.config import CameraSource, VideoPipelineConfig


@dataclass(frozen=True)
class FramePacket:
    frame_index: int
    fps: float
    width: int
    height: int


class VideoStreamError(RuntimeError):
    """Raised when a video source cannot be opened or read."""


class VideoStream:
    def __init__(self, config: VideoPipelineConfig) -> None:
        self.config = config
        self.capture: Optional[cv2.VideoCapture] = None
        self.frame_index = 0
        self._last_frame_time: Optional[float] = None

    def open(self) -> None:
        self.capture = cv2.VideoCapture(self.config.camera_source)

        if not self.capture.isOpened():
            raise VideoStreamError(
                f"Unable to open camera source: {self.config.camera_source!r}"
            )

        if self.config.target_width:
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.config.target_width)
        if self.config.target_height:
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.config.target_height)

    def read(self) -> tuple[bool, object, FramePacket | None]:
        if self.capture is None:
            raise VideoStreamError("Video stream is not open. Call open() first.")

        success, frame = self.capture.read()
        if not success:
            return False, frame, None

        self.frame_index += 1
        now = perf_counter()
        fps = 0.0
        if self._last_frame_time is not None:
            elapsed = now - self._last_frame_time
            fps = 1.0 / elapsed if elapsed > 0 else 0.0
        self._last_frame_time = now

        height, width = frame.shape[:2]
        packet = FramePacket(
            frame_index=self.frame_index,
            fps=fps,
            width=width,
            height=height,
        )

        return True, frame, packet

    def save_snapshot(self, frame: object, snapshot_dir: Path | None = None) -> Path:
        output_dir = snapshot_dir or self.config.snapshot_dir
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        output_path = output_dir / f"snapshot_{timestamp}.jpg"

        saved = cv2.imwrite(str(output_path), frame)
        if not saved:
            raise VideoStreamError(f"Failed to save snapshot: {output_path}")

        return output_path

    def release(self) -> None:
        if self.capture is not None:
            self.capture.release()
            self.capture = None


def draw_frame_overlay(frame: object, packet: FramePacket) -> object:
    label = f"Frame: {packet.frame_index} | FPS: {packet.fps:.1f}"
    cv2.putText(
        frame,
        label,
        (16, 32),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )
    return frame