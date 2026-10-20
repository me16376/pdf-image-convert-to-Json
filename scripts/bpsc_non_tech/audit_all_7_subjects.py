import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"JSON Data\BPSC Non Tech"

subjects = [
    ("Bangla", os.path.join(BASE_DIR, r"Bangla\Bangla.json"), 1248),
    ("English", os.path.join(BASE_DIR, r"English\English.json"), 1558),
    ("Bangladesh Affairs", os.path.join(BASE_DIR, r"Bangladesh Affairs\Bangladesh_Affairs.json"), 613),
    ("International Affairs", os.path.join(BASE_DIR, r"International Affairs\International_Affairs.json"), 540),
    ("Science", os.path.join(BASE_DIR, r"Science\Science.json"), 545),
    ("ICT", os.path.join(BASE_DIR, r"ICT\ICT.json"), 157),
    ("Math", os.path.join(BASE_DIR, r"Math\Math.json"), 1003),
]

valid_answers = {'ক', 'খ', 'গ', 'ঘ', 'ঙ', 'নোট'}
devanagari_pattern = re.compile(r'[\u0900-\u0963\u0966-\u097F]')
assamese_pattern = re.compile(r'[\u09F0\u09F1]')
split_kar_pattern = re.compile(r'\u09C7[\u09BE\u09D7]')
double_kar_pattern = re.compile(r'[\u09BE-\u09CC]{2,}')

total_questions_all = 0
all_passed = True

print("=" * 60)
print("BPSC Non-Tech: Comprehensive 7-Subject Final Audit")
print("=" * 60)

for name, path, expected_count in subjects:
    if not os.path.exists(path):
        print(f"❌ {name}: File NOT FOUND at {path}")
        all_passed = False
        continue

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    count = len(data)
    total_questions_all += count
    status = "✓" if count == expected_count else "❌"
    print(f"\n{status} {name}: {count} MCQs (Expected: {expected_count})")

    # 1. ID Check
    ids = [q.get('id') for q in data]
    expected_ids = list(range(1, count + 1))
    if ids != expected_ids:
        print(f"  ❌ ID sequence error in {name}!")
        all_passed = False

    # 2. Field completeness and validation
    missing_pages = 0
    empty_questions = 0
    invalid_options_len = 0
    empty_option_strings = 0
    invalid_answers_count = 0
    foreign_dev_count = 0
    split_kars_count = 0
    double_kars_count = 0
    assamese_count = 0
    dup_options = []
    unbalanced_katex = []

    for q in data:
        qid = q.get('id')
        p = q.get('page')
        if p is None or not isinstance(p, int):
            missing_pages += 1

        q_text = q.get('question', '')
        if not q_text.strip():
            empty_questions += 1

        opts = q.get('options', [])
        if not isinstance(opts, list) or len(opts) not in (4, 5):
            invalid_options_len += 1
        
        opt_str_list = []
        for opt in opts:
            s = str(opt).strip()
            if not s:
                empty_option_strings += 1
            opt_str_list.append(s)

        if len(opt_str_list) != len(set(opt_str_list)):
            dup_options.append((qid, p, opt_str_list))

        ans = q.get('answer')
        if ans not in valid_answers:
            invalid_answers_count += 1

        # Check raw json text of question
        raw_text = json.dumps(q, ensure_ascii=False)
        if devanagari_pattern.search(raw_text):
            foreign_dev_count += 1
        if assamese_pattern.search(raw_text):
            assamese_count += 1
        if split_kar_pattern.search(raw_text):
            split_kars_count += 1
        if double_kar_pattern.search(raw_text):
            double_kars_count += 1

        # KaTeX balance check
        for field in [q.get('question', ''), q.get('explanation', '')] + opts:
            if not isinstance(field, str): continue
            dollars = [m.start() for m in re.finditer(r'(?<!\\)\$', field)]
            if len(dollars) % 2 != 0:
                unbalanced_katex.append((qid, p, field[:60]))
                break

    print(f"  • Missing 'page' attributes: {missing_pages}")
    print(f"  • Empty questions: {empty_questions}")
    print(f"  • Invalid options count (<4 or >5): {invalid_options_len}")
    print(f"  • Empty option strings: {empty_option_strings}")
    print(f"  • Invalid answers: {invalid_answers_count}")
    print(f"  • Foreign Devanagari: {foreign_dev_count}")
    print(f"  • Rogue Assamese: {assamese_count}")
    print(f"  • Split Kars: {split_kars_count}")
    print(f"  • Double Kars: {double_kars_count}")
    print(f"  • Unbalanced KaTeX ($): {len(unbalanced_katex)}")
    print(f"  • Duplicate options inside question: {len(dup_options)}")
    if dup_options:
        for qid, p, d_opts in dup_options:
            print(f"     -> Q{qid} (p.{p}): {d_opts}")

    if any([missing_pages, empty_questions, invalid_options_len, empty_option_strings, 
            invalid_answers_count, foreign_dev_count, assamese_count, split_kars_count, double_kars_count, 
            len(unbalanced_katex)]):
        all_passed = False

print("\n" + "=" * 60)
print(f"Total MCQs Verified Across All 7 Subjects: {total_questions_all} / 5,664")
print(f"Audit Overall Status: {'ALL CHECKS PASSED PERFECTLY ✓' if all_passed else 'ISSUES FOUND ❌'}")
print("=" * 60)
