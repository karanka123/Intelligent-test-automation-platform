# Intelligent-test-automation-platform
AI-assisted web test automation platform that generates, prioritizes, executes, and analyzes test cases using FastAPI, Playwright, PostgreSQL, and intelligent workflows.

# Intelligent Test Automation Platform

An AI-assisted automated testing platform that generates, prioritizes, executes, and analyzes web application test cases using automation and intelligent workflows.

---

# Overview

The Intelligent Test Automation Platform is designed to reduce manual testing effort by automatically generating test cases from web applications and executing them using browser automation.

The platform supports:

* Automatic test generation from URLs
* AI-assisted custom test generation using prompts
* Unified test execution pipeline
* Smart test prioritization
* Result analysis with logs and screenshots

---

# Features

## Automatic Test Generation

* Scan webpage structure
* Detect forms and interactive elements
* Generate baseline test cases automatically

## AI-Based Test Expansion

* Generate targeted test cases using natural language prompts
* Example:

  * "Test login with SQL injection"
  * "Generate edge cases for signup form"

## Test Execution

* Execute tests using Playwright
* Capture screenshots and logs

## Smart Prioritization

* Execute high-priority tests first
* Prioritize based on failure history and criticality

## Reporting Dashboard

* View execution results
* Analyze failures
* Track test history

---

# System Architecture

```text
Frontend (React)
        ↓
FastAPI Backend
        ↓
--------------------------------
| Auto Generator | AI Engine |
--------------------------------
        ↓
Test Manager
        ↓
Playwright Execution Engine
        ↓
PostgreSQL Database
        ↓
Results Dashboard
```

---

# Tech Stack

## Backend

* Python
* FastAPI

## Frontend

* React

## Automation

* Playwright

## Database

* PostgreSQL
* SQLAlchemy

## AI Integration

* OpenAI API

---

# Workflow

1. User provides URL or prompt
2. System generates test cases
3. Test cases are merged and prioritized
4. Tests are executed using Playwright
5. Results are stored and displayed

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd intelligent-test-automation-platform
```

## Backend Setup

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn main:app --reload
```

---

# Future Enhancements

* CI/CD integration
* Parallel test execution
* AI-based self-healing selectors
* Advanced analytics dashboard

---

# Project Status

Currently under active development.

---

# Author

Karan K A
