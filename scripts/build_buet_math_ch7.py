# -*- coding: utf-8 -*-
"""
Builder and validator for BUET Pattern Math Chapter 7: বহুপদী উৎপাদক (বীজগণিত)
Compiles pages 313 to 329 (89 questions) into:
JSON Data/BUET Patern/Math/বহুপদী উৎপাদক (বীজগণিত).json
"""

import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, "JSON Data", "BUET Patern", "Math", "বহুপদী উৎপাদক (বীজগণিত).json")
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

log_path = r'C:\Users\bdCalling\.gemini\antigravity-ide\brain\0788406d-0b5c-4a95-91c8-3c51f5b2c094\.system_generated\logs\transcript_full.jsonl'
lines = open(log_path, encoding='utf-8', errors='ignore').readlines()

cp1300 = json.loads(lines[1300])['content']
s1338 = json.loads(lines[1338])['content']
s1340 = json.loads(lines[1340])['content']

questions = []

def parse_q_line(line, q_id):
    q_match = re.search(r'- Q\d+(?:\s*\([^)]*\))?:\s*`([^`]+)`', line)
    if not q_match:
        raise ValueError(f"Could not parse question text for Q{q_id}: {line}")
    question = q_match.group(1).strip()
    
    if "(Written" in line or "options: []" in line:
        options = []
    else:
        opts_match = re.search(r'->\s*`(\[.*?\])`', line)
        if not opts_match:
            raise ValueError(f"Could not parse options for Q{q_id}: {line}")
        options = json.loads(opts_match.group(1))
    
    ans_match = re.search(r'Ans:\s*`([^`]+)`', line)
    if not ans_match:
        raise ValueError(f"Could not parse answer for Q{q_id}: {line}")
    answer = ans_match.group(1).strip()
    
    expl_match = re.search(r'Expl:\s*`(.*)`', line)
    expl = expl_match.group(1).strip() if expl_match else ""
    expl = expl.replace('\\n', '\n')
    
    return {
        "id": q_id,
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": expl
    }

cp1300_lines = cp1300.splitlines()

# Q1 to Q64
for i in range(1, 65):
    prefix = f"- Q{i}:"
    found = False
    for line in cp1300_lines:
        if line.strip().startswith(prefix):
            q_obj = parse_q_line(line.strip(), i)
            questions.append(q_obj)
            found = True
            break
    if not found:
        raise ValueError(f"Q{i} not found in CP 1300!")

# Q65 to Q76 from s1338
s1338_lines = s1338.splitlines()
for i in range(65, 77):
    found = False
    for line in s1338_lines:
        line_clean = line.strip()
        if line_clean.startswith(f"- Q{i}:") or line_clean.startswith(f"- Q{i} ("):
            q_obj = parse_q_line(line_clean, i)
            # If Q76, supply the complete explanation from image scan
            if i == 76:
                q_obj["explanation"] = "Given equation, |2x - 3| ≤ 1\n⇒ -1 ≤ 2x - 3 ≤ 1\n⇒ -1 + 3 ≤ 2x - 3 + 3 ≤ 1 + 3\n⇒ 2 ≤ 2x ≤ 4\n⇒ 1 ≤ x ≤ 2 (Ans.)"
            questions.append(q_obj)
            found = True
            break
    if not found:
        raise ValueError(f"Q{i} not found in step 1338!")

# Q77 to Q89 from s1340
s1340_lines = s1340.splitlines()
for i in range(77, 90):
    found = False
    for line in s1340_lines:
        line_clean = line.strip()
        if line_clean.startswith(f"- Q{i}:") or line_clean.startswith(f"- Q{i} ("):
            q_obj = parse_q_line(line_clean, i)
            if i == 77:
                # Correct image option (ঘ): 4/3, -∞ (or 4/3, -α)
                q_obj["options"] = ["3/4, ∞", "4/3, ∞", "4/2, ∞", "4/3, -∞"]
            questions.append(q_obj)
            found = True
            break
    if not found:
        raise ValueError(f"Q{i} not found in step 1340!")

print(f"Total questions compiled: {len(questions)}")

# Validation checks
errors = 0
for q in questions:
    qid = q["id"]
    if not q["question"]:
        print(f"Error: Q{qid} empty question")
        errors += 1
    if not q["answer"]:
        print(f"Error: Q{qid} empty answer")
        errors += 1
    if not q["explanation"]:
        print(f"Error: Q{qid} empty explanation")
        errors += 1
    if qid in [27, 59]:
        if q["options"] != []:
            print(f"Warning: Q{qid} should be written with empty options, got {q['options']}")
            errors += 1
    else:
        if len(q["options"]) != 4:
            print(f"Warning: Q{qid} has {len(q['options'])} options: {q['options']}")
            errors += 1

if errors == 0:
    print("ALL 89 QUESTIONS VALIDATED WITH ZERO ERRORS!")

# Save JSON file
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=4)

print(f"Successfully saved {len(questions)} questions to {OUTPUT_PATH}")
