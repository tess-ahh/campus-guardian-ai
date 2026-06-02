from dataclasses import dataclass
from pathlib import Path
from typing import Union


CameraSource = Union[int, str]


def parse_camera_source(value: str) -> CameraSource:
    """Convert numeric camera sources to int and keep file/RTSP sources as str."""
    source = value.strip()
    if source.isdigit():
        return int(source)
    return source


@dataclass(frozen=True)
class VideoPipelineConfig:
    camera_source: CameraSource = 0
    snapshot_dir: Path = Path("data/snapshots")
    output_dir: Path = Path("data/outputs")
    window_name: str = "Campus Guardian AI"
    target_width: int | None = None
    target_height: int | None = None

    @classmethod
    def from_env(cls) -> "VideoPipelineConfig":
        import os

        return cls(
            camera_source=parse_camera_source(os.getenv("CAMERA_SOURCE", "0")),
            snapshot_dir=Path(os.getenv("SNAPSHOT_DIR", "data/snapshots")),
            output_dir=Path(os.getenv("OUTPUT_DIR", "data/outputs")),
        )
YOLO_MODEL_PATH = "yolov8n.pt"
YOLO_CONFIDENCE_THRESHOLD = 0.4