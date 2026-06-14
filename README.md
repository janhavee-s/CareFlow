CareFlow – AI-Powered Hospital Flow & Decision Support System

CareFlow is an agentic healthcare simulation platform designed to optimize hospital flow management through deterministic decision-making and explainable AI. The system evaluates patient risk, models hospital resource pressure, and generates clinical actions while maintaining transparency and auditability.

Unlike conventional AI systems, CareFlow follows a safety-first architecture where AI does not make clinical decisions. All decisions are generated through rule-based engines, while Large Language Models (LLMs) are used solely to provide post-hoc explanations of the decision-making process.

◉ Overview
The backend simulates hospital patient flow using rule-based engines for:
Patient risk assessment (temporal signals)
Hospital resource pressure
Deterministic decision-making
An LLM (via Ollama) is used only after decisions are made to generate human-readable explanations.


◉ Core Capabilities
1. Hospital Flow Simulation
Temporal patient risk evaluation
Hospital pressure modeling

Deterministic decision engine:
OBSERVE
ALLOW
PRIORITIZE

2. Structured Outputs
Each simulation step produces:
Patient ID
Timestamp
Risk level
Signal score
Decision
Engine explanation
Hospital pressure

3. Post-hoc AI Reasoning
Uses a local LLM (Ollama).
Explains why a decision was made.
Never alters or influences decisions.


◉ Project Structure:
CareFlow/
│
├── hospital_flow_engine/
│   ├── data/                    # CSV datasets
│   ├── engine/
│   │   ├── risk_engine.py       # Temporal risk agent
│   │   ├── pressure_engine.py   # Hospital pressure model
│   │   ├── decision_engine.py   # Deterministic decisions
│   │   └── resource_model.py    # Resource state builder
│   └── simulate.py              # Simulation runner
│
├── reasoning/
│   ├── llm.py                   # LLM configuration (Ollama)
│   ├── analysis_chain.py        # Analytical reasoning
│   ├── explanation_chain.py     # Human-readable explanation
│   └── post_simulation_chain.py # Reasoning orchestration
│
├── run_simulation.py            # Backend entry point
└── requirements.txt             # Python dependencies


◉ System Flow:

Patient CSV Data
        ↓
Risk Agent (temporal signals)
        ↓
Hospital Resource Pressure
        ↓
Decision Engine (deterministic)
        ↓
Simulation Output (structured)
        ↓
LLM Reasoning (post-hoc explanation)


◉ Prerequisites:
Python 3.10+
Ollama (optional, for AI explanations)
Note: The simulation works without Ollama. Only LLM-based explanations require it.


◉ Backend Run Flow:
Step 1: Set up Python environment
Mac/Linux:
python -m venv .venv
source .venv/bin/activate

Windows:
python -m venv .venv
.venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt


Step 2: (Optional) Enable AI reasoning
AI explanations use Ollama.

Pull the model:
ollama serve (keep this running)
ollama pull mistral (on different terminal)
Ensure Ollama is running on: http://localhost:11434


Step 3: Run the backend
From the project root:

python run_simulation.py
What Happens When You Run It

◉ Hospital flow simulation starts:
Reads patient CSV data.
Computes risk, pressure, and decisions.
Simulation results are displayed:
One line per patient.
Fully deterministic engine output.

◉ A patient record is selected:
Used for explanation.
Post-hoc AI reasoning runs:
Explains why the decision was made.
Does not change the decision.

◉ LangChain Design:
Query Chain: Interfaces with deterministic engine outputs.
Analysis Chain: Performs causal reasoning over simulation results.
Explanation Chain: Produces human-readable explanations for clinicians or operators.

License
Use as needed for the CareFlow project.
