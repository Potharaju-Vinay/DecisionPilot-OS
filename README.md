# DecisionPilot OS

## Intelligent Next Best Action Platform

DecisionPilot OS is an AI-powered **Agentic Decision Intelligence Platform** that transforms enterprise customer interactions and organizational knowledge into intelligent, explainable, and actionable **Next Best Action** recommendations.

The platform combines dynamic planner-based agent orchestration, enterprise knowledge retrieval, risk assessment, explainable AI, knowledge graphs, memory, and human-in-the-loop review to help organizations make confident, transparent, and data-driven business decisions.

---

# Team Details

**Team Name:** Kanyarashi

**Team Members:**

* **Potharaju Vinay**

---

# Project Overview

DecisionPilot OS analyzes enterprise proposal documents and business information using multiple AI agents. It evaluates customer qualification, business opportunities, compliance risks, and organizational readiness before generating an explainable business decision along with actionable recommendations.

The platform is designed to reduce manual effort, improve decision quality, and increase transparency in enterprise sales and strategic decision-making.

---

# GitHub Repository

Repository Link:

**https://github.com/Potharaju-Vinay/DecisionPilot-OS/tree/main**

---

# Key Features

* Dynamic Planner-Based Agent Orchestration
* Multi-Agent AI Architecture
* Enterprise Knowledge Retrieval
* Customer Discovery Intelligence
* Ideal Customer Profile (ICP) Analysis
* Business Risk Assessment
* AI Decision Intelligence
* Explainable AI (XAI)
* Next Best Action Recommendation Engine
* Interactive Enterprise Knowledge Graph
* Executive Analytics Dashboard
* Short-Term and Long-Term Memory
* Human-in-the-Loop Decision Review
* Modular and Extensible Agent Framework

---

# System Architecture

DecisionPilot OS follows a planner-driven multi-agent architecture where a Planner Agent dynamically orchestrates specialized AI agents based on business context.

## Workflow

1. Document Upload
2. Knowledge Extraction
3. Customer Discovery
4. ICP Analysis
5. Risk Assessment
6. AI Decision Intelligence
7. Recommendation Generation
8. Explainability
9. Knowledge Graph Construction
10. Analytics Dashboard
11. Memory Update
12. Human Approval

---

# Technology Stack

## Backend

* Python
* FastAPI
* LangGraph
* Google Gemini 2.5 Flash

## Frontend

* React.js
* Vite
* Tailwind CSS
* React Flow

## AI Components

* Multi-Agent Architecture
* Planner Agent
* Enterprise Knowledge Retrieval
* Explainable AI
* Knowledge Graph
* Memory Management

## Database & Storage

* ChromaDB
* Vector Embeddings
* SQLite

---

# Multi-Agent Architecture

The platform consists of the following AI agents:

* Planner Agent
* Knowledge Agent
* Customer Discovery Agent
* ICP Qualification Agent
* Risk Assessment Agent
* Decision Intelligence Agent
* Recommendation Agent
* Explainability Agent
* Graph Agent
* Analytics Agent
* Memory Agent

### Future Agents

* Scenario Agent
* Learning Agent

---

# Project Structure

```text
DecisionPilot-OS
│
├── backend/
├── frontend/
├── docs/
├── data/
│   └── samples/
├── requirements.txt
└── README.md
```

---

# Prerequisites

Install the following before running the project:

* Python 3.11+
* Node.js 18+
* npm
* Git

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Potharaju-Vinay/DecisionPilot-OS.git

cd DecisionPilot-OS
```

---

# Backend Setup

Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

# Run Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Open another terminal.

```bash
cd frontend

npm install

npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# Platform Workflow

```text
Document Upload
        │
        ▼
Knowledge Extraction
        │
        ▼
Customer Discovery
        │
        ▼
ICP Analysis
        │
        ▼
Risk Assessment
        │
        ▼
Decision Intelligence
        │
        ▼
Recommendation Generation
        │
        ▼
Explainability
        │
        ▼
Knowledge Graph
        │
        ▼
Enterprise Analytics
        │
        ▼
Memory Update
        │
        ▼
Human Review
        │
        ▼
Final Business Decision
```

---

# Sample Documents

Sample enterprise proposal documents are available in:

```text
data/samples/
```

Upload these documents to evaluate the complete workflow.

---

# Human-in-the-Loop

DecisionPilot OS keeps humans involved before any final recommendation is accepted.

Available actions:

* ✅ Approve
* ❌ Reject
* 🟡 Manual Review

This ensures enterprise decisions remain transparent and under human control.

---

# Explainable AI

Each recommendation includes:

* Supporting Evidence
* Business Reasoning
* Confidence Score
* Risk Analysis
* Decision Explanation
* Recommended Next Best Actions

This enables users to understand **why** a decision was generated.

---

# Troubleshooting

## Gemini API Quota

If AI responses stop working, the Gemini free-tier quota may have been exhausted.

Steps:

1. Generate a new Gemini API Key.
2. Replace the key inside the `.env` file.

```env
GOOGLE_API_KEY=YOUR_NEW_API_KEY
```

3. Restart the FastAPI backend.

---

# Documentation

Additional project documentation is available inside the **docs/** directory.

---

# Future Enhancements

* Scenario Simulation
* Continuous Learning
* Enterprise Authentication
* Cloud Deployment
* Role-Based Access Control
* CRM Integration
* ERP Integration
* Enterprise SSO
* Multi-Organization Memory
* Real-Time Collaboration

---

# Hackathon Submission

This project was developed as part of the **XLVentures.AI Hackathon 2026**.

---

# Author

**Potharaju Vinay**

B.Tech – Cyber Security

VNR Vignana Jyothi Institute of Engineering & Technology

---

# License

This project is developed for educational, research, and hackathon purposes only.
