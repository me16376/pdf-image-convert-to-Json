# -*- coding: utf-8 -*-
import glob
import json
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('JSON Data/BPSC ICT Wizard/*.json'))
total_mcqs = 0
all_valid = True

for fpath in files:
    fname = fpath.replace('\\', '/').split('/')[-1]
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    print(f"{fname}: {len(data)} MCQs")
    total_mcqs += len(data)
    
    answers = set()
    for idx, item in enumerate(data):
        answers.add(item.get('answer'))
        if not ('id' in item and 'question' in item and 'options' in item and 'answer' in item):
            print(f"Error in {fname} item {idx}: missing keys")
            all_valid = False
        if not isinstance(item['options'], list) or len(item['options']) < 2:
            print(f"Error in {fname} item {item.get('id')}: options not valid list")
            all_valid = False
        for o_idx, opt in enumerate(item['options']):
            if not opt or not str(opt).strip():
                print(f"Error in {fname} item {item.get('id')}: option {o_idx} is empty")
                all_valid = False
        if not item['question'] or not str(item['question']).strip():
            print(f"Error in {fname} item {item.get('id')}: question is empty")
            all_valid = False
    print(f"   Answers present: {sorted(list(str(a) for a in answers))}")

print("-" * 50)
print(f"Total MCQs across all 11 files: {total_mcqs}")
print(f"Schema Validation Status: {'PASSED' if all_valid else 'FAILED'}")
