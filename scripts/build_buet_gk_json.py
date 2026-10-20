# -*- coding: utf-8 -*-
"""
BUET Pattern GK JSON Builder
Compiles all page_*.py from scripts/buet_gk_pages into topic JSON files under JSON Data/BUET Patern/GK/
"""

import os
import sys
import glob
import importlib.util
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

TOPICS = [
    "বাংলাদেশ বিষয়াবলি",
    "আন্তর্জাতিক বিষয়াবলি",
    "সাধারণ বিজ্ঞান",
    "কম্পিউটার ও তথ্য প্রযুক্তি",
    "পাওয়ার সেক্টর ও গ্যাস সেক্টর",
    "খেলাধুলা"
]

def clean_option(opt):
    if not isinstance(opt, str):
        return ""
    # Strip (ক), [ক], {ক}, or ক., ক), ক-, ক: etc. without touching words like কৃষ্ণ, কয়লা, কক্সবাজার
    return re.sub(r'^(?:[\(\[\{][কখগঘabcdABCD][\)\]\}]|(?:[কখগঘabcdABCD][\.\)\:\-\–]))\s*', '', opt).strip()

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pages_dir = os.path.join(base_dir, "scripts", "buet_gk_pages")
    out_dir = os.path.join(base_dir, "JSON Data", "BUET Patern", "GK")
    os.makedirs(out_dir, exist_ok=True)

    py_files = sorted(glob.glob(os.path.join(pages_dir, "page_*.py")))
    print(f"Found {len(py_files)} page scripts in {pages_dir}")

    topic_questions = {t: [] for t in TOPICS}
    total_q_count = 0

    for py_file in py_files:
        module_name = os.path.splitext(os.path.basename(py_file))[0]
        spec = importlib.util.spec_from_file_location(module_name, py_file)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        topic = getattr(mod, "TOPIC", "বাংলাদেশ বিষয়াবলি")
        questions = getattr(mod, "QUESTIONS", [])

        if topic not in topic_questions:
            topic_questions[topic] = []

        for q in questions:
            q_topic = q.get("topic", topic)
            if q_topic not in topic_questions:
                topic_questions[q_topic] = []

            # Clean options
            opts = [clean_option(o) for o in q.get("options", [])]
            # Ensure answer is just the clean letter
            ans = q.get("answer", "").strip()
            ans_clean = re.sub(r'^(?:উত্তর|Ans|Answer)\s*[:ঃ\-]\s*', '', ans).strip()
            ans_map = {'a': 'ক', 'b': 'খ', 'c': 'গ', 'd': 'ঘ', 'A': 'ক', 'B': 'খ', 'C': 'গ', 'D': 'ঘ'}
            ans_final = ans_map.get(ans_clean, ans_clean)

            topic_questions[q_topic].append({
                "page": getattr(mod, "PAGE", 0),
                "orig_id": q.get("id", 0),
                "question": q.get("question", "").strip(),
                "options": opts,
                "answer": ans_final,
                "explanation": q.get("explanation", "").strip()
            })
            total_q_count += 1

    print(f"Total extracted questions across all pages: {total_q_count}\n")

    for topic, qs in topic_questions.items():
        if not qs:
            continue
        # Re-index id from 1 to N
        final_list = []
        for idx, item in enumerate(qs, start=1):
            final_list.append({
                "id": idx,
                "question": item["question"],
                "options": item["options"],
                "answer": item["answer"],
                "explanation": item["explanation"]
            })

        out_path = os.path.join(out_dir, f"{topic}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(final_list, f, ensure_ascii=False, indent=2)

        print(f"  [✓] {topic}.json: {len(final_list)} MCQs saved to {out_path}")

    print("\nBuild completed successfully!")

if __name__ == "__main__":
    main()
