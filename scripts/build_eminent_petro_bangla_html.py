import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

epb_dir = r"JSON Data/Eminent Petro Bangla"
files = sorted([f for f in os.listdir(epb_dir) if f.endswith('.json')])

exams = []
total_q = 0

for i, fname in enumerate(files):
    name_clean = os.path.splitext(fname)[0]
    # Clean short title
    short_title = name_clean
    if ' - ' in short_title:
        parts = short_title.split(' - ')
        short_title = parts[0].strip() + ' - ' + parts[1].strip()
    if len(short_title) > 42:
        short_title = short_title[:40] + '...'

    fpath = os.path.join(epb_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as fp:
        raw_list = json.load(fp)

    q_list = []
    for q_idx, item in enumerate(raw_list):
        q_id = item.get('id', q_idx + 1)
        q_text = str(item.get('question', '')).strip()
        opts = item.get('options', [])
        # Ensure 4 options or whatever exists
        clean_opts = [str(o).strip() for o in opts]
        ans = str(item.get('answer', '')).strip()
        exp = str(item.get('explanation', '')).strip()

        q_list.append({
            'id': q_id,
            'question': q_text,
            'options': clean_opts,
            'answer': ans,
            'explanation': exp
        })

    total_q += len(q_list)
    exams.append({
        'id': f'exam_{i+1}',
        'title': name_clean,
        'short': short_title,
        'filename': fname,
        'count': len(q_list),
        'questions': q_list
    })

print(f"Total exams: {len(exams)}, Total questions: {total_q}")

# Now build the full HTML content
html_template = """<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Eminent Petro Bangla - নিয়োগ পরীক্ষার প্রশ্নব্যাংক</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Bangla:wght@400;500;600;700&family=Hind+Siliguri:wght@400;500;600;700&family=Noto+Sans+Bengali:wght@400;500;600;700&family=Noto+Serif+Bengali:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <!-- Font Awesome 6 Icons (Local Driver) -->
  <link rel="stylesheet" href="drivers/fontawesome/css/all.min.css">
  <!-- KaTeX Library for Math & Formula Rendering (Local Driver) -->
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
      --primary: #ea580c;
      --primary-hover: #c2410c;
      --primary-light: #fff7ed;
      --primary-border: #fdba74;
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
      gap: 12px;
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
      color: #fb923c;
      background: rgba(234, 88, 12, 0.15);
      font-weight: 700;
    }

    /* Header Section */
    header.app-header {
      position: relative;
      background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
      border-bottom: 1px solid #e2e8f0;
      border-top: 3.5px solid #ea580c;
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
      background: linear-gradient(135deg, #c2410c 0%, #ea580c 55%, #f97316 100%);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 10px;
      font-size: 19px;
      box-shadow: 0 4px 12px rgba(234, 88, 12, 0.32);
      border: 1px solid rgba(255, 255, 255, 0.25);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      flex-shrink: 0;
    }

    .badge-icon:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 6px 18px rgba(234, 88, 12, 0.42);
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
      font-size: 19px;
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: -0.3px;
      margin: 0;
      line-height: 1.3;
    }

    .subject-title-area p {
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 500;
      margin: 0;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .top-actions {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
      justify-content: flex-end;
    }

    /* Font Selector UI */
    .font-select-wrap {
      position: relative;
      display: inline-flex;
      align-items: center;
    }

    .font-select-wrap select {
      appearance: none;
      -webkit-appearance: none;
      padding: 6px 24px 6px 26px;
      background-color: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 7px;
      font-size: 12px;
      font-weight: 600;
      color: #1e293b;
      cursor: pointer;
      font-family: inherit;
      outline: none;
      transition: all 0.18s ease;
      box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
    }

    .font-select-wrap select:hover {
      background-color: #f8fafc;
      border-color: #cbd5e1;
    }

    .font-select-wrap select:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(234, 88, 12, 0.15);
    }

    .font-icon {
      position: absolute;
      left: 8px;
      pointer-events: none;
      font-size: 11.5px;
      color: #64748b;
    }

    .font-arrow {
      position: absolute;
      right: 8px;
      pointer-events: none;
      font-size: 9px;
      color: #94a3b8;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 5.5px;
      padding: 6px 11px;
      font-size: 12px;
      font-weight: 600;
      border-radius: 7px;
      border: 1px solid var(--border-color);
      background-color: #ffffff;
      color: var(--text-sub);
      cursor: pointer;
      transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1);
      user-select: none;
      font-family: inherit;
      box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
      white-space: nowrap;
    }

    .btn:hover {
      background-color: #f8fafc;
      border-color: #cbd5e1;
      color: var(--text-main);
      transform: translateY(-1px);
      box-shadow: 0 3px 8px rgba(15, 23, 42, 0.06);
    }

    .btn:active {
      transform: translateY(0);
      box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
    }

    .btn-active {
      background: linear-gradient(180deg, #fff7ed 0%, #ffedd5 100%) !important;
      border-color: #fdba74 !important;
      color: #c2410c !important;
      box-shadow: 0 2px 6px rgba(234, 88, 12, 0.15) !important;
    }

    .btn-primary {
      background: linear-gradient(135deg, #ea580c, #c2410c);
      border-color: #9a3412;
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(234, 88, 12, 0.28);
    }

    .btn-primary:hover {
      background: linear-gradient(135deg, #c2410c, #9a3412);
      border-color: #7c2d12;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(234, 88, 12, 0.38);
      color: #ffffff;
    }

    .btn-practice {
      border-color: #fde68a;
      color: #b45309;
      background: linear-gradient(180deg, #ffffff 0%, #fffbeb 100%);
    }

    .btn-practice:hover {
      background: #fef3c7;
      border-color: #f59e0b;
      color: #92400e;
    }

    .btn-practice.active {
      background: linear-gradient(135deg, #f59e0b, #d97706) !important;
      border-color: #b45309 !important;
      color: #ffffff !important;
      box-shadow: 0 3px 10px rgba(217, 119, 6, 0.35);
    }

    /* Filter Bar */
    .filter-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 12px;
      padding-top: 2px;
    }

    .select-wrap {
      position: relative;
      flex-shrink: 0;
    }

    .select-wrap select {
      appearance: none;
      -webkit-appearance: none;
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 8px 36px 8px 14px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text-main);
      cursor: pointer;
      outline: none;
      min-width: 320px;
      max-width: 450px;
      font-family: inherit;
      box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
      transition: all 0.18s ease;
    }

    .select-wrap select:hover {
      border-color: #cbd5e1;
      background: #f8fafc;
    }

    .select-wrap select:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(234, 88, 12, 0.15);
    }

    .select-arrow {
      position: absolute;
      right: 14px;
      top: 50%;
      transform: translateY(-50%);
      pointer-events: none;
      font-size: 11px;
      color: var(--text-muted);
    }

    .search-wrap {
      position: relative;
      flex-grow: 1;
      min-width: 240px;
    }

    .search-wrap input {
      width: 100%;
      padding: 8px 14px 8px 36px;
      font-size: 13.5px;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      background: #ffffff;
      outline: none;
      transition: all 0.18s ease;
      font-family: inherit;
      box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
    }

    .search-wrap input:hover {
      border-color: #cbd5e1;
    }

    .search-wrap input:focus {
      background: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(234, 88, 12, 0.15);
    }

    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 14px;
      pointer-events: none;
    }

    /* Quick Exam Pills */
    .pills-scroll {
      display: flex;
      flex-wrap: wrap;
      gap: 7px;
      width: 100%;
      padding-top: 4px;
      max-height: 125px;
      overflow-y: auto;
      scrollbar-width: thin;
    }

    .pill {
      font-size: 12px;
      font-weight: 500;
      padding: 5px 12px;
      border-radius: 20px;
      background: #ffffff;
      color: var(--text-sub);
      border: 1px solid #e2e8f0;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.18s ease;
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
      background: linear-gradient(135deg, #1e293b, #0f172a);
      color: #ffffff;
      border-color: #0f172a;
      font-weight: 600;
      box-shadow: 0 3px 10px rgba(15, 23, 42, 0.22);
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

    body.practice-mode .practice-banner {
      display: flex;
    }

    .btn-mini-reset {
      background: #ffffff;
      border: 1px solid #f59e0b;
      color: #b45309;
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.15s ease;
    }

    .btn-mini-reset:hover {
      background: #fef3c7;
      border-color: #d97706;
    }

    /* Status Strip */
    .status-strip {
      max-width: 1300px;
      margin: 14px auto 0;
      padding: 0 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 13px;
      color: var(--text-muted);
    }

    .view-controls {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Main Container & Exam Sheet Card */
    .main-content {
      max-width: 1300px;
      margin: 14px auto 40px;
      padding: 0 16px;
    }

    .exam-sheet {
      background-color: var(--card-bg);
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      box-shadow: var(--shadow-sheet);
      padding: 24px 26px;
      margin-bottom: 30px;
      position: relative;
    }

    .sheet-meta-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2px solid #0f172a;
      padding-bottom: 8px;
      margin-bottom: 18px;
      font-size: 14px;
      font-weight: 700;
      color: #0f172a;
    }

    .sheet-chapter-title {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 15px;
    }

    .sheet-page-indicator {
      font-size: 12.5px;
      font-weight: 600;
      color: #64748b;
    }

    /* 2-Column Layout */
    .columns-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      column-gap: 0;
    }

    .column-left {
      padding-right: 20px;
      border-right: 1px dotted var(--dotted-line);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .column-right {
      padding-left: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* Single Question Block */
    .question-block {
      display: flex;
      flex-direction: column;
      gap: 6px;
      padding-bottom: 12px;
      border-bottom: 1px solid #f1f5f9;
      break-inside: avoid;
      transition: background-color 0.2s ease;
    }

    .question-block:last-child {
      border-bottom: none;
      padding-bottom: 0;
    }

    .question-title {
      font-size: 15px;
      font-weight: 700;
      line-height: 1.42;
      color: #0f172a;
      display: flex;
      align-items: baseline;
      gap: 4px;
    }

    .q-number {
      font-weight: 700;
      color: #0f172a;
      flex-shrink: 0;
    }

    .q-text {
      flex-grow: 1;
      word-break: break-word;
    }

    /* Options 2x2 Grid Layout */
    .options-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      column-gap: 14px;
      row-gap: 4px;
      margin-top: 2px;
    }

    .option-cell {
      display: flex;
      align-items: baseline;
      gap: 6px;
      font-size: 14.5px;
      line-height: 1.45;
      color: #334155;
      padding: 4px 6px;
      border-radius: 5px;
      border: 1px solid transparent;
      user-select: text;
      transition: background-color 0.15s ease, border-color 0.15s ease;
    }

    .opt-label {
      font-weight: 700;
      color: #1e293b;
      flex-shrink: 0;
      min-width: 20px;
    }

    .opt-text {
      font-weight: 400;
      color: #334155;
      word-break: break-word;
    }

    /* Math Formulas */
    .math-overline {
      border-top: 2px solid currentColor;
      padding-top: 1px;
      display: inline-block;
      line-height: 1.05;
      letter-spacing: 0.5px;
      vertical-align: baseline;
    }

    .math-sym {
      font-style: normal;
      font-size: 1.15em;
      line-height: 1;
      vertical-align: -1px;
      margin: 0 2px;
      display: inline-block;
      font-family: 'Segoe UI Symbol', 'Cambria Math', sans-serif;
    }

    .katex {
      font-size: 1.05em !important;
    }

    /* Practice Mode Option Interaction */
    body.practice-mode .option-cell {
      cursor: pointer;
      user-select: none;
    }

    body.practice-mode .option-cell:hover {
      background-color: #f1f5f9;
      border-color: #cbd5e1;
    }

    .option-cell.practice-correct {
      background-color: var(--success-light) !important;
      border-color: var(--success) !important;
    }

    .option-cell.practice-correct .opt-label,
    .option-cell.practice-correct .opt-text {
      color: #15803d !important;
      font-weight: 600;
    }

    .option-cell.practice-wrong {
      background-color: var(--danger-light) !important;
      border-color: var(--danger) !important;
    }

    .option-cell.practice-wrong .opt-label,
    .option-cell.practice-wrong .opt-text {
      color: #b91c1c !important;
    }

    .option-cell.practice-revealed {
      background-color: #ecfdf5 !important;
      border: 1px dashed var(--success) !important;
    }

    .option-cell.practice-revealed .opt-label,
    .option-cell.practice-revealed .opt-text {
      color: #15803d !important;
      font-weight: 600;
    }

    /* Show Answers Highlighting */
    .show-answers .option-cell.is-correct {
      background-color: #f0fdf4;
      border-color: #86efac;
    }

    .show-answers .option-cell.is-correct .opt-label,
    .show-answers .option-cell.is-correct .opt-text {
      color: #166534;
      font-weight: 600;
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

    .show-answers .answer-tag {
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

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
      background: #fff7ed;
      border: 1px solid #fed7aa;
      color: #c2410c;
      font-size: 11.5px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: inherit;
    }

    .btn-toggle-exp-single:hover {
      background: #ffedd5;
      border-color: #fdba74;
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
      background: #fffaf5;
      border: 1px solid #ffedd5;
      border-left: 3.5px solid #ea580c;
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
      color: #c2410c;
      font-size: 13px;
      margin-bottom: 2px;
    }

    .exp-body {
      color: #1e293b;
      word-break: break-word;
      white-space: pre-line;
    }

    .show-explanations .explanation-box {
      display: block;
    }

    .question-block.practice-answered .explanation-box {
      display: block;
    }

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
      padding: 0 10px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      font-weight: 600;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background: #fff;
      color: var(--text-sub);
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: inherit;
    }

    .page-btn:hover:not(:disabled) {
      background: #f8fafc;
      border-color: #cbd5e1;
    }

    .page-btn.active {
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
    }

    .page-btn:disabled {
      opacity: 0.45;
      cursor: not-allowed;
    }

    .empty-state {
      text-align: center;
      padding: 60px 20px;
      background: #fff;
      border-radius: 8px;
      border: 1px dashed #cbd5e1;
      color: var(--text-muted);
    }

    .empty-icon {
      font-size: 40px;
      margin-bottom: 12px;
      color: #cbd5e1;
    }

    .scroll-top-btn {
      position: fixed;
      bottom: 24px;
      right: 24px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #1e293b;
      color: #ffffff;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
      transition: transform 0.2s ease, opacity 0.2s ease;
      opacity: 0;
      pointer-events: none;
      z-index: 999;
    }

    .scroll-top-btn.visible {
      opacity: 1;
      pointer-events: auto;
    }

    .scroll-top-btn:hover {
      transform: translateY(-3px);
      background: #ea580c;
    }

    /* Print Styles */
    @media print {
      .portal-nav,
      header.app-header,
      .status-strip,
      .pagination-bar,
      .scroll-top-btn,
      .practice-banner,
      .btn-toggle-exp-single {
        display: none !important;
      }

      body {
        background: #ffffff !important;
        color: #000000 !important;
        font-size: 13.5px !important;
      }

      .main-content {
        max-width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
      }

      .exam-sheet {
        box-shadow: none !important;
        border: none !important;
        padding: 10mm 12mm !important;
        margin: 0 0 20mm 0 !important;
        page-break-after: always;
        break-after: page;
      }

      .columns-container {
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
      }

      .column-left {
        border-right: 1px dotted #666 !important;
        padding-right: 15px !important;
      }

      .column-right {
        padding-left: 15px !important;
      }

      .explanation-box {
        background: #ffffff !important;
        border: 1px solid #ccc !important;
        border-left: 2px solid #000 !important;
      }
    }

    /* Mobile Responsive */
    @media (max-width: 768px) {
      .header-container {
        padding: 12px 14px;
      }

      .columns-container {
        grid-template-columns: 1fr;
      }

      .column-left {
        border-right: none;
        padding-right: 0;
        border-bottom: 2px dashed var(--dotted-line);
        padding-bottom: 20px;
        margin-bottom: 20px;
      }

      .column-right {
        padding-left: 0;
      }

      .options-grid {
        grid-template-columns: 1fr;
      }

      .exam-sheet {
        padding: 16px 14px;
      }

      .search-wrap input {
        width: 100%;
      }

      .select-wrap select {
        min-width: 100%;
        width: 100%;
      }
    }

    @media (max-width: 1120px) {
      .brand-name {
        font-size: 17px;
      }
      .subject-title-area h1 {
        font-size: 17px;
      }
      .btn, .font-select-wrap select {
        padding: 5px 8px;
        font-size: 11.5px;
        gap: 4px;
      }
    }

    @media (max-width: 920px) {
      .header-top {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
      }
      .top-actions {
        width: 100%;
        justify-content: flex-start;
      }
    }
  </style>
</head>
<body class="show-explanations">

  <!-- Top Navigation Portal Bar -->
  <nav class="portal-nav">
    <div class="portal-nav-inner">
      <div class="portal-links">
        <span style="font-weight: 700; color: #f1f5f9; display: flex; align-items: center; gap: 6px;">
          <i class="fa-solid fa-shapes"></i> সকল প্রশ্নব্যাংক:
        </span>
        <a href="Eminent-Petro-Bangla.html" class="portal-link active"><i class="fa-solid fa-fire-flame-curved"></i> Eminent Petro Bangla</a>
        <a href="Biddabari-NTRCA.html" class="portal-link"><i class="fa-solid fa-graduation-cap"></i> Biddabari-NTRCA (১৯তম)</a>
        <a href="Ict-wizard-NTRCA-313-and-325.html" class="portal-link"><i class="fa-solid fa-laptop-code"></i> ICT Wizard NTRCA</a>
        <a href="class 9-10-Computer-GK.html" class="portal-link"><i class="fa-solid fa-desktop"></i> Class 9-10 Computer GK</a>
      </div>
      <div>
        <span style="opacity: 0.85;"><i class="fa-solid fa-file-circle-check"></i> মোট ১,৯২২টি এমসিকিউ</span>
      </div>
    </div>
  </nav>

  <!-- Header Section -->
  <header class="app-header">
    <div class="header-container">
      <div class="header-top">
        <a href="Eminent-Petro-Bangla.html" class="brand-logo" title="Eminent Petro Bangla">
          <div class="badge-icon"><i class="fa-solid fa-fire-flame-curved"></i></div>
          <span class="brand-name">Eminent Petro Bangla</span>
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
        <h1>Eminent Petro Bangla - নিয়োগ পরীক্ষার প্রশ্নব্যাংক</h1>
        <p><i class="fa-solid fa-oil-well"></i> পেট্রোবাংলা, বাপেক্স, তিতাস, বাখরাবাদ, ডেসকো, নেসকো ও বিআরইবি • মোট ৪৩টি পরীক্ষা (১,৯২২টি প্রশ্ন)</p>
      </div>

      <!-- Filters & Search -->
      <div class="filter-bar">
        <div class="select-wrap">
          <select id="chapterSelect" aria-label="পরীক্ষা নির্বাচন করুন">
            <option value="all">সকল পরীক্ষা (১,৯২২টি প্রশ্ন)</option>
          </select>
          <span class="select-arrow"><i class="fa-solid fa-chevron-down"></i></span>
        </div>

        <div class="search-wrap">
          <span class="search-icon"><i class="fa-solid fa-magnifying-glass"></i></span>
          <input type="text" id="searchInput" placeholder="প্রশ্ন, অপশন বা ব্যাখ্যা খুঁজুন..." autocomplete="off">
        </div>

        <!-- Quick Chapter / Exam Pills -->
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
      মোট প্রশ্ন: <strong>১,৯২২</strong> টি | প্রদর্শিত: <strong>১,৯২২</strong> টি
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
    // Embedded Complete Dataset of All 43 Exams (with Explanations)
    const chaptersData = %EXAMS_JSON%;

    // State Variables
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
    const optLabels = ['ক', 'খ', 'গ', 'ঘ'];
    const optLettersBn = ['ক', 'খ', 'গ', 'ঘ'];
    const optLettersEn = ['A', 'B', 'C', 'D'];

    const FONT_FAMILIES = {
      'hind': "'Hind Siliguri', 'Inter', -apple-system, sans-serif",
      'noto-sans': "'Noto Sans Bengali', 'Inter', -apple-system, sans-serif",
      'anek': "'Anek Bangla', 'Inter', -apple-system, sans-serif",
      'noto-serif': "'Noto Serif Bengali', serif"
    };

    // Helper: Logic & Math Formula Formatter
    function formatMath(text) {
      if (!text) return '';
      let s = String(text).trim();
      if ((s.startsWith("'") && s.endsWith("'")) || (s.startsWith('"') && s.endsWith('"'))) {
        s = s.slice(1, -1).trim();
      }

      if (s.includes('\\\\') || s.includes('oplus') || s.includes('overline') || s.includes('bar{')) {
        if (window.katex && window.katex.renderToString) {
          try {
            const hasBengali = /[\\u0980-\\u09FF]/.test(s);
            if (!hasBengali) {
              return window.katex.renderToString(s, { throwOnError: false, displayMode: false });
            } else {
              s = s.replace(/(\\\\overline\\{[^{}]+\\}|\\\\bar\\{[^{}]+\\}|\\\\oplus|\\\\cdot)/g, function(match) {
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
          localStorage.setItem('epb_saved_font', fontKey);
        } catch(e) {}
      }
    }

    function toBn(num) {
      return String(num).replace(/\\d/g, d => bnDigits[d]);
    }

    function formatNumber(num) {
      return useBengaliNumbers ? toBn(num) : String(num);
    }

    function cleanQuestionText(text) {
      if (!text) return '';
      return String(text).replace(/^[০-৯\\d]+[\\.\\)]\\s+/, '').trim();
    }

    function cleanOptionText(text) {
      if (!text) return '';
      return String(text).replace(/^(\\([ক-ঘa-dA-D]\\)|[ক-ঘ][\\)\\.\\-–—:]\\s*|[a-dA-D]\\)\\s*|[a-dA-D]\\.\\s+)/, '').trim();
    }

    // Robust answer index detector supporting Bengali, English, and text matching
    function getAnswerIndex(q) {
      if (!q || !q.options || !q.options.length) return -1;
      const rawAns = (q.answer !== undefined && q.answer !== null ? String(q.answer) : '').trim();
      if (!rawAns) return -1;

      // 1. Direct letter matching
      const bnIdx = optLettersBn.indexOf(rawAns);
      if (bnIdx !== -1) return bnIdx;

      const enIdx = optLettersEn.indexOf(rawAns.toUpperCase());
      if (enIdx !== -1) return enIdx;

      // 2. Starts with letter like A., B), ক.
      if (rawAns.length > 0) {
        const fBn = optLettersBn.indexOf(rawAns.charAt(0));
        if (fBn !== -1 && (rawAns.length === 1 || /^[\\.\\)\\:\\s\\-]/.test(rawAns.slice(1)))) return fBn;

        const fEn = optLettersEn.indexOf(rawAns.charAt(0).toUpperCase());
        if (fEn !== -1 && (rawAns.length === 1 || /^[\\.\\)\\:\\s\\-]/.test(rawAns.slice(1)))) return fEn;
      }

      // 3. Match against options
      const cleanRaw = cleanOptionText(rawAns).toLowerCase();
      for (let i = 0; i < q.options.length; i++) {
        const opt = String(q.options[i] || '').trim();
        if (opt === rawAns) return i;
        const cleanOpt = cleanOptionText(opt).toLowerCase();
        if (cleanOpt === cleanRaw && cleanOpt.length > 0) return i;
        if (cleanRaw && (cleanOpt.includes(cleanRaw) || cleanRaw.includes(cleanOpt))) return i;
      }

      return -1;
    }

    // Initialize UI Elements
    function initUI() {
      // Restore Saved Font
      let savedFont = 'hind';
      try {
        savedFont = localStorage.getItem('epb_saved_font') || 'hind';
      } catch(e) {}
      applyFont(savedFont, false);

      document.getElementById('fontSelect').addEventListener('change', (e) => {
        applyFont(e.target.value, true);
      });

      // Restore Chapter / Exam Filter
      let savedChapter = 'all';
      try {
        savedChapter = localStorage.getItem('epb_saved_chapter') || 'all';
      } catch(e) {}
      if (savedChapter !== 'all' && !chaptersData.some(c => c.id === savedChapter)) {
        savedChapter = 'all';
      }
      currentChapter = savedChapter;

      // Restore Per-Page Setting
      let savedPerPage = '20';
      try {
        savedPerPage = localStorage.getItem('epb_saved_per_page') || '20';
      } catch(e) {}
      const perPageSelect = document.getElementById('perPageSelect');
      if (perPageSelect) {
        perPageSelect.value = savedPerPage;
        questionsPerSheet = savedPerPage === 'all' ? 999999 : parseInt(savedPerPage, 10);
      }

      // Restore Explanations Toggle
      try {
        const savedExp = localStorage.getItem('epb_saved_exp');
        if (savedExp !== null) showExplanations = (savedExp === 'true');
      } catch(e) {}
      const btnExp = document.getElementById('btnToggleExp');
      if (btnExp) {
        btnExp.classList.toggle('btn-active', showExplanations);
        document.getElementById('expText').textContent = showExplanations ? 'ব্যাখ্যা লুকান' : 'ব্যাখ্যা দেখুন';
        document.getElementById('expIcon').innerHTML = showExplanations ? '<i class=\"fa-solid fa-lightbulb\"></i>' : '<i class=\"fa-regular fa-lightbulb\"></i>';
        document.body.classList.toggle('show-explanations', showExplanations);
      }

      // Restore Answers Toggle
      try {
        const savedAns = localStorage.getItem('epb_saved_answers');
        if (savedAns !== null) showAnswers = (savedAns === 'true');
      } catch(e) {}
      const btnAns = document.getElementById('btnToggleAnswers');
      if (btnAns) {
        btnAns.classList.toggle('btn-active', showAnswers);
        document.getElementById('ansText').textContent = showAnswers ? 'উত্তর লুকান' : 'উত্তর দেখুন';
        document.getElementById('ansIcon').innerHTML = showAnswers ? '<i class=\"fa-solid fa-eye-slash\"></i>' : '<i class=\"fa-solid fa-eye\"></i>';
        document.body.classList.toggle('show-answers', showAnswers);
      }

      // Restore Bengali Number Toggle
      try {
        const savedNum = localStorage.getItem('epb_saved_num_lang');
        if (savedNum !== null) {
          useBengaliNumbers = (savedNum === 'true');
          document.getElementById('numLangText').textContent = useBengaliNumbers ? 'সংখ্যা: বাংলা' : 'সংখ্যা: English';
        }
      } catch(e) {}

      const chSelect = document.getElementById('chapterSelect');
      const pillsContainer = document.getElementById('pillsContainer');

      // Add 'All' pill
      const allPill = document.createElement('button');
      allPill.className = 'pill' + (currentChapter === 'all' ? ' active' : '');
      allPill.innerHTML = `<i class=\"fa-solid fa-layer-group\"></i> সকল পরীক্ষা (${formatNumber(1922)})`;
      allPill.dataset.ch = 'all';
      allPill.onclick = () => selectChapter('all');
      pillsContainer.appendChild(allPill);

      // Populate Chapters Select & Pills
      chaptersData.forEach(ch => {
        const opt = document.createElement('option');
        opt.value = ch.id;
        opt.textContent = `${ch.title} (${formatNumber(ch.count)}টি)`;
        if (ch.id === currentChapter) {
          opt.selected = true;
        }
        chSelect.appendChild(opt);

        const pill = document.createElement('button');
        pill.className = 'pill' + (ch.id === currentChapter ? ' active' : '');
        pill.textContent = `${ch.short} (${formatNumber(ch.count)})`;
        pill.dataset.ch = ch.id;
        pill.onclick = () => selectChapter(ch.id);
        pillsContainer.appendChild(pill);
      });

      chSelect.value = currentChapter;

      // Event Listeners
      chSelect.addEventListener('change', (e) => selectChapter(e.target.value));

      document.getElementById('searchInput').addEventListener('input', (e) => {
        searchQuery = e.target.value.trim().toLowerCase();
        currentPage = 1;
        render();
      });

      document.getElementById('perPageSelect').addEventListener('change', (e) => {
        const val = e.target.value;
        questionsPerSheet = val === 'all' ? 999999 : parseInt(val, 10);
        currentPage = 1;
        try {
          localStorage.setItem('epb_saved_per_page', val);
        } catch(e) {}
        render();
      });

      // Restore Practice Mode Toggle
      try {
        const savedPractice = localStorage.getItem('epb_saved_practice');
        if (savedPractice !== null) isPracticeMode = (savedPractice === 'true');
      } catch(e) {}
      const btnPractice = document.getElementById('btnTogglePractice');
      if (btnPractice) {
        btnPractice.classList.toggle('active', isPracticeMode);
        document.body.classList.toggle('practice-mode', isPracticeMode);
        document.getElementById('practiceText').textContent = isPracticeMode ? 'অনুশীলন বন্ধ' : 'অনুশীলন করুন';
      }

      if (btnPractice) {
        btnPractice.addEventListener('click', () => {
          isPracticeMode = !isPracticeMode;
          btnPractice.classList.toggle('active', isPracticeMode);
          document.body.classList.toggle('practice-mode', isPracticeMode);
          document.getElementById('practiceText').textContent = isPracticeMode ? 'অনুশীলন বন্ধ' : 'অনুশীলন করুন';
          try {
            localStorage.setItem('epb_saved_practice', isPracticeMode);
          } catch(e) {}
          render();
        });
      }

      // Show/Hide Answers Toggle
      btnAns.addEventListener('click', () => {
        showAnswers = !showAnswers;
        const icon = document.getElementById('ansIcon');
        const text = document.getElementById('ansText');
        if (showAnswers) {
          btnAns.classList.add('btn-active');
          icon.innerHTML = '<i class=\"fa-solid fa-eye-slash\"></i>';
          text.textContent = 'উত্তর লুকান';
        } else {
          btnAns.classList.remove('btn-active');
          icon.innerHTML = '<i class=\"fa-solid fa-eye\"></i>';
          text.textContent = 'উত্তর দেখুন';
        }
        document.body.classList.toggle('show-answers', showAnswers);
        try {
          localStorage.setItem('epb_saved_answers', showAnswers);
        } catch(e) {}
        render();
      });

      // Show/Hide Explanations Toggle
      btnExp.addEventListener('click', () => {
        showExplanations = !showExplanations;
        const icon = document.getElementById('expIcon');
        const text = document.getElementById('expText');
        if (showExplanations) {
          btnExp.classList.add('btn-active');
          icon.innerHTML = '<i class=\"fa-solid fa-lightbulb\"></i>';
          text.textContent = 'ব্যাখ্যা লুকান';
          document.body.classList.add('show-explanations');
        } else {
          btnExp.classList.remove('btn-active');
          icon.innerHTML = '<i class=\"fa-regular fa-lightbulb\"></i>';
          text.textContent = 'ব্যাখ্যা দেখুন';
          document.body.classList.remove('show-explanations');
        }
        try {
          localStorage.setItem('epb_saved_exp', showExplanations);
        } catch(e) {}
      });

      // Number Format Toggle
      document.getElementById('btnToggleNum').addEventListener('click', () => {
        useBengaliNumbers = !useBengaliNumbers;
        document.getElementById('numLangText').textContent = useBengaliNumbers ? 'সংখ্যা: বাংলা' : 'সংখ্যা: English';
        try {
          localStorage.setItem('epb_saved_num_lang', useBengaliNumbers);
        } catch(e) {}
        // Refresh pills text
        updatePillsCount();
        render();
      });

      // Scroll to Top
      const scrollBtn = document.getElementById('scrollTopBtn');
      window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
          scrollBtn.classList.add('visible');
        } else {
          scrollBtn.classList.remove('visible');
        }
      });
      scrollBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });

      // Initial Render
      render();

      if (window.katex) {
        render();
      } else {
        window.addEventListener('load', () => {
          if (window.katex) render();
        });
      }
    }

    function updatePillsCount() {
      const pills = document.querySelectorAll('.pill');
      pills.forEach(p => {
        const chId = p.dataset.ch;
        if (chId === 'all') {
          p.innerHTML = `<i class=\"fa-solid fa-layer-group\"></i> সকল পরীক্ষা (${formatNumber(1922)})`;
        } else {
          const ch = chaptersData.find(c => c.id === chId);
          if (ch) p.textContent = `${ch.short} (${formatNumber(ch.count)})`;
        }
      });
    }

    function selectChapter(chId, save = true) {
      currentChapter = chId;
      const chSelect = document.getElementById('chapterSelect');
      if (chSelect) chSelect.value = chId;
      
      document.querySelectorAll('.pill').forEach(p => {
        p.classList.toggle('active', p.dataset.ch === chId);
      });

      if (save) {
        try {
          localStorage.setItem('epb_saved_chapter', chId);
        } catch(e) {}
      }

      currentPage = 1;
      render();
    }

    function resetPracticeAnswers() {
      practiceAnswers = {};
      render();
    }

    function getFilteredQuestions() {
      let list = [];
      if (currentChapter === 'all') {
        chaptersData.forEach(ch => {
          ch.questions.forEach((q, qIndex) => {
            list.push({
              ...q,
              chId: ch.id,
              chTitle: ch.title,
              chShort: ch.short,
              dispNum: qIndex + 1,
              uid: `${ch.id}_${q.id}`
            });
          });
        });
      } else {
        const ch = chaptersData.find(c => c.id === currentChapter);
        if (ch) {
          ch.questions.forEach((q, qIndex) => {
            list.push({
              ...q,
              chId: ch.id,
              chTitle: ch.title,
              chShort: ch.short,
              dispNum: qIndex + 1,
              uid: `${ch.id}_${q.id}`
            });
          });
        }
      }

      if (searchQuery) {
        list = list.filter(q => {
          const qMatch = q.question.toLowerCase().includes(searchQuery);
          const optMatch = (q.options || []).some(opt => opt.toLowerCase().includes(searchQuery));
          const expMatch = q.explanation ? q.explanation.toLowerCase().includes(searchQuery) : false;
          return qMatch || optMatch || expMatch;
        });
      }

      return list;
    }

    function render() {
      const container = document.getElementById('sheetsContainer');
      const paginationBar = document.getElementById('paginationBar');
      const allFiltered = getFilteredQuestions();

      const statsInfo = document.getElementById('statsInfo');
      const totalInView = allFiltered.length;
      statsInfo.innerHTML = `মোট প্রশ্ন: <strong>${formatNumber(1922)}</strong> টি | প্রদর্শিত: <strong>${formatNumber(totalInView)}</strong> টি` + 
        (currentChapter !== 'all' ? ` | <span>পরীক্ষা: ${chaptersData.find(c=>c.id===currentChapter)?.short}</span>` : '');

      if (totalInView === 0) {
        container.innerHTML = `
          <div class=\"empty-state\">
            <div class=\"empty-icon\"><i class=\"fa-solid fa-magnifying-glass\"></i></div>
            <h3>কোনো প্রশ্ন খুঁজে পাওয়া যায়নি</h3>
            <p style=\"margin-top: 6px;\">অনুগ্রহ করে অন্য শব্দ দিয়ে খুঁজুন বা ফিল্টার পরিবর্তন করুন।</p>
          </div>
        `;
        paginationBar.innerHTML = '';
        return;
      }

      const totalPages = Math.ceil(totalInView / questionsPerSheet);
      if (currentPage > totalPages) currentPage = totalPages;
      if (currentPage < 1) currentPage = 1;

      const startIndex = (currentPage - 1) * questionsPerSheet;
      const endIndex = Math.min(startIndex + questionsPerSheet, totalInView);
      const pageQuestions = allFiltered.slice(startIndex, endIndex);

      container.innerHTML = '';

      const sheetCard = document.createElement('div');
      sheetCard.className = 'exam-sheet';

      const headerTitle = currentChapter === 'all' 
        ? 'Eminent Petro Bangla - নিয়োগ পরীক্ষার প্রশ্নব্যাংক' 
        : chaptersData.find(c => c.id === currentChapter)?.title;

      sheetCard.innerHTML = `
        <div class=\"sheet-meta-bar\">
          <div class=\"sheet-chapter-title\">
            <span><i class=\"fa-solid fa-fire-flame-curved\" style=\"color: #ea580c;\"></i></span>
            <span>${headerTitle}</span>
          </div>
          <div class=\"sheet-page-indicator\">
            প্রশ্ন: ${formatNumber(startIndex + 1)} - ${formatNumber(endIndex)} (মোট: ${formatNumber(totalInView)})
          </div>
        </div>
      `;

      const half = Math.ceil(pageQuestions.length / 2);
      const leftList = pageQuestions.slice(0, half);
      const rightList = pageQuestions.slice(half);

      const columnsContainer = document.createElement('div');
      columnsContainer.className = 'columns-container';

      const leftCol = document.createElement('div');
      leftCol.className = 'column-left';
      leftList.forEach(q => {
        leftCol.appendChild(createQuestionNode(q));
      });

      const rightCol = document.createElement('div');
      rightCol.className = 'column-right';
      rightList.forEach(q => {
        rightCol.appendChild(createQuestionNode(q));
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

      const titleDiv = document.createElement('div');
      titleDiv.className = 'question-title';

      const qNumSpan = document.createElement('span');
      qNumSpan.className = 'q-number';
      qNumSpan.textContent = `${formatNumber(q.dispNum)}. `;

      const qTextSpan = document.createElement('span');
      qTextSpan.className = 'q-text';
      qTextSpan.innerHTML = formatMath(cleanQuestionText(q.question));

      titleDiv.appendChild(qNumSpan);
      titleDiv.appendChild(qTextSpan);
      qBox.appendChild(titleDiv);

      const correctIndex = getAnswerIndex(q);
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

          if (optIdx === correctIndex) {
            cell.classList.add('is-correct');
          }

          if (isPracticeMode && selectedIndex !== undefined) {
            if (selectedIndex === correctIndex) {
              if (optIdx === correctIndex) {
                cell.classList.add('practice-correct');
              }
            } else {
              if (optIdx === selectedIndex) {
                cell.classList.add('practice-wrong');
              }
              if (optIdx === correctIndex) {
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
          textSpan.innerHTML = formatMath(cleanOptionText(optText));

          cell.appendChild(labelSpan);
          cell.appendChild(textSpan);
          optsGrid.appendChild(cell);
        });

        qBox.appendChild(optsGrid);
      }

      // Answer & Explanation Row
      const ansRow = document.createElement('div');
      ansRow.className = 'answer-row';

      const ansTag = document.createElement('div');
      ansTag.className = 'answer-tag';
      ansTag.innerHTML = `<i class=\"fa-solid fa-circle-check\"></i> সঠিক উত্তর: <strong>${q.answer || 'সঠিক উত্তর দেওয়া নেই'}</strong>`;
      ansRow.appendChild(ansTag);

      let expBox = null;
      if (q.explanation) {
        expBox = document.createElement('div');
        expBox.className = 'explanation-box';
        expBox.id = `exp_${q.uid}`;
        expBox.innerHTML = `
          <div class=\"exp-badge\"><i class=\"fa-solid fa-lightbulb\"></i> ব্যাখ্যা:</div>
          <div class=\"exp-body\">${formatMath(q.explanation)}</div>
        `;

        const btnExpSingle = document.createElement('button');
        btnExpSingle.className = 'btn-toggle-exp-single';
        btnExpSingle.innerHTML = `<i class=\"fa-solid fa-lightbulb\"></i> ব্যাখ্যা`;
        btnExpSingle.title = 'এই প্রশ্নের ব্যাখ্যা দেখুন বা লুকান';
        btnExpSingle.onclick = (e) => {
          e.stopPropagation();
          const isForced = expBox.classList.toggle('force-visible');
          btnExpSingle.innerHTML = isForced ? `<i class=\"fa-solid fa-circle-xmark\"></i> ব্যাখ্যা বন্ধ` : `<i class=\"fa-solid fa-lightbulb\"></i> ব্যাখ্যা`;
        };
        ansRow.appendChild(btnExpSingle);
      }

      qBox.appendChild(ansRow);

      if (expBox) {
        qBox.appendChild(expBox);
      }

      return qBox;
    }

    function renderPagination(totalPages) {
      const bar = document.getElementById('paginationBar');
      if (totalPages <= 1) {
        bar.innerHTML = '';
        return;
      }

      let html = '';

      html += `<button class=\"page-btn\" ${currentPage === 1 ? 'disabled' : ''} onclick=\"goToPage(${currentPage - 1})\"><i class=\"fa-solid fa-chevron-left\"></i> পূর্ববর্তী</button>`;

      let startP = Math.max(1, currentPage - 2);
      let endP = Math.min(totalPages, currentPage + 2);

      if (startP > 1) {
        html += `<button class=\"page-btn\" onclick=\"goToPage(1)\">${formatNumber(1)}</button>`;
        if (startP > 2) html += `<span style=\"padding: 0 4px; color: #94a3b8;\">...</span>`;
      }

      for (let p = startP; p <= endP; p++) {
        html += `<button class=\"page-btn ${p === currentPage ? 'active' : ''}\" onclick=\"goToPage(${p})\">${formatNumber(p)}</button>`;
      }

      if (endP < totalPages) {
        if (endP < totalPages - 1) html += `<span style=\"padding: 0 4px; color: #94a3b8;\">...</span>`;
        html += `<button class=\"page-btn\" onclick=\"goToPage(${totalPages})\">${formatNumber(totalPages)}</button>`;
      }

      html += `<button class=\"page-btn\" ${currentPage === totalPages ? 'disabled' : ''} onclick=\"goToPage(${currentPage + 1})\">পরবর্তী <i class=\"fa-solid fa-chevron-right\"></i></button>`;

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

exams_json = json.dumps(exams, ensure_ascii=False)
final_html = html_template.replace("%EXAMS_JSON%", exams_json)

out_file = "Eminent-Petro-Bangla.html"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated {out_file} successfully! File size: {os.path.getsize(out_file)} bytes")
