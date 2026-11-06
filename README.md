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

### 1. Model Performance Across Partitions (Clean 82-Feature Dataset)

All models are trained strictly on pre-2015 data and evaluated on subsequent temporal splits after auditing and removing 13 target-leakage features:

#### Test Set (2016–2018 Held-Out Evaluation, n = 504,194)

| Model | AUC-ROC | KS Stat | Gini | F1 Score | Wilcoxon $p$-value | Significance |
|-------|---------|---------|------|----------|-------------------|--------------|
| XGBoost | 0.7071 | 0.2995 | 0.4142 | 0.0727 | $1.60 \times 10^{-106}$ | *** ($p < 0.001$) |
| LightGBM | 0.7047 | 0.2962 | 0.4094 | 0.0611 | $9.15 \times 10^{-102}$ | *** ($p < 0.001$) |
| Random Forest | 0.7008 | 0.2881 | 0.4015 | 0.0006 | $9.08 \times 10^{-125}$ | *** ($p < 0.001$) |
| **Ensemble (L1)** | **0.7057** | **0.2974** | **0.4115** | **0.0345** | *(Baseline)* | — |

*Wilcoxon signed-rank test conducted against the ensemble baseline on the test partition ($n = 10,000$ paired samples, all $p < 0.001$).*

#### Validation Set (2015 Tuning Partition, n = 375,220)

| Model | AUC-ROC | KS Stat | Gini | F1 Score |
|-------|---------|---------|------|----------|
| XGBoost | 0.7432 | 0.3546 | 0.4864 | 0.1070 |
| LightGBM | 0.7420 | 0.3536 | 0.4841 | 0.0886 |
| Random Forest | 0.7386 | 0.3474 | 0.4772 | 0.0007 |
| **Ensemble (L1)** | **0.7427** | **0.3538** | **0.4853** | **0.0502** |

---

### 2. Three-Layer ACRS Framework Comparison

| Capability | Layer 1 (Baseline Ensemble) | Layer 2 (Rule-Based Monitoring) | Layer 3 (Agentic Governance) |
|------------|-----------------------------|---------------------------------|------------------------------|
| **AUC-ROC** | 0.7057 | 0.7057 | 0.7057 |
| **KS Statistic** | 0.2974 | 0.2974 | 0.2974 |
| **Gini Coefficient** | 0.4115 | 0.4115 | 0.4115 |
| **F1 Score** | 0.0345 | 0.0345 | 0.0345 |
| **PSI Drift Monitoring** | ✗ None | 0.0038 (✅ Stable) | 0.0038 (✅ Stable) |
| **Streaming Drift Detection** | ✗ None | ✗ None | **10 alerts / 5k loans** (9 DDM, 1 ADWIN) |
| **Explainability** | ✗ None | Batch SHAP ($n = 2,000$) | **Per-loan real-time SHAP** (Top-3 drivers) |
| **HITL Escalation Trigger** | ✗ None | ✗ None | **3.1% referral rate** (62 / 2,000 loans) |
| **Audit Trail** | ✗ None | ✗ None | ✅ **Append-only log** (2,000 decisions recorded) |

---

### 3. Layer 3 Agentic Decision Breakdown (Sample: 2,000 Test Loans)

| Decision Category | Count | Proportion | Action Description |
|-------------------|-------|------------|--------------------|
| `AUTO_APPROVE` | 1,805 | 90.2% | Automated approval for low-risk applicants |
| `AUTO_DECLINE` | 133 | 6.7% | Automated rejection for high-risk profiles |
| `REFER_TO_HUMAN` | 62 | 3.1% | Human-in-the-Loop (HITL) escalation triggered by uncertainty / drift |

---

## Dataset & Preprocessing

**Lending Club Loan Dataset (2007–2018)** — sourced from [Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club).

> ⚠️ The raw dataset is **not tracked** in Git due to file size (~2.26M rows, 1.18 GB). Place `loan.csv` in the root or `acrs_data/raw/` prior to running `ACRS.ipynb`.

### Preprocessing & Leakage Elimination Pipeline:
1. **Target Definition**: Retained completed loans (`Fully Paid`, `Charged Off`, `Default`, and credit-policy variants), resulting in 1,329,272 loans (21.61% default rate).
2. **Missing Value Filtering**: Dropped 58 columns exhibiting $> 40\%$ missing data.
3. **Leakage Audit**: Removed 13 post-origination features that introduce lookahead bias (`total_pymnt`, `total_pymnt_inv`, `total_rec_prncp`, `total_rec_int`, `total_rec_late_fee`, `recoveries`, `collection_recovery_fee`, `last_pymnt_amnt`, `out_prncp`, `out_prncp_inv`, `funded_amnt_inv`, `installment`, `debt_settlement_flag_Y`), resulting in **82 clean features**.
4. **Temporal Partitioning**:
   - **Training Set**: 2007–2014 → 449,858 records (17.1% default rate)
   - **Validation Set**: 2015 → 375,220 records (20.5% default rate)
   - **Test Set**: 2016–2018 → 504,194 records (26.5% default rate)

---

## Notebooks

The framework is implemented as 5 sequential Jupyter notebooks:

| Notebook | Purpose & Description | Output Artifacts |
|----------|-----------------------|------------------|
| [`ACRS.ipynb`](file:///d:/Thesis/Evaluation/ACRS/ACRS.ipynb) | Phase 1 data pipeline: missingness filtering, leakage audit, categorical encoding, and temporal splits. | `X_train.parquet`, `X_val.parquet`, `X_test.parquet`, `y_*.npy` |
| [`ACRS_Layer1_Modelling.ipynb`](file:///d:/Thesis/Evaluation/ACRS/ACRS_Layer1_Modelling.ipynb) | Layer 1 modeling: Optuna tuning (30 trials), ensemble training (XGBoost + LightGBM + Random Forest soft voting). | `*_final.pkl`, `*_prob_val.npy`, `*_prob_test.npy` |
| [`ACRS_Layer2.ipynb`](file:///d:/Thesis/Evaluation/ACRS/ACRS_Layer2.ipynb) | Layer 2 monitoring: Population Stability Index (PSI) drift monitoring across models and batch TreeExplainer SHAP. | `layer2_results.json`, `shap_importance_l2.csv`, `shap_bar_l2.png` |
| [`ACRS_Layer3.ipynb`](file:///d:/Thesis/Evaluation/ACRS/ACRS_Layer3.ipynb) | Layer 3 agentic governance: `ScoringAgent`, `DriftAgent` (DDM + ADWIN streaming detection), and `ComplianceAgent` with HITL and audit logging. | `layer3_results.json`, `audit_trail.csv` |
| [`ACRS_Evaluation.ipynb`](file:///d:/Thesis/Evaluation/ACRS/ACRS_Evaluation.ipynb) | Cross-layer synthesis: Wilcoxon signed-rank test, ROC curves, multi-layer capability comparison, and visual artifact generation. | `evaluation_results.json`, `fig_roc_capability.png`, `fig_shap_drift.png` |

---

## Top SHAP Features (Batch Analysis, n = 2,000 Test Loans)

Top features driving XGBoost predictions identified via SHAP `TreeExplainer` on the test partition:

| Rank | Feature | Mean \|SHAP\| Value | Domain Meaning |
|------|---------|---------------------|----------------|
| 1 | `sub_grade` | 0.2915 | Granular borrower credit subgrade |
| 2 | `term` | 0.2033 | Loan repayment duration (36 or 60 months) |
| 3 | `annual_inc` | 0.1545 | Self-reported annual income |
| 4 | `acc_open_past_24mths` | 0.1119 | Accounts opened in the past 24 months |
| 5 | `dti` | 0.0983 | Debt-to-income ratio |
| 6 | `grade` | 0.0874 | Broad credit rating band |
| 7 | `loan_amnt` | 0.0791 | Total loan principal requested |
| 8 | `int_rate` | 0.0736 | Assigned interest rate |
| 9 | `home_ownership_RENT` | 0.0452 | Housing tenancy status (Renting) |
| 10 | `total_bc_limit` | 0.0447 | Aggregate bankcard credit limit |

---

## Regulatory Alignment

| Regulation | Institutional Requirement | ACRS Supervisory Response |
|------------|---------------------------|---------------------------|
| **SR 11-7 / SR 26-2** *(Federal Reserve, 2011 / 2026)* | Ongoing model monitoring, risk management, and documented controls | `DriftAgent` (PSI, DDM, ADWIN), `ComplianceAgent` append-only audit trail, and HITL exception routing |
| **GDPR Article 22** *(European Union, 2016)* | Right to explanation and meaningful information regarding automated decisions | `ScoringAgent` per-loan real-time SHAP attribution with top risk drivers |
| **EBA ML Guidelines** *(European Banking Authority, 2021)* | Individualized explainability and operational drift governance | Real-time TreeExplainer SHAP integration with stream drift alerts |

---

## Project Structure

```
ACRS-Credit-Risk-Supervisor/
├── ACRS.ipynb                   # Phase 1: Data Pipeline, Temporal Split, Leakage Audit
├── ACRS_Layer1_Modelling.ipynb  # Layer 1: Optuna Tuning & Hybrid Ensemble Baseline
├── ACRS_Layer2.ipynb            # Layer 2: Population Stability Index (PSI) & Batch SHAP
├── ACRS_Layer3.ipynb            # Layer 3: Agentic Governance (Scoring, Drift, Compliance)
├── ACRS_Evaluation.ipynb        # Synthesis: Statistical Significance & Visualization
├── acrs_data/
│   ├── audit_trail.csv          # Layer 3 append-only compliance audit trail (2,000 rows)
│   ├── evaluation_results.json  # Comprehensive model comparison metrics & Wilcoxon p-values
│   ├── layer2_results.json      # Layer 2 PSI and SHAP summary metrics
│   ├── layer3_results.json      # Layer 3 governance & HITL rate metrics
│   ├── shap_importance_l2.csv   # Ranked mean |SHAP| feature importances
│   ├── fig_roc_capability.png   # ROC curves & cross-layer progression visual
│   ├── fig_shap_drift.png       # SHAP summary & streaming drift alert trajectory
│   └── shap_bar_l2.png          # Top SHAP feature bar chart
├── LCDataDictionary.xlsx        # Lending Club data dictionary reference
├── requirements.txt             # Python dependencies
├── .gitignore                   # Ignore raw datasets, parquet files, pickle models, venvs
└── README.md                    # Project documentation
```

---

## Installation & Execution

```bash
git clone https://github.com/Hiremorshadul/ACRS-Credit-Risk-Supervisor.git
cd ACRS-Credit-Risk-Supervisor
pip install -r requirements.txt
```

Launch Jupyter:
```bash
jupyter notebook
```

Execute the notebooks in sequence:
1. `ACRS.ipynb`
2. `ACRS_Layer1_Modelling.ipynb`
3. `ACRS_Layer2.ipynb`
4. `ACRS_Layer3.ipynb`
5. `ACRS_Evaluation.ipynb`

---

## Research Context

This prototype serves as the implementation artifact for a Master's thesis applying the **Design Science Research (DSR)** paradigm (Hevner et al., 2004). The project addresses the operational and governance gap in production credit risk architectures — providing autonomous drift detection, real-time explainability, and structured human-in-the-loop oversight to ensure regulatory compliance and robust model risk management.

---

## License

This repository is shared for academic and research purposes. The Lending Club dataset is subject to its respective Kaggle terms of use.
