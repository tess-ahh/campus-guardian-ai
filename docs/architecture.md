# 🏛️ Campus Guardian AI - System Architecture

## Overview

**Campus Guardian AI** is a full-stack, AI-powered surveillance and campus safety platform designed to monitor live video feeds, detect security incidents, manage alerts, and provide actionable analytics through a centralized dashboard.

The system combines **Computer Vision**, **Machine Learning**, **Backend APIs**, **Database Management**, and **Modern Web Technologies** to create a scalable and production-ready monitoring solution.

---

## Architecture Goals

* Real-time video monitoring
* Intelligent event detection
* Scalable microservice-friendly design
* Modular AI pipeline
* Secure API-driven communication
* Centralized incident management
* Future cloud deployment support

---

# System Architecture

```text
┌──────────────────────────────┐
│   Camera / CCTV / Webcam     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Video Input Layer       │
│  OpenCV Stream Processing    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         AI Engine            │
│                              │
│ • Object Detection (YOLOv8)  │
│ • Multi-Object Tracking      │
│ • Face Recognition           │
│ • Event Analysis             │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│    Event Detection Layer     │
│                              │
│ • Intrusion Detection        │
│ • Loitering Detection        │
│ • Crowd Monitoring           │
│ • Unknown Person Detection   │
│ • Fire & Smoke Detection     │
│ • Fall Detection             │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       FastAPI Backend        │
│                              │
│ • REST APIs                 │
│ • Alert Management          │
│ • Incident Management       │
│ • Authentication            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      PostgreSQL Database     │
│                              │
│ • Incidents                 │
│ • Users                     │
│ • Cameras                   │
│ • Alerts                    │
│ • Attendance                │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      React Dashboard         │
│                              │
│ • Live Monitoring           │
│ • Incident Logs             │
│ • Analytics                 │
│ • Attendance Tracking       │
│ • Reports & Insights        │
└──────────────────────────────┘
```

---

# Core Components

## 1. Video Input Layer

### Purpose

The Video Input Layer is responsible for acquiring video frames from various sources and forwarding them to the AI Engine for processing.

### Supported Sources

| Source        | Description                    |
| ------------- | ------------------------------ |
| Webcam        | Local development and testing  |
| CCTV Cameras  | Real-time campus monitoring    |
| RTSP Streams  | IP camera integration          |
| Video Files   | Offline testing and evaluation |
| Demo Datasets | Model benchmarking             |

### Responsibilities

* Stream acquisition
* Frame extraction
* Resolution management
* FPS control
* Video buffering

---

## 2. AI Engine

### Purpose

The AI Engine serves as the intelligence core of the platform.

### Responsibilities

* Frame processing
* Object detection
* Multi-object tracking
* Face recognition
* Event generation

### Technology Stack

| Technology           | Purpose                    |
| -------------------- | -------------------------- |
| OpenCV               | Image and video processing |
| YOLOv8               | Object detection           |
| DeepSORT / ByteTrack | Object tracking            |
| Face Recognition     | Identity verification      |
| NumPy                | Numerical operations       |

---

## 3. Object Detection Module

### Purpose

Detect and classify entities appearing within video streams.

### Supported Objects

* Person
* Vehicle
* Animal
* Backpack
* Fire
* Smoke

### Workflow

```text
Video Frame
     │
     ▼
YOLOv8 Model
     │
     ▼
Bounding Boxes
     │
     ▼
Class Labels + Confidence Scores
```

---

## 4. Multi-Object Tracking Module

### Purpose

Maintain persistent identities for detected objects across multiple frames.

### Benefits

* Crowd analysis
* Loitering detection
* Movement tracking
* Vehicle monitoring
* Behavioral analytics

### Example

```text
Frame 1:
Person → ID 12

Frame 2:
Person → ID 12

Frame 3:
Person → ID 12
```

---

## 5. Face Recognition Module

### Purpose

Identify authorized individuals and detect unknown persons.

### Features

* Face registration
* Face embedding generation
* Face matching
* Attendance logging
* Unknown person alerts

### Output

```text
Detected Face
      │
      ▼
Face Encoding
      │
      ▼
Database Comparison
      │
      ├── Match Found
      │      └── Identity Verified
      │
      └── No Match
             └── Unknown Person Alert
```

---

## 6. Event Detection Layer

### Purpose

Transform raw AI predictions into meaningful security incidents.

### Supported Events

| Event          | Trigger Condition          |
| -------------- | -------------------------- |
| Intrusion      | Restricted zone entry      |
| Loitering      | Prolonged presence         |
| Crowd Alert    | Density threshold exceeded |
| Unknown Person | Face mismatch              |
| Fire Alert     | Fire or smoke detected     |
| Fall Alert     | Human fall identified      |

### Example

```text
Detection:
Person in Restricted Area

↓

Business Logic

↓

Incident Generated:
"Intrusion Alert"
```

---

## 7. Backend Services

### Framework

**FastAPI**

### Responsibilities

* REST API development
* Authentication & authorization
* Incident management
* Alert management
* Analytics aggregation
* Camera management

### API Categories

| Category       | Description           |
| -------------- | --------------------- |
| Auth APIs      | User authentication   |
| Camera APIs    | Camera configuration  |
| Incident APIs  | Incident records      |
| Alert APIs     | Notification handling |
| Analytics APIs | Dashboard metrics     |

---

## 8. Database Layer

### Database

**PostgreSQL**

### Core Entities

```text
Users
Cameras
Incidents
Alerts
Attendance
KnownPersons
Vehicles
ParkingRecords
```

### Benefits

* ACID compliance
* Scalability
* Structured querying
* Strong relational modeling

---

## 9. Frontend Dashboard

### Technology

* React
* Tailwind CSS
* Axios
* React Router

### Modules

| Module          | Function               |
| --------------- | ---------------------- |
| Live Monitoring | Real-time camera feeds |
| Incident Center | Incident management    |
| Attendance      | Face-based attendance  |
| Analytics       | Visual insights        |
| Camera Manager  | Device administration  |
| Settings        | System configuration   |

---

## 10. Deployment Layer

### Containerization

Docker will be used to package all services.

### Deployment Components

```text
┌────────────────────┐
│ React Frontend     │
└─────────┬──────────┘
          │
┌─────────▼──────────┐
│ FastAPI Backend    │
└─────────┬──────────┘
          │
┌─────────▼──────────┐
│ PostgreSQL DB      │
└─────────┬──────────┘
          │
┌─────────▼──────────┐
│ AI Processing Node │
└────────────────────┘
```

---

# Design Principles

The architecture follows the following engineering principles:

* Modular Design
* Separation of Concerns
* API-First Development
* Scalable Database Design
* Clean Code Practices
* Reusable Components
* Production Readiness
* Security by Design

---

# Future Enhancements

The architecture has been designed to support future expansion.

### Planned Improvements

* WebSocket-based real-time alerts
* Multi-camera orchestration
* GPU acceleration
* Edge AI deployment
* Cloud-native infrastructure
* Role-Based Access Control (RBAC)
* Notification services (Email/SMS)
* AI model monitoring
* Distributed event processing

---

# Technology Summary

| Layer            | Technology              |
| ---------------- | ----------------------- |
| Frontend         | React + Tailwind CSS    |
| Backend          | FastAPI                 |
| Database         | PostgreSQL              |
| AI Framework     | OpenCV                  |
| Detection        | YOLOv8                  |
| Tracking         | DeepSORT / ByteTrack    |
| Face Recognition | Face Recognition Models |
| Containerization | Docker                  |
| Version Control  | Git & GitHub            |

---

## Architecture Version

**Version:** 1.0.0
**Project:** Campus Guardian AI
**Status:** Architecture Design Phase
