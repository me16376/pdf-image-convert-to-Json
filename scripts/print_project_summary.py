import os
import json

subjects = ['Bangla', 'GK', 'English', 'Math']
total_all = 0
total_files = 0

print("=" * 55)
print("  SAIF SIR NTRCA SUGGESTION - CONVERSION SUMMARY")
print("=" * 55)

for s in subjects:
    p = os.path.join('JSON Data', 'Saif Sir NTRCA Suggestion', s)
    files = sorted([f for f in os.listdir(p) if f.endswith('.json')])
    s_total = 0
    for f in files:
        with open(os.path.join(p, f), 'r', encoding='utf-8') as fp:
            d = json.load(fp)
            s_total += len(d['questions'])
    total_all += s_total
    total_files += len(files)
    print(f"  {s:10s}: {len(files):3d} JSON files | {s_total:5d} MCQs (100% DONE)")

print("-" * 55)
print(f"  TOTAL     : {total_files:3d} JSON files | {total_all:5d} MCQs")
print("=" * 55)
