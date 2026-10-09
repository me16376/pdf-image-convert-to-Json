import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

found = []
for root, dirs, files in sorted(os.walk(base)):
    for f in sorted(files):
        if not f.endswith('.json'): continue
        p = os.path.join(root, f)
        with open(p, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        for q in d['questions']:
            all_t = [('q', q['question'])] + [(f'opt{i}', o) for i, o in enumerate(q['options'])]
            for field, t in all_t:
                for m in re.finditer(r'([^\s\(\)\[\]\,\.\?\!\'\"]*[\u09c7][\u09bf][^\s\(\)\[\]\,\.\?\!\'\"]*)', t):
                    found.append((f, q['id'], field, m.group(0), t[:60]))

print(f"Total occurrences of ei: {len(found)}")
unique_words = sorted(set(it[3] for it in found))
for w in unique_words:
    print("  word:", repr(w))
