# 🚀 Campus Guardian AI - Development Setup Guide

## Introduction

This guide provides step-by-step instructions for setting up the **Campus Guardian AI** development environment.

The project combines **Computer Vision**, **Artificial Intelligence**, **Backend APIs**, **Database Management**, and **Modern Web Technologies** to build a comprehensive campus safety monitoring platform.

---

# Prerequisites

Before setting up the project, ensure the following software is installed on your system.

| Tool              | Required Version |
| ----------------- | ---------------- |
| Git               | Latest Stable    |
| Python            | 3.10+            |
| Conda / Miniconda | Latest Stable    |
| Node.js           | 18+              |
| PostgreSQL        | 15+ Recommended  |
| VS Code           | Latest Stable    |
| Docker Desktop    | Latest Stable    |

---

# Clone the Repository

Clone the project repository from GitHub:

```bash
git clone https://github.com/tess-ahh/campus-guardian-ai.git
cd campus-guardian-ai
```


---

# Python Environment Setup

The project uses **Conda** for dependency and environment management.

## Create Environment

```bash
conda env create -f environment.yml
```

## Activate Environment

```bash
conda activate campus-guardian-ai
```

## Update Existing Environment

If dependencies are updated later:

```bash
conda env update -f environment.yml --prune
```

## Verify Installation

```bash
python --version
```

Expected Output:

```text
Python 3.10.x
```

---

# Environment Configuration

Application secrets and configuration variables are stored in a `.env` file.

## Create Environment File

### Windows PowerShell

```powershell
Copy-Item .env.example .env
```

### macOS / Linux

```bash
cp .env.example .env
```

---

## Security Notice

⚠️ Never commit the actual `.env` file to GitHub.

Only commit:

```text
.env.example
```

The `.env` file should already be included in `.gitignore`.

---

# Backend Setup

The backend service will be developed using **FastAPI**.

## Planned Directory

```text
backend/
```

## Development Server

```bash
cd backend
uvicorn app.main:app --reload
```

## Backend URLs

| Service               | URL                         |
| --------------------- | --------------------------- |
| API Server            | http://127.0.0.1:8000       |
| Swagger Documentation | http://127.0.0.1:8000/docs  |
| ReDoc Documentation   | http://127.0.0.1:8000/redoc |

---

# AI Engine Setup

The AI Engine contains the computer vision and machine learning pipeline.

## Core Technologies

* OpenCV
* YOLOv8
* DeepSORT / ByteTrack
* Face Recognition
* NumPy

## Planned Directory

```text
ai-engine/
```

## Development Command

```bash
cd ai-engine
python main.py
```

---

# Frontend Setup

The frontend dashboard will be built using **React** and **Tailwind CSS**.

## Planned Directory

```text
frontend/
```

## Install Dependencies

```bash
cd frontend
npm install
```

## Start Development Server

```bash
npm run dev
```

## Frontend URL

```text
http://localhost:5173
```

---

# Database Setup

The project uses **PostgreSQL** for persistent data storage.

## Database Name

```text
campus_guardian_ai
```

## Example Connection String

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/campus_guardian_ai
```

## Main Data Tables

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

---

# Docker Setup

Containerization support will be added in future development phases.

## Planned Command

```bash
docker compose up --build
```

## Future Services

```text
Frontend Service
Backend Service
AI Engine Service
PostgreSQL Service
```

---

# Project Directory Structure

```text
campus-guardian-ai/
│
├── backend/                # FastAPI backend
├── frontend/               # React dashboard
├── ai-engine/              # OpenCV & AI pipeline
├── docs/                   # Project documentation
├── data/                   # Datasets and sample videos
├── scripts/                # Utility scripts
│
├── environment.yml         # Conda environment
├── .env.example            # Environment template
├── .gitignore
├── README.md
│
└── docker-compose.yml      # Future deployment
```

---

# Recommended VS Code Extensions

For the best development experience, install the following extensions:

| Extension                 | Purpose                  |
| ------------------------- | ------------------------ |
| Python                    | Python Development       |
| Pylance                   | IntelliSense             |
| Black Formatter           | Code Formatting          |
| GitLens                   | Git Integration          |
| Docker                    | Container Management     |
| PostgreSQL                | Database Explorer        |
| Tailwind CSS IntelliSense | Frontend Development     |
| ESLint                    | JavaScript/React Linting |

---

# Common Setup Issues

## Conda Command Not Found

### Cause

Conda is not installed or not added to the system PATH.

### Solution

Verify installation:

```bash
conda --version
```

Reinstall Miniconda or Anaconda if necessary.

---

## Python Version Mismatch

### Cause

Incorrect Python version installed.

### Solution

Verify version:

```bash
python --version
```

Use Python 3.10 or higher.

---

## PostgreSQL Connection Error

### Cause

Database server is not running or credentials are incorrect.

### Solution

* Verify PostgreSQL service status.
* Check username and password.
* Confirm database exists.

---

## Port Already in Use

### Cause

Another application is using the required port.

### Solution

Identify the process:

```bash
netstat -ano
```

Stop the conflicting process or use a different port.

---

# Development Workflow

This project uses Git and GitHub for version control.

The repository is connected to GitHub using SSH authentication. Development is currently done using the VS Code Source Control panel.

## Current Workflow

1. Edit project files.
2. Open the Source Control panel in VS Code.
3. Review the changed files.
4. Enter a clear commit message.
5. Click Commit.
6. Click Sync Changes to push updates to GitHub.

## Commit Message Examples

```text
docs: add setup guide
docs: add architecture overview
docs: add project roadmap
docs: update development workflow
feat: add webcam video pipeline
fix: handle camera connection error

## Current Development Status

| Component             |  Status          |
| --------------------- | --------------   |
| Repository Setup      | ✅ Completed    |
| Documentation         | ✅ Completed    |
| Environment Setup     | 🟡 In Progress  |
| Backend Development   | ⏳ Planned      |
| AI Engine Development | ⏳ Planned      |
| Frontend Development  | ⏳ Planned      |
| Database Integration  | ⏳ Planned      |
| Docker Deployment     | ⏳ Planned      |

---

## Version Information

**Project:** Campus Guardian AI
**Version:** 1.0.0-alpha
**Phase:** Repository & Documentation Setup
