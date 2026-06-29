# DecisionPilot OS

## Intelligent Next Best Action Platform

DecisionPilot OS is a reusable **Agentic Decision Intelligence Platform** that transforms enterprise customer interactions and organizational knowledge into intelligent, explainable, and actionable Next Best Action recommendations.

The platform combines dynamic planner-based agent orchestration, enterprise knowledge retrieval, risk assessment, explainable AI, knowledge graphs, memory, and human-in-the-loop review to assist business users in making confident and data-driven decisions.

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

DecisionPilot OS follows a planner-driven multi-agent architecture where a Planner Agent dynamically orchestrates specialized agents based on the business context.

### Workflow

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
* Local Database

---

# Multi-Agent Architecture

The platform consists of specialized AI agents including:

* Planner Agent
* Knowledge Agent
* Customer Discovery Agent
* ICP Agent
* Risk Agent
* Decision Agent
* Recommendation Agent
* Explainability Agent
* Graph Agent
* Analytics Agent
* Memory Agent
* Scenario Agent *(Future Capability)*
* Learning Agent *(Future Capability)*

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

Before running the project, install the following software:

* Python 3.11 or later
* Node.js 18 or later
* npm
* Git

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/Potharaju-Vinay/DecisionPilot-OS.git

cd DecisionPilot-OS
```

---

## Backend Setup

Create a Python virtual environment.

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Run the Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger API Documentation

```
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

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

```
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
Analytics Dashboard
        │
        ▼
Human-in-the-Loop Review
        │
        ▼
Final Business Decision
```

---

# Sample Documents

Sample enterprise proposal documents are provided inside:

```text
data/samples/
```

These documents can be uploaded directly into the application to evaluate the complete workflow without preparing your own input files.

---

# Human-in-the-Loop

DecisionPilot OS supports human oversight before AI recommendations are accepted.

Available actions:

* ✅ Approve
* ❌ Reject
* 🟡 Manual Review

This ensures enterprise decisions always remain under human control while leveraging AI-powered recommendations.

---

# Explainable AI

Every recommendation includes:

* Supporting Evidence
* Business Reasoning
* Confidence Score
* Risk Analysis
* Decision Explanation

This improves transparency, trust, and decision confidence for business users.

---

# Troubleshooting

## Gemini API Quota

DecisionPilot OS uses the Google Gemini API for AI-powered document understanding and business reasoning.

If execution fails because of quota limits or no AI response is returned, the free-tier Gemini API quota has likely been exhausted.

To continue using the platform:

1. Generate a new Google Gemini API Key.
2. Replace the existing key inside the `.env` file.

```env
GOOGLE_API_KEY=YOUR_NEW_API_KEY
```

3. Restart the FastAPI backend.

The application will resume normal operation after updating the API key.

---

# Documentation

Complete project documentation is available in the **docs/** directory.

---

# Future Enhancements

* Advanced Scenario Simulation
* Continuous Learning Intelligence
* Multi-Organization Memory
* Enterprise Authentication
* Cloud Deployment
* Role-Based Access Control
* Real-Time CRM Integration
* CRM & ERP Connectors
* Enterprise SSO Support

---

# Hackathon

Developed as a submission for the **XLVentures.AI Hackathon 2026**.

---

# Author

**Potharaju Vinay**

B.Tech – Cyber Security

VNR Vignana Jyothi Institute of Engineering & Technology

---

# License

This project is developed for educational, research, and hackathon purposes only.
