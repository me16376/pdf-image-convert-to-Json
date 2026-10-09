import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA/GK'
pat = re.compile(r'\b[অ-হ]{0,2}[ড়ঃংৎঢ়ধহশষসঢ়বভ]{3,}[অ-হ]{0,2}\b')

for f in sorted(os.listdir(base)):
    if not f.endswith('.json'): continue
    with open(os.path.join(base, f), 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    for q in d['questions']:
        texts = [('q', q['question'])] + [(f'opt{i}', o) for i, o in enumerate(q['options'])]
        for field, t in texts:
            words = pat.findall(t)
            suspicious = [w for w in words if any(prefix in w for prefix in ['ঠরঃধ', 'ওহভড়', 'জবংড়', 'ঘড়হব', 'চঈও', 'ইটঝ', 'ইরঃ', 'ঠওজ', 'গড়ঃয', 'টঝঅ', 'অটকট', 'ঔটঝ', 'ংবরুব', 'ঁহফবৎ', 'ঝবরুব', 'জবযঁ', 'ঝবৎার', 'ডযধঃ', 'নবহমধ', 'সবধহর'])]
            if suspicious:
                print(f"{f} Q{q['id']} {field}: {suspicious} in: {t[:60]}")
