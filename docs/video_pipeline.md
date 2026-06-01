# 🎥 Campus Guardian AI - Video Pipeline Documentation

## Overview

The Video Pipeline serves as the foundational layer of the **Campus Guardian AI** system.

Its primary responsibility is to acquire video frames from various input sources and provide a reliable, reusable, and extensible processing pipeline for all future computer vision operations.

Every advanced AI capability planned for the project, including object detection, tracking, face recognition, crowd monitoring, intrusion detection, and incident generation, will be built on top of this pipeline.

The current implementation focuses on establishing a robust and production-oriented video ingestion framework before integrating AI models.

---

# Objectives

The Video Pipeline is designed to:

* Capture video from multiple source types
* Maintain a consistent frame processing loop
* Track frame metadata
* Calculate and display FPS metrics
* Support optional visual debugging
* Save periodic snapshots
* Handle invalid sources gracefully
* Release resources safely
* Provide a reusable foundation for future AI modules

---

# Architecture

```text
Video Source
      │
      ▼
Video Stream Manager
      │
      ▼
Frame Acquisition
      │
      ▼
Frame Processing Layer
      │
      ▼
Overlay Rendering
      │
      ▼
Snapshot Manager
      │
      ▼
Display / Output
```

---

# Current Implementation

The video pipeline is implemented inside the AI Engine package.

```text
ai_engine/
│
├── config.py
├── main.py
│
└── pipelines/
    └── video_stream.py
```

---

# Core Components

## 1. Entry Point

### File

```text
ai_engine/main.py
```

### Purpose

Acts as the command-line entry point for the AI Engine.

### Responsibilities

* Parse command-line arguments
* Load configuration settings
* Initialize the video stream
* Execute the frame processing loop
* Render overlays
* Save snapshots
* Handle display operations
* Manage application shutdown
* Release resources safely

---

## 2. Video Stream Module

### File

```text
ai_engine/pipelines/video_stream.py
```

### Purpose

Provides reusable video acquisition and stream management functionality.

### Responsibilities

* Open video sources
* Read video frames
* Calculate FPS
* Maintain frame counters
* Save image snapshots
* Handle source failures
* Release resources

### Design Philosophy

The stream module is intentionally separated from business logic to allow future AI components to focus solely on computer vision tasks without managing video acquisition.

---

# Supported Video Sources

The pipeline is designed to support multiple input types.

| Source Type     | Example                       |
| --------------- | ----------------------------- |
| Webcam          | `0`                           |
| External Camera | `1`, `2`, etc.                |
| Video File      | `data/sample_videos/test.mp4` |
| RTSP Stream     | `rtsp://camera-ip/stream`     |
| IP Camera       | HTTP/HTTPS camera URL         |

### Default Source

```text
0
```

This typically corresponds to the system's default webcam.

---

# Processing Features

The current version includes several foundational capabilities.

## Frame Acquisition

Frames are continuously captured from the selected source.

---

## FPS Monitoring

Real-time FPS (Frames Per Second) is calculated and displayed to monitor pipeline performance.

Benefits:

* Performance analysis
* Hardware benchmarking
* Future AI optimization

---

## Frame Index Tracking

Each processed frame receives a unique frame index.

Example:

```text
Frame 1
Frame 2
Frame 3
...
```

This metadata will later support:

* Incident logging
* Event tracking
* Debugging
* Snapshot management

---

## Overlay Rendering

The pipeline draws informational overlays directly onto video frames.

Current overlays include:

* FPS
* Frame number

Future overlays may include:

* Bounding boxes
* Tracking IDs
* Face labels
* Alert messages
* Incident information

---

## Snapshot Capture

Snapshots can be automatically saved at configurable intervals.

Use Cases:

* Debugging
* Dataset collection
* Incident evidence
* Model validation

---

# Command-Line Usage

## Run Without Display

Suitable for servers, automated testing, and headless environments.

```bash
python -m ai_engine.main
```

---

## Run With Display

Displays the OpenCV video window.

```bash
python -m ai_engine.main --display
```

---

## Process a Fixed Number of Frames

```bash
python -m ai_engine.main --display --max-frames 100
```

---

## Save Periodic Snapshots

```bash
python -m ai_engine.main --display --snapshot-every 50
```

---

## Use a Different Camera

```bash
python -m ai_engine.main --source 1 --display
```

---

## Use a Video File

```bash
python -m ai_engine.main --source data/sample_videos/test.mp4 --display
```

---

## Use an RTSP Stream

```bash
python -m ai_engine.main --source rtsp://username:password@camera-ip:554/stream1 --display
```

---

# Command-Line Arguments

| Argument           | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| `--source`         | Camera index, video file path, RTSP stream, or IP camera URL |
| `--display`        | Display video output using OpenCV                            |
| `--max-frames`     | Stop processing after a specified number of frames           |
| `--snapshot-every` | Save one snapshot every N frames                             |

---

# Why Display Is Optional

The display window is intentionally disabled by default.

### Development Environment

```text
Developer Laptop
        │
        ▼
Display Enabled
```

Developers can visually inspect frame processing.

### Production Environment

```text
Server
Cloud VM
Docker Container
Edge Device
```

Most production systems run without a graphical interface.

Keeping display optional ensures compatibility across all deployment environments.

---

# Error Handling

The pipeline includes basic validation and error handling.

### Supported Scenarios

* Invalid camera index
* Missing video file
* Unreachable RTSP stream
* Failed frame reads
* Resource cleanup during shutdown

### Example Error

```text
Failed to open video source: rtsp://invalid-stream
```

---

# Testing Checklist

Verify the following before moving to the next development phase.

## Functional Testing

* [ ] Webcam opens successfully
* [ ] External camera opens successfully
* [ ] Video file loads correctly
* [ ] RTSP stream connects successfully
* [ ] Frames are processed continuously

## Display Testing

* [ ] Video window appears when `--display` is enabled
* [ ] FPS overlay updates correctly
* [ ] Frame index overlay updates correctly
* [ ] Pressing `q` closes the application

## Snapshot Testing

* [ ] Snapshots are created
* [ ] Snapshot interval works correctly
* [ ] Saved images are valid

## Reliability Testing

* [ ] Invalid source produces clear error
* [ ] Resources are released properly
* [ ] Application exits gracefully

---

# Future Enhancements

The current implementation establishes the foundation for future AI modules.

Planned additions include:

* Frame Processor Architecture
* YOLOv8 Object Detection
* Multi-Object Tracking
* Face Recognition
* Crowd Monitoring
* Intrusion Detection
* Loitering Detection
* Fire & Smoke Detection
* Incident Generation
* Event Logging
* Real-Time Alerts

---

# Development Status

| Component               | Status       |
| ----------------------- | ------------ |
| Video Source Management | ✅ Complete   |
| Frame Processing Loop   | ✅ Complete   |
| FPS Monitoring          | ✅ Complete   |
| Frame Index Tracking    | ✅ Complete   |
| Snapshot Capture        | ✅ Complete   |
| Error Handling          | ✅ Complete   |
| Frame Processor Layer   | ⏳ Next Phase |
| Object Detection        | ⏳ Planned    |
| Object Tracking         | ⏳ Planned    |
| Event Detection         | ⏳ Planned    |

---

## Version Information

**Project:** Campus Guardian AI
**Module:** Video Pipeline
**Version:** 1.0.0
**Phase:** Phase 1 - Video Processing Foundation
