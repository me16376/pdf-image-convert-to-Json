# -*- coding: utf-8 -*-
import os
import sys
import json
import importlib

sys.stdout.reconfigure(encoding='utf-8')

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.abspath(os.path.join(CURRENT_DIR, '../../../JSON Data/BPSC Non Tech/Science/Science.json'))

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Scan all p<number>.py files
page_files = []
for f in os.listdir(CURRENT_DIR):
    if f.startswith('p') and f.endswith('.py') and f[1:-3].isdigit():
        page_num = int(f[1:-3])
        page_files.append((page_num, f[:-3]))

page_files.sort(key=lambda x: x[0])

all_questions = []
for page_num, mod_name in page_files:
    if CURRENT_DIR not in sys.path:
        sys.path.insert(0, CURRENT_DIR)
    mod = importlib.import_module(mod_name)
    qs = None
    for attr in dir(mod):
        val = getattr(mod, attr)
        if isinstance(val, list) and len(val) > 0 and isinstance(val[0], dict) and 'id' in val[0] and 'question' in val[0]:
            qs = val
            break
    if qs is None:
        qs = []
    print(f"Page {page_num}: loaded {len(qs)} questions")
    all_questions.extend(qs)

# Validate all questions
valid_answers = {'ক', 'খ', 'গ', 'ঘ', 'ঙ', 'নোট'}
errors = []
for idx, q in enumerate(all_questions, 1):
    qid = q.get('id')
    if qid != idx:
        errors.append(f"Q ID mismatch at position {idx}: got {qid}")
    if len(q.get('options', [])) not in (4, 5):
        errors.append(f"Q {qid} does not have 4 or 5 options (found {len(q.get('options', []))})")
    ans = q.get('answer')
    if ans not in valid_answers:
        errors.append(f"Q {qid} has invalid answer: {ans}")
    if not q.get('question', '').strip():
        errors.append(f"Q {qid} has empty question text")

if errors:
    print(f"\nVALIDATION FAILED with {len(errors)} errors:")
    for err in errors[:20]:
        print(f" - {err}")
    if len(errors) > 20:
        print(f" ... and {len(errors) - 20} more errors")
    sys.exit(1)
else:
    print("\n✓ Validation PASSED: All questions are consecutive and valid.")

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"Successfully compiled {len(all_questions)} questions from {len(page_files)} pages into:\n{OUTPUT_FILE}")
