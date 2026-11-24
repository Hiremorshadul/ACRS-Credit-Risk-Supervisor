# ACRS — Agentic Credit Risk Supervisor

Code for the MSc thesis *Evaluating Agentic AI for Supervisory Control in Hybrid Credit Risk Models*
(Md Morshadul Alam, NOVA Information Management School, Universidade NOVA de Lisboa, 2026; supervisor: Afshin Ashofteh).

ACRS places three rule-based agents above a hybrid credit risk model. The agents explain each decision,
monitor drift, refer uncertain applications to a human and record every decision in a tamper-evident audit log.
The agents are deterministic rules; no large language model is used.

| Layer | Content |
|---|---|
| Layer 1 | Soft-voting ensemble of XGBoost, LightGBM and Random Forest (equal weights), with a logistic regression baseline |
| Layer 2 | Population Stability Index (PSI) of the predicted PD and SHAP explanations on the probability scale |
| Layer 3 | **Agent 1 (Scoring):** PD, risk band and the three largest SHAP contributions for each application<br>**Agent 2 (Drift Detection):** real-time, label-free monitoring of the PD stream (sliding-window detector and Page-Hinkley) and delayed-label monitoring once outcomes are known (DDM and a monthly report)<br>**Agent 3 (Compliance):** approve, decline or refer to a human (gray zone or drift alarm); every decision is written to an append-only audit log with a SHA-256 hash chain |

## Data

The Lending Club loan file `loan.csv` (2,260,668 loans, 145 columns, issued June 2007 to December 2018) from Kaggle:
<https://www.kaggle.com/datasets/wendykan/lending-club-loan-data>. It is not included in this repository (1.1 GB).
Place it in the repository folder before running the notebooks. The SHA-256 of the file used in the thesis is
stored in `acrs_data/environment.json`.

- **Default definition:** Charged Off or Default = 1, Fully Paid = 0. Current, late and grace-period loans, and loans
  issued outside Lending Club's credit policy, are excluded, leaving 1,303,638 resolved loans.
- **Temporal split:** training June 2007 – December 2014 (449,414 loans, 17.0% default), validation 2015
  (373,412 loans, 20.2%), test 2016–2018 (480,812 loans, 22.9%).
- **Features:** 36 post-origination columns are removed to prevent leakage; the models use 77 encoded features
  from 60 source columns (`acrs_data/feature_lists.json`, `acrs_data/feature_dictionary.csv`).

## Notebooks (run in this order)

| # | Notebook | What it does |
|---|---|---|
| 1 | `ACRS.ipynb` | Loads the data, applies the default definition and the temporal split, removes leaked and unusable columns, runs the leakage diagnostic and prepares the features |
| 2 | `ACRS_Layer1_Modelling.ipynb` | Tunes XGBoost, LightGBM and Random Forest with Optuna (TPE, 30 trials, seed 42), fits the final models, the logistic regression baseline and the ensemble |
| 3 | `ACRS_Layer2.ipynb` | PSI of the predicted PD and batch SHAP explanations (interventional TreeSHAP, 100 background loans, 2,000 test loans) |
| 4 | `ACRS_Evaluation.ipynb` | ROC-AUC with DeLong confidence intervals, DeLong and paired bootstrap tests, calibration, drift analysis by issue year and a domain classifier |
| 5 | `ACRS_Layer3.ipynb` | Decision cut-offs, calibration and validation of the drift detectors, the 2016–2018 test stream, an end-to-end run of the three agents with the audit log, and latency |

All outputs are written to `acrs_data/`. Large intermediate files (`.parquet`, `.npy`, `.pkl`) are not tracked;
they are recreated by the notebooks.

After the five notebooks have run, `python make_results_register.py` builds `acrs_data/RESULTS_REGISTER.md`.
The register lists every number reported in the thesis together with the file (and key) it was read from,
and the SHA-256 fingerprint of each source file, so each number can be traced to this run.

## Main results (test set, 2016–2018)

| Result | Value |
|---|---|
| Ensemble ROC-AUC | 0.7112 (95% CI 0.7096–0.7129) |
| LightGBM / XGBoost / Random Forest / logistic regression | 0.7118 / 0.7114 / 0.7046 / 0.7018 |
| Leakage diagnostic (same model with post-origination columns) | 0.9999 instead of 0.7101 |
| Calibration intercept; mean PD vs observed default rate | 0.408; 17.0% vs 22.9% |
| Decision rule (cut-off 0.2776, gray zone 0.2621–0.2955) | 82.4% approved, 5.0% referred, 12.6% declined |
| Label-free detectors, injected change in borrower mix | detected in 100% of streams (median 104 and 72 applications) |
| Label-free detectors, real change 2015 → 2016–2018 | detected in 0% of streams; DDM in 18% (median 1,828 loans) |
| Time added by the agents | about 0.23 s per application (about 0.31 s in total) |

The ensemble ranks borrowers as well as its best member but not better, and it under-predicts risk after the
training period. The agents make every decision explainable and traceable; they do not change the predictions.

## Environment

The thesis results were produced with Python 3.12.7 on Windows 11 (12 logical cores). Package versions are pinned
in `requirements.txt` and recorded in `acrs_data/environment.json`.

```bash
pip install -r requirements.txt
```

## Repository structure

```
ACRS.ipynb                     data preparation and leakage diagnostic
ACRS_Layer1_Modelling.ipynb    Layer 1: tuning, models and ensemble
ACRS_Layer2.ipynb              Layer 2: PSI and SHAP
ACRS_Evaluation.ipynb          evaluation: discrimination, tests, calibration, drift
ACRS_Layer3.ipynb              Layer 3: agents, detectors, audit log, latency
make_results_register.py       builds acrs_data/RESULTS_REGISTER.md
LCDataDictionary.xlsx          Lending Club data dictionary
acrs_data/                     results (JSON, CSV), figures and the audit log of the thesis run
```

## Citation

Alam, M. M. (2026). *Evaluating agentic AI for supervisory control in hybrid credit risk models*
[Master's thesis, NOVA Information Management School, Universidade NOVA de Lisboa].

## License

This repository is shared for academic and research purposes. The Lending Club dataset is subject to its respective
Kaggle terms of use.
