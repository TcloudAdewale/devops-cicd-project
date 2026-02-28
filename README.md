# 🚀 DevOps CI/CD Pipeline Project

> A fully automated CI/CD pipeline that builds, tests, and deploys a containerized Flask web application using Docker and GitHub Actions.

![Status](https://img.shields.io/badge/status-active-success)
![Platform](https://img.shields.io/badge/platform-Linux-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange)

---

## 📌 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Challenges & Lessons Learned](#challenges--lessons-learned)
- [What I'd Improve Next](#what-id-improve-next)
- [Author](#author)

---

## 📖 Overview

**What does this project do?**
This project demonstrates a complete CI/CD pipeline for a Python Flask web application. Every time code is pushed to the main branch, GitHub Actions automatically runs tests, builds a Docker image, and pushes it to Docker Hub — without any manual intervention.

**Why did I build it?**
As part of my DevOps engineering journey at NaNa DevOps Bootcamp, I wanted to build a real, working pipeline from scratch — not just follow a tutorial. This project represents Phase 1 of my 3-project DevOps portfolio.

**What problem does it solve?**
It eliminates manual deployment steps by automating the entire build-test-deploy workflow. Any developer on the team can push code and trust that it will be tested and packaged automatically.

---

## 🏗️ Architecture

```
Developer pushes code to GitHub (main branch)
            ↓
GitHub Actions triggered automatically
            ↓
Python environment set up
            ↓
Dependencies installed (Flask, pytest)
            ↓
Automated tests run (pytest)
            ↓
Docker image built
            ↓
Image pushed to Docker Hub
            ↓
✅ Pipeline complete — image ready for deployment
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Application runtime |
| Flask 3.0 | Web framework |
| Pytest | Automated testing |
| Docker | Containerization |
| GitHub Actions | CI/CD pipeline automation |
| Docker Hub | Container image registry |
| Ubuntu (Linux) | Development environment |

---

## ✅ Prerequisites

Before running this project, make sure you have:

- [ ] Linux / Ubuntu (or WSL on Windows)
- [ ] Docker installed → `docker --version`
- [ ] Git installed → `git --version`
- [ ] Python 3.11+ → `python3 --version`
- [ ] Docker Hub account → hub.docker.com

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/TcloudAdewale/devops-cicd-project.git
cd devops-cicd-project
```

### 2. Create virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run tests locally

```bash
pytest test_app.py -v
```

Expected output:
```
test_app.py::test_home PASSED    [ 50%]
test_app.py::test_health PASSED  [100%]
2 passed in 0.24s
```

### 4. Build and run with Docker

```bash
docker build -t devops-app .
docker run -p 5000:5000 devops-app
```

### 5. Test the running app

```bash
curl http://localhost:5000
curl http://localhost:5000/health
```

---

## 📁 Project Structure

```
devops-cicd-project/
├── app.py                        # Flask web application
├── test_app.py                   # Automated tests (pytest)
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Container definition
├── .gitignore                    # Files excluded from git
└── .github/
    └── workflows/
        └── deploy.yml            # GitHub Actions CI/CD pipeline
```

---

## 💻 Usage

```bash
# Run tests
pytest test_app.py -v

# Build Docker image
docker build -t devops-app .

# Run container
docker run -p 5000:5000 devops-app

# Check app endpoints
curl http://localhost:5000           # Main endpoint
curl http://localhost:5000/health    # Health check
```

**API Endpoints:**

| Endpoint | Method | Response |
|----------|--------|----------|
| `/` | GET | JSON with app info and status |
| `/health` | GET | `{"status": "healthy"}` |

---

## 📸 Screenshots

**✅ CI/CD Pipeline — All Steps Passing:**

> Add your GitHub Actions screenshot here
> (Settings → Actions → Latest run → Screenshot)

**🐳 Docker Hub — Image Published:**

> Add your Docker Hub screenshot here
> (hub.docker.com/r/tcloudguy/devops-app)

---

## 🧠 Challenges & Lessons Learned

**Challenge 1: Docker daemon was masked**
When I first tried to start Docker, I got `Unit docker.service is masked`. I had to unmask both `docker.service` and `docker.socket` using `systemctl unmask` before Docker would start. This taught me how systemd manages service states.

**Challenge 2: GitHub Actions failing with Docker Hub credentials**
The pipeline initially failed with `Username and password required`. I learned that GitHub Actions needs secrets stored in the repository settings — it cannot access local environment variables. Adding `DOCKER_USERNAME` and `DOCKER_PASSWORD` as repository secrets fixed this.

**Challenge 3: Wrong Docker Hub username in pipeline**
The workflow was pushing to `tcloudadewale/devops-app` but my Docker Hub username is `tcloudguy`. This caused a `denied: requested access to the resource is denied` error. Updating the image name in the workflow file resolved it.

**Challenge 4: venv committed to git**
My first commit accidentally included the entire `venv/` folder (839 files!). I learned to always add `venv/` to `.gitignore` before the first commit and use `git rm -r --cached venv/` to remove it from tracking.

**What I learned:**
- How GitHub Actions secrets work and why they matter for security
- How to debug CI/CD pipeline failures by reading job logs
- The importance of `.gitignore` from the very first commit
- How systemd manages Docker service states on Linux

---

## 🔧 What I'd Improve Next

- [ ] Add SSH deployment step to push to a live cloud VM
- [ ] Implement secrets management with environment variables
- [ ] Add more comprehensive test coverage
- [ ] Set up staging and production environments
- [ ] Add Slack/email notifications for pipeline failures
- [ ] Integrate with Terraform for infrastructure provisioning (Phase 2)

---

## 👤 Author

**Abidemi Adewale (Tcloud)**

DevOps / Cloud Engineer | AltSchool Africa Graduate | CS Student @ University of the People

- 🌐 Medium: [@tcloudadewale](https://medium.com/@tcloudadewale)
- 💼 LinkedIn: [Abidemi Adewale](https://linkedin.com/in/tcloudadewale)
- 🐙 GitHub: [@TcloudAdewale](https://github.com/TcloudAdewale)
- 🐳 Docker Hub: [tcloudguy](https://hub.docker.com/u/tcloudguy)

---

> *"Build it. Break it. Document it. Automate it."*

---
