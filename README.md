# ACRS — Agentic Credit Risk Supervisor

> Master's Thesis Prototype | Python 3.10 | Jupyter Notebooks

A three-layer, three-agent framework for autonomous credit risk supervision, combining hybrid machine learning prediction with real-time drift detection, per-loan SHAP explainability, and compliance-grade audit logging.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 3 — Agentic Governance                           │
│  Agent 1: Scoring   Agent 2: Drift   Agent 3: Compliance│
├─────────────────────────────────────────────────────────┤
│  LAYER 2 — Rule-Based Monitoring                        │
│  PSI Drift Monitoring + Batch SHAP Explainability       │
├─────────────────────────────────────────────────────────┤
│  LAYER 1 — Hybrid Ensemble Baseline                     │
│  XGBoost + LightGBM + Random Forest (Soft Voting)       │
└─────────────────────────────────────────────────────────┘
```

---

## Key Results

| Model | AUC-ROC | KS Stat | Gini | F1 |
|-------|---------|---------|------|----|
| XGBoost | 0.7438 | 0.3448 | 0.4876 | 0.2401 |
| LightGBM | 0.7409 | 0.3413 | 0.4818 | 0.2330 |
| Random Forest | 0.7374 | 0.3342 | 0.4747 | 0.2052 |
| **Ensemble (L1)** | **0.7424** | **0.3433** | **0.4848** | **0.2189** |

Wilcoxon signed-rank test: ensemble vs each individual model — all ***p < 0.001** (n=10,000).

| Layer | PSI | Drift Alerts | HITL Rate | Audit Trail |
|-------|-----|-------------|-----------|-------------|
| Layer 1 | — | — | — | — |
| Layer 2 | 0.0176 ✅ Stable | — | — | — |
| Layer 3 | 0.0176 ✅ Stable | 10 / 5,000 loans | 1.0% | ✅ Append-only |

---

## Dataset

**Lending Club Loan Dataset (2007–2018)** — sourced from [Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club).

> ⚠️ The dataset is **not included** in this repository due to file size (~2.26M records). Download it from Kaggle and place the CSV in `acrs_data/raw/` before running the notebooks.

Temporal split used:
- **Training**: Jan 2007 – Dec 2014 → 449,858 records, 17.1% default rate
- **Validation**: Jan 2015 – Dec 2015 → 375,220 records, 20.5% default rate
- **Test**: Jan 2016 – Sep 2018 → 504,194 records, 26.5% default rate

---

## Notebooks

| Notebook | Description |
|----------|-------------|
| `ACRS_Layer1_Ensemble.ipynb` | Data pipeline, leakage detection, Optuna tuning, ensemble construction |
| `ACRS_Layer2_Monitoring.ipynb` | PSI computation, batch SHAP, Layer 2 evaluation |
| `ACRS_Layer3_Agents.ipynb` | ScoringAgent, DriftAgent, ComplianceAgent implementation |
| `ACRS_Evaluation.ipynb` | Wilcoxon test, ROC curves, cross-layer comparison |

---

## Installation

```bash
git clone https://github.com/<your-username>/ACRS-Credit-Risk-Supervisor.git
cd ACRS-Credit-Risk-Supervisor
pip install -r requirements.txt
```

Then open Jupyter:
```bash
jupyter notebook
```

Run notebooks in order: Layer1 → Layer2 → Layer3 → Evaluation.

---

## Project Structure

```
ACRS-Credit-Risk-Supervisor/
├── notebooks/
│   ├── ACRS_Layer1_Ensemble.ipynb
│   ├── ACRS_Layer2_Monitoring.ipynb
│   ├── ACRS_Layer3_Agents.ipynb
│   └── ACRS_Evaluation.ipynb
├── acrs_data/
│   ├── audit_trail.csv
│   ├── shap_importance_l2.csv
│   ├── layer2_results.json
│   ├── layer3_results.json
│   ├── fig_roc_capability.png
│   └── fig_shap_drift.png
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Regulatory Alignment

| Regulation | Requirement | ACRS Response |
|------------|-------------|---------------|
| SR 11-7 (Fed Reserve, 2011) | Model risk management & documentation | Agent 3 audit trail + HITL escalation |
| GDPR Article 22 (EU, 2016) | Meaningful info about automated decisions | Per-loan SHAP attribution |
| EBA ML Guidelines (2021) | Explainability at individual decision level | Real-time SHAP via TreeExplainer |

---

## Top SHAP Features (Batch Analysis, n=2,000)

| Rank | Feature | Mean \|SHAP\| |
|------|---------|--------------|
| 1 | debt_settlement_flag_Y | 0.307 |
| 2 | sub_grade | 0.247 |
| 3 | term | 0.204 |
| 4 | annual_inc | 0.169 |
| 5 | acc_open_past_24mths | 0.117 |

---

## Research Context

This prototype is the implementation artefact for a Master's thesis applying the Design Science Research (DSR) paradigm (Hevner et al., 2004). The research addresses the governance gap in deployed credit risk systems — the absence of real-time explainability, autonomous drift detection, and structured human-in-the-loop oversight.

---

## License

This repository is shared for academic and research purposes. The Lending Club dataset is subject to its own Kaggle terms of use.
