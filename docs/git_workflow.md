# 🌿 Campus Guardian AI - Git Workflow & Version Control Guide

## Purpose

This document defines the Git workflow, commit conventions, branching strategy, and version control best practices used throughout the **Campus Guardian AI** project.

Maintaining a consistent Git workflow ensures clean project history, easier collaboration, improved traceability, and smoother development as the project scales.

---

# Version Control Overview

The project uses:

* **Git** for source code management
* **GitHub** for remote repository hosting
* **SSH Authentication** for secure repository access
* **Visual Studio Code Source Control** for daily development operations

---

# Repository Information

## Remote Repository

```text
git@github.com:tess-ahh/campus-guardian-ai.git
```

## Authentication Method

SSH Key Authentication

### Benefits

* Secure access
* No repeated credential prompts
* Faster Git operations
* Recommended GitHub workflow

---

# Development Workflow

The current development process follows a simple and efficient workflow suitable for solo project development.

## Standard Workflow

### 1. Make Changes

Modify project files within VS Code.

Examples:

* Documentation updates
* Backend development
* Frontend development
* AI model integration
* Configuration changes

---

### 2. Review Changes

Open the **Source Control** panel in VS Code and review all modified files.

Verify:

* Intended changes only
* No temporary files
* No sensitive information
* No accidental deletions

---

### 3. Stage Changes

Stage files that belong to the current update.

Recommended practice:

Group related changes into a single commit.

---

### 4. Write Commit Message

Provide a concise and descriptive commit message following the project's commit conventions.

Example:

```text
docs: add setup guide
```

---

### 5. Commit Changes

Commit staged files through:

* VS Code Source Control
* Git command line
* GitHub Desktop (optional)

---

### 6. Synchronize Repository

Push local commits to GitHub.

Using VS Code:

```text
Sync Changes
```

Or using Git:

```bash
git push origin main
```

---

# Commit Message Convention

The project follows a lightweight convention inspired by **Conventional Commits**.

## Format

```text
type: short description
```

---

## Commit Types

| Type     | Purpose                                     |
| -------- | ------------------------------------------- |
| docs     | Documentation updates                       |
| feat     | New functionality                           |
| fix      | Bug fixes                                   |
| refactor | Code restructuring without behavior changes |
| test     | Test-related changes                        |
| chore    | Configuration, setup, maintenance tasks     |
| style    | Formatting and code style improvements      |
| perf     | Performance improvements                    |

---

## Documentation Examples

```text
docs: add setup guide
docs: add architecture overview
docs: add project roadmap
docs: add git workflow
docs: update project structure
```

---

## Feature Examples

```text
feat: add webcam video pipeline
feat: implement yolo object detection
feat: add incident logging api
feat: create dashboard layout
```

---

## Fix Examples

```text
fix: handle invalid camera source
fix: resolve database connection issue
fix: correct api response schema
```

---

## Maintenance Examples

```text
chore: add environment configuration
chore: update dependencies
chore: configure docker setup
```

---

# Branching Strategy

## Current Approach

Since the project is currently in the early development phase and maintained by a single developer, all work is performed directly on the `main` branch.

```text
main
```

This approach simplifies project management during the initial setup and documentation stages.

---

# Future Branching Model

As the project grows, a structured branching strategy will be adopted.

```text
main
│
├── develop
│
├── feature/video-pipeline
├── feature/yolo-detection
├── feature/face-recognition
├── feature/backend-api
├── feature/frontend-dashboard
├── feature/database-integration
└── feature/docker-deployment
```

---

## Branch Purpose

| Branch    | Purpose                        |
| --------- | ------------------------------ |
| main      | Stable production-ready code   |
| develop   | Active integration branch      |
| feature/* | Individual feature development |
| hotfix/*  | Urgent production fixes        |
| release/* | Release preparation            |

---

# Git Best Practices

## Commit Frequently

Create commits after completing meaningful, self-contained tasks.

Good Example:

```text
feat: implement object detection module
```

Avoid:

```text
update
changes
fixed stuff
```

---

## Keep Commits Focused

Each commit should represent a single logical change.

Examples:

✅ One feature per commit

❌ Multiple unrelated changes in the same commit

---

## Review Before Committing

Always inspect modified files before creating a commit.

Checklist:

* Correct files staged
* No debug code
* No unnecessary files
* Documentation updated if needed

---

## Protect Sensitive Information

Never commit:

```text
.env
credentials
api keys
database passwords
private certificates
```

Use:

```text
.env.example
```

for configuration templates.

---

## Manage Large Files Carefully

Avoid committing:

* Large datasets
* Trained model weights
* Generated outputs
* Temporary files

Recommended solutions:

* GitHub Releases
* Cloud Storage
* Model Registries
* External Dataset Links

---

## Keep Documentation Updated

Documentation should evolve alongside the codebase.

Update documentation whenever:

* New features are added
* Architecture changes
* Setup instructions change
* Dependencies change

---

# Recommended Development Cycle

```text
Plan
  ↓
Develop
  ↓
Test
  ↓
Document
  ↓
Commit
  ↓
Push
  ↓
Repeat
```

---

# VS Code Integration

The project is primarily managed through the VS Code Source Control interface.

### Common Actions

| Action            | VS Code Feature    |
| ----------------- | ------------------ |
| Review Changes    | Source Control     |
| Stage Files       | "+" Button         |
| Commit Changes    | Commit Message Box |
| Push Changes      | Sync Changes       |
| Resolve Conflicts | Merge Editor       |

---

# Repository Standards

The following standards should be maintained throughout development:

* Clean commit history
* Meaningful commit messages
* Consistent documentation
* No sensitive information in Git
* Modular feature development
* Regular synchronization with GitHub

---

# Current Development Status

| Item                   | Status        |
| ---------------------- | ------------- |
| Git Repository         | ✅ Initialized |
| GitHub Repository      | ✅ Connected   |
| SSH Authentication     | ✅ Configured  |
| VS Code Integration    | ✅ Active      |
| Documentation Workflow | ✅ Established |
| Feature Branching      | ⏳ Planned     |
| CI/CD Pipeline         | ⏳ Planned     |

---

## Version Information

**Project:** Campus Guardian AI
**Document:** Git Workflow Guide
**Version:** 1.0.0
**Status:** Active Development

---

## Suggested Commit Message

```text
docs: add git workflow and version control guide
```
