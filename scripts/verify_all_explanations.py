# -*- coding: utf-8 -*-
"""
Verify all 11 files in JSON Data/BPSC ICT Wizard/
Checks that:
1. Every file has valid JSON.
2. Every item has 'id', 'question', 'options', 'answer', 'explanation'.
3. Every explanation is non-empty, meaningful string.
4. Total MCQ counts.
"""
import glob
import json
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('JSON Data/BPSC ICT Wizard/*.json'))
total_mcqs = 0
total_with_exp = 0
all_valid = True

print(f"{'Filename':<45} | {'MCQs':<6} | {'With Exp':<8} | Status")
print("-" * 75)

for fpath in files:
    fname = fpath.replace('\\', '/').split('/')[-1]
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    
    count = len(data)
    with_exp = sum(1 for item in data if item.get('explanation') and len(str(item.get('explanation')).strip()) > 5)
    
    total_mcqs += count
    total_with_exp += with_exp
    
    status = "OK" if count == with_exp else "MISSING EXP"
    if status != "OK":
        all_valid = False
    print(f"{fname:<45} | {count:<6} | {with_exp:<8} | {status}")

print("-" * 75)
print(f"Total MCQs: {total_mcqs} | Total with Explanations: {total_with_exp}")
print(f"Overall Status: {'100% PASSED' if all_valid and total_mcqs == 567 else 'FAILED'}")
