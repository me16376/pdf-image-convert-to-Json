import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA/English'
found = 0
for f in sorted(os.listdir(base)):
    if not f.endswith('.json'): continue
    with open(os.path.join(base, f), 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    for q in d['questions']:
        texts = [('q', q['question'])] + [(f'opt{i}', o) for i, o in enumerate(q['options'])]
        for field, t in texts:
            if not isinstance(t, str): continue
            if any(k in t for k in ['ঝবহর', 'ঙভভর', 'ঔধহ', 'ইধহ', 'ঝড়হ', 'ঘঅঞ']):
                print(f"{f} Q{q['id']} {field}: {repr(t[:60])}")
                found += 1

print(f"Total English remnants: {found}")
