# 🏥 CareFlow: AI-Powered Hospital Flow & Decision Support System

## Overview

CareFlow is an agentic healthcare simulation platform designed to optimize hospital flow management through deterministic decision-making and explainable AI. The system evaluates patient risk, models hospital resource pressure, and generates operational decisions while maintaining transparency, auditability, and safety.

Unlike conventional AI systems, CareFlow follows a **Safety-First AI Architecture** where artificial intelligence never makes clinical or operational decisions. All decisions are generated through deterministic rule-based engines, while Large Language Models (LLMs) are used exclusively for post-hoc reasoning and explanation generation.

This architecture ensures that decisions remain explainable, reproducible, and fully auditable while still benefiting from AI-powered insights.

---

## Objectives

* Simulate hospital patient flow using deterministic decision engines.
* Evaluate patient risk using temporal healthcare signals.
* Model hospital resource pressure and operational constraints.
* Generate explainable healthcare decisions.
* Provide structured simulation outputs for analysis.
* Use AI for post-hoc reasoning without influencing decisions.
* Improve transparency and auditability in healthcare operations.

---

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **LangChain**
* **Ollama**
* **Mistral LLM**
* **Rule-Based Decision Systems**
* **Agentic AI Architecture**

---

## System Architecture

```text
Patient CSV Data
        ↓
Risk Agent (Temporal Signals)
        ↓
Hospital Resource Pressure
        ↓
Decision Engine (Deterministic)
        ↓
Structured Simulation Output
        ↓
Post-Hoc AI Reasoning (LLM)
        ↓
Human-Readable Explanation
```

---

## Core Capabilities

### 1. Hospital Flow Simulation

The simulation engine models healthcare operations using deterministic rules.

Features include:

* Temporal Patient Risk Evaluation
* Hospital Resource Pressure Modeling
* Resource State Management
* Deterministic Healthcare Decision-Making

Possible actions:

* OBSERVE
* ALLOW
* PRIORITIZE

---

### 2. Structured Simulation Outputs

Each simulation step generates:

* Patient ID
* Timestamp
* Risk Level
* Signal Score
* Hospital Pressure
* Decision Outcome
* Engine Explanation

This structured output enables auditing, monitoring, and downstream analysis.

---

### 3. Explainable AI Reasoning

Large Language Models are used only after simulation decisions have been generated.

The AI system:

* Explains why a decision occurred.
* Provides operational reasoning.
* Generates clinician-friendly summaries.

The AI system does **not**:

* Make decisions
* Override decisions
* Influence decision logic

This ensures complete separation between decision-making and explanation generation.

---

## Project Workflow

### 1. Risk Assessment

The Risk Engine analyzes temporal patient signals and evaluates urgency levels.

Key factors include:

* Signal Severity
* Temporal Patterns
* Patient State Evolution

---

### 2. Hospital Pressure Modeling

The Pressure Engine evaluates hospital operational load using:

* Resource Utilization
* Capacity Constraints
* Patient Demand

This helps simulate real-world healthcare system pressure.

---

### 3. Deterministic Decision Engine

The Decision Engine combines:

* Patient Risk
* Hospital Pressure
* Resource Availability

to generate operational decisions.

Possible outputs:

| Decision   | Description                      |
| ---------- | -------------------------------- |
| OBSERVE    | Continue monitoring              |
| ALLOW      | Allow standard flow              |
| PRIORITIZE | Escalate for immediate attention |

---

### 4. Simulation Output Generation

Simulation results are generated for every patient and timestamp.

Outputs remain:

* Deterministic
* Reproducible
* Explainable
* Auditable

---

### 5. Post-Hoc AI Reasoning

Once simulation results are available:

* Analytical reasoning is performed.
* Human-readable explanations are generated.
* Operational insights are provided.

The reasoning layer never modifies simulation outputs.

---

## Repository Structure

```text
CareFlow/
│
├── hospital_flow_engine/
│   ├── data/
│   │   └── CSV datasets
│   │
│   ├── engine/
│   │   ├── risk_engine.py
│   │   ├── pressure_engine.py
│   │   ├── decision_engine.py
│   │   └── resource_model.py
│   │
│   └── simulate.py
│
├── reasoning/
│   ├── llm.py
│   ├── analysis_chain.py
│   ├── explanation_chain.py
│   └── post_simulation_chain.py
│
├── run_simulation.py
├── requirements.txt
└── README.md
```

---

## LangChain Design

### Query Chain

Interfaces directly with deterministic simulation outputs.

### Analysis Chain

Performs causal and operational reasoning over simulation results.

### Explanation Chain

Generates clinician-friendly and operator-friendly explanations.

### Post Simulation Chain

Coordinates the complete reasoning workflow.

---

## Key Features

* Agentic Healthcare Simulation
* Temporal Risk Assessment
* Hospital Pressure Modeling
* Deterministic Decision Engine
* Structured Operational Outputs
* Explainable AI Reasoning
* LangChain Integration
* Ollama-Based Local LLM Support
* Auditable Healthcare Decisions
* Safety-First AI Architecture

---

## Installation & Setup

### Prerequisites

* Python 3.10+
* pip
* Ollama (Optional)

> The simulation engine works without Ollama. Only AI-generated explanations require it.

---

### Clone the Repository

```bash
git clone https://github.com/janhavee-s/CareFlow.git
cd CareFlow
```

---

### Create Virtual Environment

#### Mac/Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Optional: Enable AI Reasoning

Start Ollama:

```bash
ollama serve
```

In a separate terminal:

```bash
ollama pull mistral
```

Ensure Ollama is running on:

```text
http://localhost:11434
```

---

## Run the Simulation

From the project root directory:

```bash
python run_simulation.py
```

---

## What Happens When You Run It?

### Hospital Flow Simulation

The system:

* Loads patient datasets.
* Computes patient risk.
* Evaluates hospital pressure.
* Generates deterministic decisions.
* Produces structured simulation outputs.

---

### AI-Powered Reasoning

A sample patient record is selected.

The reasoning layer:

* Analyzes simulation outcomes.
* Generates explanations.
* Produces operational insights.

The generated explanations never influence decisions.

---

## Skills Demonstrated

* Agentic AI Systems
* Healthcare Analytics
* Decision Support Systems
* Explainable AI (XAI)
* LangChain Development
* Simulation Modeling
* Risk Assessment
* Resource Optimization
* Rule-Based AI Systems
* System Architecture Design

---

## Future Enhancements

* Real-Time Hospital Capacity Integration
* Bed Availability Prediction
* Emergency Department Optimization
* Multi-Hospital Network Simulation
* Predictive Resource Allocation
* Advanced Healthcare Digital Twin Modeling
* Dashboard Visualization Layer

---

## Author

**Janhavee Singh**

B.Tech Computer Science | Artificial Intelligence | Machine Learning | Healthcare Analytics

CareFlow demonstrates the integration of deterministic healthcare simulation, explainable AI, hospital operations modeling, and agentic system design to create transparent, auditable, and safety-focused healthcare decision support systems.