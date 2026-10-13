import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

base = r"JSON Data/Saif Sir NTRCA Suggestion"
subjects = [
    ('Bangla', 'বাংলা', 'bn', 'fa-book'),
    ('English', 'ইংরেজি', 'eng', 'fa-language'),
    ('GK', 'সাধারণ জ্ঞান', 'gk', 'fa-earth-americas'),
    ('Math', 'গণিত', 'math', 'fa-calculator')
]

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def clean_question_text(t):
    if not t: return ''
    return re.sub(r'^[০-৯\d]+[\.\)]\s*', '', str(t)).strip()

def clean_option_text(t):
    if not t: return ''
    return re.sub(r'^(\([ক-ঘa-dA-D1-4]\)|[ক-ঘ][\)\.\-–—:]\s*|[a-dA-D][\)\.\-–—:]\s*|[1-4][\)\.\-–—:]\s*)', '', str(t)).strip()

lectures = []
total_q = 0
subject_counts = {'Bangla': 0, 'English': 0, 'GK': 0, 'Math': 0}

for s_dir, s_bn, s_prefix, s_icon in subjects:
    dir_path = os.path.join(base, s_dir)
    files = sorted([f for f in os.listdir(dir_path) if f.endswith('.json')], key=natural_sort_key)
    for idx, fname in enumerate(files):
        fpath = os.path.join(dir_path, fname)
        with open(fpath, 'r', encoding='utf-8') as fp:
            d = json.load(fp)

        raw_questions = d.get('questions', [])
        clean_fname = os.path.splitext(fname)[0]
        title = d.get('title', clean_fname) or clean_fname
        short_title = clean_fname

        cleaned_questions = []
        for q_idx, q in enumerate(raw_questions):
            # Normalize options: might be dict or list
            raw_opts = q.get('options')
            if isinstance(raw_opts, dict):
                opts_list = [raw_opts.get('ক', ''), raw_opts.get('খ', ''), raw_opts.get('গ', ''), raw_opts.get('ঘ', '')]
            elif isinstance(raw_opts, list):
                opts_list = raw_opts
            else:
                opts_list = []

            # Clean option texts
            opts = [clean_option_text(o) for o in opts_list]
            ans = str(q.get('answer', '')).strip()
            exp = str(q.get('explanation', '')).strip()

            cleaned_questions.append({
                'id': q.get('id', q_idx + 1),
                'question': clean_question_text(q.get('question', '')),
                'options': opts,
                'answer': ans,
                'explanation': exp
            })

        count = len(cleaned_questions)
        total_q += count
        subject_counts[s_dir] += count

        lectures.append({
            'id': f'{s_prefix}_{idx+1}',
            'subject': s_dir,
            'subjectBn': s_bn,
            'subjectIcon': s_icon,
            'filename': fname,
            'title': title,
            'short': short_title,
            'count': count,
            'questions': cleaned_questions
        })

print(f"Loaded {len(lectures)} model tests, total {total_q} questions.")
for s_dir, s_bn, _, _ in subjects:
    print(f"  {s_bn}: {subject_counts[s_dir]} questions")

html_template = """<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Saif Sir NTRCA Suggestion (মডেল টেস্ট স্পেশাল) - বিষয় ও মডেল টেস্টভিত্তিক প্রশ্নব্যাংক</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Bangla:wght@400;500;600;700&family=Hind+Siliguri:wght@400;500;600;700&family=Noto+Sans+Bengali:wght@400;500;600;700&family=Noto+Serif+Bengali:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <!-- Font Awesome 6 Icons (Local Driver) -->
  <link rel="stylesheet" href="drivers/fontawesome/css/all.min.css">
  <!-- KaTeX Library for Math Formula Rendering (Local Driver) -->
  <link rel="stylesheet" href="drivers/katex/katex.min.css">
  <script defer src="drivers/katex/katex.min.js"></script>
  <style>
    :root {
      --bg-page: #f8fafc;
      --card-bg: #ffffff;
      --text-main: #0f172a;
      --text-sub: #334155;
      --text-muted: #64748b;
      --border-color: #e2e8f0;
      --dotted-line: #94a3b8;
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --primary-light: #eef2ff;
      --primary-border: #a5b4fc;
      --success: #16a34a;
      --success-light: #ecfdf5;
      --danger: #dc2626;
      --danger-light: #fef2f2;
      --amber: #d97706;
      --amber-light: #fffbeb;
      --shadow-sheet: 0 4px 20px -2px rgba(15, 23, 42, 0.06), 0 2px 6px -1px rgba(15, 23, 42, 0.03);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Hind Siliguri', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      transition: font-family 0.15s ease;
    }

    /* Top Navigation Portal Bar */
    .portal-nav {
      background: #0f172a;
      color: #94a3b8;
      font-size: 12px;
      border-bottom: 1px solid #1e293b;
    }

    .portal-nav-inner {
      max-width: 1300px;
      margin: 0 auto;
      padding: 6px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }

    .portal-links {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .portal-link {
      color: #cbd5e1;
      text-decoration: none;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 8px;
      border-radius: 4px;
      transition: all 0.15s ease;
    }

    .portal-link:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.08);
    }

    .portal-link.active {
      color: #818cf8;
      background: rgba(129, 140, 248, 0.15);
      font-weight: 700;
    }

    /* Header Section */
    header.app-header {
      position: relative;
      background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
      border-bottom: 1px solid #e2e8f0;
      border-top: 3.5px solid #4f46e5;
      box-shadow: 0 4px 20px -4px rgba(15, 23, 42, 0.06);
    }

    .header-container {
      max-width: 1300px;
      margin: 0 auto;
      padding: 16px 20px 14px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .header-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }

    .brand-logo {
      display: flex;
      align-items: center;
      gap: 10px;
      user-select: none;
      flex-shrink: 0;
      text-decoration: none;
    }

    .badge-icon {
      width: 42px;
      height: 42px;
      background: linear-gradient(135deg, #4338ca 0%, #4f46e5 55%, #6366f1 100%);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 10px;
      font-size: 19px;
      box-shadow: 0 4px 12px rgba(79, 70, 229, 0.32);
      border: 1px solid rgba(255, 255, 255, 0.25);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      flex-shrink: 0;
    }

    .badge-icon:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 6px 18px rgba(79, 70, 229, 0.42);
    }

    .brand-name {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      font-weight: 800;
      font-size: 19px;
      color: #0f172a;
      letter-spacing: -0.4px;
      white-space: nowrap;
    }

    .subject-title-area {
      display: flex;
      flex-direction: column;
      gap: 3px;
      margin-top: 2px;
    }

    .subject-title-area h1 {
      font-size: 21px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.3px;
    }

    .subject-title-area p {
      font-size: 13.5px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }

    /* Subject Tabs Navigation */
    .subject-nav-tabs {
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 2px;
      border-bottom: 1px solid #e2e8f0;
      scrollbar-width: thin;
    }

    .subject-tab {
      padding: 7px 16px;
      border-radius: 8px 8px 0 0;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text-sub);
      background: transparent;
      border: 1px solid transparent;
      border-bottom: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.16s ease;
      white-space: nowrap;
      position: relative;
      font-family: inherit;
    }

    .subject-tab:hover {
      color: var(--primary);
      background: var(--primary-light);
    }

    .subject-tab.active {
      color: var(--primary);
      background: #ffffff;
      border-color: #e2e8f0;
      border-bottom: 2px solid #ffffff;
      margin-bottom: -1px;
      font-weight: 700;
      box-shadow: 0 -2px 6px rgba(0, 0, 0, 0.03);
    }

    .subject-tab.active::after {
      content: '';
      position: absolute;
      top: -1px;
      left: 0;
      right: 0;
      height: 3px;
      background: var(--primary);
      border-radius: 8px 8px 0 0;
    }

    .top-actions {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    /* Action Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: inherit;
      font-size: 13px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background-color: #ffffff;
      color: var(--text-sub);
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
    }

    .btn:hover {
      background-color: #f1f5f9;
      color: var(--text-main);
      border-color: #cbd5e1;
    }

    .btn-active {
      background-color: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary-border);
    }

    .btn-primary {
      background: linear-gradient(135deg, #4338ca 0%, #4f46e5 100%);
      color: #ffffff;
      border-color: #4338ca;
    }

    .btn-primary:hover {
      background: linear-gradient(135deg, #3730a3 0%, #4338ca 100%);
      color: #ffffff;
    }

    .btn-practice {
      background-color: #fffbeb;
      color: #b45309;
      border-color: #fde68a;
    }

    .btn-practice:hover {
      background-color: #fef3c7;
      color: #92400e;
    }

    .btn-practice.active {
      background-color: #f59e0b;
      color: #ffffff;
      border-color: #d97706;
      box-shadow: 0 2px 8px rgba(245, 158, 11, 0.35);
    }

    /* Font Selector Wrap */
    .font-select-wrap {
      position: relative;
      display: inline-flex;
      align-items: center;
    }

    .font-select-wrap select {
      appearance: none;
      -webkit-appearance: none;
      font-family: inherit;
      font-size: 13px;
      font-weight: 500;
      padding: 6px 28px 6px 30px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background-color: #ffffff;
      color: var(--text-sub);
      cursor: pointer;
      outline: none;
      transition: all 0.15s ease;
    }

    .font-select-wrap select:hover {
      border-color: #cbd5e1;
      background-color: #f8fafc;
    }

    .font-select-wrap select:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.15);
    }

    .font-icon {
      position: absolute;
      left: 10px;
      font-size: 12px;
      color: var(--text-muted);
      pointer-events: none;
    }

    .font-arrow {
      position: absolute;
      right: 10px;
      font-size: 10px;
      color: var(--text-muted);
      pointer-events: none;
    }

    /* Filters Bar */
    .filter-bar {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      background-color: #ffffff;
      padding: 10px 14px;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);
    }

    .select-wrap {
      position: relative;
      min-width: 250px;
      flex-shrink: 0;
    }

    .select-wrap select {
      width: 100%;
      appearance: none;
      -webkit-appearance: none;
      font-family: inherit;
      font-size: 13.5px;
      font-weight: 600;
      padding: 7px 32px 7px 12px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background-color: #f8fafc;
      color: var(--text-main);
      cursor: pointer;
      outline: none;
      transition: all 0.15s ease;
    }

    .select-wrap select:hover {
      border-color: #cbd5e1;
      background-color: #ffffff;
    }

    .select-wrap select:focus {
      border-color: var(--primary);
      background-color: #ffffff;
      box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.15);
    }

    .select-arrow {
      position: absolute;
      right: 11px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 11px;
      color: var(--text-muted);
      pointer-events: none;
    }

    /* Search Box */
    .search-wrap {
      position: relative;
      flex-grow: 1;
      min-width: 200px;
    }

    .search-wrap input {
      width: 100%;
      font-family: inherit;
      font-size: 13.5px;
      padding: 7px 12px 7px 32px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background-color: #f8fafc;
      color: var(--text-main);
      outline: none;
      transition: all 0.15s ease;
    }

    .search-wrap input:hover {
      border-color: #cbd5e1;
      background-color: #ffffff;
    }

    .search-wrap input:focus {
      border-color: var(--primary);
      background-color: #ffffff;
      box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.15);
    }

    .search-icon {
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 12px;
      color: var(--text-muted);
      pointer-events: none;
    }

    /* Pills Scroll */
    .pills-scroll {
      display: flex;
      align-items: center;
      gap: 6px;
      width: 100%;
      padding-top: 6px;
      border-top: 1px dashed var(--border-color);
      flex-wrap: wrap;
      max-height: 84px;
      overflow-y: auto;
      scrollbar-width: thin;
    }

    .pill {
      font-size: 12px;
      font-weight: 500;
      padding: 4px 10px;
      border-radius: 16px;
      background: #ffffff;
      color: var(--text-sub);
      border: 1px solid #e2e8f0;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.16s ease;
      font-family: inherit;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03);
    }

    .pill:hover {
      background: #f1f5f9;
      border-color: #cbd5e1;
      color: var(--text-main);
      transform: translateY(-1px);
    }

    .pill.active {
      background: linear-gradient(135deg, #3730a3, #4338ca);
      color: #ffffff;
      border-color: #3730a3;
      font-weight: 600;
      box-shadow: 0 3px 10px rgba(67, 56, 202, 0.28);
    }

    /* Practice Mode Info Banner */
    .practice-banner {
      display: none;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      background: linear-gradient(135deg, #fffbeb, #fef3c7);
      border: 1px solid #fde68a;
      border-radius: 8px;
      padding: 9px 16px;
      font-size: 13px;
      color: #92400e;
      box-shadow: 0 2px 6px rgba(245, 158, 11, 0.08);
      margin-top: 2px;
    }

    .practice-banner.active {
      display: flex;
    }

    .btn-mini-reset {
      background: #ffffff;
      color: #b45309;
      border: 1px solid #fcd34d;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 11.5px;
      font-weight: 700;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.15s ease;
    }

    .btn-mini-reset:hover {
      background: #fef3c7;
      color: #78350f;
    }

    /* Status Strip */
    .status-strip {
      max-width: 1300px;
      margin: 12px auto 0;
      padding: 0 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      font-size: 13px;
      color: var(--text-muted);
      flex-wrap: wrap;
    }

    .stats-info strong {
      color: var(--text-main);
    }

    .view-controls {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Main Sheets Content */
    .main-content {
      max-width: 1300px;
      margin: 14px auto 30px;
      padding: 0 20px;
    }

    .sheet-card {
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      box-shadow: var(--shadow-sheet);
      padding: 24px;
      margin-bottom: 24px;
      transition: box-shadow 0.2s ease;
    }

    .sheet-header {
      padding-bottom: 14px;
      margin-bottom: 18px;
      border-bottom: 2px solid #f1f5f9;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }

    .sheet-title {
      font-size: 18px;
      font-weight: 700;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sheet-title-badge {
      font-size: 11.5px;
      font-weight: 600;
      background: var(--primary-light);
      color: var(--primary);
      padding: 2px 8px;
      border-radius: 4px;
      border: 1px solid var(--primary-border);
    }

    .sheet-count {
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 500;
    }

    /* Two Columns Container */
    .columns-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      column-gap: 24px;
      position: relative;
    }

    .columns-container::after {
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      left: 50%;
      width: 1px;
      border-left: 1.5px dotted var(--dotted-line);
      transform: translateX(-50%);
    }

    .column-half {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* Question Block */
    .question-block {
      padding: 12px 14px;
      background: #ffffff;
      border: 1px solid #eef2f6;
      border-radius: 8px;
      transition: all 0.16s ease;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .question-block:hover {
      border-color: #cbd5e1;
      box-shadow: 0 3px 12px rgba(15, 23, 42, 0.04);
    }

    .meta-badges-row {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }

    .sec-badge {
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 4px;
      background: #f1f5f9;
      color: #475569;
      border: 1px solid #e2e8f0;
    }

    .sec-badge.subject-badge {
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary-border);
    }

    .question-title {
      font-size: 14.5px;
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.5;
    }

    .q-number {
      color: var(--primary);
      font-weight: 700;
      margin-right: 2px;
    }

    /* 2x2 Options Grid */
    .options-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px 14px;
    }

    .option-cell {
      display: flex;
      align-items: flex-start;
      gap: 6px;
      font-size: 13.5px;
      line-height: 1.45;
      color: var(--text-sub);
      padding: 5px 8px;
      border-radius: 6px;
      background-color: #fafbfc;
      border: 1px solid transparent;
      transition: all 0.15s ease;
      cursor: default;
      user-select: none;
    }

    .is-practice .option-cell {
      cursor: pointer;
    }

    .is-practice .option-cell:hover {
      background-color: #f1f5f9;
      border-color: #cbd5e1;
    }

    .opt-label {
      font-weight: 600;
      color: #64748b;
      min-width: 22px;
      flex-shrink: 0;
    }

    .opt-text {
      flex-grow: 1;
      word-break: break-word;
    }

    /* Highlight Correct Answers */
    .show-answers .option-cell.is-correct {
      background-color: #ecfdf5;
      border-color: #a7f3d0;
    }

    .show-answers .option-cell.is-correct .opt-label,
    .show-answers .option-cell.is-correct .opt-text {
      color: #166534;
      font-weight: 600;
    }

    /* Practice Mode Colors */
    .option-cell.practice-correct {
      background-color: #dcfce7 !important;
      border-color: #86efac !important;
    }
    .option-cell.practice-correct .opt-label,
    .option-cell.practice-correct .opt-text {
      color: #15803d !important;
      font-weight: 700 !important;
    }

    .option-cell.practice-wrong {
      background-color: #fee2e2 !important;
      border-color: #fca5a5 !important;
    }
    .option-cell.practice-wrong .opt-label,
    .option-cell.practice-wrong .opt-text {
      color: #b91c1c !important;
      font-weight: 600 !important;
    }

    .option-cell.practice-revealed {
      background-color: #f0fdf4 !important;
      border-color: #bbf7d0 !important;
    }
    .option-cell.practice-revealed .opt-label,
    .option-cell.practice-revealed .opt-text {
      color: #166534 !important;
      font-weight: 700 !important;
    }

    /* Answer Row & Tag */
    .answer-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 4px;
      flex-wrap: wrap;
    }

    .answer-tag {
      display: none;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--success);
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: 4px;
      padding: 2px 8px;
      width: fit-content;
    }

    .show-answers .answer-tag,
    .question-block.practice-answered .answer-tag {
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    /* Individual Question Explanation Toggle Button */
    .btn-toggle-exp-single {
      display: none;
      align-items: center;
      gap: 3px;
      background: #eef2ff;
      border: 1px solid #c7d2fe;
      color: #4338ca;
      font-size: 11.5px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: inherit;
    }

    .btn-toggle-exp-single:hover {
      background: #e0e7ff;
      border-color: #a5b4fc;
    }

    .show-answers .btn-toggle-exp-single,
    .show-explanations .btn-toggle-exp-single,
    .question-block.practice-answered .btn-toggle-exp-single {
      display: inline-flex;
    }

    /* Explanation Box */
    .explanation-box {
      display: none;
      margin-top: 6px;
      padding: 9px 13px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 3.5px solid #4f46e5;
      border-radius: 6px;
      font-size: 13.5px;
      line-height: 1.55;
      color: #334155;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
      animation: fadeInExp 0.18s ease-in-out;
    }

    @keyframes fadeInExp {
      from { opacity: 0; transform: translateY(-3px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .exp-badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-weight: 700;
      color: #4338ca;
      font-size: 13px;
      margin-bottom: 2px;
    }

    .exp-body {
      color: #1e293b;
      word-break: break-word;
      white-space: pre-line;
    }

    .show-explanations .explanation-box,
    .question-block.practice-answered .explanation-box,
    .explanation-box.force-visible {
      display: block !important;
    }

    /* Pagination Bar */
    .pagination-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      gap: 6px;
      margin: 30px 0 60px 0;
    }

    .page-btn {
      min-width: 38px;
      height: 38px;
      padding: 0 12px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background-color: #ffffff;
      color: var(--text-sub);
      font-family: inherit;
      font-size: 13.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      transition: all 0.15s ease;
    }

    .page-btn:hover:not(:disabled) {
      background-color: #f1f5f9;
      color: var(--text-main);
      border-color: #cbd5e1;
    }

    .page-btn.active {
      background-color: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 2px 6px rgba(79, 70, 229, 0.28);
    }

    .page-btn:disabled {
      opacity: 0.45;
      cursor: not-allowed;
    }

    /* Scroll Top Button */
    .scroll-top-btn {
      position: fixed;
      bottom: 24px;
      right: 24px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #0f172a;
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 4px 14px rgba(15, 23, 42, 0.35);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      cursor: pointer;
      opacity: 0;
      visibility: hidden;
      transition: all 0.2s ease;
      z-index: 99;
    }

    .scroll-top-btn.visible {
      opacity: 1;
      visibility: visible;
    }

    .scroll-top-btn:hover {
      background: var(--primary);
      transform: translateY(-2px);
    }

    /* Responsive */
    @media (max-width: 900px) {
      .columns-container {
        grid-template-columns: 1fr;
        gap: 16px;
      }
      .columns-container::after {
        display: none;
      }
      .sheet-card {
        padding: 16px;
      }
      .options-grid {
        grid-template-columns: 1fr;
      }
    }

    @media print {
      .portal-nav, header.app-header, .status-strip, .pagination-bar, .scroll-top-btn, .btn-toggle-exp-single {
        display: none !important;
      }
      body {
        background: #ffffff;
        color: #000000;
      }
      .sheet-card {
        box-shadow: none;
        border: none;
        padding: 0;
        margin: 0 0 20px 0;
      }
      .explanation-box {
        display: block !important;
      }
      .answer-tag {
        display: inline-flex !important;
      }
    }
  </style>
</head>
<body>

  <!-- Top Navigation Portal Bar -->
  <nav class="portal-nav">
    <div class="portal-nav-inner">
      <div class="portal-links">
        <span style="font-weight: 700; color: #f1f5f9; display: flex; align-items: center; gap: 6px;">
          <i class="fa-solid fa-shapes"></i> সকল প্রশ্নব্যাংক:
        </span>
        <a href="Ict-wizard-NTRCA-313-and-325.html" class="portal-link"><i class="fa-solid fa-laptop-code"></i> ICT Wizard NTRCA</a>
        <a href="Biddabari-NTRCA.html" class="portal-link"><i class="fa-solid fa-graduation-cap"></i> Biddabari-NTRCA (১৯তম)</a>
        <a href="Eminent-Petro-Bangla.html" class="portal-link"><i class="fa-solid fa-fire-flame-curved"></i> Eminent Petro Bangla</a>
        <a href="class 9-10-Computer-GK.html" class="portal-link"><i class="fa-solid fa-desktop"></i> Class 9-10 Computer GK</a>
        <a href="Saif-Sir-NTRCA-Suggestion.html" class="portal-link active"><i class="fa-solid fa-award"></i> Saif Sir NTRCA</a>
        <a href="Ampibian-Suggestion.html" class="portal-link"><i class="fa-solid fa-book-bookmark"></i> Ampibian Suggestion</a>
      </div>
      <div>
        <span style="opacity: 0.85;"><i class="fa-solid fa-file-circle-check"></i> ৩৩৮টি মডেল টেস্ট (৭,২২৫টি প্রশ্ন)</span>
      </div>
    </div>
  </nav>

  <!-- Header Section -->
  <header class="app-header">
    <div class="header-container">
      <div class="header-top">
        <a href="Saif-Sir-NTRCA-Suggestion.html" class="brand-logo" title="Saif Sir NTRCA Suggestion">
          <div class="badge-icon"><i class="fa-solid fa-award"></i></div>
          <span class="brand-name">Saif Sir NTRCA Suggestion</span>
        </a>

        <div class="top-actions">
          <!-- Font Selection -->
          <div class="font-select-wrap">
            <span class="font-icon"><i class="fa-solid fa-font"></i></span>
            <select id="fontSelect" title="ফন্ট পরিবর্তন করুন" aria-label="ফন্ট পরিবর্তন করুন">
              <option value="hind">হিন্দ শিলিগুড়ি (Hind Siliguri)</option>
              <option value="noto-sans">নোতো সান্স (Noto Sans)</option>
              <option value="anek">আনেক বাংলা (Anek Bangla)</option>
              <option value="noto-serif">নোতো সেরিফ (Noto Serif)</option>
            </select>
            <span class="font-arrow"><i class="fa-solid fa-chevron-down"></i></span>
          </div>

          <!-- Practice Button -->
          <button class="btn btn-practice" id="btnTogglePractice" title="অনুশীলন করুন (অপশনে ক্লিক করে উত্তর যাচাই)">
            <span id="practiceIcon"><i class="fa-solid fa-bullseye"></i></span> <span id="practiceText">অনুশীলন করুন</span>
          </button>

          <!-- Show/Hide Answers Toggle -->
          <button class="btn" id="btnToggleAnswers" title="উত্তর দেখুন বা লুকান">
            <span id="ansIcon"><i class="fa-solid fa-eye"></i></span> <span id="ansText">উত্তর দেখুন</span>
          </button>

          <!-- Show/Hide Explanations Toggle -->
          <button class="btn btn-active" id="btnToggleExp" title="ব্যাখ্যা দেখুন বা লুকান">
            <span id="expIcon"><i class="fa-solid fa-lightbulb"></i></span> <span id="expText">ব্যাখ্যা লুকান</span>
          </button>

          <!-- Number Format Toggle -->
          <button class="btn" id="btnToggleNum" title="বাংলা বা ইংরেজি সংখ্যা পরিবর্তন">
            <span><i class="fa-solid fa-arrow-down-1-9"></i></span> <span id="numLangText">সংখ্যা: বাংলা</span>
          </button>

          <!-- Print / PDF -->
          <button class="btn btn-primary" onclick="window.print()" title="প্রিন্ট করুন বা PDF এ সংরক্ষণ করুন">
            <span><i class="fa-solid fa-print"></i></span> <span>প্রিন্ট / PDF</span>
          </button>
        </div>
      </div>

      <!-- Subject Title & Description -->
      <div class="subject-title-area">
        <h1>Saif Sir NTRCA Suggestion (মডেল টেস্ট স্পেশাল)</h1>
        <p><i class="fa-solid fa-book-open-reader"></i> বাংলা, ইংরেজি, সাধারণ জ্ঞান ও গণিত • মোট ৪টি বিষয়, ৩৩৮টি মডেল টেস্ট (৭,২২৫টি প্রশ্ন)</p>
      </div>

      <!-- Subject Tabs Navigation -->
      <div class="subject-nav-tabs" id="subjectNavTabs">
        <button class="subject-tab active" data-subject="all" onclick="selectSubject('all')">
          <i class="fa-solid fa-layer-group"></i> সকল বিষয় (৭,২২৫)
        </button>
        <button class="subject-tab" data-subject="Bangla" onclick="selectSubject('Bangla')">
          <i class="fa-solid fa-book"></i> বাংলা (২,২৩১)
        </button>
        <button class="subject-tab" data-subject="English" onclick="selectSubject('English')">
          <i class="fa-solid fa-language"></i> ইংরেজি (২,০৩৪)
        </button>
        <button class="subject-tab" data-subject="GK" onclick="selectSubject('GK')">
          <i class="fa-solid fa-earth-americas"></i> সাধারণ জ্ঞান (২,২১১)
        </button>
        <button class="subject-tab" data-subject="Math" onclick="selectSubject('Math')">
          <i class="fa-solid fa-calculator"></i> গণিত (৭৪৯)
        </button>
      </div>

      <!-- Filters & Search -->
      <div class="filter-bar">
        <!-- Model Test Selector -->
        <div class="select-wrap">
          <select id="chapterSelect" aria-label="মডেল টেস্ট নির্বাচন করুন">
            <option value="all">সকল মডেল টেস্ট (৭,২২৫টি প্রশ্ন)</option>
          </select>
          <span class="select-arrow"><i class="fa-solid fa-chevron-down"></i></span>
        </div>

        <!-- Search Input -->
        <div class="search-wrap">
          <span class="search-icon"><i class="fa-solid fa-magnifying-glass"></i></span>
          <input type="text" id="searchInput" placeholder="প্রশ্ন, অপশন বা ব্যাখ্যা খুঁজুন..." autocomplete="off">
        </div>

        <!-- Quick Model Test Pills -->
        <div class="pills-scroll" id="pillsContainer"></div>
      </div>

      <!-- Practice Mode Info Banner -->
      <div class="practice-banner" id="practiceBanner">
        <span><i class="fa-solid fa-bullseye"></i> <strong>অনুশীলন মোড সক্রিয়:</strong> যেকোনো প্রশ্নের অপশনে ক্লিক করে তাৎক্ষণিক সঠিক উত্তর ও বিস্তারিত ব্যাখ্যা দেখুন।</span>
        <button class="btn-mini-reset" onclick="resetPracticeAnswers()">অনুশীলন রিসেট</button>
      </div>
    </div>
  </header>

  <!-- Status & Info Strip -->
  <div class="status-strip">
    <div class="stats-info" id="statsInfo">
      মোট প্রশ্ন: <strong>৭,২২৫</strong> টি | প্রদর্শিত: <strong>৭,২২৫</strong> টি
    </div>

    <div class="view-controls">
      <label for="perPageSelect">পৃষ্ঠা প্রতি শিট:</label>
      <select id="perPageSelect" style="padding: 4px 8px; border-radius: 4px; border: 1px solid #cbd5e1; font-family: inherit;">
        <option value="10">১০ টি (৫+৫)</option>
        <option value="20" selected>২০ টি (১০+১০)</option>
        <option value="40">৪০ টি (২০+২০)</option>
        <option value="all">সব প্রশ্ন একসাথে</option>
      </select>
    </div>
  </div>

  <!-- Main Sheets Content -->
  <main class="main-content" id="sheetsContainer"></main>

  <!-- Pagination Controls -->
  <div class="pagination-bar" id="paginationBar"></div>

  <!-- Quick Scroll to Top Button -->
  <button class="scroll-top-btn" id="scrollTopBtn" title="উপরে যান"><i class="fa-solid fa-arrow-up"></i></button>

  <script>
    // Embedded Complete Dataset of All 338 Model Tests
    const chaptersData = %LECTURES_JSON%;

    // State Variables
    let currentSubject = 'all';
    let currentChapter = 'all';
    let searchQuery = '';
    let currentPage = 1;
    let questionsPerSheet = 20;
    let showAnswers = false;
    let showExplanations = true;
    let isPracticeMode = false;
    let practiceAnswers = {};
    let useBengaliNumbers = true;

    const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
    const optLabels = ['(ক)', '(খ)', '(গ)', '(ঘ)'];
    const optLetters = ['ক', 'খ', 'গ', 'ঘ'];
    const letterMap = {'ক': 0, 'খ': 1, 'গ': 2, 'ঘ': 3, 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'a': 0, 'b': 1, 'c': 2, 'd': 3};

    const FONT_FAMILIES = {
      'hind': "'Hind Siliguri', 'Inter', -apple-system, sans-serif",
      'noto-sans': "'Noto Sans Bengali', 'Inter', -apple-system, sans-serif",
      'anek': "'Anek Bangla', 'Inter', -apple-system, sans-serif",
      'noto-serif': "'Noto Serif Bengali', serif"
    };

    function formatMath(text) {
      if (!text) return '';
      let s = String(text).trim();
      if ((s.startsWith("'") && s.endsWith("'")) || (s.startsWith('"') && s.endsWith('"'))) {
        s = s.slice(1, -1).trim();
      }

      if (s.includes('\\\\') || s.includes('oplus') || s.includes('overline') || s.includes('bar{') || s.includes('^') || s.includes('_')) {
        if (window.katex && window.katex.renderToString) {
          try {
            const hasBengali = /[\\u0980-\\u09FF]/.test(s);
            if (!hasBengali) {
              return window.katex.renderToString(s, { throwOnError: false, displayMode: false });
            } else {
              s = s.replace(/(\\\\frac\\{[^{}]+\\}\\{[^{}]+\\}|\\\\sqrt\\{[^{}]+\\}|\\\\overline\\{[^{}]+\\}|\\\\bar\\{[^{}]+\\}|\\\\oplus|\\\\cdot|\\\\times)/g, function(match) {
                try {
                  return window.katex.renderToString(match, { throwOnError: false, displayMode: false });
                } catch(e) {
                  return match;
                }
              });
              return s;
            }
          } catch(e) {}
        }

        s = s.replace(/\\\\bar\\{\\\\bar\\{([^{}]+)\\}\\}/g, '<span class="math-overline"><span class="math-overline">$1</span></span>');
        s = s.replace(/\\\\overline\\{\\\\overline\\{([^{}]+)\\}\\}/g, '<span class="math-overline"><span class="math-overline">$1</span></span>');

        for (let i = 0; i < 4; i++) {
          s = s.replace(/\\\\overline\\{([^{}]+)\\}/g, '<span class="math-overline">$1</span>');
          s = s.replace(/\\\\bar\\{([^{}]+)\\}/g, '<span class="math-overline">$1</span>');
        }

        s = s.replace(/\\\\oplus\\b/g, '<span class="math-sym">⊕</span>');
        s = s.replace(/\\\\cdot\\b/g, '<span class="math-sym">·</span>');
        s = s.replace(/\\\\times\\b/g, '<span class="math-sym">×</span>');
      }

      return s;
    }

    function applyFont(fontKey, save = true) {
      if (!FONT_FAMILIES[fontKey]) fontKey = 'hind';
      document.body.style.fontFamily = FONT_FAMILIES[fontKey];
      const sel = document.getElementById('fontSelect');
      if (sel) sel.value = fontKey;
      if (save) {
        try {
          localStorage.setItem('saif_sir_saved_font', fontKey);
        } catch(e) {}
      }
    }

    function toBn(num) {
      return String(num).replace(/\\d/g, d => bnDigits[d]);
    }

    function formatNumber(num) {
      return useBengaliNumbers ? toBn(num) : String(num);
    }

    function selectSubject(subj) {
      currentSubject = subj;
      currentChapter = 'all';
      currentPage = 1;

      // Update tabs UI
      document.querySelectorAll('#subjectNavTabs .subject-tab').forEach(tab => {
        tab.classList.toggle('active', tab.dataset.subject === subj);
      });

      updateChapterSelectAndPills();
      render();
    }

    function updateChapterSelectAndPills() {
      const chSelect = document.getElementById('chapterSelect');
      const pillsContainer = document.getElementById('pillsContainer');

      // Filter available lectures
      const filteredLectures = currentSubject === 'all' 
        ? chaptersData 
        : chaptersData.filter(l => l.subject === currentSubject);

      const totalSubjQ = filteredLectures.reduce((acc, l) => acc + l.count, 0);

      // Rebuild select options
      chSelect.innerHTML = `<option value="all">সকল মডেল টেস্ট (${formatNumber(totalSubjQ)}টি প্রশ্ন)</option>`;
      filteredLectures.forEach(l => {
        const opt = document.createElement('option');
        opt.value = l.id;
        opt.textContent = `${l.subjectBn} - ${l.title} (${formatNumber(l.count)}টি)`;
        if (l.id === currentChapter) opt.selected = true;
        chSelect.appendChild(opt);
      });

      // Rebuild pills
      pillsContainer.innerHTML = '';
      const allPill = document.createElement('button');
      allPill.className = 'pill' + (currentChapter === 'all' ? ' active' : '');
      allPill.innerHTML = `<i class="fa-solid fa-layer-group"></i> সকল (${formatNumber(totalSubjQ)})`;
      allPill.onclick = () => selectChapter('all');
      pillsContainer.appendChild(allPill);

      filteredLectures.forEach(l => {
        const pill = document.createElement('button');
        pill.className = 'pill' + (l.id === currentChapter ? ' active' : '');
        pill.textContent = `${l.short} (${formatNumber(l.count)})`;
        pill.onclick = () => selectChapter(l.id);
        pillsContainer.appendChild(pill);
      });

      if (!filteredLectures.some(l => l.id === currentChapter)) {
        currentChapter = 'all';
      }
      chSelect.value = currentChapter;
    }

    function selectChapter(chId) {
      currentChapter = chId;
      currentPage = 1;

      const chSelect = document.getElementById('chapterSelect');
      if (chSelect) chSelect.value = chId;

      document.querySelectorAll('#pillsContainer .pill').forEach(p => {
        if (chId === 'all') {
          p.classList.toggle('active', p.textContent.includes('সকল'));
        } else {
          const l = chaptersData.find(x => x.id === chId);
          p.classList.toggle('active', l && p.textContent.startsWith(l.short));
        }
      });

      render();
    }

    function initUI() {
      let savedFont = 'hind';
      try {
        savedFont = localStorage.getItem('saif_sir_saved_font') || 'hind';
      } catch(e) {}
      applyFont(savedFont, false);

      document.getElementById('fontSelect').addEventListener('change', (e) => {
        applyFont(e.target.value, true);
      });

      // Number toggle
      try {
        const savedNum = localStorage.getItem('saif_sir_saved_num_lang');
        if (savedNum !== null) {
          useBengaliNumbers = (savedNum === 'true');
          document.getElementById('numLangText').textContent = useBengaliNumbers ? 'সংখ্যা: বাংলা' : 'সংখ্যা: English';
        }
      } catch(e) {}

      document.getElementById('btnToggleNum').addEventListener('click', () => {
        useBengaliNumbers = !useBengaliNumbers;
        document.getElementById('numLangText').textContent = useBengaliNumbers ? 'সংখ্যা: বাংলা' : 'সংখ্যা: English';
        try {
          localStorage.setItem('saif_sir_saved_num_lang', useBengaliNumbers);
        } catch(e) {}
        updateChapterSelectAndPills();
        render();
      });

      // Answer Toggle
      const btnAns = document.getElementById('btnToggleAnswers');
      btnAns.addEventListener('click', () => {
        showAnswers = !showAnswers;
        btnAns.classList.toggle('btn-active', showAnswers);
        document.getElementById('ansText').textContent = showAnswers ? 'উত্তর লুকান' : 'উত্তর দেখুন';
        document.getElementById('ansIcon').innerHTML = showAnswers ? '<i class="fa-solid fa-eye-slash"></i>' : '<i class="fa-solid fa-eye"></i>';
        document.body.classList.toggle('show-answers', showAnswers);
      });

      // Explanations Toggle
      const btnExp = document.getElementById('btnToggleExp');
      btnExp.addEventListener('click', () => {
        showExplanations = !showExplanations;
        btnExp.classList.toggle('btn-active', showExplanations);
        document.getElementById('expText').textContent = showExplanations ? 'ব্যাখ্যা লুকান' : 'ব্যাখ্যা দেখুন';
        document.getElementById('expIcon').innerHTML = showExplanations ? '<i class="fa-solid fa-lightbulb"></i>' : '<i class="fa-regular fa-lightbulb"></i>';
        document.body.classList.toggle('show-explanations', showExplanations);
      });
      document.body.classList.toggle('show-explanations', showExplanations);

      // Practice Mode Toggle
      const btnPractice = document.getElementById('btnTogglePractice');
      const practiceBanner = document.getElementById('practiceBanner');
      btnPractice.addEventListener('click', () => {
        isPracticeMode = !isPracticeMode;
        btnPractice.classList.toggle('active', isPracticeMode);
        practiceBanner.classList.toggle('active', isPracticeMode);
        document.body.classList.toggle('is-practice', isPracticeMode);
        render();
      });

      // Chapter change
      document.getElementById('chapterSelect').addEventListener('change', (e) => {
        selectChapter(e.target.value);
      });

      // Search
      document.getElementById('searchInput').addEventListener('input', (e) => {
        searchQuery = e.target.value.trim().toLowerCase();
        currentPage = 1;
        render();
      });

      // Per Page
      document.getElementById('perPageSelect').addEventListener('change', (e) => {
        const val = e.target.value;
        questionsPerSheet = val === 'all' ? 999999 : parseInt(val, 10);
        currentPage = 1;
        render();
      });

      // Scroll top button
      const topBtn = document.getElementById('scrollTopBtn');
      window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
          topBtn.classList.add('visible');
        } else {
          topBtn.classList.remove('visible');
        }
      });
      topBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });

      updateChapterSelectAndPills();
      render();
    }

    function resetPracticeAnswers() {
      practiceAnswers = {};
      render();
    }

    function render() {
      const container = document.getElementById('sheetsContainer');
      container.innerHTML = '';

      let lecturesToRender = chaptersData;
      if (currentSubject !== 'all') {
        lecturesToRender = lecturesToRender.filter(l => l.subject === currentSubject);
      }
      if (currentChapter !== 'all') {
        lecturesToRender = lecturesToRender.filter(l => l.id === currentChapter);
      }

      // Collect questions
      let allFilteredQuestions = [];
      lecturesToRender.forEach(lecture => {
        lecture.questions.forEach((q, qIndex) => {
          let matchesSearch = true;
          if (searchQuery) {
            const inQ = (q.question || '').toLowerCase().includes(searchQuery);
            const inOpts = (q.options || []).some(o => o.toLowerCase().includes(searchQuery));
            const inExp = (q.explanation || '').toLowerCase().includes(searchQuery);
            matchesSearch = inQ || inOpts || inExp;
          }

          if (matchesSearch) {
            allFilteredQuestions.push({
              ...q,
              dispNum: allFilteredQuestions.length + 1,
              lectureRef: lecture,
              uid: `${lecture.id}_${q.id}_${qIndex}`
            });
          }
        });
      });

      const totalItems = allFilteredQuestions.length;
      document.getElementById('statsInfo').innerHTML = 
        `মোট প্রশ্ন: <strong>${formatNumber(totalItems)}</strong> টি | প্রদর্শিত: <strong>${formatNumber(totalItems)}</strong> টি`;

      if (totalItems === 0) {
        container.innerHTML = `
          <div style="text-align: center; padding: 60px 20px; background: #ffffff; border-radius: 12px; border: 1px dashed #cbd5e1;">
            <i class="fa-solid fa-folder-open" style="font-size: 40px; color: #94a3b8; margin-bottom: 12px;"></i>
            <h3 style="font-size: 18px; color: #334155;">কোনো প্রশ্ন পাওয়া যায়নি!</h3>
            <p style="font-size: 14px; color: #64748b; margin-top: 4px;">অনুগ্রহ করে আপনার ফিল্টার বা সার্চ কি-ওয়ার্ড পরিবর্তন করুন।</p>
          </div>
        `;
        renderPagination(0);
        return;
      }

      // Pagination slice
      const totalPages = Math.ceil(totalItems / questionsPerSheet);
      if (currentPage > totalPages) currentPage = 1;

      const startIndex = (currentPage - 1) * questionsPerSheet;
      const pagedQuestions = allFilteredQuestions.slice(startIndex, startIndex + questionsPerSheet);

      // Create sheet card
      const sheetCard = document.createElement('div');
      sheetCard.className = 'sheet-card';

      const sheetHeader = document.createElement('div');
      sheetHeader.className = 'sheet-header';

      let headerTitleText = 'মডেল টেস্ট প্রশ্নগুচ্ছ';
      let headerBadgeText = '';
      if (currentChapter !== 'all') {
        const activeLec = chaptersData.find(l => l.id === currentChapter);
        if (activeLec) {
          headerTitleText = `${activeLec.subjectBn} - ${activeLec.title}`;
          headerBadgeText = `${formatNumber(activeLec.count)}টি প্রশ্ন`;
        }
      } else if (currentSubject !== 'all') {
        const subBn = currentSubject === 'Bangla' ? 'বাংলা' : currentSubject === 'English' ? 'ইংরেজি' : currentSubject === 'GK' ? 'সাধারণ জ্ঞান' : 'গণিত';
        headerTitleText = `${subBn} বিষয়ের মডেল টেস্টসমূহ`;
        headerBadgeText = `${formatNumber(totalItems)}টি প্রশ্ন`;
      } else {
        headerBadgeText = `পৃষ্ঠা ${formatNumber(currentPage)} / ${formatNumber(totalPages)}`;
      }

      sheetHeader.innerHTML = `
        <div class="sheet-title">
          <i class="fa-solid fa-file-signature" style="color: var(--primary);"></i>
          <span>${headerTitleText}</span>
          ${headerBadgeText ? `<span class="sheet-title-badge">${headerBadgeText}</span>` : ''}
        </div>
        <div class="sheet-count">
          প্রদর্শিত হচ্ছে: <strong>${formatNumber(startIndex + 1)}</strong> - <strong>${formatNumber(Math.min(startIndex + questionsPerSheet, totalItems))}</strong> (মোট: ${formatNumber(totalItems)})
        </div>
      `;
      sheetCard.appendChild(sheetHeader);

      // Two columns layout
      const columnsContainer = document.createElement('div');
      columnsContainer.className = 'columns-container';

      const leftCol = document.createElement('div');
      leftCol.className = 'column-half';

      const rightCol = document.createElement('div');
      rightCol.className = 'column-half';

      const midPoint = Math.ceil(pagedQuestions.length / 2);
      pagedQuestions.forEach((q, idx) => {
        const qNode = createQuestionNode(q);
        if (idx < midPoint) {
          leftCol.appendChild(qNode);
        } else {
          rightCol.appendChild(qNode);
        }
      });

      columnsContainer.appendChild(leftCol);
      columnsContainer.appendChild(rightCol);
      sheetCard.appendChild(columnsContainer);
      container.appendChild(sheetCard);

      renderPagination(totalPages);
    }

    function createQuestionNode(q) {
      const qBox = document.createElement('div');
      qBox.className = 'question-block';
      qBox.id = `q_${q.uid}`;

      // Metadata badges row
      const metaRow = document.createElement('div');
      metaRow.className = 'meta-badges-row';

      const subBadge = document.createElement('span');
      subBadge.className = 'sec-badge subject-badge';
      subBadge.innerHTML = `<i class="fa-solid ${q.lectureRef.subjectIcon}"></i> ${q.lectureRef.subjectBn}`;
      metaRow.appendChild(subBadge);

      const lecBadge = document.createElement('span');
      lecBadge.className = 'sec-badge';
      lecBadge.innerHTML = `<i class="fa-solid fa-file-lines"></i> ${q.lectureRef.title}`;
      metaRow.appendChild(lecBadge);

      qBox.appendChild(metaRow);

      // Question Title
      const titleDiv = document.createElement('div');
      titleDiv.className = 'question-title';

      const qNumSpan = document.createElement('span');
      qNumSpan.className = 'q-number';
      qNumSpan.textContent = `${formatNumber(q.dispNum)}. `;

      const qTextSpan = document.createElement('span');
      qTextSpan.className = 'q-text';
      qTextSpan.innerHTML = formatMath(q.question);

      titleDiv.appendChild(qNumSpan);
      titleDiv.appendChild(qTextSpan);
      qBox.appendChild(titleDiv);

      // Options
      // Check multiple answers e.g. 'খ+গ'
      let correctIndices = [];
      const ansTrim = (q.answer || '').trim();
      if (ansTrim.includes('+')) {
        const parts = ansTrim.split('+');
        parts.forEach(p => {
          const trimmedP = p.trim();
          if (letterMap[trimmedP] !== undefined) correctIndices.push(letterMap[trimmedP]);
        });
      } else if (letterMap[ansTrim] !== undefined) {
        correctIndices.push(letterMap[ansTrim]);
      } else {
        // match against options text
        const foundIdx = q.options.indexOf(ansTrim);
        if (foundIdx !== -1) correctIndices.push(foundIdx);
      }

      const selectedIndex = practiceAnswers[q.uid];
      if (selectedIndex !== undefined) {
        qBox.classList.add('practice-answered');
      }

      if (q.options && q.options.length > 0) {
        const optsGrid = document.createElement('div');
        optsGrid.className = 'options-grid';

        q.options.forEach((optText, optIdx) => {
          const cell = document.createElement('div');
          cell.className = 'option-cell';

          if (correctIndices.includes(optIdx)) {
            cell.classList.add('is-correct');
          }

          if (isPracticeMode && selectedIndex !== undefined) {
            if (correctIndices.includes(selectedIndex)) {
              if (optIdx === selectedIndex) {
                cell.classList.add('practice-correct');
              }
            } else {
              if (optIdx === selectedIndex) {
                cell.classList.add('practice-wrong');
              }
              if (correctIndices.includes(optIdx)) {
                cell.classList.add('practice-revealed');
              }
            }
          }

          cell.onclick = () => {
            if (!isPracticeMode) return;
            practiceAnswers[q.uid] = optIdx;
            render();
          };

          const labelSpan = document.createElement('span');
          labelSpan.className = 'opt-label';
          labelSpan.textContent = optLabels[optIdx] || `(${optIdx + 1})`;

          const textSpan = document.createElement('span');
          textSpan.className = 'opt-text';
          textSpan.innerHTML = formatMath(optText);

          cell.appendChild(labelSpan);
          cell.appendChild(textSpan);
          optsGrid.appendChild(cell);
        });

        qBox.appendChild(optsGrid);
      }

      // Answer row
      const ansRow = document.createElement('div');
      ansRow.className = 'answer-row';

      const ansTag = document.createElement('div');
      ansTag.className = 'answer-tag';
      let ansDisplay = q.answer || 'সঠিক উত্তর দেওয়া নেই';
      if (ansDisplay === '-') {
        ansDisplay = '- (সঠিক উত্তর দেওয়া নেই বা প্রশ্নটি বাতিল)';
      }
      ansTag.innerHTML = `<i class="fa-solid fa-circle-check"></i> সঠিক উত্তর: <strong>${ansDisplay}</strong>`;
      ansRow.appendChild(ansTag);

      // Explanation
      let expBox = null;
      if (q.explanation && q.explanation.trim() !== '') {
        expBox = document.createElement('div');
        expBox.className = 'explanation-box';
        expBox.id = `exp_${q.uid}`;
        expBox.innerHTML = `
          <div class="exp-badge"><i class="fa-solid fa-lightbulb"></i> ব্যাখ্যা:</div>
          <div class="exp-body">${formatMath(q.explanation)}</div>
        `;

        const btnExpSingle = document.createElement('button');
        btnExpSingle.className = 'btn-toggle-exp-single';
        btnExpSingle.innerHTML = `<i class="fa-solid fa-lightbulb"></i> ব্যাখ্যা`;
        btnExpSingle.title = 'ব্যাখ্যা দেখুন বা লুকান';
        btnExpSingle.onclick = (e) => {
          e.stopPropagation();
          const isForced = expBox.classList.toggle('force-visible');
          btnExpSingle.innerHTML = isForced 
            ? `<i class="fa-solid fa-circle-xmark"></i> ব্যাখ্যা বন্ধ` 
            : `<i class="fa-solid fa-lightbulb"></i> ব্যাখ্যা`;
        };
        ansRow.appendChild(btnExpSingle);
      }

      qBox.appendChild(ansRow);
      if (expBox) qBox.appendChild(expBox);

      return qBox;
    }

    function renderPagination(totalPages) {
      const bar = document.getElementById('paginationBar');
      if (totalPages <= 1) {
        bar.innerHTML = '';
        return;
      }

      let html = '';
      html += `<button class="page-btn" ${currentPage === 1 ? 'disabled' : ''} onclick="goToPage(${currentPage - 1})"><i class="fa-solid fa-chevron-left"></i> পূর্ববর্তী</button>`;

      let startP = Math.max(1, currentPage - 2);
      let endP = Math.min(totalPages, currentPage + 2);

      if (startP > 1) {
        html += `<button class="page-btn" onclick="goToPage(1)">${formatNumber(1)}</button>`;
        if (startP > 2) html += `<span style="padding: 0 4px; color: #94a3b8;">...</span>`;
      }

      for (let p = startP; p <= endP; p++) {
        html += `<button class="page-btn ${p === currentPage ? 'active' : ''}" onclick="goToPage(${p})">${formatNumber(p)}</button>`;
      }

      if (endP < totalPages) {
        if (endP < totalPages - 1) html += `<span style="padding: 0 4px; color: #94a3b8;">...</span>`;
        html += `<button class="page-btn" onclick="goToPage(${totalPages})">${formatNumber(totalPages)}</button>`;
      }

      html += `<button class="page-btn" ${currentPage === totalPages ? 'disabled' : ''} onclick="goToPage(${currentPage + 1})">পরবর্তী <i class="fa-solid fa-chevron-right"></i></button>`;
      bar.innerHTML = html;
    }

    function goToPage(p) {
      currentPage = p;
      render();
      const container = document.getElementById('sheetsContainer');
      if (container) {
        const topPos = container.getBoundingClientRect().top + window.scrollY - 15;
        window.scrollTo({ top: topPos, behavior: 'smooth' });
      } else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    window.addEventListener('DOMContentLoaded', initUI);
  </script>
</body>
</html>
"""

lectures_json = json.dumps(lectures, ensure_ascii=False)
final_html = html_template.replace("%LECTURES_JSON%", lectures_json)

out_file = "Saif-Sir-NTRCA-Suggestion.html"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated {out_file} successfully! File size: {os.path.getsize(out_file):,} bytes")
