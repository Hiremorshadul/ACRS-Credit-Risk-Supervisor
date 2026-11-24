# ACRS results register

Generated 2026-11-24 14:10 by `make_results_register.py` from the files in `acrs_data`.
Every value below is read from a file written by the notebooks. Nothing is typed by hand.

## Source files

The SHA-256 fingerprint identifies the exact file each number came from. If a file changes, its fingerprint changes.

| File | SHA-256 (first 16 characters) |
|---|---|
| `ACRS.ipynb` | `23661ae2fb4f0446` |
| `best_params.json` | `8f973d6644a2aada` |
| `delayed_label_monitoring_by_month.csv` | `7e6c90122ab2a68e` |
| `drift_by_year.csv` | `4e76cefcd612eaa4` |
| `drift_detector_validation.csv` | `5ded8f3d8d07484a` |
| `environment.json` | `e3639738767f922f` |
| `evaluation_results.json` | `fd1837d606a4b781` |
| `feature_lists.json` | `41293b7f00bb9f77` |
| `layer1_metrics.json` | `ea7991da993b33a9` |
| `layer2_results.json` | `7acd32f6c846d604` |
| `layer3_results.json` | `7b997af85e9ab1d7` |
| `leakage_diagnostic.json` | `2b4f6491bbfc1c30` |
| `policy_by_year.csv` | `75b2b155bd19e532` |
| `policy_threshold_sensitivity.csv` | `e533551d4b38a691` |
| `resolved_share_by_year.csv` | `d7e846a39d6cfe79` |

## 1. Data and partitions (Table 3.2, Section 4.2.1)

Source: `environment.json`.

| Number | Value | Source |
|---|---|---|
| Data file | loan.csv | environment.json → data_file |
| Data file SHA-256 | 23783ef320e4df24ac113d6e5b830edb909912b7783d49b89aacd5690dc9120c | environment.json → data_sha256 |
| Loans in file | 2,260,668 | environment.json → raw_rows |
| Columns in file | 145 | environment.json → raw_cols minus 1 (the code adds a `year` column before counting) |
| Issue dates | Jun 2007 to Dec 2018 | environment.json → issue_first / issue_last |
| Resolved loans modelled | 1,303,638 | environment.json → modelled_rows |
| Default definition strict (Charged Off/Default vs Fully Paid) | True | environment.json → strict_default |
| Features after encoding | 77 | environment.json → n_features |
| train: loans | 449,414 | environment.json → partitions/train/rows |
| train: default rate | 0.17 | environment.json → partitions/train/default_rate |
| train: issue dates | Jun 2007 to Dec 2014 | environment.json → partitions/train/first, last |
| val: loans | 373,412 | environment.json → partitions/val/rows |
| val: default rate | 0.2016 | environment.json → partitions/val/default_rate |
| val: issue dates | Jan 2015 to Dec 2015 | environment.json → partitions/val/first, last |
| test: loans | 480,812 | environment.json → partitions/test/rows |
| test: default rate | 0.2288 | environment.json → partitions/test/default_rate |
| test: issue dates | Jan 2016 to Dec 2018 | environment.json → partitions/test/first, last |


## Software environment (Section 3.4.1)

Source: `environment.json`. Use these versions in requirements.txt and Section 3.

| Item | Value |
|---|---|
| python | 3.12.7 |
| numpy | 1.26.4 |
| pandas | 2.3.1 |
| scikit-learn | 1.7.1 |
| xgboost | 3.4.1 |
| lightgbm | 4.7.0 |
| shap | 0.52.0 |
| optuna | 5.0.0 |
| scipy | 1.16.0 |
| platform | Windows-11-10.0.26200-SP0 |
| cpu_count | 12 |
| seed | 42 |


## Loan status in the raw file (Section 4.2.1)

Source: printed output of the executed `ACRS.ipynb`.

| Status | Loans | Source |
|---|---|---|
| Fully Paid | 1,041,952 | ACRS.ipynb output (loan_status counts) |
| Current | 919,695 | ACRS.ipynb output (loan_status counts) |
| Charged Off | 261,655 | ACRS.ipynb output (loan_status counts) |
| Late (31-120 days) | 21,897 | ACRS.ipynb output (loan_status counts) |
| In Grace Period | 8,952 | ACRS.ipynb output (loan_status counts) |
| Late (16-30 days) | 3,737 | ACRS.ipynb output (loan_status counts) |
| Does not meet the credit policy. Status:Fully Paid | 1,988 | ACRS.ipynb output (loan_status counts) |
| Does not meet the credit policy. Status:Charged Off | 761 | ACRS.ipynb output (loan_status counts) |
| Default | 31 | ACRS.ipynb output (loan_status counts) |


## Maturity by issue year (Table 4.1)

Source: `resolved_share_by_year.csv`.

| year | loans | resolved_share | late_share | current_share | modelled_loans | default_rate | term60_share |
|---|---|---|---|---|---|---|---|
| 2007 | 603 | 0.4163 | 0.0 | 0.0 | 251 | 0.1793 | 0.0 |
| 2008 | 2393 | 0.6527 | 0.0 | 0.0 | 1562 | 0.1581 | 0.0 |
| 2009 | 5281 | 0.893 | 0.0 | 0.0 | 4716 | 0.126 | 0.0 |
| 2010 | 12537 | 0.9202 | 0.0 | 0.0 | 11536 | 0.1289 | 0.2661 |
| 2011 | 21721 | 1.0 | 0.0 | 0.0 | 21721 | 0.1518 | 0.3508 |
| 2012 | 53367 | 1.0 | 0.0 | 0.0 | 53367 | 0.162 | 0.1855 |
| 2013 | 134814 | 0.9998 | 0.0001 | 0.0001 | 134793 | 0.156 | 0.255 |
| 2014 | 235629 | 0.9399 | 0.0018 | 0.0583 | 221468 | 0.1854 | 0.2659 |
| 2015 | 421095 | 0.8868 | 0.0043 | 0.1089 | 373412 | 0.2016 | 0.2425 |
| 2016 | 434407 | 0.6324 | 0.0133 | 0.3544 | 274711 | 0.2427 | 0.2153 |
| 2017 | 443579 | 0.3582 | 0.0221 | 0.6197 | 158910 | 0.229 | 0.2421 |
| 2018 | 495242 | 0.0953 | 0.0158 | 0.8889 | 47191 | 0.1473 | 0.2717 |


## 2. Features (Table 4.2) and leakage check (Table 4.3)

Source: `feature_lists.json`, `leakage_diagnostic.json`.

| List | Count | Source |
|---|---|---|
| post_origination_removed | 36 | feature_lists.json → post_origination_removed |
| redundant_removed | 2 | feature_lists.json → redundant_removed |
| high_missing_removed | 33 | feature_lists.json → high_missing_removed |
| constant_removed | 3 | feature_lists.json → constant_removed |
| raw_features | 60 | feature_lists.json → raw_features |
| encoded_features | 77 | feature_lists.json → encoded_features |

- **post_origination_removed** (36): `total_pymnt`, `total_pymnt_inv`, `total_rec_prncp`, `total_rec_int`, `total_rec_late_fee`, `recoveries`, `collection_recovery_fee`, `last_pymnt_amnt`, `out_prncp`, `out_prncp_inv`, `last_pymnt_d`, `next_pymnt_d`, `last_credit_pull_d`, `debt_settlement_flag`, `hardship_flag`, `pymnt_plan`, `hardship_type`, `hardship_reason`, `hardship_status`, `deferral_term`, `hardship_amount`, `hardship_start_date`, `hardship_end_date`, `payment_plan_start_date`, `hardship_length`, `hardship_dpd`, `hardship_loan_status`, `orig_projected_additional_accrued_interest`, `hardship_payoff_balance_amount`, `hardship_last_payment_amount`, `debt_settlement_flag_date`, `settlement_status`, `settlement_date`, `settlement_amount`, `settlement_percentage`, `settlement_term`
- **redundant_removed** (2): `installment`, `funded_amnt_inv`
- **high_missing_removed** (33): `mths_since_last_delinq`, `mths_since_last_record`, `mths_since_last_major_derog`, `annual_inc_joint`, `dti_joint`, `verification_status_joint`, `open_acc_6m`, `open_act_il`, `open_il_12m`, `open_il_24m`, `mths_since_rcnt_il`, `total_bal_il`, `il_util`, `open_rv_12m`, `open_rv_24m`, `max_bal_bc`, `all_util`, `inq_fi`, `total_cu_tl`, `inq_last_12m`, `mths_since_recent_bc_dlq`, `mths_since_recent_revol_delinq`, `revol_bal_joint`, `sec_app_earliest_cr_line`, `sec_app_inq_last_6mths`, `sec_app_mort_acc`, `sec_app_open_acc`, `sec_app_revol_util`, `sec_app_open_act_il`, `sec_app_num_rev_accts`, `sec_app_chargeoff_within_12_mths`, `sec_app_collections_12_mths_ex_med`, `sec_app_mths_since_last_major_derog`
- **constant_removed** (3): `policy_code`, `application_type`, `disbursement_method`
- **raw_features** (60): `loan_amnt`, `funded_amnt`, `term`, `int_rate`, `grade`, `sub_grade`, `emp_length`, `home_ownership`, `annual_inc`, `verification_status`, `purpose`, `dti`, `delinq_2yrs`, `inq_last_6mths`, `open_acc`, `pub_rec`, `revol_bal`, `revol_util`, `total_acc`, `initial_list_status`, `collections_12_mths_ex_med`, `acc_now_delinq`, `tot_coll_amt`, `tot_cur_bal`, `total_rev_hi_lim`, `acc_open_past_24mths`, `avg_cur_bal`, `bc_open_to_buy`, `bc_util`, `chargeoff_within_12_mths`, `delinq_amnt`, `mo_sin_old_il_acct`, `mo_sin_old_rev_tl_op`, `mo_sin_rcnt_rev_tl_op`, `mo_sin_rcnt_tl`, `mort_acc`, `mths_since_recent_bc`, `mths_since_recent_inq`, `num_accts_ever_120_pd`, `num_actv_bc_tl`, `num_actv_rev_tl`, `num_bc_sats`, `num_bc_tl`, `num_il_tl`, `num_op_rev_tl`, `num_rev_accts`, `num_rev_tl_bal_gt_0`, `num_sats`, `num_tl_120dpd_2m`, `num_tl_30dpd`, `num_tl_90g_dpd_24m`, `num_tl_op_past_12m`, `pct_tl_nvr_dlq`, `percent_bc_gt_75`, `pub_rec_bankruptcies`, `tax_liens`, `tot_hi_cred_lim`, `total_bal_ex_mort`, `total_bc_limit`, `total_il_high_credit_limit`
- **encoded_features** (77): `loan_amnt`, `funded_amnt`, `term`, `int_rate`, `grade`, `sub_grade`, `emp_length`, `annual_inc`, `dti`, `delinq_2yrs`, `inq_last_6mths`, `open_acc`, `pub_rec`, `revol_bal`, `revol_util`, `total_acc`, `collections_12_mths_ex_med`, `acc_now_delinq`, `tot_coll_amt`, `tot_cur_bal`, `total_rev_hi_lim`, `acc_open_past_24mths`, `avg_cur_bal`, `bc_open_to_buy`, `bc_util`, `chargeoff_within_12_mths`, `delinq_amnt`, `mo_sin_old_il_acct`, `mo_sin_old_rev_tl_op`, `mo_sin_rcnt_rev_tl_op`, `mo_sin_rcnt_tl`, `mort_acc`, `mths_since_recent_bc`, `mths_since_recent_inq`, `num_accts_ever_120_pd`, `num_actv_bc_tl`, `num_actv_rev_tl`, `num_bc_sats`, `num_bc_tl`, `num_il_tl`, `num_op_rev_tl`, `num_rev_accts`, `num_rev_tl_bal_gt_0`, `num_sats`, `num_tl_120dpd_2m`, `num_tl_30dpd`, `num_tl_90g_dpd_24m`, `num_tl_op_past_12m`, `pct_tl_nvr_dlq`, `percent_bc_gt_75`, `pub_rec_bankruptcies`, `tax_liens`, `tot_hi_cred_lim`, `total_bal_ex_mort`, `total_bc_limit`, `total_il_high_credit_limit`, `home_ownership_MORTGAGE`, `home_ownership_NONE`, `home_ownership_OTHER`, `home_ownership_OWN`, `home_ownership_RENT`, `verification_status_Source Verified`, `verification_status_Verified`, `purpose_credit_card`, `purpose_debt_consolidation`, `purpose_educational`, `purpose_home_improvement`, `purpose_house`, `purpose_major_purchase`, `purpose_medical`, `purpose_moving`, `purpose_other`, `purpose_renewable_energy`, `purpose_small_business`, `purpose_vacation`, `purpose_wedding`, `initial_list_status_w`

| Number | Value | Source |
|---|---|---|
| Diagnostic model | XGBoost, 100 trees, depth 5, learning rate 0.1 | leakage_diagnostic.json → model |
| With leakage: features | 88 | leakage_diagnostic.json → with_leakage/features |
| With leakage: val ROC-AUC | 0.9998 | leakage_diagnostic.json → with_leakage/val_auc |
| With leakage: test ROC-AUC | 0.9999 | leakage_diagnostic.json → with_leakage/test_auc |
| Without leakage: features | 77 | leakage_diagnostic.json → without_leakage/features |
| Without leakage: val ROC-AUC | 0.74 | leakage_diagnostic.json → without_leakage/val_auc |
| Without leakage: test ROC-AUC | 0.7101 | leakage_diagnostic.json → without_leakage/test_auc |
| Columns added back | total_pymnt, total_pymnt_inv, total_rec_prncp, total_rec_int, total_rec_late_fee, recoveries, collection_recovery_fee, last_pymnt_amnt, installment, funded_amnt_inv, debt_settlement_flag_Y | leakage_diagnostic.json → leakage_columns_encoded |


## 3. Tuning (Table 4.4)

Source: `best_params.json`.

| Model | Parameter | Value | Source |
|---|---|---|---|
| xgb | n_estimators | 394 | best_params.json → xgb/n_estimators |
| xgb | max_depth | 3 | best_params.json → xgb/max_depth |
| xgb | learning_rate | 0.05687 | best_params.json → xgb/learning_rate |
| xgb | subsample | 0.722279 | best_params.json → xgb/subsample |
| xgb | colsample_bytree | 0.930396 | best_params.json → xgb/colsample_bytree |
| lgbm | n_estimators | 425 | best_params.json → lgbm/n_estimators |
| lgbm | max_depth | 3 | best_params.json → lgbm/max_depth |
| lgbm | learning_rate | 0.07478 | best_params.json → lgbm/learning_rate |
| lgbm | subsample | 0.615854 | best_params.json → lgbm/subsample |
| lgbm | colsample_bytree | 0.631845 | best_params.json → lgbm/colsample_bytree |
| rf | n_estimators | 400 | best_params.json → rf/n_estimators |
| rf | max_depth | 10 | best_params.json → rf/max_depth |
| rf | max_features | log2 | best_params.json → rf/max_features |
| lr | C | 1.0 | best_params.json → lr/C |
| lr | max_iter | 5,000 | best_params.json → lr/max_iter |
| all | n_trials | 30 | best_params.json → n_trials |
| all | tuning_sample | 100,000 | best_params.json → tuning_sample |
| all | seed | 42 | best_params.json → seed |
| xgb | best val ROC-AUC on tuning sample | 0.7379 | best_params.json → best_val_auc_tuning_sample/xgb |
| lgbm | best val ROC-AUC on tuning sample | 0.7371 | best_params.json → best_val_auc_tuning_sample/lgbm |
| rf | best val ROC-AUC on tuning sample | 0.7341 | best_params.json → best_val_auc_tuning_sample/rf |


## 4. Discrimination with 95% CI (Table 4.5)

Source: `evaluation_results.json` → discrimination.

**val**

| Model | ROC-AUC | 95% CI low | 95% CI high | KS | Gini | Brier |
|---|---|---|---|---|---|---|
| Logistic regression | 0.7343 | 0.7324 | 0.7363 | 0.3425 | 0.4686 | 0.1433 |
| XGBoost | 0.7408 | 0.7389 | 0.7427 | 0.3512 | 0.4816 | 0.1416 |
| LightGBM | 0.7414 | 0.7395 | 0.7433 | 0.3524 | 0.4828 | 0.1416 |
| Random Forest | 0.736 | 0.734 | 0.7379 | 0.342 | 0.4719 | 0.1451 |
| Ensemble (L1) | 0.7411 | 0.7392 | 0.743 | 0.3514 | 0.4822 | 0.1423 |

**test**

| Model | ROC-AUC | 95% CI low | 95% CI high | KS | Gini | Brier |
|---|---|---|---|---|---|---|
| Logistic regression | 0.7018 | 0.7001 | 0.7035 | 0.2934 | 0.4036 | 0.1645 |
| XGBoost | 0.7114 | 0.7098 | 0.7131 | 0.3068 | 0.4229 | 0.1627 |
| LightGBM | 0.7118 | 0.7102 | 0.7135 | 0.3064 | 0.4237 | 0.1627 |
| Random Forest | 0.7046 | 0.7029 | 0.7062 | 0.2932 | 0.4091 | 0.1654 |
| Ensemble (L1) | 0.7112 | 0.7096 | 0.7129 | 0.3049 | 0.4225 | 0.1633 |

F1 at the 0.50 cut-off (reported only for continuity; not a decision threshold). Source: `layer1_metrics.json`.

| Model | val F1@0.50 | test F1@0.50 | test mean PD | test default rate |
|---|---|---|---|---|
| lr | 0.1016 | 0.1019 | 0.1744 | 0.2288 |
| xgb | 0.0983 | 0.0654 | 0.1707 | 0.2288 |
| lgbm | 0.1041 | 0.072 | 0.1704 | 0.2288 |
| rf | 0.0 | 0.0001 | 0.1677 | 0.2288 |
| ensemble | 0.0511 | 0.0342 | 0.1696 | 0.2288 |


## 5. DeLong and bootstrap tests, ensemble vs each model, test set (Table 4.6)

Source: `evaluation_results.json` → delong_ensemble_vs, bootstrap_ensemble_vs (bootstrap resamples: 2000).

| vs model | AUC ensemble | AUC model | Difference | DeLong CI low | DeLong CI high | z | p | Bootstrap CI low | Bootstrap CI high | Share of resamples ensemble better |
|---|---|---|---|---|---|---|---|---|---|---|
| xgb | 0.7112 | 0.7114 | -0.0002 | -0.0004 | -0.0 | -2.5 | 0.012578 | -0.0004 | -0.0 | 0.006 |
| lgbm | 0.7112 | 0.7118 | -0.0006 | -0.0008 | -0.0004 | -6.32 | 2.61e-10 | -0.0008 | -0.0004 | 0.0 |
| rf | 0.7112 | 0.7046 | 0.0067 | 0.0063 | 0.007 | 36.36 | 1.55e-289 | 0.0063 | 0.007 | 1.0 |
| lr | 0.7112 | 0.7018 | 0.0094 | 0.0088 | 0.0101 | 29.36 | 1.71e-189 | 0.0088 | 0.0101 | 1.0 |


## 6. Calibration (Table 4.7, Figure 4.2)

Source: `evaluation_results.json` → calibration. Intercept and slope on the log-odds scale.

**train**

| Model | Brier | Mean PD | Default rate | Calibration intercept | Calibration slope |
|---|---|---|---|---|---|
| lr | 0.1302 | 0.17 | 0.17 | -0.0 | 1.003 |
| xgb | 0.1279 | 0.17 | 0.17 | 0.0 | 1.071 |
| lgbm | 0.1276 | 0.17 | 0.17 | -0.0 | 1.079 |
| rf | 0.1273 | 0.1698 | 0.17 | 0.001 | 1.497 |
| ensemble | 0.1273 | 0.1699 | 0.17 | 0.001 | 1.216 |

**val**

| Model | Brier | Mean PD | Default rate | Calibration intercept | Calibration slope |
|---|---|---|---|---|---|
| lr | 0.1433 | 0.1723 | 0.2016 | 0.213 | 1.139 |
| xgb | 0.1416 | 0.1752 | 0.2016 | 0.193 | 1.076 |
| lgbm | 0.1416 | 0.1746 | 0.2016 | 0.199 | 1.068 |
| rf | 0.1451 | 0.1673 | 0.2016 | 0.244 | 1.404 |
| ensemble | 0.1423 | 0.1723 | 0.2016 | 0.212 | 1.187 |

**test**

| Model | Brier | Mean PD | Default rate | Calibration intercept | Calibration slope |
|---|---|---|---|---|---|
| lr | 0.1645 | 0.1744 | 0.2288 | 0.378 | 0.912 |
| xgb | 0.1627 | 0.1707 | 0.2288 | 0.406 | 0.964 |
| lgbm | 0.1627 | 0.1704 | 0.2288 | 0.41 | 0.953 |
| rf | 0.1654 | 0.1677 | 0.2288 | 0.412 | 1.212 |
| ensemble | 0.1633 | 0.1696 | 0.2288 | 0.408 | 1.056 |

**Ensemble by PD decile, test set** (source: `evaluation_results.json` → reliability_ensemble_test)

| Decile | Mean PD | Default rate | Loans |
|---|---|---|---|
| 0 | 0.0389 | 0.0441 | 48,082 |
| 1 | 0.0661 | 0.0879 | 48,081 |
| 2 | 0.0895 | 0.1237 | 48,081 |
| 3 | 0.1121 | 0.1608 | 48,081 |
| 4 | 0.136 | 0.1937 | 48,081 |
| 5 | 0.162 | 0.2278 | 48,081 |
| 6 | 0.1912 | 0.2665 | 48,081 |
| 7 | 0.2273 | 0.3183 | 48,081 |
| 8 | 0.28 | 0.374 | 48,081 |
| 9 | 0.3929 | 0.4915 | 48,082 |


## 7. Drift decomposition (Table 4.10, Figure 4.4, Section 4.4.3)

Source: `evaluation_results.json` → drift, and `drift_by_year.csv`.

| Number | Value | Source |
|---|---|---|
| Domain classifier ROC-AUC (train vs test borrowers, 5-fold) | 0.993 | evaluation_results.json → drift/domain_classifier_auc |

| Feature | Share of gain in domain classifier |
|---|---|
| int_rate | 0.4494 |
| initial_list_status_w | 0.1732 |
| sub_grade | 0.1729 |
| grade | 0.0465 |
| num_bc_tl | 0.0252 |
| percent_bc_gt_75 | 0.0124 |
| term | 0.0119 |
| total_rev_hi_lim | 0.0116 |
| total_il_high_credit_limit | 0.0091 |
| bc_open_to_buy | 0.0082 |

| Feature | PSI train vs test |
|---|---|
| initial_list_status_w | 0.7698 |
| delinq_amnt | 0.4468 |
| mo_sin_old_rev_tl_op | 0.3622 |
| total_il_high_credit_limit | 0.3322 |
| total_rev_hi_lim | 0.3159 |
| mo_sin_old_il_acct | 0.282 |
| bc_util | 0.2795 |
| tot_hi_cred_lim | 0.2767 |
| tot_cur_bal | 0.2752 |
| avg_cur_bal | 0.269 |

**By issue year** (source: `drift_by_year.csv`; train years are in-sample)

| year | partition | loans | default_rate | mean_pd | roc_auc | calibration_intercept | calibration_slope | resolved_share |
|---|---|---|---|---|---|---|---|---|
| 2007 | train | 251 | 0.1793 | 0.1329 |  |  |  | 0.4163 |
| 2008 | train | 1562 | 0.1581 | 0.131 | 0.6409 | 0.225 | 1.191 | 0.6527 |
| 2009 | train | 4716 | 0.126 | 0.1311 | 0.6481 | -0.047 | 1.161 | 0.893 |
| 2010 | train | 11536 | 0.1289 | 0.1449 | 0.7043 | -0.141 | 1.286 | 0.9202 |
| 2011 | train | 21721 | 0.1518 | 0.1542 | 0.7079 | -0.019 | 1.17 | 1.0 |
| 2012 | train | 53367 | 0.162 | 0.1579 | 0.7056 | 0.032 | 1.15 | 1.0 |
| 2013 | train | 134793 | 0.156 | 0.167 | 0.7154 | -0.088 | 1.145 | 0.9998 |
| 2014 | train | 221468 | 0.1854 | 0.1786 | 0.7399 | 0.05 | 1.266 | 0.9399 |
| 2015 | val | 373412 | 0.2016 | 0.1723 | 0.7411 | 0.212 | 1.187 | 0.8868 |
| 2016 | test | 274711 | 0.2427 | 0.1704 | 0.7147 | 0.488 | 1.079 | 0.6324 |
| 2017 | test | 158910 | 0.229 | 0.1704 | 0.707 | 0.402 | 1.046 | 0.3582 |
| 2018 | test | 47191 | 0.1473 | 0.1621 | 0.7014 | -0.123 | 0.937 | 0.0953 |


## 8. Layer 2: PSI (Table 4.8) and SHAP (Table 4.9, Section 4.4.2)

Source: `layer2_results.json`.

| Model | PSI train vs val | PSI train vs test | Status (test) |
|---|---|---|---|
| XGBoost | 0.0191 | 0.003 | Stable |
| LightGBM | 0.0185 | 0.0036 | Stable |
| Random Forest | 0.0107 | 0.0022 | Stable |
| Ensemble | 0.0162 | 0.0027 | Stable |

| Split | Ensemble mean PD | Observed default rate |
|---|---|---|
| train | 0.1699 | 0.17 |
| val | 0.1723 | 0.2016 |
| test | 0.1696 | 0.2288 |

| Number | Value | Source |
|---|---|---|
| SHAP method | interventional TreeSHAP, probability scale, average of the three members (weights 1/3) | layer2_results.json → shap/method |
| Loans explained | 2,000 | layer2_results.json → shap/n_explained |
| Background rows | 100 | layer2_results.json → shap/n_background |
| Base value E[f(X)] | 0.1584 | layer2_results.json → shap/base_value |
| Reconstruction error, median | 1.73e-08 | layer2_results.json → shap/reconstruction |
| Reconstruction error, 99th percentile | 0.000705 | layer2_results.json → shap/reconstruction |
| Reconstruction error, max | 0.001324 | layer2_results.json → shap/reconstruction |
| Loans with error > 0.001 | 1 | layer2_results.json → shap/reconstruction |

| Rank | Feature | Mean |SHAP| (PD points) |
|---|---|---|
| 1 | sub_grade | 0.0269 |
| 2 | term | 0.0262 |
| 3 | annual_inc | 0.0169 |
| 4 | acc_open_past_24mths | 0.0127 |
| 5 | grade | 0.0119 |
| 6 | dti | 0.0106 |
| 7 | loan_amnt | 0.0094 |
| 8 | int_rate | 0.008 |
| 9 | funded_amnt | 0.0056 |
| 10 | total_bc_limit | 0.0052 |

**Worked example (Section 4.4.2):** test row 30, base value 0.1584, sum of contributions -0.046, reconstructed PD 0.1124, ensemble PD 0.1124.

| Feature | SHAP (PD points) |
|---|---|
| annual_inc | -0.0227 |
| term | -0.0162 |
| avg_cur_bal | -0.016 |
| acc_open_past_24mths | 0.0159 |
| loan_amnt | 0.0071 |


## 9. Layer 3: decision policy, drift detectors, decisions, audit log, latency (Tables 4.11–4.17)

Source: `layer3_results.json` and the Layer 3 CSV files.

| Key | Value |
|---|---|
| layer | 3 |
| policy/t_star | 0.2776 |
| policy/t_low | 0.2621 |
| policy/t_high | 0.2955 |
| policy/refer_share_target | 0.05 |
| policy/chosen_on | validation (2015), realised profit/loss |
| policy/validation_profit_approve_all | 191249698.0 |
| policy/validation_profit_approve_below_t_star | 274347415.0 |
| monitor_settings/window | 500 |
| monitor_settings/window_threshold | 0.026 |
| monitor_settings/window_reference_mean_pd | 0.1723 |
| monitor_settings/ph_delta | 0.005 |
| monitor_settings/ph_lambda | 10.48 |
| monitor_settings/ddm_warning_sd | 2.0 |
| monitor_settings/ddm_drift_sd | 3.0 |
| monitor_settings/calibrated_on | no-change streams from Jan–Jun 2015 (99th percentile of the maximum statistic) |
| detector_validation[0]/scenario | no_change |
| detector_validation[0]/detector | window |
| detector_validation[0]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[0]/detection_rate | None |
| detector_validation[0]/median_delay_loans | None |
| detector_validation[1]/scenario | no_change |
| detector_validation[1]/detector | page_hinkley |
| detector_validation[1]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[1]/detection_rate | None |
| detector_validation[1]/median_delay_loans | None |
| detector_validation[2]/scenario | no_change |
| detector_validation[2]/detector | ddm_delayed_labels |
| detector_validation[2]/false_alarms_per_10k_loans | 0.68 |
| detector_validation[2]/detection_rate | None |
| detector_validation[2]/median_delay_loans | None |
| detector_validation[3]/scenario | real_change_2015_to_2016_18 |
| detector_validation[3]/detector | window |
| detector_validation[3]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[3]/detection_rate | 0.0 |
| detector_validation[3]/median_delay_loans | None |
| detector_validation[4]/scenario | real_change_2015_to_2016_18 |
| detector_validation[4]/detector | page_hinkley |
| detector_validation[4]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[4]/detection_rate | 0.0 |
| detector_validation[4]/median_delay_loans | None |
| detector_validation[5]/scenario | real_change_2015_to_2016_18 |
| detector_validation[5]/detector | ddm_delayed_labels |
| detector_validation[5]/false_alarms_per_10k_loans | 1.16 |
| detector_validation[5]/detection_rate | 0.18 |
| detector_validation[5]/median_delay_loans | 1,828 |
| detector_validation[6]/scenario | injected_riskier_mix |
| detector_validation[6]/detector | window |
| detector_validation[6]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[6]/detection_rate | 1.0 |
| detector_validation[6]/median_delay_loans | 104 |
| detector_validation[7]/scenario | injected_riskier_mix |
| detector_validation[7]/detector | page_hinkley |
| detector_validation[7]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[7]/detection_rate | 1.0 |
| detector_validation[7]/median_delay_loans | 72 |
| detector_validation[8]/scenario | injected_riskier_mix |
| detector_validation[8]/detector | ddm_delayed_labels |
| detector_validation[8]/false_alarms_per_10k_loans | 1.32 |
| detector_validation[8]/detection_rate | 0.97 |
| detector_validation[8]/median_delay_loans | 228 |
| test_stream/order_within_month | random (fixed seed); issue dates are monthly |
| test_stream/window_alarms | 3 |
| test_stream/page_hinkley_alarms | 3 |
| test_stream/ddm_delayed_label_alarms | 1 |
| test_stream/file_order_window_alarms | 226 |
| test_stream/file_order_page_hinkley_alarms | 48 |
| test_stream/window_alarm_months[0] | 2016-01 |
| test_stream/window_alarm_months[1] | 2018-12 |
| test_stream/ddm_alarm_months[0] | 2016-03 |
| decisions_full_test/approve_rate | 0.8237 |
| decisions_full_test/refer_rate | 0.0504 |
| decisions_full_test/decline_rate | 0.126 |
| decisions_full_test/default_rate_approved | 0.1828 |
| decisions_full_test/default_rate_referred | 0.3724 |
| decisions_full_test/default_rate_declined | 0.4725 |
| decisions_full_test/approval_errors | 72,386 |
| decisions_full_test/decline_errors | 31,950 |
| decisions_full_test/profit_if_referred_declined | -128518501.6741 |
| decisions_full_test/profit_if_referred_approved | -180596869.7033 |
| decisions_full_test/share_of_defaults_caught | 0.3421 |
| decisions_full_test/precision_decline | 0.4725 |
| decisions_full_test/recall_decline | 0.2601 |
| decisions_full_test/f1_decline | 0.3355 |
| decisions_full_test/precision_flagged | 0.4439 |
| decisions_full_test/recall_flagged | 0.3421 |
| decisions_full_test/f1_flagged | 0.3864 |
| baselines/approve_all_profit | -401946965.0 |
| baselines/single_threshold_t_star_profit | -153202891.0 |
| baselines/single_threshold_t_star_f1 | 0.3633 |
| latency/score/mean_ms | 77.84 |
| latency/score/median_ms | 75.44 |
| latency/score/p95_ms | 88.1 |
| latency/shap/mean_ms | 233.63 |
| latency/shap/median_ms | 227.02 |
| latency/shap/p95_ms | 297.63 |
| latency/monitor/mean_ms | 0.01 |
| latency/monitor/median_ms | 0.01 |
| latency/monitor/p95_ms | 0.02 |
| latency/decide_and_log/mean_ms | 1.21 |
| latency/decide_and_log/median_ms | 0.77 |
| latency/decide_and_log/p95_ms | 1.06 |
| latency/layer3_total_per_loan/mean_ms | 312.69 |
| latency/layer3_total_per_loan/median_ms | 305.57 |
| latency/layer3_total_per_loan/p95_ms | 379.86 |
| latency/layer1_batch_scoring/loans | 100,000 |
| latency/layer1_batch_scoring/seconds | 1.22 |
| latency/layer1_batch_scoring/loans_per_second | 81,763 |
| latency/process_memory_mb | 1272.0 |
| latency/hardware/platform | Windows-11-10.0.26200-SP0 |
| latency/hardware/processor | AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD |
| latency/hardware/cpu_count | 12 |

| Key | Value |
|---|---|
| loans | 2,000 |
| decisions/AUTO_APPROVE | 1,684 |
| decisions/AUTO_DECLINE | 228 |
| decisions/REFER_TO_HUMAN | 88 |
| first_month | 2016-01 |
| last_month | 2016-01 |
| audit_file | audit_trail_20261121_193025.csv |
| hash_chain_valid | True |

**drift_detector_validation.csv**

| scenario | detector | false_alarms_per_10k_loans | detection_rate | median_delay_loans |
|---|---|---|---|---|
| no_change | window | 0.0 |  |  |
| no_change | page_hinkley | 0.0 |  |  |
| no_change | ddm_delayed_labels | 0.68 |  |  |
| real_change_2015_to_2016_18 | window | 0.0 | 0.0 |  |
| real_change_2015_to_2016_18 | page_hinkley | 0.0 | 0.0 |  |
| real_change_2015_to_2016_18 | ddm_delayed_labels | 1.16 | 0.18 | 1828.0 |
| injected_riskier_mix | window | 0.0 | 1.0 | 104.0 |
| injected_riskier_mix | page_hinkley | 0.0 | 1.0 | 72.0 |
| injected_riskier_mix | ddm_delayed_labels | 1.32 | 0.97 | 228.0 |

**policy_threshold_sensitivity.csv**

| refer_share_target | quantile_shift | t_low | t_high | approve_rate | refer_rate | decline_rate | default_rate_approved | approval_errors | decline_errors | profit_if_referred_declined |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.02 | -0.1 | 0.2204 | 0.229 | 0.7342 | 0.0217 | 0.2441 | 0.1646 | 58115 | 68716 | -64828016.4366 |
| 0.02 | -0.05 | 0.2431 | 0.2537 | 0.7872 | 0.0212 | 0.1915 | 0.1751 | 66291 | 51893 | -98005767.8604 |
| 0.02 | 0.0 | 0.2712 | 0.2845 | 0.8391 | 0.0202 | 0.1408 | 0.1861 | 75077 | 36361 | -143432253.1763 |
| 0.02 | 0.05 | 0.3074 | 0.3257 | 0.8886 | 0.0194 | 0.092 | 0.1969 | 84132 | 22241 | -196745641.5057 |
| 0.02 | 0.1 | 0.3575 | 0.3835 | 0.9351 | 0.0175 | 0.0474 | 0.2083 | 93632 | 10307 | -261862909.8249 |
| 0.05 | -0.1 | 0.2143 | 0.236 | 0.7186 | 0.0533 | 0.2281 | 0.1616 | 55833 | 63514 | -55727917.5762 |
| 0.05 | -0.05 | 0.236 | 0.2621 | 0.7719 | 0.0517 | 0.1763 | 0.1721 | 63878 | 47145 | -88293780.5094 |
| 0.05 | 0.0 | 0.2621 | 0.2955 | 0.8237 | 0.0503 | 0.126 | 0.1828 | 72386 | 31952 | -128517154.3709 |
| 0.05 | 0.05 | 0.2955 | 0.3408 | 0.874 | 0.0481 | 0.0779 | 0.1937 | 81401 | 18303 | -180582955.0269 |
| 0.05 | 0.1 | 0.3408 | 0.4061 | 0.9221 | 0.0426 | 0.0352 | 0.205 | 90888 | 7250 | -241662230.5155 |
| 0.1 | -0.1 | 0.2046 | 0.2484 | 0.6916 | 0.1065 | 0.2019 | 0.156 | 51879 | 55139 | -40695614.7924 |
| 0.1 | -0.05 | 0.2246 | 0.2776 | 0.7449 | 0.1041 | 0.151 | 0.1666 | 59690 | 39412 | -71084408.2933 |
| 0.1 | 0.0 | 0.2484 | 0.3161 | 0.7981 | 0.1002 | 0.1017 | 0.1774 | 68091 | 24928 | -107024931.0456 |
| 0.1 | 0.05 | 0.2776 | 0.3698 | 0.849 | 0.0948 | 0.0561 | 0.1883 | 76851 | 12537 | -153202890.6874 |
| 0.1 | 0.1 | 0.3161 | 0.4565 | 0.8983 | 0.0861 | 0.0156 | 0.1993 | 86064 | 2888 | -208908196.6814 |

**policy_by_year.csv**

| year | approve_rate | refer_rate | decline_rate | default_rate_approved | default_rate_referred | default_rate_declined | approval_errors | decline_errors | profit_if_referred_declined | profit_if_referred_approved | share_of_defaults_caught | precision_decline | recall_decline | f1_decline | precision_flagged | recall_flagged | f1_flagged |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 0.8217 | 0.0496 | 0.1287 | 0.1928 | 0.3933 | 0.5034 | 43519 | 17558 | 12992104.1718 | -6618232.6503 | 0.3473 | 0.5034 | 0.267 | 0.3489 | 0.4728 | 0.3473 | 0.4005 |
| 2017 | 0.8237 | 0.0527 | 0.1236 | 0.185 | 0.3721 | 0.4615 | 24210 | 10574 | -99872785.3924 | -124929334.5152 | 0.3347 | 0.4615 | 0.2491 | 0.3235 | 0.4348 | 0.3347 | 0.3782 |
| 2018 | 0.8351 | 0.0469 | 0.118 | 0.1182 | 0.2448 | 0.3145 | 4657 | 3818 | -41637820.4535 | -49049302.5377 | 0.33 | 0.3145 | 0.2521 | 0.2798 | 0.2947 | 0.33 | 0.3114 |

**delayed_label_monitoring_by_month.csv**

| month | loans | default_rate | mean_pd | roc_auc |
|---|---|---|---|---|
| 2016-01 | 27985.0 | 0.1927 | 0.1594 | 0.7552 |
| 2016-02 | 32076.0 | 0.2066 | 0.1631 | 0.7398 |
| 2016-03 | 40701.0 | 0.2563 | 0.1746 | 0.7209 |
| 2016-04 | 22997.0 | 0.2632 | 0.1688 | 0.7157 |
| 2016-05 | 17394.0 | 0.2681 | 0.1692 | 0.7135 |
| 2016-06 | 19978.0 | 0.2475 | 0.1632 | 0.7109 |
| 2016-07 | 20916.0 | 0.2691 | 0.1798 | 0.6944 |
| 2016-08 | 21417.0 | 0.2648 | 0.1764 | 0.698 |
| 2016-09 | 16263.0 | 0.2511 | 0.178 | 0.7057 |
| 2016-10 | 18209.0 | 0.2253 | 0.1704 | 0.6875 |
| 2016-11 | 18163.0 | 0.2442 | 0.1711 | 0.6917 |
| 2016-12 | 18612.0 | 0.2498 | 0.1768 | 0.6888 |
| 2017-01 | 15669.0 | 0.2265 | 0.1698 | 0.7039 |
| 2017-02 | 12903.0 | 0.231 | 0.168 | 0.7005 |
| 2017-03 | 16129.0 | 0.2302 | 0.1664 | 0.7065 |
| 2017-04 | 12428.0 | 0.2379 | 0.1701 | 0.7081 |
| 2017-05 | 15287.0 | 0.2382 | 0.1695 | 0.6955 |
| 2017-06 | 14330.0 | 0.2345 | 0.1698 | 0.7056 |
| 2017-07 | 13969.0 | 0.239 | 0.1747 | 0.7095 |
| 2017-08 | 14449.0 | 0.2268 | 0.1688 | 0.7038 |
| 2017-09 | 12452.0 | 0.2465 | 0.185 | 0.7151 |
| 2017-10 | 11024.0 | 0.2156 | 0.1705 | 0.714 |
| 2017-11 | 11143.0 | 0.202 | 0.1646 | 0.7082 |
| 2017-12 | 9127.0 | 0.2054 | 0.1677 | 0.7189 |
| 2018-01 | 7681.0 | 0.189 | 0.162 | 0.7134 |
| 2018-02 | 5996.0 | 0.1855 | 0.1655 | 0.7052 |
| 2018-03 | 6320.0 | 0.1861 | 0.1643 | 0.7037 |
| 2018-04 | 6009.0 | 0.1846 | 0.1653 | 0.7159 |
| 2018-05 | 5620.0 | 0.166 | 0.1644 | 0.6893 |
| 2018-06 | 4029.0 | 0.1348 | 0.1573 | 0.7212 |
| 2018-07 | 3461.0 | 0.0977 | 0.1611 | 0.6853 |
| 2018-08 | 2785.0 | 0.0628 | 0.1578 | 0.6525 |
| 2018-09 | 1819.0 | 0.044 | 0.1573 | 0.6525 |
| 2018-10 | 1547.0 | 0.0136 | 0.1598 | 0.5145 |
| 2018-11 | 1099.0 | 0.0091 | 0.1544 | 0.5099 |
| 2018-12 | 825.0 | 0.0024 | 0.1481 | 0.4514 |


## 10. Every stored number (complete list, for searching)

Every scalar in every results JSON, as stored. If a number in the thesis is not in this list or the tables above, it did not come from the code.

<details><summary><code>best_params.json</code></summary>

| Key | Value |
|---|---|
| xgb/n_estimators | 394 |
| xgb/max_depth | 3 |
| xgb/learning_rate | 0.05687 |
| xgb/subsample | 0.722279 |
| xgb/colsample_bytree | 0.930396 |
| lgbm/n_estimators | 425 |
| lgbm/max_depth | 3 |
| lgbm/learning_rate | 0.07478 |
| lgbm/subsample | 0.615854 |
| lgbm/colsample_bytree | 0.631845 |
| rf/n_estimators | 400 |
| rf/max_depth | 10 |
| rf/max_features | log2 |
| best_val_auc_tuning_sample/xgb | 0.7379 |
| best_val_auc_tuning_sample/lgbm | 0.7371 |
| best_val_auc_tuning_sample/rf | 0.7341 |
| n_trials | 30 |
| tuning_sample | 100,000 |
| seed | 42 |
| lr/C | 1.0 |
| lr/max_iter | 5,000 |

</details>

<details><summary><code>environment.json</code></summary>

| Key | Value |
|---|---|
| python | 3.12.7 |
| numpy | 1.26.4 |
| pandas | 2.3.1 |
| scikit-learn | 1.7.1 |
| xgboost | 3.4.1 |
| lightgbm | 4.7.0 |
| shap | 0.52.0 |
| optuna | 5.0.0 |
| scipy | 1.16.0 |
| platform | Windows-11-10.0.26200-SP0 |
| cpu_count | 12 |
| seed | 42 |
| strict_default | True |
| data_file | loan.csv |
| data_sha256 | 23783ef320e4df24ac113d6e5b830edb909912b7783d49b89aacd5690dc9120c |
| data_bytes | 1,189,395,649 |
| raw_rows | 2,260,668 |
| raw_cols | 146 |
| issue_first | Jun 2007 |
| issue_last | Dec 2018 |
| modelled_rows | 1,303,638 |
| partitions/train/rows | 449,414 |
| partitions/train/default_rate | 0.17 |
| partitions/train/first | Jun 2007 |
| partitions/train/last | Dec 2014 |
| partitions/val/rows | 373,412 |
| partitions/val/default_rate | 0.2016 |
| partitions/val/first | Jan 2015 |
| partitions/val/last | Dec 2015 |
| partitions/test/rows | 480,812 |
| partitions/test/default_rate | 0.2288 |
| partitions/test/first | Jan 2016 |
| partitions/test/last | Dec 2018 |
| n_features | 77 |

</details>

<details><summary><code>evaluation_results.json</code></summary>

| Key | Value |
|---|---|
| discrimination/val[0]/model | Logistic regression |
| discrimination/val[0]/roc_auc | 0.7343 |
| discrimination/val[0]/auc_ci_low | 0.7324 |
| discrimination/val[0]/auc_ci_high | 0.7363 |
| discrimination/val[0]/ks | 0.3425 |
| discrimination/val[0]/gini | 0.4686 |
| discrimination/val[0]/brier | 0.1433 |
| discrimination/val[1]/model | XGBoost |
| discrimination/val[1]/roc_auc | 0.7408 |
| discrimination/val[1]/auc_ci_low | 0.7389 |
| discrimination/val[1]/auc_ci_high | 0.7427 |
| discrimination/val[1]/ks | 0.3512 |
| discrimination/val[1]/gini | 0.4816 |
| discrimination/val[1]/brier | 0.1416 |
| discrimination/val[2]/model | LightGBM |
| discrimination/val[2]/roc_auc | 0.7414 |
| discrimination/val[2]/auc_ci_low | 0.7395 |
| discrimination/val[2]/auc_ci_high | 0.7433 |
| discrimination/val[2]/ks | 0.3524 |
| discrimination/val[2]/gini | 0.4828 |
| discrimination/val[2]/brier | 0.1416 |
| discrimination/val[3]/model | Random Forest |
| discrimination/val[3]/roc_auc | 0.736 |
| discrimination/val[3]/auc_ci_low | 0.734 |
| discrimination/val[3]/auc_ci_high | 0.7379 |
| discrimination/val[3]/ks | 0.342 |
| discrimination/val[3]/gini | 0.4719 |
| discrimination/val[3]/brier | 0.1451 |
| discrimination/val[4]/model | Ensemble (L1) |
| discrimination/val[4]/roc_auc | 0.7411 |
| discrimination/val[4]/auc_ci_low | 0.7392 |
| discrimination/val[4]/auc_ci_high | 0.743 |
| discrimination/val[4]/ks | 0.3514 |
| discrimination/val[4]/gini | 0.4822 |
| discrimination/val[4]/brier | 0.1423 |
| discrimination/test[0]/model | Logistic regression |
| discrimination/test[0]/roc_auc | 0.7018 |
| discrimination/test[0]/auc_ci_low | 0.7001 |
| discrimination/test[0]/auc_ci_high | 0.7035 |
| discrimination/test[0]/ks | 0.2934 |
| discrimination/test[0]/gini | 0.4036 |
| discrimination/test[0]/brier | 0.1645 |
| discrimination/test[1]/model | XGBoost |
| discrimination/test[1]/roc_auc | 0.7114 |
| discrimination/test[1]/auc_ci_low | 0.7098 |
| discrimination/test[1]/auc_ci_high | 0.7131 |
| discrimination/test[1]/ks | 0.3068 |
| discrimination/test[1]/gini | 0.4229 |
| discrimination/test[1]/brier | 0.1627 |
| discrimination/test[2]/model | LightGBM |
| discrimination/test[2]/roc_auc | 0.7118 |
| discrimination/test[2]/auc_ci_low | 0.7102 |
| discrimination/test[2]/auc_ci_high | 0.7135 |
| discrimination/test[2]/ks | 0.3064 |
| discrimination/test[2]/gini | 0.4237 |
| discrimination/test[2]/brier | 0.1627 |
| discrimination/test[3]/model | Random Forest |
| discrimination/test[3]/roc_auc | 0.7046 |
| discrimination/test[3]/auc_ci_low | 0.7029 |
| discrimination/test[3]/auc_ci_high | 0.7062 |
| discrimination/test[3]/ks | 0.2932 |
| discrimination/test[3]/gini | 0.4091 |
| discrimination/test[3]/brier | 0.1654 |
| discrimination/test[4]/model | Ensemble (L1) |
| discrimination/test[4]/roc_auc | 0.7112 |
| discrimination/test[4]/auc_ci_low | 0.7096 |
| discrimination/test[4]/auc_ci_high | 0.7129 |
| discrimination/test[4]/ks | 0.3049 |
| discrimination/test[4]/gini | 0.4225 |
| discrimination/test[4]/brier | 0.1633 |
| delong_ensemble_vs/xgb/auc_1 | 0.7112 |
| delong_ensemble_vs/xgb/auc_2 | 0.7114 |
| delong_ensemble_vs/xgb/diff | -0.0002 |
| delong_ensemble_vs/xgb/ci_low | -0.0004 |
| delong_ensemble_vs/xgb/ci_high | -0.0 |
| delong_ensemble_vs/xgb/z | -2.5 |
| delong_ensemble_vs/xgb/p_value | 0.012578 |
| delong_ensemble_vs/lgbm/auc_1 | 0.7112 |
| delong_ensemble_vs/lgbm/auc_2 | 0.7118 |
| delong_ensemble_vs/lgbm/diff | -0.0006 |
| delong_ensemble_vs/lgbm/ci_low | -0.0008 |
| delong_ensemble_vs/lgbm/ci_high | -0.0004 |
| delong_ensemble_vs/lgbm/z | -6.32 |
| delong_ensemble_vs/lgbm/p_value | 2.61e-10 |
| delong_ensemble_vs/rf/auc_1 | 0.7112 |
| delong_ensemble_vs/rf/auc_2 | 0.7046 |
| delong_ensemble_vs/rf/diff | 0.0067 |
| delong_ensemble_vs/rf/ci_low | 0.0063 |
| delong_ensemble_vs/rf/ci_high | 0.007 |
| delong_ensemble_vs/rf/z | 36.36 |
| delong_ensemble_vs/rf/p_value | 1.55e-289 |
| delong_ensemble_vs/lr/auc_1 | 0.7112 |
| delong_ensemble_vs/lr/auc_2 | 0.7018 |
| delong_ensemble_vs/lr/diff | 0.0094 |
| delong_ensemble_vs/lr/ci_low | 0.0088 |
| delong_ensemble_vs/lr/ci_high | 0.0101 |
| delong_ensemble_vs/lr/z | 29.36 |
| delong_ensemble_vs/lr/p_value | 1.71e-189 |
| bootstrap_ensemble_vs/xgb/mean_diff | -0.0002 |
| bootstrap_ensemble_vs/xgb/ci_low | -0.0004 |
| bootstrap_ensemble_vs/xgb/ci_high | -0.0 |
| bootstrap_ensemble_vs/xgb/share_ensemble_better | 0.006 |
| bootstrap_ensemble_vs/lgbm/mean_diff | -0.0006 |
| bootstrap_ensemble_vs/lgbm/ci_low | -0.0008 |
| bootstrap_ensemble_vs/lgbm/ci_high | -0.0004 |
| bootstrap_ensemble_vs/lgbm/share_ensemble_better | 0.0 |
| bootstrap_ensemble_vs/rf/mean_diff | 0.0067 |
| bootstrap_ensemble_vs/rf/ci_low | 0.0063 |
| bootstrap_ensemble_vs/rf/ci_high | 0.007 |
| bootstrap_ensemble_vs/rf/share_ensemble_better | 1.0 |
| bootstrap_ensemble_vs/lr/mean_diff | 0.0095 |
| bootstrap_ensemble_vs/lr/ci_low | 0.0088 |
| bootstrap_ensemble_vs/lr/ci_high | 0.0101 |
| bootstrap_ensemble_vs/lr/share_ensemble_better | 1.0 |
| n_boot | 2,000 |
| calibration/train/lr/brier | 0.1302 |
| calibration/train/lr/mean_pd | 0.17 |
| calibration/train/lr/default_rate | 0.17 |
| calibration/train/lr/calibration_intercept | -0.0 |
| calibration/train/lr/calibration_slope | 1.003 |
| calibration/train/xgb/brier | 0.1279 |
| calibration/train/xgb/mean_pd | 0.17 |
| calibration/train/xgb/default_rate | 0.17 |
| calibration/train/xgb/calibration_intercept | 0.0 |
| calibration/train/xgb/calibration_slope | 1.071 |
| calibration/train/lgbm/brier | 0.1276 |
| calibration/train/lgbm/mean_pd | 0.17 |
| calibration/train/lgbm/default_rate | 0.17 |
| calibration/train/lgbm/calibration_intercept | -0.0 |
| calibration/train/lgbm/calibration_slope | 1.079 |
| calibration/train/rf/brier | 0.1273 |
| calibration/train/rf/mean_pd | 0.1698 |
| calibration/train/rf/default_rate | 0.17 |
| calibration/train/rf/calibration_intercept | 0.001 |
| calibration/train/rf/calibration_slope | 1.497 |
| calibration/train/ensemble/brier | 0.1273 |
| calibration/train/ensemble/mean_pd | 0.1699 |
| calibration/train/ensemble/default_rate | 0.17 |
| calibration/train/ensemble/calibration_intercept | 0.001 |
| calibration/train/ensemble/calibration_slope | 1.216 |
| calibration/val/lr/brier | 0.1433 |
| calibration/val/lr/mean_pd | 0.1723 |
| calibration/val/lr/default_rate | 0.2016 |
| calibration/val/lr/calibration_intercept | 0.213 |
| calibration/val/lr/calibration_slope | 1.139 |
| calibration/val/xgb/brier | 0.1416 |
| calibration/val/xgb/mean_pd | 0.1752 |
| calibration/val/xgb/default_rate | 0.2016 |
| calibration/val/xgb/calibration_intercept | 0.193 |
| calibration/val/xgb/calibration_slope | 1.076 |
| calibration/val/lgbm/brier | 0.1416 |
| calibration/val/lgbm/mean_pd | 0.1746 |
| calibration/val/lgbm/default_rate | 0.2016 |
| calibration/val/lgbm/calibration_intercept | 0.199 |
| calibration/val/lgbm/calibration_slope | 1.068 |
| calibration/val/rf/brier | 0.1451 |
| calibration/val/rf/mean_pd | 0.1673 |
| calibration/val/rf/default_rate | 0.2016 |
| calibration/val/rf/calibration_intercept | 0.244 |
| calibration/val/rf/calibration_slope | 1.404 |
| calibration/val/ensemble/brier | 0.1423 |
| calibration/val/ensemble/mean_pd | 0.1723 |
| calibration/val/ensemble/default_rate | 0.2016 |
| calibration/val/ensemble/calibration_intercept | 0.212 |
| calibration/val/ensemble/calibration_slope | 1.187 |
| calibration/test/lr/brier | 0.1645 |
| calibration/test/lr/mean_pd | 0.1744 |
| calibration/test/lr/default_rate | 0.2288 |
| calibration/test/lr/calibration_intercept | 0.378 |
| calibration/test/lr/calibration_slope | 0.912 |
| calibration/test/xgb/brier | 0.1627 |
| calibration/test/xgb/mean_pd | 0.1707 |
| calibration/test/xgb/default_rate | 0.2288 |
| calibration/test/xgb/calibration_intercept | 0.406 |
| calibration/test/xgb/calibration_slope | 0.964 |
| calibration/test/lgbm/brier | 0.1627 |
| calibration/test/lgbm/mean_pd | 0.1704 |
| calibration/test/lgbm/default_rate | 0.2288 |
| calibration/test/lgbm/calibration_intercept | 0.41 |
| calibration/test/lgbm/calibration_slope | 0.953 |
| calibration/test/rf/brier | 0.1654 |
| calibration/test/rf/mean_pd | 0.1677 |
| calibration/test/rf/default_rate | 0.2288 |
| calibration/test/rf/calibration_intercept | 0.412 |
| calibration/test/rf/calibration_slope | 1.212 |
| calibration/test/ensemble/brier | 0.1633 |
| calibration/test/ensemble/mean_pd | 0.1696 |
| calibration/test/ensemble/default_rate | 0.2288 |
| calibration/test/ensemble/calibration_intercept | 0.408 |
| calibration/test/ensemble/calibration_slope | 1.056 |
| reliability_ensemble_test[0]/bin | 0 |
| reliability_ensemble_test[0]/mean_pd | 0.0389 |
| reliability_ensemble_test[0]/default_rate | 0.0441 |
| reliability_ensemble_test[0]/loans | 48,082 |
| reliability_ensemble_test[1]/bin | 1 |
| reliability_ensemble_test[1]/mean_pd | 0.0661 |
| reliability_ensemble_test[1]/default_rate | 0.0879 |
| reliability_ensemble_test[1]/loans | 48,081 |
| reliability_ensemble_test[2]/bin | 2 |
| reliability_ensemble_test[2]/mean_pd | 0.0895 |
| reliability_ensemble_test[2]/default_rate | 0.1237 |
| reliability_ensemble_test[2]/loans | 48,081 |
| reliability_ensemble_test[3]/bin | 3 |
| reliability_ensemble_test[3]/mean_pd | 0.1121 |
| reliability_ensemble_test[3]/default_rate | 0.1608 |
| reliability_ensemble_test[3]/loans | 48,081 |
| reliability_ensemble_test[4]/bin | 4 |
| reliability_ensemble_test[4]/mean_pd | 0.136 |
| reliability_ensemble_test[4]/default_rate | 0.1937 |
| reliability_ensemble_test[4]/loans | 48,081 |
| reliability_ensemble_test[5]/bin | 5 |
| reliability_ensemble_test[5]/mean_pd | 0.162 |
| reliability_ensemble_test[5]/default_rate | 0.2278 |
| reliability_ensemble_test[5]/loans | 48,081 |
| reliability_ensemble_test[6]/bin | 6 |
| reliability_ensemble_test[6]/mean_pd | 0.1912 |
| reliability_ensemble_test[6]/default_rate | 0.2665 |
| reliability_ensemble_test[6]/loans | 48,081 |
| reliability_ensemble_test[7]/bin | 7 |
| reliability_ensemble_test[7]/mean_pd | 0.2273 |
| reliability_ensemble_test[7]/default_rate | 0.3183 |
| reliability_ensemble_test[7]/loans | 48,081 |
| reliability_ensemble_test[8]/bin | 8 |
| reliability_ensemble_test[8]/mean_pd | 0.28 |
| reliability_ensemble_test[8]/default_rate | 0.374 |
| reliability_ensemble_test[8]/loans | 48,081 |
| reliability_ensemble_test[9]/bin | 9 |
| reliability_ensemble_test[9]/mean_pd | 0.3929 |
| reliability_ensemble_test[9]/default_rate | 0.4915 |
| reliability_ensemble_test[9]/loans | 48,082 |
| drift/domain_classifier_auc | 0.993 |
| drift/domain_top_features/int_rate | 0.4494 |
| drift/domain_top_features/initial_list_status_w | 0.1732 |
| drift/domain_top_features/sub_grade | 0.1729 |
| drift/domain_top_features/grade | 0.0465 |
| drift/domain_top_features/num_bc_tl | 0.0252 |
| drift/domain_top_features/percent_bc_gt_75 | 0.0124 |
| drift/domain_top_features/term | 0.0119 |
| drift/domain_top_features/total_rev_hi_lim | 0.0116 |
| drift/domain_top_features/total_il_high_credit_limit | 0.0091 |
| drift/domain_top_features/bc_open_to_buy | 0.0082 |
| drift/feature_psi_top10/initial_list_status_w | 0.7698 |
| drift/feature_psi_top10/delinq_amnt | 0.4468 |
| drift/feature_psi_top10/mo_sin_old_rev_tl_op | 0.3622 |
| drift/feature_psi_top10/total_il_high_credit_limit | 0.3322 |
| drift/feature_psi_top10/total_rev_hi_lim | 0.3159 |
| drift/feature_psi_top10/mo_sin_old_il_acct | 0.282 |
| drift/feature_psi_top10/bc_util | 0.2795 |
| drift/feature_psi_top10/tot_hi_cred_lim | 0.2767 |
| drift/feature_psi_top10/tot_cur_bal | 0.2752 |
| drift/feature_psi_top10/avg_cur_bal | 0.269 |
| drift/by_year_file | drift_by_year.csv |

</details>

<details><summary><code>feature_lists.json</code></summary>

| Key | Value |
|---|---|
| post_origination_removed[0] | total_pymnt |
| post_origination_removed[1] | total_pymnt_inv |
| post_origination_removed[2] | total_rec_prncp |
| post_origination_removed[3] | total_rec_int |
| post_origination_removed[4] | total_rec_late_fee |
| post_origination_removed[5] | recoveries |
| post_origination_removed[6] | collection_recovery_fee |
| post_origination_removed[7] | last_pymnt_amnt |
| post_origination_removed[8] | out_prncp |
| post_origination_removed[9] | out_prncp_inv |
| post_origination_removed[10] | last_pymnt_d |
| post_origination_removed[11] | next_pymnt_d |
| post_origination_removed[12] | last_credit_pull_d |
| post_origination_removed[13] | debt_settlement_flag |
| post_origination_removed[14] | hardship_flag |
| post_origination_removed[15] | pymnt_plan |
| post_origination_removed[16] | hardship_type |
| post_origination_removed[17] | hardship_reason |
| post_origination_removed[18] | hardship_status |
| post_origination_removed[19] | deferral_term |
| post_origination_removed[20] | hardship_amount |
| post_origination_removed[21] | hardship_start_date |
| post_origination_removed[22] | hardship_end_date |
| post_origination_removed[23] | payment_plan_start_date |
| post_origination_removed[24] | hardship_length |
| post_origination_removed[25] | hardship_dpd |
| post_origination_removed[26] | hardship_loan_status |
| post_origination_removed[27] | orig_projected_additional_accrued_interest |
| post_origination_removed[28] | hardship_payoff_balance_amount |
| post_origination_removed[29] | hardship_last_payment_amount |
| post_origination_removed[30] | debt_settlement_flag_date |
| post_origination_removed[31] | settlement_status |
| post_origination_removed[32] | settlement_date |
| post_origination_removed[33] | settlement_amount |
| post_origination_removed[34] | settlement_percentage |
| post_origination_removed[35] | settlement_term |
| redundant_removed[0] | installment |
| redundant_removed[1] | funded_amnt_inv |
| high_missing_removed[0] | mths_since_last_delinq |
| high_missing_removed[1] | mths_since_last_record |
| high_missing_removed[2] | mths_since_last_major_derog |
| high_missing_removed[3] | annual_inc_joint |
| high_missing_removed[4] | dti_joint |
| high_missing_removed[5] | verification_status_joint |
| high_missing_removed[6] | open_acc_6m |
| high_missing_removed[7] | open_act_il |
| high_missing_removed[8] | open_il_12m |
| high_missing_removed[9] | open_il_24m |
| high_missing_removed[10] | mths_since_rcnt_il |
| high_missing_removed[11] | total_bal_il |
| high_missing_removed[12] | il_util |
| high_missing_removed[13] | open_rv_12m |
| high_missing_removed[14] | open_rv_24m |
| high_missing_removed[15] | max_bal_bc |
| high_missing_removed[16] | all_util |
| high_missing_removed[17] | inq_fi |
| high_missing_removed[18] | total_cu_tl |
| high_missing_removed[19] | inq_last_12m |
| high_missing_removed[20] | mths_since_recent_bc_dlq |
| high_missing_removed[21] | mths_since_recent_revol_delinq |
| high_missing_removed[22] | revol_bal_joint |
| high_missing_removed[23] | sec_app_earliest_cr_line |
| high_missing_removed[24] | sec_app_inq_last_6mths |
| high_missing_removed[25] | sec_app_mort_acc |
| high_missing_removed[26] | sec_app_open_acc |
| high_missing_removed[27] | sec_app_revol_util |
| high_missing_removed[28] | sec_app_open_act_il |
| high_missing_removed[29] | sec_app_num_rev_accts |
| high_missing_removed[30] | sec_app_chargeoff_within_12_mths |
| high_missing_removed[31] | sec_app_collections_12_mths_ex_med |
| high_missing_removed[32] | sec_app_mths_since_last_major_derog |
| constant_removed[0] | policy_code |
| constant_removed[1] | application_type |
| constant_removed[2] | disbursement_method |
| raw_features[0] | loan_amnt |
| raw_features[1] | funded_amnt |
| raw_features[2] | term |
| raw_features[3] | int_rate |
| raw_features[4] | grade |
| raw_features[5] | sub_grade |
| raw_features[6] | emp_length |
| raw_features[7] | home_ownership |
| raw_features[8] | annual_inc |
| raw_features[9] | verification_status |
| raw_features[10] | purpose |
| raw_features[11] | dti |
| raw_features[12] | delinq_2yrs |
| raw_features[13] | inq_last_6mths |
| raw_features[14] | open_acc |
| raw_features[15] | pub_rec |
| raw_features[16] | revol_bal |
| raw_features[17] | revol_util |
| raw_features[18] | total_acc |
| raw_features[19] | initial_list_status |
| raw_features[20] | collections_12_mths_ex_med |
| raw_features[21] | acc_now_delinq |
| raw_features[22] | tot_coll_amt |
| raw_features[23] | tot_cur_bal |
| raw_features[24] | total_rev_hi_lim |
| raw_features[25] | acc_open_past_24mths |
| raw_features[26] | avg_cur_bal |
| raw_features[27] | bc_open_to_buy |
| raw_features[28] | bc_util |
| raw_features[29] | chargeoff_within_12_mths |
| raw_features[30] | delinq_amnt |
| raw_features[31] | mo_sin_old_il_acct |
| raw_features[32] | mo_sin_old_rev_tl_op |
| raw_features[33] | mo_sin_rcnt_rev_tl_op |
| raw_features[34] | mo_sin_rcnt_tl |
| raw_features[35] | mort_acc |
| raw_features[36] | mths_since_recent_bc |
| raw_features[37] | mths_since_recent_inq |
| raw_features[38] | num_accts_ever_120_pd |
| raw_features[39] | num_actv_bc_tl |
| raw_features[40] | num_actv_rev_tl |
| raw_features[41] | num_bc_sats |
| raw_features[42] | num_bc_tl |
| raw_features[43] | num_il_tl |
| raw_features[44] | num_op_rev_tl |
| raw_features[45] | num_rev_accts |
| raw_features[46] | num_rev_tl_bal_gt_0 |
| raw_features[47] | num_sats |
| raw_features[48] | num_tl_120dpd_2m |
| raw_features[49] | num_tl_30dpd |
| raw_features[50] | num_tl_90g_dpd_24m |
| raw_features[51] | num_tl_op_past_12m |
| raw_features[52] | pct_tl_nvr_dlq |
| raw_features[53] | percent_bc_gt_75 |
| raw_features[54] | pub_rec_bankruptcies |
| raw_features[55] | tax_liens |
| raw_features[56] | tot_hi_cred_lim |
| raw_features[57] | total_bal_ex_mort |
| raw_features[58] | total_bc_limit |
| raw_features[59] | total_il_high_credit_limit |
| encoded_features[0] | loan_amnt |
| encoded_features[1] | funded_amnt |
| encoded_features[2] | term |
| encoded_features[3] | int_rate |
| encoded_features[4] | grade |
| encoded_features[5] | sub_grade |
| encoded_features[6] | emp_length |
| encoded_features[7] | annual_inc |
| encoded_features[8] | dti |
| encoded_features[9] | delinq_2yrs |
| encoded_features[10] | inq_last_6mths |
| encoded_features[11] | open_acc |
| encoded_features[12] | pub_rec |
| encoded_features[13] | revol_bal |
| encoded_features[14] | revol_util |
| encoded_features[15] | total_acc |
| encoded_features[16] | collections_12_mths_ex_med |
| encoded_features[17] | acc_now_delinq |
| encoded_features[18] | tot_coll_amt |
| encoded_features[19] | tot_cur_bal |
| encoded_features[20] | total_rev_hi_lim |
| encoded_features[21] | acc_open_past_24mths |
| encoded_features[22] | avg_cur_bal |
| encoded_features[23] | bc_open_to_buy |
| encoded_features[24] | bc_util |
| encoded_features[25] | chargeoff_within_12_mths |
| encoded_features[26] | delinq_amnt |
| encoded_features[27] | mo_sin_old_il_acct |
| encoded_features[28] | mo_sin_old_rev_tl_op |
| encoded_features[29] | mo_sin_rcnt_rev_tl_op |
| encoded_features[30] | mo_sin_rcnt_tl |
| encoded_features[31] | mort_acc |
| encoded_features[32] | mths_since_recent_bc |
| encoded_features[33] | mths_since_recent_inq |
| encoded_features[34] | num_accts_ever_120_pd |
| encoded_features[35] | num_actv_bc_tl |
| encoded_features[36] | num_actv_rev_tl |
| encoded_features[37] | num_bc_sats |
| encoded_features[38] | num_bc_tl |
| encoded_features[39] | num_il_tl |
| encoded_features[40] | num_op_rev_tl |
| encoded_features[41] | num_rev_accts |
| encoded_features[42] | num_rev_tl_bal_gt_0 |
| encoded_features[43] | num_sats |
| encoded_features[44] | num_tl_120dpd_2m |
| encoded_features[45] | num_tl_30dpd |
| encoded_features[46] | num_tl_90g_dpd_24m |
| encoded_features[47] | num_tl_op_past_12m |
| encoded_features[48] | pct_tl_nvr_dlq |
| encoded_features[49] | percent_bc_gt_75 |
| encoded_features[50] | pub_rec_bankruptcies |
| encoded_features[51] | tax_liens |
| encoded_features[52] | tot_hi_cred_lim |
| encoded_features[53] | total_bal_ex_mort |
| encoded_features[54] | total_bc_limit |
| encoded_features[55] | total_il_high_credit_limit |
| encoded_features[56] | home_ownership_MORTGAGE |
| encoded_features[57] | home_ownership_NONE |
| encoded_features[58] | home_ownership_OTHER |
| encoded_features[59] | home_ownership_OWN |
| encoded_features[60] | home_ownership_RENT |
| encoded_features[61] | verification_status_Source Verified |
| encoded_features[62] | verification_status_Verified |
| encoded_features[63] | purpose_credit_card |
| encoded_features[64] | purpose_debt_consolidation |
| encoded_features[65] | purpose_educational |
| encoded_features[66] | purpose_home_improvement |
| encoded_features[67] | purpose_house |
| encoded_features[68] | purpose_major_purchase |
| encoded_features[69] | purpose_medical |
| encoded_features[70] | purpose_moving |
| encoded_features[71] | purpose_other |
| encoded_features[72] | purpose_renewable_energy |
| encoded_features[73] | purpose_small_business |
| encoded_features[74] | purpose_vacation |
| encoded_features[75] | purpose_wedding |
| encoded_features[76] | initial_list_status_w |

</details>

<details><summary><code>layer1_metrics.json</code></summary>

| Key | Value |
|---|---|
| lr/val/roc_auc | 0.7343 |
| lr/val/ks | 0.3425 |
| lr/val/gini | 0.4686 |
| lr/val/brier | 0.1433 |
| lr/val/f1_at_0.50 | 0.1016 |
| lr/val/mean_pd | 0.1723 |
| lr/val/default_rate | 0.2016 |
| lr/test/roc_auc | 0.7018 |
| lr/test/ks | 0.2934 |
| lr/test/gini | 0.4036 |
| lr/test/brier | 0.1645 |
| lr/test/f1_at_0.50 | 0.1019 |
| lr/test/mean_pd | 0.1744 |
| lr/test/default_rate | 0.2288 |
| xgb/val/roc_auc | 0.7408 |
| xgb/val/ks | 0.3512 |
| xgb/val/gini | 0.4816 |
| xgb/val/brier | 0.1416 |
| xgb/val/f1_at_0.50 | 0.0983 |
| xgb/val/mean_pd | 0.1752 |
| xgb/val/default_rate | 0.2016 |
| xgb/test/roc_auc | 0.7114 |
| xgb/test/ks | 0.3068 |
| xgb/test/gini | 0.4229 |
| xgb/test/brier | 0.1627 |
| xgb/test/f1_at_0.50 | 0.0654 |
| xgb/test/mean_pd | 0.1707 |
| xgb/test/default_rate | 0.2288 |
| lgbm/val/roc_auc | 0.7414 |
| lgbm/val/ks | 0.3524 |
| lgbm/val/gini | 0.4828 |
| lgbm/val/brier | 0.1416 |
| lgbm/val/f1_at_0.50 | 0.1041 |
| lgbm/val/mean_pd | 0.1746 |
| lgbm/val/default_rate | 0.2016 |
| lgbm/test/roc_auc | 0.7118 |
| lgbm/test/ks | 0.3064 |
| lgbm/test/gini | 0.4237 |
| lgbm/test/brier | 0.1627 |
| lgbm/test/f1_at_0.50 | 0.072 |
| lgbm/test/mean_pd | 0.1704 |
| lgbm/test/default_rate | 0.2288 |
| rf/val/roc_auc | 0.736 |
| rf/val/ks | 0.342 |
| rf/val/gini | 0.4719 |
| rf/val/brier | 0.1451 |
| rf/val/f1_at_0.50 | 0.0 |
| rf/val/mean_pd | 0.1673 |
| rf/val/default_rate | 0.2016 |
| rf/test/roc_auc | 0.7046 |
| rf/test/ks | 0.2932 |
| rf/test/gini | 0.4091 |
| rf/test/brier | 0.1654 |
| rf/test/f1_at_0.50 | 0.0001 |
| rf/test/mean_pd | 0.1677 |
| rf/test/default_rate | 0.2288 |
| ensemble/val/roc_auc | 0.7411 |
| ensemble/val/ks | 0.3514 |
| ensemble/val/gini | 0.4822 |
| ensemble/val/brier | 0.1423 |
| ensemble/val/f1_at_0.50 | 0.0511 |
| ensemble/val/mean_pd | 0.1723 |
| ensemble/val/default_rate | 0.2016 |
| ensemble/test/roc_auc | 0.7112 |
| ensemble/test/ks | 0.3049 |
| ensemble/test/gini | 0.4225 |
| ensemble/test/brier | 0.1633 |
| ensemble/test/f1_at_0.50 | 0.0342 |
| ensemble/test/mean_pd | 0.1696 |
| ensemble/test/default_rate | 0.2288 |

</details>

<details><summary><code>layer2_results.json</code></summary>

| Key | Value |
|---|---|
| layer | 2 |
| psi[0]/model | XGBoost |
| psi[0]/psi_train_vs_val | 0.0191 |
| psi[0]/psi_train_vs_test | 0.003 |
| psi[0]/status_test | Stable |
| psi[1]/model | LightGBM |
| psi[1]/psi_train_vs_val | 0.0185 |
| psi[1]/psi_train_vs_test | 0.0036 |
| psi[1]/status_test | Stable |
| psi[2]/model | Random Forest |
| psi[2]/psi_train_vs_val | 0.0107 |
| psi[2]/psi_train_vs_test | 0.0022 |
| psi[2]/status_test | Stable |
| psi[3]/model | Ensemble |
| psi[3]/psi_train_vs_val | 0.0162 |
| psi[3]/psi_train_vs_test | 0.0027 |
| psi[3]/status_test | Stable |
| score_vs_outcome/train/mean_pd | 0.1699 |
| score_vs_outcome/train/default_rate | 0.17 |
| score_vs_outcome/val/mean_pd | 0.1723 |
| score_vs_outcome/val/default_rate | 0.2016 |
| score_vs_outcome/test/mean_pd | 0.1696 |
| score_vs_outcome/test/default_rate | 0.2288 |
| shap/method | interventional TreeSHAP, probability scale, average of the three members (weights 1/3) |
| shap/n_explained | 2,000 |
| shap/n_background | 100 |
| shap/base_value | 0.1584 |
| shap/reconstruction/median_abs_error | 1.73e-08 |
| shap/reconstruction/p99_abs_error | 0.000705 |
| shap/reconstruction/max_abs_error | 0.001324 |
| shap/reconstruction/loans_error_above_0.001 | 1 |
| shap/top10[0]/feature | sub_grade |
| shap/top10[0]/mean_abs_shap | 0.0269 |
| shap/top10[1]/feature | term |
| shap/top10[1]/mean_abs_shap | 0.0262 |
| shap/top10[2]/feature | annual_inc |
| shap/top10[2]/mean_abs_shap | 0.0169 |
| shap/top10[3]/feature | acc_open_past_24mths |
| shap/top10[3]/mean_abs_shap | 0.0127 |
| shap/top10[4]/feature | grade |
| shap/top10[4]/mean_abs_shap | 0.0119 |
| shap/top10[5]/feature | dti |
| shap/top10[5]/mean_abs_shap | 0.0106 |
| shap/top10[6]/feature | loan_amnt |
| shap/top10[6]/mean_abs_shap | 0.0094 |
| shap/top10[7]/feature | int_rate |
| shap/top10[7]/mean_abs_shap | 0.008 |
| shap/top10[8]/feature | funded_amnt |
| shap/top10[8]/mean_abs_shap | 0.0056 |
| shap/top10[9]/feature | total_bc_limit |
| shap/top10[9]/mean_abs_shap | 0.0052 |
| shap/worked_example/test_row | 30 |
| shap/worked_example/base_value | 0.1584 |
| shap/worked_example/sum_of_contributions | -0.046 |
| shap/worked_example/reconstructed_pd | 0.1124 |
| shap/worked_example/ensemble_pd | 0.1124 |
| shap/worked_example/top5/annual_inc | -0.0227 |
| shap/worked_example/top5/term | -0.0162 |
| shap/worked_example/top5/avg_cur_bal | -0.016 |
| shap/worked_example/top5/acc_open_past_24mths | 0.0159 |
| shap/worked_example/top5/loan_amnt | 0.0071 |

</details>

<details><summary><code>layer3_results.json</code></summary>

| Key | Value |
|---|---|
| layer | 3 |
| policy/t_star | 0.2776 |
| policy/t_low | 0.2621 |
| policy/t_high | 0.2955 |
| policy/refer_share_target | 0.05 |
| policy/chosen_on | validation (2015), realised profit/loss |
| policy/validation_profit_approve_all | 191249698.0 |
| policy/validation_profit_approve_below_t_star | 274347415.0 |
| monitor_settings/window | 500 |
| monitor_settings/window_threshold | 0.026 |
| monitor_settings/window_reference_mean_pd | 0.1723 |
| monitor_settings/ph_delta | 0.005 |
| monitor_settings/ph_lambda | 10.48 |
| monitor_settings/ddm_warning_sd | 2.0 |
| monitor_settings/ddm_drift_sd | 3.0 |
| monitor_settings/calibrated_on | no-change streams from Jan–Jun 2015 (99th percentile of the maximum statistic) |
| detector_validation[0]/scenario | no_change |
| detector_validation[0]/detector | window |
| detector_validation[0]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[0]/detection_rate | None |
| detector_validation[0]/median_delay_loans | None |
| detector_validation[1]/scenario | no_change |
| detector_validation[1]/detector | page_hinkley |
| detector_validation[1]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[1]/detection_rate | None |
| detector_validation[1]/median_delay_loans | None |
| detector_validation[2]/scenario | no_change |
| detector_validation[2]/detector | ddm_delayed_labels |
| detector_validation[2]/false_alarms_per_10k_loans | 0.68 |
| detector_validation[2]/detection_rate | None |
| detector_validation[2]/median_delay_loans | None |
| detector_validation[3]/scenario | real_change_2015_to_2016_18 |
| detector_validation[3]/detector | window |
| detector_validation[3]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[3]/detection_rate | 0.0 |
| detector_validation[3]/median_delay_loans | None |
| detector_validation[4]/scenario | real_change_2015_to_2016_18 |
| detector_validation[4]/detector | page_hinkley |
| detector_validation[4]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[4]/detection_rate | 0.0 |
| detector_validation[4]/median_delay_loans | None |
| detector_validation[5]/scenario | real_change_2015_to_2016_18 |
| detector_validation[5]/detector | ddm_delayed_labels |
| detector_validation[5]/false_alarms_per_10k_loans | 1.16 |
| detector_validation[5]/detection_rate | 0.18 |
| detector_validation[5]/median_delay_loans | 1,828 |
| detector_validation[6]/scenario | injected_riskier_mix |
| detector_validation[6]/detector | window |
| detector_validation[6]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[6]/detection_rate | 1.0 |
| detector_validation[6]/median_delay_loans | 104 |
| detector_validation[7]/scenario | injected_riskier_mix |
| detector_validation[7]/detector | page_hinkley |
| detector_validation[7]/false_alarms_per_10k_loans | 0.0 |
| detector_validation[7]/detection_rate | 1.0 |
| detector_validation[7]/median_delay_loans | 72 |
| detector_validation[8]/scenario | injected_riskier_mix |
| detector_validation[8]/detector | ddm_delayed_labels |
| detector_validation[8]/false_alarms_per_10k_loans | 1.32 |
| detector_validation[8]/detection_rate | 0.97 |
| detector_validation[8]/median_delay_loans | 228 |
| test_stream/order_within_month | random (fixed seed); issue dates are monthly |
| test_stream/window_alarms | 3 |
| test_stream/page_hinkley_alarms | 3 |
| test_stream/ddm_delayed_label_alarms | 1 |
| test_stream/file_order_window_alarms | 226 |
| test_stream/file_order_page_hinkley_alarms | 48 |
| test_stream/window_alarm_months[0] | 2016-01 |
| test_stream/window_alarm_months[1] | 2018-12 |
| test_stream/ddm_alarm_months[0] | 2016-03 |
| decisions_full_test/approve_rate | 0.8237 |
| decisions_full_test/refer_rate | 0.0504 |
| decisions_full_test/decline_rate | 0.126 |
| decisions_full_test/default_rate_approved | 0.1828 |
| decisions_full_test/default_rate_referred | 0.3724 |
| decisions_full_test/default_rate_declined | 0.4725 |
| decisions_full_test/approval_errors | 72,386 |
| decisions_full_test/decline_errors | 31,950 |
| decisions_full_test/profit_if_referred_declined | -128518501.6741 |
| decisions_full_test/profit_if_referred_approved | -180596869.7033 |
| decisions_full_test/share_of_defaults_caught | 0.3421 |
| decisions_full_test/precision_decline | 0.4725 |
| decisions_full_test/recall_decline | 0.2601 |
| decisions_full_test/f1_decline | 0.3355 |
| decisions_full_test/precision_flagged | 0.4439 |
| decisions_full_test/recall_flagged | 0.3421 |
| decisions_full_test/f1_flagged | 0.3864 |
| baselines/approve_all_profit | -401946965.0 |
| baselines/single_threshold_t_star_profit | -153202891.0 |
| baselines/single_threshold_t_star_f1 | 0.3633 |
| demo/loans | 2,000 |
| demo/decisions/AUTO_APPROVE | 1,684 |
| demo/decisions/AUTO_DECLINE | 228 |
| demo/decisions/REFER_TO_HUMAN | 88 |
| demo/first_month | 2016-01 |
| demo/last_month | 2016-01 |
| demo/audit_file | audit_trail_20261121_193025.csv |
| demo/hash_chain_valid | True |
| demo/first_three[0]/loan_idx | 23,138 |
| demo/first_three[0]/issue_month | 2016-01 |
| demo/first_three[0]/true_label | DEFAULT |
| demo/first_three[0]/pd | 0.2291 |
| demo/first_three[0]/band | Low |
| demo/first_three[0]/monitor | OK |
| demo/first_three[0]/decision | AUTO_APPROVE |
| demo/first_three[0]/reason |  |
| demo/first_three[0]/top3[0][0] | acc_open_past_24mths |
| demo/first_three[0]/top3[0][1] | 0.0403 |
| demo/first_three[0]/top3[1][0] | sub_grade |
| demo/first_three[0]/top3[1][1] | 0.0292 |
| demo/first_three[0]/top3[2][0] | term |
| demo/first_three[0]/top3[2][1] | -0.0203 |
| demo/first_three[1]/loan_idx | 20,615 |
| demo/first_three[1]/issue_month | 2016-01 |
| demo/first_three[1]/true_label | PAID |
| demo/first_three[1]/pd | 0.0429 |
| demo/first_three[1]/band | Low |
| demo/first_three[1]/monitor | OK |
| demo/first_three[1]/decision | AUTO_APPROVE |
| demo/first_three[1]/reason |  |
| demo/first_three[1]/top3[0][0] | sub_grade |
| demo/first_three[1]/top3[0][1] | -0.034 |
| demo/first_three[1]/top3[1][0] | int_rate |
| demo/first_three[1]/top3[1][1] | -0.0171 |
| demo/first_three[1]/top3[2][0] | grade |
| demo/first_three[1]/top3[2][1] | -0.0139 |
| demo/first_three[2]/loan_idx | 27,154 |
| demo/first_three[2]/issue_month | 2016-01 |
| demo/first_three[2]/true_label | PAID |
| demo/first_three[2]/pd | 0.4151 |
| demo/first_three[2]/band | High |
| demo/first_three[2]/monitor | OK |
| demo/first_three[2]/decision | AUTO_DECLINE |
| demo/first_three[2]/reason |  |
| demo/first_three[2]/top3[0][0] | sub_grade |
| demo/first_three[2]/top3[0][1] | 0.077 |
| demo/first_three[2]/top3[1][0] | term |
| demo/first_three[2]/top3[1][1] | 0.065 |
| demo/first_three[2]/top3[2][0] | grade |
| demo/first_three[2]/top3[2][1] | 0.0335 |
| latency/score/mean_ms | 77.84 |
| latency/score/median_ms | 75.44 |
| latency/score/p95_ms | 88.1 |
| latency/shap/mean_ms | 233.63 |
| latency/shap/median_ms | 227.02 |
| latency/shap/p95_ms | 297.63 |
| latency/monitor/mean_ms | 0.01 |
| latency/monitor/median_ms | 0.01 |
| latency/monitor/p95_ms | 0.02 |
| latency/decide_and_log/mean_ms | 1.21 |
| latency/decide_and_log/median_ms | 0.77 |
| latency/decide_and_log/p95_ms | 1.06 |
| latency/layer3_total_per_loan/mean_ms | 312.69 |
| latency/layer3_total_per_loan/median_ms | 305.57 |
| latency/layer3_total_per_loan/p95_ms | 379.86 |
| latency/layer1_batch_scoring/loans | 100,000 |
| latency/layer1_batch_scoring/seconds | 1.22 |
| latency/layer1_batch_scoring/loans_per_second | 81,763 |
| latency/process_memory_mb | 1272.0 |
| latency/hardware/platform | Windows-11-10.0.26200-SP0 |
| latency/hardware/processor | AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD |
| latency/hardware/cpu_count | 12 |

</details>

<details><summary><code>leakage_diagnostic.json</code></summary>

| Key | Value |
|---|---|
| model | XGBoost, 100 trees, depth 5, learning rate 0.1 |
| leakage_columns_encoded[0] | total_pymnt |
| leakage_columns_encoded[1] | total_pymnt_inv |
| leakage_columns_encoded[2] | total_rec_prncp |
| leakage_columns_encoded[3] | total_rec_int |
| leakage_columns_encoded[4] | total_rec_late_fee |
| leakage_columns_encoded[5] | recoveries |
| leakage_columns_encoded[6] | collection_recovery_fee |
| leakage_columns_encoded[7] | last_pymnt_amnt |
| leakage_columns_encoded[8] | installment |
| leakage_columns_encoded[9] | funded_amnt_inv |
| leakage_columns_encoded[10] | debt_settlement_flag_Y |
| with_leakage/features | 88 |
| with_leakage/val_auc | 0.9998 |
| with_leakage/test_auc | 0.9999 |
| without_leakage/features | 77 |
| without_leakage/val_auc | 0.74 |
| without_leakage/test_auc | 0.7101 |

</details>

