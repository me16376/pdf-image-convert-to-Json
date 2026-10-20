# -*- coding: utf-8 -*-
"""
Build standalone interactive web application BPSC-Non-Tech.html
with complete embedded dataset of all 7 subjects (5,664 MCQs, 448 pages)
from "ডি. মাওলা [BPSC] নন-টেক MCQ ডাইজেস্ট".
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.join("JSON Data", "BPSC Non Tech")
OUTPUT_FILE = "BPSC-Non-Tech.html"

SUBJECTS_CONFIG = [
    {
        "id": "bangla",
        "nameBn": "বাংলা",
        "nameEn": "Bangla",
        "icon": "fa-book-open",
        "prefix": "bn",
        "badgeColor": "#e11d48",
        "pages": "Pages 30–112 (৮৩ পৃষ্ঠা)",
        "subtitle": "সাহিত্য, ব্যাকরণ, বাক্য শুদ্ধি, পরিভাষা ও কারক-সমাস",
        "path": os.path.join(BASE_DIR, "Bangla", "Bangla.json")
    },
    {
        "id": "english",
        "nameBn": "ইংরেজি",
        "nameEn": "English",
        "icon": "fa-language",
        "prefix": "en",
        "badgeColor": "#2563eb",
        "pages": "Pages 292–388 (৯৭ পৃষ্ঠা)",
        "subtitle": "Grammar, Vocabulary, Preposition, Voice, Narration & Literature",
        "path": os.path.join(BASE_DIR, "English", "English.json")
    },
    {
        "id": "bangladesh_affairs",
        "nameBn": "বাংলাদেশ বিষয়াবলি",
        "nameEn": "Bangladesh Affairs",
        "icon": "fa-landmark",
        "prefix": "bd",
        "badgeColor": "#059669",
        "pages": "Pages 538–584 (৪৭ পৃষ্ঠা)",
        "subtitle": "ইতিহাস, মুক্তিযুদ্ধ, সংবিধান, ভৌগোলিক অবস্থান ও জাতীয় অর্জন",
        "path": os.path.join(BASE_DIR, "Bangladesh Affairs", "Bangladesh_Affairs.json")
    },
    {
        "id": "international_affairs",
        "nameBn": "আন্তর্জাতিক বিষয়াবলি",
        "nameEn": "International Affairs",
        "icon": "fa-earth-americas",
        "prefix": "intl",
        "badgeColor": "#0891b2",
        "pages": "Pages 722–758 (৩৭ পৃষ্ঠা)",
        "subtitle": "বিশ্ব ইতিহাস, জাতিসংঘ, আন্তর্জাতিক সংস্থা, চুক্তি ও ভূ-রাজনীতি",
        "path": os.path.join(BASE_DIR, "International Affairs", "International_Affairs.json")
    },
    {
        "id": "science",
        "nameBn": "সাধারণ বিজ্ঞান",
        "nameEn": "General Science",
        "icon": "fa-flask-vial",
        "prefix": "sci",
        "badgeColor": "#7c3aed",
        "pages": "Pages 872–913 (৪২ পৃষ্ঠা)",
        "subtitle": "পদার্থ, রসায়ন, জীববিজ্ঞান, স্বাস্থ্যবিজ্ঞান ও আধুনিক প্রযুক্তি",
        "path": os.path.join(BASE_DIR, "Science", "Science.json")
    },
    {
        "id": "ict",
        "nameBn": "কম্পিউটার ও তথ্যপ্রযুক্তি",
        "nameEn": "ICT",
        "icon": "fa-laptop-code",
        "prefix": "ict",
        "badgeColor": "#ea580c",
        "pages": "Pages 914–926 (১৩ পৃষ্ঠা)",
        "subtitle": "কম্পিউটার সংগঠন, হার্ডওয়্যার, নেটওয়ার্কিং, ইন্টারনেট ও নিরাপত্তা",
        "path": os.path.join(BASE_DIR, "ICT", "ICT.json")
    },
    {
        "id": "math",
        "nameBn": "গণিত ও মানসিক দক্ষতা",
        "nameEn": "Mathematics",
        "icon": "fa-calculator",
        "prefix": "math",
        "badgeColor": "#b91c1c",
        "pages": "Pages 1002–1130 (১২৯ পৃষ্ঠা)",
        "subtitle": "পাটিগণিত, বীজগণিত, জ্যামিতি, পরিমিতি, ত্রিকোণমিতি ও মানসিক দক্ষতা",
        "path": os.path.join(BASE_DIR, "Math", "Math.json")
    }
]

def clean_option_text(t):
    if not t: return ''
    return re.sub(r'^(\([ক-ঙa-eA-E1-5]\)|\[[ক-ঙa-eA-E1-5]\]|[ক-ঙa-eA-E][\)\.\:–—\-]\s*|[1-5][\)\.\:–—\-]\s*)', '', str(t)).strip()

subjects_data = []
total_questions = 0

for s in SUBJECTS_CONFIG:
    fpath = s["path"]
    if not os.path.exists(fpath):
        print(f"Error: file not found: {fpath}")
        sys.exit(1)

    with open(fpath, 'r', encoding='utf-8') as f:
        raw_qs = json.load(f)

    cleaned_qs = []
    for q_idx, q in enumerate(raw_qs):
        opts = q.get("options", [])
        clean_opts = [clean_option_text(o) for o in opts]
        cleaned_qs.append({
            "id": q.get("id", q_idx + 1),
            "page": q.get("page"),
            "question": str(q.get("question", "")).strip(),
            "options": clean_opts,
            "answer": str(q.get("answer", "")).strip(),
            "explanation": str(q.get("explanation", "")).strip()
        })

    q_count = len(cleaned_qs)
    total_questions += q_count

    subjects_data.append({
        "id": s["id"],
        "nameBn": s["nameBn"],
        "nameEn": s["nameEn"],
        "icon": s["icon"],
        "prefix": s["prefix"],
        "badgeColor": s["badgeColor"],
        "pages": s["pages"],
        "subtitle": s["subtitle"],
        "count": q_count,
        "questions": cleaned_qs
    })

    print(f"Loaded {s['nameBn']}: {q_count} MCQs")

print(f"\nTotal loaded: {total_questions} MCQs across {len(subjects_data)} subjects.")

json_data_str = json.dumps(subjects_data, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BPSC Non-Tech Digest - বিপিএসসি নন-ক্যাডার ১০ম গ্রেড প্রশ্নব্যাংক (৫,৬৬৪ MCQ)</title>
  <meta name="description" content="ডি. মাওলা BPSC নন-টেক MCQ ডাইজেস্ট - বাংলা, ইংরেজি, বাংলাদেশ ও আন্তর্জাতিক বিষয়াবলি, বিজ্ঞান, আইসিটি এবং গণিত ও মানসিক দক্ষতার ৫,৬৬৪টি ব্যাখ্যাসহ সমাধান">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Bangla:wght@400;500;600;700;800&family=Hind+Siliguri:wght@400;500;600;700;800&family=Noto+Sans+Bengali:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <!-- Font Awesome 6 Icons (Local Driver with CDN fallback) -->
  <link rel="stylesheet" href="drivers/fontawesome/css/all.min.css" onerror="this.onerror=null;this.href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css';">
  <!-- KaTeX Library for Math Formula Rendering (Local Driver with CDN fallback) -->
  <link rel="stylesheet" href="drivers/katex/katex.min.css" onerror="this.onerror=null;this.href='https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css';">
  <script defer src="drivers/katex/katex.min.js" onerror="this.onerror=null;this.src='https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js';"></script>

  <style>
    :root {
      --bg-page: #f8fafc;
      --card-bg: #ffffff;
      --text-main: #0f172a;
      --text-sub: #334155;
      --text-muted: #64748b;
      --border-color: #e2e8f0;
      --primary: #1e3a8a;
      --primary-hover: #1e40af;
      --primary-dark: #172554;
      --primary-light: #eff6ff;
      --primary-border: #bfdbfe;
      --gold: #d97706;
      --gold-light: #fef3c7;
      --success: #059669;
      --success-light: #ecfdf5;
      --danger: #dc2626;
      --danger-light: #fef2f2;
      --amber: #d97706;
      --shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.05);
      --shadow-md: 0 4px 16px -2px rgba(15, 23, 42, 0.08), 0 2px 6px -1px rgba(15, 23, 42, 0.04);
      --shadow-lg: 0 12px 30px -4px rgba(15, 23, 42, 0.12), 0 4px 12px -2px rgba(15, 23, 42, 0.06);
      --radius-lg: 14px;
      --radius-md: 10px;
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
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* Top Strip */
    .portal-nav {
      background: linear-gradient(90deg, #091326 0%, #0f172a 40%, #172554 100%);
      color: #94a3b8;
      font-size: 12.5px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }

    .portal-nav-inner {
      max-width: 1320px;
      margin: 0 auto;
      padding: 7px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }

    .portal-nav-left {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .pill-badge {
      background: rgba(37, 99, 235, 0.22);
      color: #93c5fd;
      border: 1px solid rgba(147, 197, 253, 0.35);
      padding: 2px 10px;
      border-radius: 20px;
      font-size: 11.5px;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    .portal-links {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .portal-link {
      color: #cbd5e1;
      text-decoration: none;
      font-size: 12px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 8px;
      border-radius: 6px;
      transition: all 0.15s ease;
    }

    .portal-link:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.1);
    }

    .portal-link.active {
      color: #93c5fd;
      background: rgba(30, 58, 138, 0.4);
      font-weight: 700;
    }

    /* Main Header */
    header.app-header {
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      border-top: 3.5px solid var(--primary);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 18px -4px rgba(15, 23, 42, 0.05);
    }

    .header-container {
      max-width: 1320px;
      margin: 0 auto;
      padding: 14px 20px 12px;
    }

    .header-top-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 14px;
    }

    .brand-area {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }

    .brand-logo {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: linear-gradient(135deg, #1e3a8a 0%, #1d4ed8 50%, #0284c7 100%);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      box-shadow: 0 6px 16px rgba(30, 58, 138, 0.28);
      border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .brand-title {
      font-size: 21px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.3px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .brand-badge {
      font-size: 11px;
      font-weight: 700;
      background: var(--gold-light);
      color: #b45309;
      border: 1px solid #fde68a;
      padding: 2px 7px;
      border-radius: 6px;
      text-transform: uppercase;
    }

    .brand-subtitle {
      font-size: 12.5px;
      color: var(--text-muted);
      font-weight: 500;
    }

    .header-controls {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .ctrl-btn {
      padding: 7px 12px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: #ffffff;
      color: var(--text-sub);
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      font-family: inherit;
    }

    .ctrl-btn:hover {
      background: #f1f5f9;
      color: var(--text-main);
      border-color: #cbd5e1;
    }

    .ctrl-btn.active {
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary-border);
    }

    /* Subject Tabs Row */
    .subject-tabs-scroll {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 2px;
      scrollbar-width: thin;
    }

    .subject-tabs-scroll::-webkit-scrollbar {
      height: 4px;
    }
    .subject-tabs-scroll::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border-radius: 4px;
    }

    .subject-tab {
      padding: 8px 14px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: #f8fafc;
      color: var(--text-sub);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.15s ease;
      font-family: inherit;
    }

    .subject-tab:hover {
      background: #ffffff;
      border-color: #94a3b8;
      color: #0f172a;
    }

    .subject-tab.active {
      background: #1e3a8a;
      color: #ffffff;
      border-color: #1e3a8a;
      box-shadow: 0 2px 8px rgba(30, 58, 138, 0.25);
    }

    .subject-tab .count-badge {
      font-size: 11px;
      font-weight: 700;
      padding: 1px 6px;
      border-radius: 10px;
      background: rgba(15, 23, 42, 0.08);
      color: inherit;
    }

    .subject-tab.active .count-badge {
      background: rgba(255, 255, 255, 0.25);
      color: #ffffff;
    }

    /* Main Layout */
    .main-wrapper {
      max-width: 1320px;
      margin: 18px auto 40px;
      padding: 0 20px;
      display: grid;
      grid-template-columns: 290px 1fr;
      gap: 20px;
      align-items: start;
    }

    /* Sidebar / Filters */
    .sidebar-panel {
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 18px;
      box-shadow: var(--shadow-sm);
      position: sticky;
      top: 140px;
      max-height: calc(100vh - 160px);
      overflow-y: auto;
    }

    .sidebar-section-title {
      font-size: 13px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .filter-input-wrap {
      position: relative;
      margin-bottom: 16px;
    }

    .filter-input {
      width: 100%;
      padding: 9px 12px 9px 34px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      font-size: 13.5px;
      font-family: inherit;
      color: var(--text-main);
      background: #f8fafc;
      transition: all 0.15s ease;
    }

    .filter-input:focus {
      outline: none;
      border-color: #2563eb;
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    }

    .filter-input-icon {
      position: absolute;
      left: 11px;
      top: 50%;
      transform: translateY(-50%);
      color: #94a3b8;
      font-size: 13px;
    }

    .mode-switch-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 18px;
    }

    .mode-btn {
      padding: 8px 12px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: #ffffff;
      color: var(--text-sub);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.15s ease;
      font-family: inherit;
      text-align: left;
    }

    .mode-btn:hover {
      background: #f8fafc;
      border-color: #cbd5e1;
    }

    .mode-btn.active {
      background: var(--primary-light);
      border-color: var(--primary-border);
      color: var(--primary);
    }

    .mode-btn i {
      font-size: 14px;
    }

    /* Score Box */
    .practice-scorecard {
      background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
      border: 1px solid #bbf7d0;
      border-radius: 10px;
      padding: 12px;
      margin-bottom: 18px;
    }

    .score-title {
      font-size: 12px;
      font-weight: 700;
      color: #166534;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }

    .score-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
      text-align: center;
    }

    .score-box-item {
      background: #ffffff;
      border-radius: 6px;
      padding: 6px 4px;
      border: 1px solid rgba(22, 101, 52, 0.15);
    }

    .score-val {
      font-size: 16px;
      font-weight: 800;
      font-family: 'Inter', 'Hind Siliguri', sans-serif;
      line-height: 1.1;
    }

    .score-val.val-correct { color: #16a34a; }
    .score-val.val-wrong { color: #dc2626; }
    .score-val.val-acc { color: #2563eb; }

    .score-lbl {
      font-size: 10.5px;
      color: var(--text-muted);
      font-weight: 600;
    }

    .btn-reset-score {
      width: 100%;
      margin-top: 8px;
      padding: 4px;
      font-size: 11px;
      font-weight: 600;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      color: #64748b;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .btn-reset-score:hover {
      background: #fee2e2;
      color: #b91c1c;
      border-color: #fca5a5;
    }

    /* Content Area */
    .content-area {
      min-width: 0;
    }

    .banner-subject {
      background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 50%, #0369a1 100%);
      color: #ffffff;
      border-radius: var(--radius-lg);
      padding: 22px 24px;
      margin-bottom: 18px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
    }

    .banner-subject::after {
      content: '';
      position: absolute;
      right: -20px;
      bottom: -30px;
      width: 160px;
      height: 160px;
      background: rgba(255, 255, 255, 0.06);
      border-radius: 50%;
      pointer-events: none;
    }

    .banner-top-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 3px 10px;
      border-radius: 20px;
      margin-bottom: 8px;
      color: #f8fafc;
    }

    .banner-title {
      font-size: 24px;
      font-weight: 800;
      letter-spacing: -0.4px;
      margin-bottom: 4px;
    }

    .banner-sub {
      font-size: 14px;
      color: #e2e8f0;
      max-width: 680px;
      line-height: 1.45;
    }

    .banner-stats-row {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-top: 14px;
      font-size: 13px;
      color: #cbd5e1;
      flex-wrap: wrap;
    }

    .banner-stat-chip {
      background: rgba(0, 0, 0, 0.2);
      padding: 3px 10px;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-weight: 600;
      color: #ffffff;
    }

    /* Actions Bar */
    .actions-bar {
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 10px 16px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
      box-shadow: var(--shadow-sm);
    }

    .actions-left {
      font-size: 13.5px;
      color: var(--text-sub);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .actions-right {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .select-dropdown {
      padding: 6px 10px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background: #ffffff;
      font-size: 12.5px;
      font-family: inherit;
      color: var(--text-sub);
      cursor: pointer;
    }

    /* MCQ Card */
    .mcq-card {
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 20px 22px;
      margin-bottom: 16px;
      box-shadow: var(--shadow-sm);
      transition: all 0.16s ease;
      position: relative;
    }

    .mcq-card:hover {
      box-shadow: var(--shadow-md);
      border-color: #cbd5e1;
    }

    .mcq-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }

    .mcq-meta-left {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .q-number-pill {
      font-family: 'Inter', 'Hind Siliguri', sans-serif;
      font-size: 12px;
      font-weight: 800;
      background: #1e3a8a;
      color: #ffffff;
      padding: 3px 9px;
      border-radius: 6px;
      letter-spacing: 0.3px;
    }

    .subject-pill {
      font-size: 11.5px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      border: 1px solid transparent;
    }

    .page-pill {
      font-size: 11.5px;
      color: var(--text-muted);
      background: #f1f5f9;
      padding: 2px 7px;
      border-radius: 4px;
      font-weight: 600;
    }

    .btn-bookmark {
      background: transparent;
      border: none;
      color: #94a3b8;
      cursor: pointer;
      font-size: 15px;
      padding: 4px;
      transition: all 0.15s ease;
    }

    .btn-bookmark:hover {
      color: #f59e0b;
    }

    .btn-bookmark.bookmarked {
      color: #f59e0b;
    }

    .mcq-question {
      font-size: 16px;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.5;
      margin-bottom: 14px;
      word-break: break-word;
    }

    .exam-tag {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 12px;
      font-weight: 700;
      color: #1e40af;
      background: #dbeafe;
      border: 1px solid #bfdbfe;
      padding: 1px 7px;
      border-radius: 4px;
      margin-left: 6px;
      vertical-align: middle;
    }

    /* Options Grid */
    .options-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 14px;
    }

    @media (max-width: 768px) {
      .options-grid {
        grid-template-columns: 1fr;
      }
    }

    .option-btn {
      background: #f8fafc;
      border: 1.5px solid var(--border-color);
      border-radius: 8px;
      padding: 10px 14px;
      font-size: 14px;
      font-weight: 500;
      color: var(--text-main);
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.14s ease;
      font-family: inherit;
      line-height: 1.4;
      word-break: break-word;
    }

    .option-btn:hover:not(.locked) {
      background: #ffffff;
      border-color: #93c5fd;
      transform: translateY(-1px);
      box-shadow: 0 2px 6px rgba(37, 99, 235, 0.08);
    }

    .opt-letter {
      font-weight: 700;
      color: #64748b;
      min-width: 26px;
      font-size: 13.5px;
    }

    /* Practice Answer States */
    .option-btn.opt-correct {
      background: #ecfdf5 !important;
      border-color: #10b981 !important;
      color: #065f46 !important;
      font-weight: 700;
    }
    .option-btn.opt-correct .opt-letter {
      color: #059669 !important;
    }

    .option-btn.opt-wrong {
      background: #fef2f2 !important;
      border-color: #ef4444 !important;
      color: #991b1b !important;
      font-weight: 600;
    }
    .option-btn.opt-wrong .opt-letter {
      color: #dc2626 !important;
    }

    /* Study Mode Revealed Answer */
    .study-correct-indicator {
      border-color: #10b981 !important;
      background: #f0fdf4 !important;
    }

    /* Explanation Container */
    .mcq-explanation-wrap {
      background: #f8fafc;
      border-left: 3.5px solid #2563eb;
      border-radius: 0 8px 8px 0;
      padding: 12px 16px;
      margin-top: 10px;
      font-size: 13.5px;
      color: #1e293b;
      line-height: 1.6;
    }

    .mcq-explanation-wrap.hidden {
      display: none;
    }

    .exp-title-row {
      font-weight: 700;
      color: #1e40af;
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 6px;
      font-size: 12.5px;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    .exp-body {
      white-space: pre-line;
      color: #334155;
    }

    .mcq-footer-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-top: 8px;
      padding-top: 8px;
      border-top: 1px dashed #e2e8f0;
      font-size: 12px;
      color: var(--text-muted);
    }

    .btn-toggle-exp {
      background: none;
      border: none;
      color: #2563eb;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 12px;
      padding: 2px 4px;
      border-radius: 4px;
    }

    .btn-toggle-exp:hover {
      background: #eff6ff;
    }

    /* Pagination */
    .pagination-bar {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      margin-top: 24px;
      flex-wrap: wrap;
    }

    .page-btn {
      min-width: 38px;
      height: 38px;
      padding: 0 10px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: #ffffff;
      color: var(--text-main);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s ease;
      font-family: inherit;
    }

    .page-btn:hover:not(:disabled) {
      background: #f1f5f9;
      border-color: #cbd5e1;
    }

    .page-btn.active {
      background: #1e3a8a;
      color: #ffffff;
      border-color: #1e3a8a;
    }

    .page-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    /* Empty state */
    .empty-state {
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 50px 20px;
      text-align: center;
      color: var(--text-muted);
    }
    .empty-state i {
      font-size: 42px;
      color: #94a3b8;
      margin-bottom: 14px;
    }

    /* Responsive */
    @media (max-width: 960px) {
      .main-wrapper {
        grid-template-columns: 1fr;
      }
      .sidebar-panel {
        position: static;
        max-height: none;
      }
    }
  </style>
</head>
<body>

  <!-- Top Strip -->
  <div class="portal-nav">
    <div class="portal-nav-inner">
      <div class="portal-nav-left">
        <span class="pill-badge"><i class="fa-solid fa-star"></i> বিপিএসসি স্পেশাল</span>
        <span>ডি. মাওলা BPSC নন-টেক MCQ ডাইজেস্ট (১০ম গ্রেড ও নন-ক্যাডার প্রশ্নব্যাংক)</span>
      </div>
      <div class="portal-links">
        <a href="index.html" class="portal-link"><i class="fa-solid fa-house"></i> হোম পোর্টাল</a>
        <a href="BUET-Pattern.html" class="portal-link"><i class="fa-solid fa-building-columns"></i> BUET Pattern</a>
        <a href="Biddabari-NTRCA.html" class="portal-link"><i class="fa-solid fa-graduation-cap"></i> Biddabari</a>
        <a href="Saif-Sir-NTRCA-Suggestion.html" class="portal-link"><i class="fa-solid fa-award"></i> Saif Sir</a>
        <a href="Ampibian-Suggestion.html" class="portal-link"><i class="fa-solid fa-book-bookmark"></i> Ampibian</a>
        <a href="Eminent-Petro-Bangla.html" class="portal-link"><i class="fa-solid fa-fire-flame-curved"></i> Petro Bangla</a>
        <span class="portal-link active"><i class="fa-solid fa-shield-halved"></i> BPSC Non-Tech</span>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="app-header">
    <div class="header-container">
      <div class="header-top-row">
        <a href="BPSC-Non-Tech.html" class="brand-area">
          <div class="brand-logo">
            <i class="fa-solid fa-shield-halved"></i>
          </div>
          <div>
            <div class="brand-title">
              BPSC Non-Tech Digest
              <span class="brand-badge">১০ম গ্রেড</span>
            </div>
            <div class="brand-subtitle">ডি. মাওলা • বিপিএসসি নন-ক্যাডার নিয়োগ পরীক্ষার প্রশ্নব্যাখ্যাসহ সমাধান</div>
          </div>
        </a>

        <div class="header-controls">
          <button class="ctrl-btn" id="btnNumToggle" onclick="toggleNumberFormat()" title="সংখ্যা ফরম্যাট পরিবর্তন">
            <i class="fa-solid fa-arrow-down-1-9"></i>
            <span id="numLangLabel">সংখ্যা: বাংলা</span>
          </button>

          <select class="select-dropdown" id="fontSelector" onchange="changeFont(this.value)" title="ফন্ট পরিবর্তন">
            <option value="hind">Hind Siliguri</option>
            <option value="anek">Anek Bangla</option>
            <option value="noto">Noto Sans Bengali</option>
            <option value="inter">Inter (English)</option>
          </select>
        </div>
      </div>

      <!-- Subject Tabs -->
      <div class="subject-tabs-scroll" id="subjectTabsContainer">
        <!-- Rendered by JS -->
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <div class="main-wrapper">

    <!-- Sidebar Filters -->
    <aside class="sidebar-panel">
      <div class="sidebar-section-title">
        <span>অনুসন্ধান ও ফিল্টার</span>
        <i class="fa-solid fa-sliders"></i>
      </div>

      <div class="filter-input-wrap">
        <i class="fa-solid fa-magnifying-glass filter-input-icon"></i>
        <input type="text" class="filter-input" id="searchInput" placeholder="প্রশ্ন, অপশন বা পরীক্ষা খুঁজুন..." oninput="handleSearch(this.value)">
      </div>

      <div class="sidebar-section-title">
        <span>পড়াশোনার মোড</span>
      </div>

      <div class="mode-switch-group">
        <button class="mode-btn active" id="modeStudy" onclick="switchMode('study')">
          <span><i class="fa-solid fa-book-open-reader" style="color: #2563eb; margin-right: 8px;"></i> অধ্যায়ন মোড (উত্তরসহ)</span>
          <i class="fa-solid fa-check"></i>
        </button>
        <button class="mode-btn" id="modePractice" onclick="switchMode('practice')">
          <span><i class="fa-solid fa-circle-question" style="color: #059669; margin-right: 8px;"></i> অনুশীলন মোড (MCQ টেস্ট)</span>
          <i class="fa-solid fa-chevron-right" style="font-size: 11px;"></i>
        </button>
      </div>

      <!-- Practice Scorecard (Visible in Practice Mode) -->
      <div class="practice-scorecard" id="practiceScorecard" style="display: none;">
        <div class="score-title">
          <span><i class="fa-solid fa-chart-pie"></i> আপনার স্কোরকার্ড</span>
          <span id="scoreAccuracy">০% নির্ভুল</span>
        </div>
        <div class="score-grid">
          <div class="score-box-item">
            <div class="score-val val-acc" id="scoreAttempted">০</div>
            <div class="score-lbl">উত্তর দিয়েছেন</div>
          </div>
          <div class="score-box-item">
            <div class="score-val val-correct" id="scoreCorrect">০</div>
            <div class="score-lbl">সঠিক</div>
          </div>
          <div class="score-box-item">
            <div class="score-val val-wrong" id="scoreWrong">০</div>
            <div class="score-lbl">ভুল</div>
          </div>
        </div>
        <button class="btn-reset-score" onclick="resetPracticeScore()">
          <i class="fa-solid fa-rotate-left"></i> স্কোর রিসেট করুন
        </button>
      </div>

      <div class="sidebar-section-title">
        <span>ফিল্টার অপশন</span>
      </div>

      <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 16px;">
        <label style="font-size: 13px; font-weight: 600; color: var(--text-sub); display: flex; align-items: center; gap: 8px; cursor: pointer;">
          <input type="checkbox" id="chkBookmarkedOnly" onchange="toggleBookmarkedFilter(this.checked)">
          <span><i class="fa-solid fa-star" style="color: #f59e0b;"></i> শুধুমাত্র বুকমার্ককৃত প্রশ্ন</span>
        </label>
        <label style="font-size: 13px; font-weight: 600; color: var(--text-sub); display: flex; align-items: center; gap: 8px; cursor: pointer;">
          <input type="checkbox" id="chkShowAllExplanations" onchange="toggleAllExplanations(this.checked)" checked>
          <span><i class="fa-solid fa-lightbulb" style="color: #eab308;"></i> সবসময় ব্যাখ্যা উন্মুক্ত রাখুন</span>
        </label>
      </div>

      <div class="sidebar-section-title">
        <span>প্রতি পৃষ্ঠায় প্রশ্ন</span>
      </div>
      <select class="select-dropdown" style="width: 100%; padding: 8px;" id="perPageSelect" onchange="changePerPage(this.value)">
        <option value="25">২৫টি করে প্রশ্ন</option>
        <option value="50" selected>৫০টি করে প্রশ্ন</option>
        <option value="100">১০০টি করে প্রশ্ন</option>
        <option value="all">সব প্রশ্ন একসাথে</option>
      </select>
    </aside>

    <!-- Content -->
    <main class="content-area">
      <!-- Subject Banner -->
      <div class="banner-subject" id="subjectBanner">
        <!-- Rendered by JS -->
      </div>

      <!-- Actions Bar -->
      <div class="actions-bar">
        <div class="actions-left" id="actionsCountInfo">
          <!-- Rendered by JS -->
        </div>
        <div class="actions-right">
          <button class="ctrl-btn" onclick="scrollToTop()" title="উপরে যান">
            <i class="fa-solid fa-arrow-up"></i> উপরে যান
          </button>
        </div>
      </div>

      <!-- MCQ Container -->
      <div id="mcqContainer">
        <!-- Rendered by JS -->
      </div>

      <!-- Pagination -->
      <div class="pagination-bar" id="paginationContainer">
        <!-- Rendered by JS -->
      </div>
    </main>

  </div>

  <script>
    // Embedded Dataset (All 7 subjects, 5,664 MCQs)
    const rawData = JSON_DATA_PLACEHOLDER;

    // State
    let currentSubjectId = 'all';
    let currentMode = 'study'; // 'study' or 'practice'
    let searchQuery = '';
    let bookmarkedOnly = false;
    let showAllExplanations = true;
    let perPage = 50;
    let currentPage = 1;
    let numFormat = 'bn'; // 'bn' or 'en'
    let userAnswers = {}; // { "subj_id_qid": { selectedIdx, isCorrect } }
    let bookmarks = new Set(JSON.parse(localStorage.getItem('bpsc_bookmarks') || '[]'));

    const BN_DIGITS = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
    const EN_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

    function formatNumber(num) {
      if (num === null || num === undefined) return '';
      const str = String(num);
      if (numFormat === 'bn') {
        return str.replace(/\\d/g, d => BN_DIGITS[d]);
      } else {
        return str.replace(/[০-৯]/g, d => EN_DIGITS[BN_DIGITS.indexOf(d)]);
      }
    }

    function getOptionMarker(idx) {
      const bnMarkers = ['(ক)', '(খ)', '(গ)', '(ঘ)', '(ঙ)'];
      const enMarkers = ['(a)', '(b)', '(c)', '(d)', '(e)'];
      return numFormat === 'bn' ? bnMarkers[idx] || `(${idx+1})` : enMarkers[idx] || `(${idx+1})`;
    }

    function normalizeAnswerLetter(ans) {
      if (!ans) return null;
      const str = String(ans).trim();
      const m = str.match(/^[\\(（\\[]?\\s*([a-eক-ঙ1-5])/i);
      if (m) {
        const s = m[1].toLowerCase();
        if (s === 'ক' || s === 'a' || s === '১' || s === '1') return 0;
        if (s === 'খ' || s === 'b' || s === '২' || s === '2') return 1;
        if (s === 'গ' || s === 'c' || s === '৩' || s === '3') return 2;
        if (s === 'ঘ' || s === 'd' || s === '৪' || s === '4') return 3;
        if (s === 'ঙ' || s === 'e' || s === '৫' || s === '5') return 4;
      }
      return null;
    }

    function formatTextAndMath(text) {
      if (!text) return '';
      let s = String(text);

      // Exam tags: [PWD-2015], [BPSC-2012], etc.
      s = s.replace(/\\[([^\\]]+)\\]/g, '<span class="exam-tag"><i class="fa-solid fa-tag"></i> $1</span>');

      // KaTeX math rendering if available
      if (window.katex && window.katex.renderToString && (s.includes('\\\\') || s.includes('^') || s.includes('_'))) {
        try {
          if (!/[\\u0980-\\u09FF]/.test(s)) {
            return window.katex.renderToString(s, { throwOnError: false, displayMode: false });
          } else {
            s = s.replace(/(\\\\[a-zA-Z]+(\\{[^}]*\\})*)/g, function(match) {
              try {
                return window.katex.renderToString(match, { throwOnError: false, displayMode: false });
              } catch(e) {
                return match;
              }
            });
          }
        } catch(e) {}
      }
      return s;
    }

    function renderSubjectTabs() {
      const container = document.getElementById('subjectTabsContainer');
      const totalAll = rawData.reduce((acc, s) => acc + s.count, 0);

      let html = `
        <button class="subject-tab ${currentSubjectId === 'all' ? 'active' : ''}" onclick="selectSubject('all')">
          <i class="fa-solid fa-layer-group"></i>
          <span>সকল বিষয়</span>
          <span class="count-badge">${formatNumber(totalAll)}</span>
        </button>
      `;

      rawData.forEach(s => {
        const isActive = currentSubjectId === s.id;
        html += `
          <button class="subject-tab ${isActive ? 'active' : ''}" onclick="selectSubject('${s.id}')">
            <i class="fa-solid ${s.icon}"></i>
            <span>${s.nameBn}</span>
            <span class="count-badge">${formatNumber(s.count)}</span>
          </button>
        `;
      });

      container.innerHTML = html;
    }

    function selectSubject(subjId) {
      currentSubjectId = subjId;
      currentPage = 1;
      renderSubjectTabs();
      renderBanner();
      renderQuestions();
    }

    function renderBanner() {
      const banner = document.getElementById('subjectBanner');
      if (currentSubjectId === 'all') {
        const totalQ = rawData.reduce((acc, s) => acc + s.count, 0);
        banner.innerHTML = `
          <span class="banner-top-badge"><i class="fa-solid fa-shield-halved"></i> বিপিএসসি নন-ক্যাডার ১০ম গ্রেড স্পেশাল</span>
          <h2 class="banner-title">ডি. মাওলা BPSC নন-টেক MCQ ডাইজেস্ট</h2>
          <p class="banner-sub">বিপিএসসি'র ১০ম গ্রেড নন-ক্যাডার পরীক্ষা এবং বিভিন্ন সরকারি ও স্বায়ত্তশাসিত প্রতিষ্ঠানে নিয়োগ পরীক্ষার জন্য রচিত পূর্ণাঙ্গ প্রশ্নব্যাংক ও ব্যাখ্যাসহ সমাধান।</p>
          <div class="banner-stats-row">
            <span class="banner-stat-chip"><i class="fa-solid fa-list-check"></i> মোট প্রশ্ন: ${formatNumber(totalQ)}টি</span>
            <span class="banner-stat-chip"><i class="fa-solid fa-layer-group"></i> ৭টি পূর্ণাঙ্গ বিষয়</span>
            <span class="banner-stat-chip"><i class="fa-solid fa-book-open"></i> ৪৪৮ পৃষ্ঠা সংকলন</span>
            <span class="banner-stat-chip"><i class="fa-solid fa-lightbulb"></i> ১০০% বিস্তারিত সমাধান</span>
          </div>
        `;
      } else {
        const subj = rawData.find(s => s.id === currentSubjectId);
        if (!subj) return;
        banner.innerHTML = `
          <span class="banner-top-badge"><i class="fa-solid ${subj.icon}"></i> বিষয়ভিত্তিক প্রস্তুতি</span>
          <h2 class="banner-title">${subj.nameBn} (${subj.nameEn})</h2>
          <p class="banner-sub">${subj.subtitle}</p>
          <div class="banner-stats-row">
            <span class="banner-stat-chip"><i class="fa-solid fa-list-check"></i> প্রশ্ন: ${formatNumber(subj.count)}টি MCQ</span>
            <span class="banner-stat-chip"><i class="fa-solid fa-file-lines"></i> ${subj.pages}</span>
            <span class="banner-stat-chip"><i class="fa-solid fa-check-double"></i> ১০০% নির্ভুল ব্যাখ্যা</span>
          </div>
        `;
      }
    }

    function getFilteredQuestions() {
      let filtered = [];
      const query = searchQuery.trim().toLowerCase();

      rawData.forEach(subj => {
        if (currentSubjectId !== 'all' && subj.id !== currentSubjectId) return;

        subj.questions.forEach(q => {
          const qKey = `${subj.id}_${q.id}`;
          if (bookmarkedOnly && !bookmarks.has(qKey)) return;

          if (query) {
            const matchQ = q.question.toLowerCase().includes(query);
            const matchOpt = q.options.some(o => String(o).toLowerCase().includes(query));
            const matchExp = q.explanation.toLowerCase().includes(query);
            if (!matchQ && !matchOpt && !matchExp) return;
          }

          filtered.push({
            subject: subj,
            question: q,
            key: qKey
          });
        });
      });

      return filtered;
    }

    function renderQuestions() {
      const container = document.getElementById('mcqContainer');
      const allFiltered = getFilteredQuestions();
      const totalFiltered = allFiltered.length;

      // Update count info
      document.getElementById('actionsCountInfo').innerHTML = `
        <i class="fa-solid fa-circle-info" style="color: #2563eb;"></i>
        <span>মোট দেখানো হচ্ছে: <strong>${formatNumber(totalFiltered)}</strong> টি প্রশ্ন</span>
      `;

      if (totalFiltered === 0) {
        container.innerHTML = `
          <div class="empty-state">
            <i class="fa-solid fa-magnifying-glass"></i>
            <h3 style="font-size: 18px; color: #0f172a; margin-bottom: 6px;">কোনো প্রশ্ন পাওয়া যায়নি</h3>
            <p>আপনার সার্চ কীওয়ার্ড বা ফিল্টার পরিবর্তন করে আবার চেষ্টা করুন।</p>
          </div>
        `;
        document.getElementById('paginationContainer').innerHTML = '';
        return;
      }

      // Pagination slice
      let itemsToRender = allFiltered;
      let totalPages = 1;
      if (perPage !== 'all') {
        totalPages = Math.ceil(totalFiltered / perPage);
        if (currentPage > totalPages) currentPage = totalPages;
        if (currentPage < 1) currentPage = 1;
        const startIdx = (currentPage - 1) * perPage;
        itemsToRender = allFiltered.slice(startIdx, startIdx + perPage);
      }

      let html = '';
      itemsToRender.forEach(item => {
        const s = item.subject;
        const q = item.question;
        const qKey = item.key;
        const isBookmarked = bookmarks.has(qKey);
        const userAns = userAnswers[qKey];
        const correctIdx = normalizeAnswerLetter(q.answer);

        html += `
          <div class="mcq-card" id="card_${qKey}">
            <div class="mcq-header">
              <div class="mcq-meta-left">
                <span class="q-number-pill">#${formatNumber(q.id)}</span>
                <span class="subject-pill" style="background: ${s.badgeColor}15; color: ${s.badgeColor}; border-color: ${s.badgeColor}30;">
                  <i class="fa-solid ${s.icon}"></i> ${s.nameBn}
                </span>
                ${q.page ? `<span class="page-pill"><i class="fa-regular fa-file-lines"></i> পৃষ্ঠা ${formatNumber(q.page)}</span>` : ''}
              </div>
              <button class="btn-bookmark ${isBookmarked ? 'bookmarked' : ''}" onclick="toggleBookmark('${qKey}')" title="${isBookmarked ? 'বুকমার্ক মুছুন' : 'বুকমার্ক করুন'}">
                <i class="fa-${isBookmarked ? 'solid' : 'regular'} fa-star"></i>
              </button>
            </div>

            <div class="mcq-question">
              ${formatTextAndMath(q.question)}
            </div>

            <div class="options-grid">
        `;

        q.options.forEach((opt, oIdx) => {
          let extraClass = '';
          const optLetter = getOptionMarker(oIdx);

          if (currentMode === 'study') {
            if (correctIdx !== null && oIdx === correctIdx) {
              extraClass = 'study-correct-indicator';
            }
          } else if (currentMode === 'practice' && userAns) {
            extraClass = 'locked ';
            if (oIdx === userAns.selectedIdx) {
              extraClass += userAns.isCorrect ? 'opt-correct' : 'opt-wrong';
            }
            if (!userAns.isCorrect && correctIdx !== null && oIdx === correctIdx) {
              extraClass += ' opt-correct';
            }
          }

          html += `
            <button class="option-btn ${extraClass}" onclick="handleOptionSelect('${qKey}', ${oIdx})">
              <span class="opt-letter">${optLetter}</span>
              <span>${formatTextAndMath(opt)}</span>
            </button>
          `;
        });

        html += `
            </div>

            <!-- Explanation Wrap -->
            <div class="mcq-explanation-wrap ${showAllExplanations || (userAns && currentMode === 'practice') ? '' : 'hidden'}" id="exp_${qKey}">
              <div class="exp-title-row">
                <i class="fa-solid fa-lightbulb" style="color: #f59e0b;"></i>
                <span>সঠিক উত্তর: <strong>${q.answer || '—'}</strong></span>
              </div>
              <div class="exp-body">${q.explanation ? formatTextAndMath(q.explanation) : 'এই প্রশ্নের জন্য কোনো অতিরিক্ত ব্যাখ্যা নেই।'}</div>
            </div>

            <div class="mcq-footer-actions">
              <span>BPSC নন-টেক MCQ ডাইজেস্ট</span>
              <button class="btn-toggle-exp" onclick="toggleSingleExp('${qKey}')">
                <i class="fa-solid fa-eye"></i> ব্যাখ্যা দেখুন / লুকান
              </button>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
      renderPagination(totalPages);
    }

    function renderPagination(totalPages) {
      const container = document.getElementById('paginationContainer');
      if (perPage === 'all' || totalPages <= 1) {
        container.innerHTML = '';
        return;
      }

      let html = `
        <button class="page-btn" onclick="goToPage(1)" ${currentPage === 1 ? 'disabled' : ''} title="প্রথম পৃষ্ঠা">
          <i class="fa-solid fa-angles-left"></i>
        </button>
        <button class="page-btn" onclick="goToPage(${currentPage - 1})" ${currentPage === 1 ? 'disabled' : ''} title="আগের পৃষ্ঠা">
          <i class="fa-solid fa-chevron-left"></i>
        </button>
      `;

      let startP = Math.max(1, currentPage - 2);
      let endP = Math.min(totalPages, currentPage + 2);

      if (startP > 1) {
        html += `<button class="page-btn" onclick="goToPage(1)">${formatNumber(1)}</button>`;
        if (startP > 2) html += `<span style="color: #94a3b8; padding: 0 4px;">...</span>`;
      }

      for (let p = startP; p <= endP; p++) {
        html += `
          <button class="page-btn ${p === currentPage ? 'active' : ''}" onclick="goToPage(${p})">
            ${formatNumber(p)}
          </button>
        `;
      }

      if (endP < totalPages) {
        if (endP < totalPages - 1) html += `<span style="color: #94a3b8; padding: 0 4px;">...</span>`;
        html += `<button class="page-btn" onclick="goToPage(${totalPages})">${formatNumber(totalPages)}</button>`;
      }

      html += `
        <button class="page-btn" onclick="goToPage(${currentPage + 1})" ${currentPage === totalPages ? 'disabled' : ''} title="পরের পৃষ্ঠা">
          <i class="fa-solid fa-chevron-right"></i>
        </button>
        <button class="page-btn" onclick="goToPage(${totalPages})" ${currentPage === totalPages ? 'disabled' : ''} title="শেষ পৃষ্ঠা">
          <i class="fa-solid fa-angles-right"></i>
        </button>
      `;

      container.innerHTML = html;
    }

    function goToPage(p) {
      currentPage = p;
      renderQuestions();
      scrollToTop();
    }

    function handleOptionSelect(qKey, optIdx) {
      if (currentMode !== 'practice') return;
      if (userAnswers[qKey]) return; // already answered

      // Find question
      const [subjId, qIdStr] = qKey.split('_');
      const qId = parseInt(qIdStr);
      const subj = rawData.find(s => s.id === subjId);
      if (!subj) return;
      const q = subj.questions.find(item => item.id === qId);
      if (!q) return;

      const correctIdx = normalizeAnswerLetter(q.answer);
      const isCorrect = correctIdx !== null && optIdx === correctIdx;

      userAnswers[qKey] = {
        selectedIdx: optIdx,
        correctIdx: correctIdx,
        isCorrect: isCorrect
      };

      updatePracticeScorecard();
      renderQuestions();
    }

    function updatePracticeScorecard() {
      const keys = Object.keys(userAnswers);
      const attempted = keys.length;
      let correct = 0;
      keys.forEach(k => {
        if (userAnswers[k].isCorrect) correct++;
      });
      const wrong = attempted - correct;
      const accuracy = attempted > 0 ? Math.round((correct / attempted) * 100) : 0;

      document.getElementById('scoreAttempted').innerText = formatNumber(attempted);
      document.getElementById('scoreCorrect').innerText = formatNumber(correct);
      document.getElementById('scoreWrong').innerText = formatNumber(wrong);
      document.getElementById('scoreAccuracy').innerText = formatNumber(accuracy) + '%';
    }

    function resetPracticeScore() {
      userAnswers = {};
      updatePracticeScorecard();
      renderQuestions();
    }

    function switchMode(mode) {
      currentMode = mode;
      document.getElementById('modeStudy').classList.toggle('active', mode === 'study');
      document.getElementById('modePractice').classList.toggle('active', mode === 'practice');
      document.getElementById('practiceScorecard').style.display = mode === 'practice' ? 'block' : 'none';
      renderQuestions();
    }

    function handleSearch(val) {
      searchQuery = val;
      currentPage = 1;
      renderQuestions();
    }

    function toggleBookmark(qKey) {
      if (bookmarks.has(qKey)) {
        bookmarks.delete(qKey);
      } else {
        bookmarks.add(qKey);
      }
      localStorage.setItem('bpsc_bookmarks', JSON.stringify(Array.from(bookmarks)));
      renderQuestions();
    }

    function toggleBookmarkedFilter(checked) {
      bookmarkedOnly = checked;
      currentPage = 1;
      renderQuestions();
    }

    function toggleAllExplanations(checked) {
      showAllExplanations = checked;
      document.querySelectorAll('.mcq-explanation-wrap').forEach(el => {
        if (checked) {
          el.classList.remove('hidden');
        } else {
          el.classList.add('hidden');
        }
      });
    }

    function toggleSingleExp(qKey) {
      const el = document.getElementById(`exp_${qKey}`);
      if (el) {
        el.classList.toggle('hidden');
      }
    }

    function changePerPage(val) {
      perPage = val === 'all' ? 'all' : parseInt(val);
      currentPage = 1;
      renderQuestions();
    }

    function toggleNumberFormat() {
      numFormat = numFormat === 'bn' ? 'en' : 'bn';
      document.getElementById('numLangLabel').innerText = numFormat === 'bn' ? 'সংখ্যা: বাংলা' : 'সংখ্যা: English';
      renderSubjectTabs();
      renderBanner();
      updatePracticeScorecard();
      renderQuestions();
    }

    function changeFont(fontKey) {
      const fontMap = {
        'hind': "'Hind Siliguri', sans-serif",
        'anek': "'Anek Bangla', sans-serif",
        'noto': "'Noto Sans Bengali', sans-serif",
        'inter': "'Inter', sans-serif"
      };
      document.body.style.fontFamily = fontMap[fontKey] || fontMap['hind'];
    }

    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Initialize
    window.addEventListener('DOMContentLoaded', () => {
      renderSubjectTabs();
      renderBanner();
      renderQuestions();
    });
  </script>
</body>
</html>
"""

final_html = html_template.replace("JSON_DATA_PLACEHOLDER", json_data_str)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated {OUTPUT_FILE} with size {len(final_html)/1024/1024:.2f} MB!")
