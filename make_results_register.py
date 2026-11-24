"""
make_results_register.py — builds RESULTS_REGISTER.md from the files the ACRS notebooks write.

Every number in the register is read from acrs_data/*.json, acrs_data/*.csv or the executed ACRS.ipynb.
Nothing is typed by hand. Each row names the file (and key) it came from, and the header lists the
SHA-256 of every source file, so the register is tied to one specific run.

Usage (from the ACRS folder, after all five notebooks have run):
    python make_results_register.py
or
    python make_results_register.py "C:/path/to/ACRS"
"""
import csv
import datetime as dt
import hashlib
import json
import os
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
DATA = os.path.join(ROOT, 'acrs_data')
OUT_FILE = os.path.join(DATA, 'RESULTS_REGISTER.md')

used_files = set()
lines = []


def path(name):
    return os.path.join(DATA, name)


def exists(name):
    return os.path.exists(path(name))


def load_json(name):
    used_files.add(name)
    with open(path(name), encoding='utf-8') as f:
        return json.load(f)


def load_csv(name):
    used_files.add(name)
    with open(path(name), encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def fmt(v):
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, float):
        if v != 0 and abs(v) < 1e-4:
            return f'{v:.2e}'
        return repr(round(v, 6))
    if isinstance(v, int):
        return f'{v:,}'
    return str(v)


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def section(title, note=None):
    lines.append(f'\n## {title}\n')
    if note:
        lines.append(f'{note}\n')


def table(header, rows):
    lines.append('| ' + ' | '.join(header) + ' |')
    lines.append('|' + '|'.join('---' for _ in header) + '|')
    for r in rows:
        lines.append('| ' + ' | '.join(fmt(x) if not isinstance(x, str) else x for x in r) + ' |')
    lines.append('')


def missing(name):
    lines.append(f'_Not available yet: `{name}` not found (notebook not run)._\n')


def flatten(x, prefix=''):
    out = []
    if isinstance(x, dict):
        for k, v in x.items():
            out += flatten(v, f'{prefix}/{k}' if prefix else str(k))
    elif isinstance(x, list):
        for i, v in enumerate(x):
            out += flatten(v, f'{prefix}[{i}]')
    else:
        out.append((prefix, x))
    return out


# ---------------------------------------------------------------- data and partitions
section('1. Data and partitions (Table 3.2, Section 4.2.1)', 'Source: `environment.json`.')
if exists('environment.json'):
    env = load_json('environment.json')
    rows = [
        ['Data file', env.get('data_file'), 'environment.json → data_file'],
        ['Data file SHA-256', env.get('data_sha256'), 'environment.json → data_sha256'],
        ['Loans in file', env.get('raw_rows'), 'environment.json → raw_rows'],
        ['Columns in file', (env['raw_cols'] - 1) if 'raw_cols' in env else 'n/a',
         'environment.json → raw_cols minus 1 (the code adds a `year` column before counting)'],
        ['Issue dates', f"{env.get('issue_first')} to {env.get('issue_last')}", 'environment.json → issue_first / issue_last'],
        ['Resolved loans modelled', env.get('modelled_rows'), 'environment.json → modelled_rows'],
        ['Default definition strict (Charged Off/Default vs Fully Paid)', env.get('strict_default'), 'environment.json → strict_default'],
        ['Features after encoding', env.get('n_features'), 'environment.json → n_features'],
    ]
    for part, p in env.get('partitions', {}).items():
        rows.append([f'{part}: loans', p['rows'], f'environment.json → partitions/{part}/rows'])
        rows.append([f'{part}: default rate', p['default_rate'], f'environment.json → partitions/{part}/default_rate'])
        rows.append([f'{part}: issue dates', f"{p['first']} to {p['last']}", f'environment.json → partitions/{part}/first, last'])
    table(['Number', 'Value', 'Source'], rows)
    section('Software environment (Section 3.4.1)', 'Source: `environment.json`. Use these versions in requirements.txt and Section 3.')
    table(['Item', 'Value'], [[k, env[k]] for k in ['python', 'numpy', 'pandas', 'scikit-learn', 'xgboost', 'lightgbm',
                                                     'shap', 'optuna', 'scipy', 'platform', 'cpu_count', 'seed'] if k in env])
else:
    missing('environment.json')

# loan status counts are only printed in the executed ACRS.ipynb
nb_path = os.path.join(ROOT, 'ACRS.ipynb')
if os.path.exists(nb_path):
    nb = json.load(open(nb_path, encoding='utf-8'))
    text = ''
    for c in nb['cells']:
        for o in c.get('outputs', []):
            if o.get('output_type') == 'stream':
                text += ''.join(o['text'])
    if 'loan_status' in text:
        block = text.split('loan_status', 1)[1].split('Name: count')[0].strip().splitlines()
        rows = []
        for ln in block:
            parts = ln.rsplit(None, 1)
            if len(parts) == 2 and parts[1].isdigit():
                rows.append([parts[0].strip(), int(parts[1]), 'ACRS.ipynb output (loan_status counts)'])
        if rows:
            section('Loan status in the raw file (Section 4.2.1)', 'Source: printed output of the executed `ACRS.ipynb`.')
            table(['Status', 'Loans', 'Source'], rows)
            used_files.add('../ACRS.ipynb')

if exists('resolved_share_by_year.csv'):
    section('Maturity by issue year (Table 4.1)', 'Source: `resolved_share_by_year.csv`.')
    r = load_csv('resolved_share_by_year.csv')
    table(list(r[0].keys()), [list(x.values()) for x in r])

# ---------------------------------------------------------------- features and leakage
section('2. Features (Table 4.2) and leakage check (Table 4.3)', 'Source: `feature_lists.json`, `leakage_diagnostic.json`.')
if exists('feature_lists.json'):
    fl = load_json('feature_lists.json')
    rows = [[k, len(v) if isinstance(v, list) else v, f'feature_lists.json → {k}'] for k, v in fl.items()]
    table(['List', 'Count', 'Source'], rows)
    for k, v in fl.items():
        if isinstance(v, list):
            lines.append(f'- **{k}** ({len(v)}): ' + ', '.join(f'`{c}`' for c in v))
    lines.append('')
else:
    missing('feature_lists.json')
if exists('leakage_diagnostic.json'):
    lk = load_json('leakage_diagnostic.json')
    table(['Number', 'Value', 'Source'], [
        ['Diagnostic model', lk['model'], 'leakage_diagnostic.json → model'],
        ['With leakage: features', lk['with_leakage']['features'], 'leakage_diagnostic.json → with_leakage/features'],
        ['With leakage: val ROC-AUC', lk['with_leakage']['val_auc'], 'leakage_diagnostic.json → with_leakage/val_auc'],
        ['With leakage: test ROC-AUC', lk['with_leakage']['test_auc'], 'leakage_diagnostic.json → with_leakage/test_auc'],
        ['Without leakage: features', lk['without_leakage']['features'], 'leakage_diagnostic.json → without_leakage/features'],
        ['Without leakage: val ROC-AUC', lk['without_leakage']['val_auc'], 'leakage_diagnostic.json → without_leakage/val_auc'],
        ['Without leakage: test ROC-AUC', lk['without_leakage']['test_auc'], 'leakage_diagnostic.json → without_leakage/test_auc'],
        ['Columns added back', ', '.join(lk['leakage_columns_encoded']), 'leakage_diagnostic.json → leakage_columns_encoded'],
    ])
else:
    missing('leakage_diagnostic.json')

# ---------------------------------------------------------------- layer 1
section('3. Tuning (Table 4.4)', 'Source: `best_params.json`.')
if exists('best_params.json'):
    bp = load_json('best_params.json')
    rows = []
    for m in ['xgb', 'lgbm', 'rf', 'lr']:
        for k, v in bp.get(m, {}).items():
            rows.append([m, k, v, f'best_params.json → {m}/{k}'])
    for k in ['n_trials', 'tuning_sample', 'seed']:
        if k in bp:
            rows.append(['all', k, bp[k], f'best_params.json → {k}'])
    for m, v in bp.get('best_val_auc_tuning_sample', {}).items():
        rows.append([m, 'best val ROC-AUC on tuning sample', v, f'best_params.json → best_val_auc_tuning_sample/{m}'])
    table(['Model', 'Parameter', 'Value', 'Source'], rows)
else:
    missing('best_params.json')

section('4. Discrimination with 95% CI (Table 4.5)', 'Source: `evaluation_results.json` → discrimination.')
if exists('evaluation_results.json'):
    ev = load_json('evaluation_results.json')
    for split in ['val', 'test']:
        lines.append(f'**{split}**\n')
        rs = ev['discrimination'][split]
        table(['Model', 'ROC-AUC', '95% CI low', '95% CI high', 'KS', 'Gini', 'Brier'],
              [[r['model'], r['roc_auc'], r['auc_ci_low'], r['auc_ci_high'], r['ks'], r['gini'], r['brier']] for r in rs])
    if exists('layer1_metrics.json'):
        l1 = load_json('layer1_metrics.json')
        lines.append('F1 at the 0.50 cut-off (reported only for continuity; not a decision threshold). Source: `layer1_metrics.json`.\n')
        table(['Model', 'val F1@0.50', 'test F1@0.50', 'test mean PD', 'test default rate'],
              [[m, l1[m]['val']['f1_at_0.50'], l1[m]['test']['f1_at_0.50'], l1[m]['test']['mean_pd'], l1[m]['test']['default_rate']]
               for m in l1])

    section('5. DeLong and bootstrap tests, ensemble vs each model, test set (Table 4.6)',
            f"Source: `evaluation_results.json` → delong_ensemble_vs, bootstrap_ensemble_vs (bootstrap resamples: {ev.get('n_boot')}).")
    rows = []
    for m, d in ev['delong_ensemble_vs'].items():
        b = ev['bootstrap_ensemble_vs'][m]
        rows.append([m, d['auc_1'], d['auc_2'], d['diff'], d['ci_low'], d['ci_high'], d['z'], d['p_value'],
                     b['ci_low'], b['ci_high'], b['share_ensemble_better']])
    table(['vs model', 'AUC ensemble', 'AUC model', 'Difference', 'DeLong CI low', 'DeLong CI high', 'z', 'p',
           'Bootstrap CI low', 'Bootstrap CI high', 'Share of resamples ensemble better'], rows)

    section('6. Calibration (Table 4.7, Figure 4.2)', 'Source: `evaluation_results.json` → calibration. Intercept and slope on the log-odds scale.')
    for split, ms in ev['calibration'].items():
        lines.append(f'**{split}**\n')
        table(['Model', 'Brier', 'Mean PD', 'Default rate', 'Calibration intercept', 'Calibration slope'],
              [[m, v['brier'], v['mean_pd'], v['default_rate'], v['calibration_intercept'], v['calibration_slope']] for m, v in ms.items()])
    lines.append('**Ensemble by PD decile, test set** (source: `evaluation_results.json` → reliability_ensemble_test)\n')
    table(['Decile', 'Mean PD', 'Default rate', 'Loans'],
          [[r['bin'], r['mean_pd'], r['default_rate'], r['loans']] for r in ev['reliability_ensemble_test']])

    section('7. Drift decomposition (Table 4.10, Figure 4.4, Section 4.4.3)', 'Source: `evaluation_results.json` → drift, and `drift_by_year.csv`.')
    table(['Number', 'Value', 'Source'],
          [['Domain classifier ROC-AUC (train vs test borrowers, 5-fold)', ev['drift']['domain_classifier_auc'],
            'evaluation_results.json → drift/domain_classifier_auc']])
    table(['Feature', 'Share of gain in domain classifier'], [[k, v] for k, v in ev['drift']['domain_top_features'].items()])
    table(['Feature', 'PSI train vs test'], [[k, v] for k, v in ev['drift']['feature_psi_top10'].items()])
    if exists('drift_by_year.csv'):
        r = load_csv('drift_by_year.csv')
        lines.append('**By issue year** (source: `drift_by_year.csv`; train years are in-sample)\n')
        table(list(r[0].keys()), [list(x.values()) for x in r])
else:
    missing('evaluation_results.json')

# ---------------------------------------------------------------- layer 2
section('8. Layer 2: PSI (Table 4.8) and SHAP (Table 4.9, Section 4.4.2)', 'Source: `layer2_results.json`.')
if exists('layer2_results.json'):
    l2 = load_json('layer2_results.json')
    table(['Model', 'PSI train vs val', 'PSI train vs test', 'Status (test)'],
          [[r['model'], r['psi_train_vs_val'], r['psi_train_vs_test'], r['status_test']] for r in l2['psi']])
    table(['Split', 'Ensemble mean PD', 'Observed default rate'],
          [[s, v['mean_pd'], v['default_rate']] for s, v in l2['score_vs_outcome'].items()])
    sh = l2['shap']
    rec = sh['reconstruction']
    table(['Number', 'Value', 'Source'], [
        ['SHAP method', sh['method'], 'layer2_results.json → shap/method'],
        ['Loans explained', sh['n_explained'], 'layer2_results.json → shap/n_explained'],
        ['Background rows', sh['n_background'], 'layer2_results.json → shap/n_background'],
        ['Base value E[f(X)]', sh['base_value'], 'layer2_results.json → shap/base_value'],
        ['Reconstruction error, median', rec['median_abs_error'], 'layer2_results.json → shap/reconstruction'],
        ['Reconstruction error, 99th percentile', rec['p99_abs_error'], 'layer2_results.json → shap/reconstruction'],
        ['Reconstruction error, max', rec['max_abs_error'], 'layer2_results.json → shap/reconstruction'],
        ['Loans with error > 0.001', rec['loans_error_above_0.001'], 'layer2_results.json → shap/reconstruction'],
    ])
    table(['Rank', 'Feature', 'Mean |SHAP| (PD points)'], [[i + 1, r['feature'], r['mean_abs_shap']] for i, r in enumerate(sh['top10'])])
    we = sh['worked_example']
    lines.append(f"**Worked example (Section 4.4.2):** test row {we['test_row']}, base value {we['base_value']}, "
                 f"sum of contributions {we['sum_of_contributions']}, reconstructed PD {we['reconstructed_pd']}, "
                 f"ensemble PD {we['ensemble_pd']}.\n")
    table(['Feature', 'SHAP (PD points)'], [[k, v] for k, v in we['top5'].items()])
else:
    missing('layer2_results.json')

# ---------------------------------------------------------------- layer 3
section('9. Layer 3: decision policy, drift detectors, decisions, audit log, latency (Tables 4.11–4.17)',
        'Source: `layer3_results.json` and the Layer 3 CSV files.')
if exists('layer3_results.json'):
    l3 = load_json('layer3_results.json')
    table(['Key', 'Value'], [[k, v] for k, v in flatten({k: v for k, v in l3.items() if k != 'demo'})])
    demo = l3.get('demo', {})
    table(['Key', 'Value'], [[k, v] for k, v in flatten({k: v for k, v in demo.items() if k != 'first_three'})])
    for name in ['drift_detector_validation.csv', 'policy_threshold_sensitivity.csv', 'policy_by_year.csv',
                 'delayed_label_monitoring_by_month.csv']:
        if exists(name):
            r = load_csv(name)
            lines.append(f'**{name}**\n')
            table(list(r[0].keys()), [list(x.values()) for x in r])
else:
    missing('layer3_results.json')

# ---------------------------------------------------------------- full dump
section('10. Every stored number (complete list, for searching)',
        'Every scalar in every results JSON, as stored. If a number in the thesis is not in this list or the tables above, it did not come from the code.')
for name in sorted(n for n in os.listdir(DATA) if n.endswith('.json')):
    data = load_json(name)
    lines.append(f'<details><summary><code>{name}</code></summary>\n')
    table(['Key', 'Value'], [[k, v] for k, v in flatten(data)])
    lines.append('</details>\n')

# ---------------------------------------------------------------- header with file hashes
head = ['# ACRS results register', '',
        f'Generated {dt.datetime.now().strftime("%Y-%m-%d %H:%M")} by `make_results_register.py` from the files in `acrs_data`.',
        'Every value below is read from a file written by the notebooks. Nothing is typed by hand.', '',
        '## Source files', '',
        'The SHA-256 fingerprint identifies the exact file each number came from. If a file changes, its fingerprint changes.', '',
        '| File | SHA-256 (first 16 characters) |', '|---|---|']
for name in sorted(used_files):
    p = os.path.normpath(os.path.join(DATA, name))
    if os.path.exists(p):
        head.append(f'| `{os.path.basename(p)}` | `{sha256(p)[:16]}` |')
with open(OUT_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(head + lines) + '\n')
print(f'Wrote {OUT_FILE} ({len(lines)} lines, {len(used_files)} source files)')
