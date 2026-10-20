# -*- coding: utf-8 -*-
"""
Build standalone interactive web application BUET-Pattern.html
with complete embedded dataset of all 57 chapters (5,460 MCQs)
across Bangla, English, Math, and GK.
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.join("JSON Data", "BUET Patern")

SUBJECTS_CONFIG = [
    {
        "id": "Bangla",
        "nameBn": "বাংলা",
        "icon": "fa-book",
        "prefix": "bn",
        "badgeColor": "#e11d48",
        "files": [
            ("ভাষা ও ব্যাকরণ.json", "ভাষা ও ব্যাকরণ", "Pages 3–8"),
            ("ধ্বনি, বর্ণ ও যুক্তবর্ণ.json", "ধ্বনি, বর্ণ ও যুক্তবর্ণ", "Pages 8–12"),
            ("ণত্ব ও ষত্ব বিধান, পরিভাষা.json", "ণত্ব ও ষত্ব বিধান, পরিভাষা", "Pages 12–15"),
            ("সন্ধি ও সমাস.json", "সন্ধি ও সমাস", "Pages 15–28"),
            ("শব্দ ও শব্দার্থ.json", "শব্দ ও শব্দার্থ", "Pages 29–42"),
            ("পদ প্রকরণ, ক্রিয়ার কাল.json", "পদ প্রকরণ, ক্রিয়ার কাল", "Pages 43–47"),
            ("উপসর্গ-অনুসর্গ.json", "উপসর্গ-অনুসর্গ", "Pages 47–49"),
            ("প্রকৃতি ও প্রত্যয়.json", "প্রকৃতি ও প্রত্যয়", "Pages 50–52"),
            ("সংখ্যা, কারক ও বিভক্তি.json", "সংখ্যা, কারক ও বিভক্তি", "Pages 52–57"),
            ("যতি বা ছেদ চিহ্ন, বাক্য ও বাক্য শুদ্ধি.json", "যতি বা ছেদ চিহ্ন, বাক্য ও বাক্য শুদ্ধি", "Pages 57–63"),
            ("বানান ও শুদ্ধিকরণ.json", "বানান ও শুদ্ধিকরণ", "Pages 64–72"),
            ("সমার্থক ও বিপরীত শব্দ.json", "সমার্থক ও বিপরীত শব্দ", "Pages 73–82"),
            ("এক কথায় প্রকাশ.json", "এক কথায় প্রকাশ", "Pages 83–88"),
            ("বাগধারা ও প্রবাদ প্রবচন.json", "বাগধারা ও প্রবাদ প্রবচন", "Pages 89–96"),
            ("প্রয়োগ-অপপ্রয়োগ, লিঙ্গান্তর.json", "প্রয়োগ-অপপ্রয়োগ, লিঙ্গান্তর", "Pages 97–99"),
            ("বাংলা সাহিত্য.json", "বাংলা সাহিত্য", "Pages 100–134"),
        ]
    },
    {
        "id": "English",
        "nameBn": "ইংরেজি",
        "icon": "fa-language",
        "prefix": "eng",
        "badgeColor": "#2563eb",
        "files": [
            ("Parts of Speech.json", "Parts of Speech", "Pages 137–155"),
            ("Tense.json", "Tense", "Pages 156–158"),
            ("Right Form of Verb.json", "Right Form of Verb", "Pages 159–168"),
            ("Corrections.json", "Corrections", "Pages 169–182"),
            ("Narration.json", "Narration", "Pages 183–188"),
            ("Synonyms & Antonyms.json", "Synonyms & Antonyms", "Pages 189–215"),
            ("Article.json", "Article", "Pages 216–218"),
            ("Degree.json", "Degree", "Pages 218–219"),
            ("Conjunction & Verb.json", "Conjunction & Verb", "Pages 219–220"),
            ("Preposition.json", "Preposition", "Pages 220–225"),
            ("Appropriate Sentence and Word.json", "Appropriate Sentence and Word", "Pages 225–228"),
            ("Translation.json", "Translation", "Pages 228–233"),
            ("Word Meaning.json", "Word Meaning", "Pages 233–239"),
            ("Voice.json", "Voice", "Pages 240–243"),
            ("Gender and Number.json", "Gender and Number", "Pages 243–244"),
            ("Idioms & Phrases.json", "Idioms & Phrases", "Pages 244"),
            ("English Literature.json", "English Literature", "Pages 244–250"),
        ]
    },
    {
        "id": "Math",
        "nameBn": "গণিত",
        "icon": "fa-calculator",
        "prefix": "math",
        "badgeColor": "#b91c1c",
        "files": [
            ("ভেক্টর.json", "ভেক্টর", "Pages 253–254"),
            ("বাস্তব সংখ্যা.json", "বাস্তব সংখ্যা", "Pages 255–277"),
            ("ল.সা.গু ও গ.সা.গু.json", "ল.সা.গু ও গ.সা.গু", "Pages 277–279"),
            ("সরল ও যৌগিক মুনাফা.json", "সরল ও যৌগিক মুনাফা", "Pages 280–283"),
            ("অনুপাত ও সমানুপাত.json", "অনুপাত ও সমানুপাত", "Pages 284–298"),
            ("শতকরা, লাভ ও ক্ষতি.json", "শতকরা, লাভ ও ক্ষতি", "Pages 298–312"),
            ("বহুপদী উৎপাদক (বীজগণিত).json", "বহুপদী উৎপাদক (বীজগণিত)", "Pages 313–329"),
            ("সরল সহসমীকরণ.json", "সরল সহসমীকরণ", "Pages 330–346"),
            ("সূচক ও লগারিদম.json", "সূচক ও লগারিদম", "Pages 347–353"),
            ("বেগ ও সময়.json", "বেগ ও সময়", "Pages 354–363"),
            ("সমান্তর, গুণোত্তর ও অনুক্রম ধারা.json", "সমান্তর, গুণোত্তর ও অনুক্রম ধারা", "Pages 364–372"),
            ("আংশিক ভগ্নাংশ.json", "আংশিক ভগ্নাংশ", "Page 373"),
            ("জ্যামিতি.json", "জ্যামিতি", "Pages 374–397"),
            ("ত্রিকোণমিতি এবং পরিমিতি.json", "ত্রিকোণমিতি এবং পরিমিতি", "Pages 398–405"),
            ("সেট, বিন্যাস ও সমাবেশ, পরিসংখ্যান ও সম্ভাবনা.json", "সেট, বিন্যাস ও সমাবেশ, পরিসংখ্যান ও সম্ভাবনা", "Pages 406–417"),
            ("ক্যালকুলাস.json", "ক্যালকুলাস", "Pages 417–425"),
            ("ম্যাট্রিক্স ও নির্ণায়ক.json", "ম্যাট্রিক্স ও নির্ণায়ক", "Pages 425–427"),
            ("মানসিক দক্ষতা.json", "মানসিক দক্ষতা", "Pages 428–453"),
        ]
    },
    {
        "id": "GK",
        "nameBn": "সাধারণ জ্ঞান",
        "icon": "fa-earth-americas",
        "prefix": "gk",
        "badgeColor": "#059669",
        "files": [
            ("বাংলাদেশ বিষয়াবলি.json", "বাংলাদেশ বিষয়াবলি", "Pages 457–566"),
            ("আন্তর্জাতিক বিষয়াবলি.json", "আন্তর্জাতিক বিষয়াবলি", "Pages 566–643"),
            ("সাধারণ বিজ্ঞান.json", "সাধারণ বিজ্ঞান", "Pages 643–677"),
            ("কম্পিউটার ও তথ্য প্রযুক্তি.json", "কম্পিউটার ও তথ্য প্রযুক্তি", "Pages 678–696"),
            ("পাওয়ার সেক্টর ও গ্যাস সেক্টর.json", "পাওয়ার সেক্টর ও গ্যাস সেক্টর", "Pages 697–747"),
            ("খেলাধুলা.json", "খেলাধুলা", "Pages 748–750"),
        ]
    }
]

def clean_option_text(t):
    if not t: return ''
    return re.sub(r'^(\([ক-ঙa-eA-E1-5]\)|\[[ক-ঙa-eA-E1-5]\]|[ক-ঙa-eA-E][\)\.\:–—\-]\s*|[1-5][\)\.\:–—\-]\s*)', '', str(t)).strip()

chapters_data = []
total_questions = 0
subject_stats = {}

for s in SUBJECTS_CONFIG:
    s_id = s["id"]
    s_name = s["nameBn"]
    s_icon = s["icon"]
    s_prefix = s["prefix"]
    s_dir = os.path.join(BASE_DIR, s_id)
    s_count = 0

    for idx, (fname, title, pages) in enumerate(s["files"]):
        fpath = os.path.join(s_dir, fname)
        if not os.path.exists(fpath):
            print(f"Warning: file not found: {fpath}")
            continue

        with open(fpath, 'r', encoding='utf-8') as f:
            raw_qs = json.load(f)

        cleaned_qs = []
        for q_idx, q in enumerate(raw_qs):
            opts = q.get("options", [])
            clean_opts = [clean_option_text(o) for o in opts]
            cleaned_qs.append({
                "id": q.get("id", q_idx + 1),
                "question": str(q.get("question", "")).strip(),
                "options": clean_opts,
                "answer": str(q.get("answer", "")).strip(),
                "explanation": str(q.get("explanation", "")).strip()
            })

        q_count = len(cleaned_qs)
        s_count += q_count
        total_questions += q_count

        chapters_data.append({
            "id": f"{s_prefix}_{idx+1}",
            "subject": s_id,
            "subjectBn": s_name,
            "subjectIcon": s_icon,
            "filename": fname,
            "title": title,
            "pages": pages,
            "count": q_count,
            "questions": cleaned_qs
        })

    subject_stats[s_id] = s_count

print(f"Successfully processed {len(chapters_data)} chapters with {total_questions} MCQs total:")
for s in SUBJECTS_CONFIG:
    print(f"  - {s['nameBn']} ({s['id']}): {subject_stats.get(s['id'], 0)} MCQs")

json_data_str = json.dumps(chapters_data, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BUET Pattern (Non Dept.) Question Bank - বুয়েট প্যাটার্ন বিষয় ও অধ্যায়ভিত্তিক প্রশ্নব্যাংক</title>
  <meta name="description" content="Exceptional Question Bank (Non Dept.) - BUET Pattern বাংলা, ইংরেজি, গণিত ও সাধারণ জ্ঞানের ৫৭টি অধ্যায়ের ৫,৪৬০টি নির্ভুল MCQ ও ব্যাখ্যাসহ সমাধান">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Bangla:wght@400;500;600;700;800&family=Hind+Siliguri:wght@400;500;600;700;800&family=Noto+Sans+Bengali:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
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
      --primary: #b91c1c;
      --primary-hover: #991b1b;
      --primary-dark: #7f1d1d;
      --primary-light: #fef2f2;
      --primary-border: #fecaca;
      --success: #059669;
      --success-light: #ecfdf5;
      --danger: #dc2626;
      --danger-light: #fef2f2;
      --amber: #d97706;
      --amber-light: #fffbeb;
      --blue: #2563eb;
      --blue-light: #eff6ff;
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

    /* Top Announcement Strip */
    .portal-nav {
      background: linear-gradient(90deg, #0f172a 0%, #1e1b4b 50%, #450a0a 100%);
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
      background: rgba(225, 29, 72, 0.22);
      color: #fda4af;
      border: 1px solid rgba(253, 164, 175, 0.35);
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
      color: #fca5a5;
      background: rgba(185, 28, 28, 0.28);
      font-weight: 700;
    }

    /* App Header */
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
      width: 46px;
      height: 46px;
      border-radius: 12px;
      background: linear-gradient(135deg, #b91c1c 0%, #dc2626 50%, #e11d48 100%);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      box-shadow: 0 6px 16px rgba(185, 28, 28, 0.28);
      border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .brand-text h1 {
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.4px;
      color: #0f172a;
      line-height: 1.2;
    }

    .brand-text p {
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 2px;
      font-weight: 500;
    }

    /* Actions Toolbar */
    .actions-bar {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 12px;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-sub);
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.15s ease;
      user-select: none;
    }

    .btn:hover {
      background: #f1f5f9;
      border-color: #cbd5e1;
      color: var(--text-main);
    }

    .btn-active {
      background: var(--primary-light) !important;
      color: var(--primary) !important;
      border-color: var(--primary-border) !important;
      box-shadow: 0 1px 3px rgba(185, 28, 28, 0.1);
    }

    .btn-primary {
      background: linear-gradient(135deg, var(--primary) 0%, #dc2626 100%);
      color: #ffffff !important;
      border-color: var(--primary);
      box-shadow: 0 2px 6px rgba(185, 28, 28, 0.25);
    }

    .btn-primary:hover {
      background: linear-gradient(135deg, var(--primary-hover) 0%, #b91c1c 100%);
      transform: translateY(-1px);
    }

    /* Subject Tabs Navigation */
    .subject-nav-tabs {
      display: flex;
      align-items: center;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 6px;
      margin-bottom: 12px;
      border-bottom: 1px solid #f1f5f9;
    }

    .subject-nav-tabs::-webkit-scrollbar {
      height: 4px;
    }
    .subject-nav-tabs::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border-radius: 4px;
    }

    .subject-tab {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 13.5px;
      font-weight: 600;
      background: #f8fafc;
      color: var(--text-sub);
      border: 1px solid var(--border-color);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.16s ease;
      font-family: inherit;
    }

    .subject-tab:hover {
      background: #e2e8f0;
      color: #0f172a;
    }

    .subject-tab.active {
      background: linear-gradient(135deg, #b91c1c 0%, #dc2626 100%);
      color: #ffffff;
      border-color: #b91c1c;
      box-shadow: 0 2px 8px rgba(185, 28, 28, 0.28);
    }

    /* Filter Bar */
    .filter-bar {
      display: grid;
      grid-template-columns: 280px 1fr auto;
      gap: 12px;
      align-items: center;
    }

    .select-wrap {
      position: relative;
    }

    .select-wrap select {
      width: 100%;
      padding: 8px 32px 8px 12px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text-main);
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      appearance: none;
      font-family: inherit;
      cursor: pointer;
      outline: none;
      transition: border-color 0.15s ease;
    }

    .select-wrap select:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(185, 28, 28, 0.1);
    }

    .select-arrow {
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      pointer-events: none;
      color: var(--text-muted);
      font-size: 11px;
    }

    .search-wrap {
      position: relative;
    }

    .search-wrap input {
      width: 100%;
      padding: 8px 12px 8px 36px;
      font-size: 13.5px;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      background: #ffffff;
      font-family: inherit;
      outline: none;
      transition: all 0.15s ease;
    }

    .search-wrap input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(185, 28, 28, 0.1);
    }

    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 13px;
      pointer-events: none;
    }

    .font-select-wrap select {
      padding: 8px 12px;
      font-size: 13px;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      background: #ffffff;
      font-family: inherit;
      cursor: pointer;
      outline: none;
    }

    /* Practice Mode Banner */
    .practice-banner {
      background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
      border: 1px solid #a7f3d0;
      border-radius: 10px;
      padding: 10px 16px;
      margin-top: 12px;
      display: none;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }

    .practice-banner.visible {
      display: flex;
    }

    .practice-scores {
      display: flex;
      align-items: center;
      gap: 16px;
      font-size: 13.5px;
      font-weight: 600;
    }

    .score-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 12.5px;
    }
    .score-badge.correct { background: #10b981; color: #ffffff; }
    .score-badge.wrong { background: #ef4444; color: #ffffff; }
    .score-badge.attempted { background: #0284c7; color: #ffffff; }

    .btn-reset-practice {
      padding: 4px 10px;
      font-size: 12px;
      font-weight: 700;
      color: #065f46;
      background: #ffffff;
      border: 1px solid #6ee7b7;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .btn-reset-practice:hover {
      background: #f0fdf4;
      border-color: #34d399;
    }

    /* Status Bar */
    .status-strip {
      max-width: 1320px;
      margin: 14px auto 0;
      padding: 0 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      font-size: 13.5px;
      color: var(--text-muted);
    }

    .stats-info strong {
      color: var(--text-main);
      font-family: 'Inter', 'Hind Siliguri', sans-serif;
    }

    /* Question Cards Container */
    .main-content {
      max-width: 1320px;
      margin: 16px auto 40px;
      padding: 0 20px;
      flex-grow: 1;
    }

    .sheet-card {
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
      transition: box-shadow 0.2s ease;
    }

    .sheet-card:hover {
      box-shadow: var(--shadow-md);
    }

    .sheet-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      border-bottom: 2px solid #f1f5f9;
      padding-bottom: 12px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }

    .sheet-title {
      font-size: 17px;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sheet-meta {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 12.5px;
      color: var(--text-muted);
    }

    .sheet-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 9px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
    }

    /* Questions 2-Column Grid */
    .questions-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 22px 28px;
    }

    .question-item {
      background: #ffffff;
      border: 1px solid #f1f5f9;
      border-radius: var(--radius-md);
      padding: 16px;
      position: relative;
      transition: all 0.16s ease;
      display: flex;
      flex-direction: column;
    }

    .question-item:hover {
      border-color: #cbd5e1;
      background: #fdfdfd;
    }

    .q-header {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      margin-bottom: 12px;
    }

    .q-num {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 26px;
      height: 26px;
      border-radius: 6px;
      background: #f1f5f9;
      color: #334155;
      font-size: 13px;
      font-weight: 800;
      flex-shrink: 0;
      margin-top: 2px;
    }

    .q-body {
      flex-grow: 1;
      font-size: 15px;
      line-height: 1.6;
      color: #0f172a;
      font-weight: 600;
      white-space: pre-line;
    }

    .exam-tag {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 11.5px;
      font-weight: 700;
      color: #b91c1c;
      background: #fef2f2;
      border: 1px solid #fecaca;
      padding: 1px 7px;
      border-radius: 4px;
      margin-left: 6px;
      white-space: nowrap;
      vertical-align: middle;
    }

    /* Options List */
    .options-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px 10px;
      margin-bottom: 12px;
    }

    .option-btn {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 8px 10px;
      font-size: 13.5px;
      font-family: inherit;
      color: var(--text-sub);
      text-align: left;
      cursor: default;
      display: flex;
      align-items: flex-start;
      gap: 8px;
      line-height: 1.45;
      transition: all 0.14s ease;
      position: relative;
    }

    .practice-active .option-btn {
      cursor: pointer;
    }

    .practice-active .option-btn:hover:not(.opt-selected) {
      background: #f1f5f9;
      border-color: #cbd5e1;
      transform: translateY(-1px);
    }

    .opt-marker {
      font-weight: 700;
      color: var(--text-muted);
      flex-shrink: 0;
      min-width: 18px;
    }

    .opt-text {
      flex-grow: 1;
      word-break: break-word;
    }

    /* Answer States */
    .option-btn.opt-correct {
      background: #ecfdf5 !important;
      border-color: #10b981 !important;
      color: #065f46 !important;
      font-weight: 700;
    }

    .option-btn.opt-incorrect {
      background: #fef2f2 !important;
      border-color: #ef4444 !important;
      color: #991b1b !important;
      font-weight: 700;
    }

    .opt-status-icon {
      position: absolute;
      right: 8px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 13px;
    }

    /* Direct Answer Pill (for fill in the blanks / numeric) */
    .direct-ans-box {
      background: #f0fdf4;
      border: 1px dashed #34d399;
      border-radius: 6px;
      padding: 6px 12px;
      font-size: 13.5px;
      color: #065f46;
      font-weight: 700;
      margin-bottom: 10px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    /* Explanation Drawer */
    .explanation-box {
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-radius: 8px;
      padding: 10px 14px;
      font-size: 13.5px;
      line-height: 1.6;
      color: #78350f;
      margin-top: auto;
      display: block;
      transition: all 0.2s ease;
    }

    .explanation-box.hidden {
      display: none;
    }

    .exp-title {
      font-weight: 800;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
      color: #b45309;
      font-size: 12.5px;
    }

    .btn-toggle-exp-single {
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 12px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      margin-top: 6px;
      font-family: inherit;
    }

    .btn-toggle-exp-single:hover {
      color: var(--primary);
    }

    /* Pagination */
    .pagination-bar {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      margin: 30px auto;
      flex-wrap: wrap;
    }

    .page-btn {
      min-width: 38px;
      height: 38px;
      padding: 0 12px;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      background: #ffffff;
      color: var(--text-sub);
      font-size: 13.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-family: inherit;
      transition: all 0.15s ease;
    }

    .page-btn:hover:not(:disabled) {
      background: #f1f5f9;
      color: #0f172a;
    }

    .page-btn.active {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 2px 6px rgba(185, 28, 28, 0.28);
    }

    .page-btn:disabled {
      opacity: 0.45;
      cursor: not-allowed;
    }

    /* Floating Scroll Top */
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

    /* Math Formula Styles */
    .math-overline {
      text-decoration: overline;
    }
    .math-sym {
      font-weight: bold;
      padding: 0 2px;
    }

    /* Responsive */
    @media (max-width: 960px) {
      .questions-grid {
        grid-template-columns: 1fr;
        gap: 16px;
      }
      .filter-bar {
        grid-template-columns: 1fr;
      }
      .sheet-card {
        padding: 16px;
      }
    }

    @media (max-width: 600px) {
      .options-grid {
        grid-template-columns: 1fr;
      }
      .brand-text h1 {
        font-size: 17px;
      }
    }

    /* Print Styles */
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
        margin: 0 0 24px 0;
      }
      .questions-grid {
        grid-template-columns: 1fr 1fr;
        gap: 14px 20px;
      }
      .question-item {
        border: 1px solid #cbd5e1;
        break-inside: avoid;
        page-break-inside: avoid;
      }
      .explanation-box {
        display: block !important;
      }
    }
  </style>
</head>
<body>

  <!-- Top Announcement Bar -->
  <div class="portal-nav">
    <div class="portal-nav-inner">
      <div class="portal-nav-left">
        <span class="pill-badge"><i class="fa-solid fa-layer-group"></i> BUET Pattern Question Bank</span>
        <span>বাংলা, ইংরেজি, গণিত ও সাধারণ জ্ঞানের ৫৭টি অধ্যায় (৫,৪৬০টি প্রশ্ন)</span>
      </div>
      <div class="portal-links">
        <a href="index.html" class="portal-link"><i class="fa-solid fa-house"></i> হোম পোর্টাল</a>
        <a href="BUET-Pattern.html" class="portal-link active"><i class="fa-solid fa-graduation-cap"></i> BUET Pattern</a>
        <a href="Saif-Sir-NTRCA-Suggestion.html" class="portal-link"><i class="fa-solid fa-award"></i> Saif Sir NTRCA</a>
        <a href="Biddabari-NTRCA.html" class="portal-link"><i class="fa-solid fa-book-open"></i> Biddabari</a>
        <a href="Eminent-Petro-Bangla.html" class="portal-link"><i class="fa-solid fa-fire-flame-curved"></i> Petro Bangla</a>
        <a href="Ampibian-Suggestion.html" class="portal-link"><i class="fa-solid fa-book-bookmark"></i> Ampibian</a>
        <a href="Ict-wizard-NTRCA-313-and-325.html" class="portal-link"><i class="fa-solid fa-laptop-code"></i> ICT Wizard</a>
        <a href="class 9-10-Computer-GK.html" class="portal-link"><i class="fa-solid fa-desktop"></i> Computer GK</a>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="app-header">
    <div class="header-container">
      <div class="header-top-row">
        <a href="BUET-Pattern.html" class="brand-area">
          <div class="brand-logo"><i class="fa-solid fa-building-columns"></i></div>
          <div class="brand-text">
            <h1>BUET Pattern (Non Dept.) Question Bank</h1>
            <p>Exceptional Question Bank • ৪টি বিষয় • ৫৭টি অধ্যায় • ৫,৪৬০টি MCQ</p>
          </div>
        </a>

        <!-- Toolbar Buttons -->
        <div class="actions-bar">
          <!-- Practice Mode Toggle -->
          <button class="btn" id="btnTogglePractice" title="অনুশীলন মোড চালু বা বন্ধ করুন">
            <i class="fa-solid fa-bullseye"></i> <span id="practiceText">অনুশীলন করুন</span>
          </button>

          <!-- Show/Hide Answers Toggle -->
          <button class="btn" id="btnToggleAnswers" title="সকল সঠিক উত্তর দেখুন বা লুকান">
            <i class="fa-solid fa-eye"></i> <span id="ansText">উত্তর দেখুন</span>
          </button>

          <!-- Show/Hide Explanations Toggle -->
          <button class="btn btn-active" id="btnToggleExp" title="সকল ব্যাখ্যা দেখুন বা লুকান">
            <i class="fa-solid fa-lightbulb"></i> <span id="expText">ব্যাখ্যা লুকান</span>
          </button>

          <!-- Number Format Toggle -->
          <button class="btn" id="btnToggleNum" title="বাংলা বা ইংরেজি সংখ্যা পরিবর্তন">
            <i class="fa-solid fa-arrow-down-1-9"></i> <span id="numLangText">সংখ্যা: বাংলা</span>
          </button>

          <!-- Print / PDF -->
          <button class="btn btn-primary" onclick="window.print()" title="প্রিন্ট করুন বা PDF এ সংরক্ষণ করুন">
            <i class="fa-solid fa-print"></i> <span>প্রিন্ট / PDF</span>
          </button>
        </div>
      </div>

      <!-- Subject Tabs -->
      <div class="subject-nav-tabs" id="subjectNavTabs">
        <button class="subject-tab active" data-subject="all" onclick="selectSubject('all')">
          <i class="fa-solid fa-layer-group"></i> সকল বিষয় (৫,৪৬০)
        </button>
        <button class="subject-tab" data-subject="Bangla" onclick="selectSubject('Bangla')">
          <i class="fa-solid fa-book"></i> বাংলা (১,১৩৫)
        </button>
        <button class="subject-tab" data-subject="English" onclick="selectSubject('English')">
          <i class="fa-solid fa-language"></i> ইংরেজি (১,০২৩)
        </button>
        <button class="subject-tab" data-subject="Math" onclick="selectSubject('Math')">
          <i class="fa-solid fa-calculator"></i> গণিত (১,০০১)
        </button>
        <button class="subject-tab" data-subject="GK" onclick="selectSubject('GK')">
          <i class="fa-solid fa-earth-americas"></i> সাধারণ জ্ঞান (২,৩০১)
        </button>
      </div>

      <!-- Filters & Search -->
      <div class="filter-bar">
        <!-- Chapter Selector -->
        <div class="select-wrap">
          <select id="chapterSelect" aria-label="অধ্যায় নির্বাচন করুন" onchange="onChapterChange(this.value)">
            <option value="all">সকল অধ্যায় (৫,৪৬০টি প্রশ্ন)</option>
          </select>
          <span class="select-arrow"><i class="fa-solid fa-chevron-down"></i></span>
        </div>

        <!-- Search Input -->
        <div class="search-wrap">
          <span class="search-icon"><i class="fa-solid fa-magnifying-glass"></i></span>
          <input type="text" id="searchInput" placeholder="প্রশ্ন, অপশন বা ব্যাখ্যার মধ্যে খুঁজুন..." autocomplete="off">
        </div>

        <!-- Font Selector -->
        <div class="font-select-wrap">
          <select id="fontSelect" onchange="applyFont(this.value)" aria-label="ফন্ট পরিবর্তন">
            <option value="hind">Hind Siliguri</option>
            <option value="anek">Anek Bangla</option>
            <option value="noto">Noto Sans Bengali</option>
            <option value="inter">Inter (Default)</option>
          </select>
        </div>
      </div>

      <!-- Practice Banner -->
      <div class="practice-banner" id="practiceBanner">
        <div class="practice-scores">
          <span><i class="fa-solid fa-bullseye"></i> <strong>অনুশীলন মোড:</strong> অপশনে ক্লিক করে পরীক্ষা দিন</span>
          <span class="score-badge attempted"><i class="fa-solid fa-pen"></i> চেষ্টা: <span id="scoreAttempted">০</span></span>
          <span class="score-badge correct"><i class="fa-solid fa-check"></i> সঠিক: <span id="scoreCorrect">০</span></span>
          <span class="score-badge wrong"><i class="fa-solid fa-xmark"></i> ভুল: <span id="scoreWrong">০</span></span>
          <span style="color: #065f46; font-weight: 700;">নির্ভুলতা: <span id="scoreAccuracy">০%</span></span>
        </div>
        <button class="btn-reset-practice" onclick="resetPracticeAnswers()">অনুশীলন রিসেট</button>
      </div>
    </div>
  </header>

  <!-- Status Bar -->
  <div class="status-strip">
    <div class="stats-info" id="statsInfo">
      মোট প্রশ্ন: <strong>৫,৪৬০</strong> টি | প্রদর্শিত: <strong>৫,৪৬০</strong> টি
    </div>

    <div class="view-controls">
      <label for="perPageSelect" style="font-size: 13px;">পৃষ্ঠা প্রতি শিট:</label>
      <select id="perPageSelect" onchange="onPerPageChange(this.value)" style="padding: 4px 8px; border-radius: 6px; border: 1px solid #cbd5e1; font-family: inherit;">
        <option value="10">১০ টি</option>
        <option value="20" selected>২০ টি</option>
        <option value="50">৫০ টি</option>
        <option value="all">সব প্রশ্ন একসাথে</option>
      </select>
    </div>
  </div>

  <!-- Main Sheets Content -->
  <main class="main-content" id="sheetsContainer"></main>

  <!-- Pagination Controls -->
  <div class="pagination-bar" id="paginationBar"></div>

  <!-- Scroll to Top -->
  <button class="scroll-top-btn" id="scrollTopBtn" title="উপরে যান" onclick="window.scrollTo({ top: 0, behavior: 'smooth' })">
    <i class="fa-solid fa-arrow-up"></i>
  </button>

  <script>
    // Embedded Complete Dataset of BUET Pattern (57 Chapters, 5,460 MCQs)
    const chaptersData = __JSON_DATA__;

    // State Variables
    let currentSubject = 'all';
    let currentChapter = 'all';
    let searchQuery = '';
    let practiceMode = false;
    let showAllAnswers = false;
    let showAllExplanations = true;
    let numFormat = 'bn';
    let perPage = 20;
    let currentPage = 1;
    let userAnswers = {}; // key: qKey -> { selectedIdx, isCorrect }

    const FONT_FAMILIES = {
      hind: "'Hind Siliguri', 'Inter', sans-serif",
      anek: "'Anek Bangla', 'Inter', sans-serif",
      noto: "'Noto Sans Bengali', 'Inter', sans-serif",
      inter: "'Inter', sans-serif"
    };

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
      const bnMarkers = ['(ক)', '(খ)', '(গ)', '(ঘ)'];
      const enMarkers = ['(a)', '(b)', '(c)', '(d)'];
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

    function formatMathAndText(text) {
      if (!text) return '';
      let s = String(text).trim();

      // Detect institution / exam tags like [DESCO-ME-19], [46th BCS]
      s = s.replace(/\\[([^\\]]+)\\]/g, '<span class="exam-tag"><i class="fa-solid fa-tag"></i> $1</span>');

      // KaTeX math rendering if LaTeX characters present
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

    function applyFont(fontKey) {
      if (!FONT_FAMILIES[fontKey]) fontKey = 'hind';
      document.body.style.fontFamily = FONT_FAMILIES[fontKey];
      try { localStorage.setItem('buet_pattern_font', fontKey); } catch(e) {}
    }

    function populateChapterDropdown() {
      const select = document.getElementById('chapterSelect');
      const filteredChapters = currentSubject === 'all' 
        ? chaptersData 
        : chaptersData.filter(c => c.subject === currentSubject);

      let totalFilteredQ = filteredChapters.reduce((acc, c) => acc + c.count, 0);

      let html = `<option value="all">সকল অধ্যায় (${formatNumber(totalFilteredQ)}টি প্রশ্ন)</option>`;
      filteredChapters.forEach(c => {
        html += `<option value="${c.id}">${c.title} (${formatNumber(c.count)}টি প্রশ্ন)</option>`;
      });
      select.innerHTML = html;
      select.value = currentChapter;
    }

    function selectSubject(subj) {
      currentSubject = subj;
      currentChapter = 'all';
      currentPage = 1;

      // Update subject tabs UI
      document.querySelectorAll('.subject-tab').forEach(tab => {
        if (tab.dataset.subject === subj) {
          tab.classList.add('active');
        } else {
          tab.classList.remove('active');
        }
      });

      populateChapterDropdown();
      render();
    }

    function onChapterChange(chapId) {
      currentChapter = chapId;
      currentPage = 1;
      render();
    }

    function onPerPageChange(val) {
      perPage = val === 'all' ? 'all' : parseInt(val);
      currentPage = 1;
      render();
    }

    function togglePracticeMode() {
      practiceMode = !practiceMode;
      const btn = document.getElementById('btnTogglePractice');
      const banner = document.getElementById('practiceBanner');
      if (practiceMode) {
        btn.classList.add('btn-active');
        banner.classList.add('visible');
        document.body.classList.add('practice-active');
      } else {
        btn.classList.remove('btn-active');
        banner.classList.remove('visible');
        document.body.classList.remove('practice-active');
      }
      render();
    }

    function toggleAnswers() {
      showAllAnswers = !showAllAnswers;
      const btn = document.getElementById('btnToggleAnswers');
      const text = document.getElementById('ansText');
      if (showAllAnswers) {
        btn.classList.add('btn-active');
        text.innerText = 'উত্তর লুকান';
      } else {
        btn.classList.remove('btn-active');
        text.innerText = 'উত্তর দেখুন';
      }
      render();
    }

    function toggleExplanations() {
      showAllExplanations = !showAllExplanations;
      const btn = document.getElementById('btnToggleExp');
      const text = document.getElementById('expText');
      if (showAllExplanations) {
        btn.classList.add('btn-active');
        text.innerText = 'ব্যাখ্যা লুকান';
      } else {
        btn.classList.remove('btn-active');
        text.innerText = 'ব্যাখ্যা দেখুন';
      }
      render();
    }

    function toggleNumberFormat() {
      numFormat = numFormat === 'bn' ? 'en' : 'bn';
      document.getElementById('numLangText').innerText = numFormat === 'bn' ? 'সংখ্যা: বাংলা' : 'সংখ্যা: English';
      populateChapterDropdown();
      render();
    }

    function handleOptionClick(chapId, qId, optIdx) {
      if (!practiceMode) return;
      const qKey = `${chapId}_${qId}`;
      if (userAnswers[qKey]) return; // already answered

      const chap = chaptersData.find(c => c.id === chapId);
      if (!chap) return;
      const q = chap.questions.find(item => item.id === qId);
      if (!q) return;

      const correctIdx = normalizeAnswerLetter(q.answer);
      const optText = String(q.options[optIdx] || '').trim();
      const ansText = String(q.answer || '').trim();
      const isCorrect = (correctIdx !== null && optIdx === correctIdx) || 
                        (ansText === optText) ||
                        (optText.length > 2 && ansText.toLowerCase().includes(optText.toLowerCase()));

      userAnswers[qKey] = {
        selectedIdx: optIdx,
        correctIdx: correctIdx,
        isCorrect: isCorrect
      };

      updatePracticeScore();
      render();
    }

    function updatePracticeScore() {
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

    function resetPracticeAnswers() {
      userAnswers = {};
      updatePracticeScore();
      render();
    }

    function toggleSingleExp(qKey) {
      const el = document.getElementById(`exp_${qKey}`);
      if (el) {
        el.classList.toggle('hidden');
      }
    }

    function getFilteredQuestions() {
      let results = [];
      const query = searchQuery.trim().toLowerCase();

      chaptersData.forEach(chap => {
        if (currentSubject !== 'all' && chap.subject !== currentSubject) return;
        if (currentChapter !== 'all' && chap.id !== currentChapter) return;

        chap.questions.forEach(q => {
          if (query) {
            const matchQ = q.question.toLowerCase().includes(query);
            const matchOpt = q.options.some(o => String(o).toLowerCase().includes(query));
            const matchExp = q.explanation.toLowerCase().includes(query);
            if (!matchQ && !matchOpt && !matchExp) return;
          }
          results.push({
            chapter: chap,
            question: q
          });
        });
      });

      return results;
    }

    function render() {
      const container = document.getElementById('sheetsContainer');
      const allFiltered = getFilteredQuestions();
      const totalFiltered = allFiltered.length;

      // Update stats info
      document.getElementById('statsInfo').innerHTML = 
        `মোট প্রশ্ন: <strong>${formatNumber(5460)}</strong> টি | ফিল্টার অনুযায়ী: <strong>${formatNumber(totalFiltered)}</strong> টি`;

      if (totalFiltered === 0) {
        container.innerHTML = `
          <div style="text-align: center; padding: 60px 20px; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0;">
            <i class="fa-solid fa-magnifying-glass" style="font-size: 40px; color: #94a3b8; margin-bottom: 16px;"></i>
            <h3 style="font-size: 18px; color: #0f172a; margin-bottom: 8px;">কোনো প্রশ্ন পাওয়া যায়নি</h3>
            <p style="color: #64748b; font-size: 14px;">আপনার সার্চ বা ফিল্টার পরিবর্তন করে আবার চেষ্টা করুন।</p>
          </div>
        `;
        document.getElementById('paginationBar').innerHTML = '';
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

      // Group items by chapter
      const groupedByChapter = {};
      itemsToRender.forEach(item => {
        const cId = item.chapter.id;
        if (!groupedByChapter[cId]) {
          groupedByChapter[cId] = {
            chapter: item.chapter,
            questions: []
          };
        }
        groupedByChapter[cId].questions.push(item.question);
      });

      // Render cards
      let html = '';
      for (const cId in groupedByChapter) {
        const group = groupedByChapter[cId];
        const chap = group.chapter;
        const qList = group.questions;

        html += `
          <div class="sheet-card">
            <div class="sheet-header">
              <div class="sheet-title">
                <i class="fa-solid ${chap.subjectIcon}" style="color: #b91c1c;"></i>
                <span>${chap.title}</span>
                <span style="font-size: 13px; font-weight: 600; color: #64748b;">(${chap.pages})</span>
              </div>
              <div class="sheet-meta">
                <span class="sheet-badge" style="background: #fef2f2; color: #b91c1c; border: 1px solid #fecaca;">
                  <i class="fa-solid fa-list-check"></i> ${formatNumber(chap.count)}টি প্রশ্ন
                </span>
                <span class="sheet-badge" style="background: #f1f5f9; color: #334155; border: 1px solid #e2e8f0;">
                  ${chap.subjectBn}
                </span>
              </div>
            </div>

            <div class="questions-grid">
        `;

        qList.forEach(q => {
          const qKey = `${chap.id}_${q.id}`;
          const userAns = userAnswers[qKey];
          const correctIdx = normalizeAnswerLetter(q.answer);

          html += `
            <div class="question-item" id="q_${qKey}">
              <div class="q-header">
                <span class="q-num">${formatNumber(q.id)}</span>
                <div class="q-body">${formatMathAndText(q.question)}</div>
              </div>
          `;

          if (q.options && q.options.length > 0) {
            html += `<div class="options-grid">`;
            q.options.forEach((opt, optIdx) => {
              let optClass = 'option-btn';
              let statusIcon = '';

              if (practiceMode && userAns) {
                if (userAns.selectedIdx === optIdx) {
                  optClass += userAns.isCorrect ? ' opt-correct opt-selected' : ' opt-incorrect opt-selected';
                  statusIcon = userAns.isCorrect ? '<i class="fa-solid fa-check opt-status-icon"></i>' : '<i class="fa-solid fa-xmark opt-status-icon"></i>';
                } else if (optIdx === userAns.correctIdx) {
                  optClass += ' opt-correct';
                  statusIcon = '<i class="fa-solid fa-check opt-status-icon"></i>';
                }
              } else if (showAllAnswers) {
                const optText = String(opt || '').trim();
                const ansText = String(q.answer || '').trim();
                if (correctIdx === optIdx || ansText === optText || (optText.length > 2 && ansText.toLowerCase().includes(optText.toLowerCase()))) {
                  optClass += ' opt-correct';
                  statusIcon = '<i class="fa-solid fa-check opt-status-icon"></i>';
                }
              }

              html += `
                <div class="${optClass}" onclick="handleOptionClick('${chap.id}', ${q.id}, ${optIdx})">
                  <span class="opt-marker">${getOptionMarker(optIdx)}</span>
                  <span class="opt-text">${formatMathAndText(opt)}</span>
                  ${statusIcon}
                </div>
              `;
            });
            html += `</div>`;
          } else {
            // Direct Answer
            html += `
              <div class="direct-ans-box">
                <i class="fa-solid fa-bullseye"></i> সঠিক উত্তর: ${formatMathAndText(q.answer)}
              </div>
            `;
          }

          // Explanation
          if (q.explanation && q.explanation.trim()) {
            const isExpHidden = !showAllExplanations && !(practiceMode && userAns);
            html += `
              <div class="explanation-box ${isExpHidden ? 'hidden' : ''}" id="exp_${qKey}">
                <div class="exp-title"><i class="fa-solid fa-lightbulb"></i> ব্যাখ্যা:</div>
                <div>${formatMathAndText(q.explanation)}</div>
              </div>
              <button class="btn-toggle-exp-single" onclick="toggleSingleExp('${qKey}')">
                <i class="fa-solid fa-circle-info"></i> ব্যাখ্যা দেখুন / লুকান
              </button>
            `;
          }

          html += `</div>`; // question-item
        });

        html += `
            </div>
          </div>
        `;
      }

      container.innerHTML = html;
      renderPagination(totalPages);
    }

    function renderPagination(totalPages) {
      const bar = document.getElementById('paginationBar');
      if (totalPages <= 1 || perPage === 'all') {
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
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Event Listeners
    window.addEventListener('DOMContentLoaded', () => {
      populateChapterDropdown();

      // Saved font
      try {
        const savedFont = localStorage.getItem('buet_pattern_font');
        if (savedFont && FONT_FAMILIES[savedFont]) {
          document.getElementById('fontSelect').value = savedFont;
          applyFont(savedFont);
        }
      } catch(e) {}

      // Button listeners
      document.getElementById('btnTogglePractice').addEventListener('click', togglePracticeMode);
      document.getElementById('btnToggleAnswers').addEventListener('click', toggleAnswers);
      document.getElementById('btnToggleExp').addEventListener('click', toggleExplanations);
      document.getElementById('btnToggleNum').addEventListener('click', toggleNumberFormat);

      // Search input with debounce
      let searchTimeout = null;
      document.getElementById('searchInput').addEventListener('input', e => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
          searchQuery = e.target.value;
          currentPage = 1;
          render();
        }, 250);
      });

      // Scroll top button visibility
      window.addEventListener('scroll', () => {
        const btn = document.getElementById('scrollTopBtn');
        if (window.scrollY > 400) {
          btn.classList.add('visible');
        } else {
          btn.classList.remove('visible');
        }
      });

      render();
    });
  </script>
</body>
</html>
"""

final_html = html_template.replace('__JSON_DATA__', json_data_str)

out_file = "BUET-Pattern.html"
with open(out_file, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Generated {out_file} successfully! Size: {os.path.getsize(out_file) / (1024*1024):.2f} MB")
