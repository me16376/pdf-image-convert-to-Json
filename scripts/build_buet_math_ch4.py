# -*- coding: utf-8 -*-
"""
Builder script for BUET Pattern Math Chapter 4: সরল ও যৌগিক মুনাফা
Compiles pages 280 to 283 into JSON Data/BUET Patern/Math/সরল ও যৌগিক মুনাফা.json
"""

import importlib
import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, "JSON Data", "BUET Patern", "Math", "সরল ও যৌগিক মুনাফা.json")

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

modules = [
    "buet_math_pages.ch4_page_280",
    "buet_math_pages.ch4_page_281",
    "buet_math_pages.ch4_page_282",
    "buet_math_pages.ch4_page_283"
]

all_questions = []

for mod_name in modules:
    mod = importlib.import_module(mod_name)
    qs = getattr(mod, "QUESTIONS", [])
    print(f"Loaded {mod_name}: {len(qs)} questions (IDs: {[q['id'] for q in qs]})")
    all_questions.extend(qs)

print(f"\nTotal questions loaded: {len(all_questions)}")

# Validation
expected_id = 1
errors = []

for idx, q in enumerate(all_questions):
    qid = q.get("id")
    if qid != expected_id:
        errors.append(f"Expected ID {expected_id} at index {idx}, found {qid}")
    expected_id += 1
    
    if not q.get("question"):
        errors.append(f"Empty question text at ID {qid}")
    
    if "options" not in q or not isinstance(q["options"], list):
        errors.append(f"Invalid options at ID {qid}")
        
    if "answer" not in q or not q["answer"]:
        errors.append(f"Missing answer at ID {qid}")
        
    if "explanation" not in q:
        errors.append(f"Missing explanation at ID {qid}")

if errors:
    print("\nValidation Errors:")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)
else:
    print("All validations passed! IDs are continuous 1 to", len(all_questions))

# Write JSON
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=4)

print(f"\nSuccessfully wrote {len(all_questions)} questions to {OUTPUT_PATH}")
