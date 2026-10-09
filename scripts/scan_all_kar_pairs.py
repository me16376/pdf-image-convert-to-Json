import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

# Bengali vowel marks (kar signs):
# া (09be), ি (09bf), ী (09c0), ু (09c1), ূ (09c2), ৃ (09c3), ৄ (09c4), ে (09c7), ৈ (09c8), ো (09cb), ৌ (09cc)
KAR_CHARS = r'[\u09be\u09bf\u09c0\u09c1\u09c2\u09c3\u09c4\u09c7\u09c8\u09cb\u09cc]'

found_pairs = {}

for root, dirs, files in sorted(os.walk(base)):
    for f in sorted(files):
        if not f.endswith('.json'): continue
        p = os.path.join(root, f)
        with open(p, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        for q in d['questions']:
            all_t = [('q', q['question'])] + [(f'opt{i}', o) for i, o in enumerate(q['options'])]
            for field, t in all_t:
                for m in re.finditer(f'([^\s\(\)\[\]\,\.\?\!\'\"]*{KAR_CHARS}{{2,}}[^\s\(\)\[\]\,\.\?\!\'\"]*)', t):
                    w = m.group(0)
                    found_pairs.setdefault(w, []).append((f, q['id']))

print(f"Total unique words with adjacent kar marks: {len(found_pairs)}")
for w in sorted(found_pairs.keys()):
    print(f"  {repr(w)} (found {len(found_pairs[w])} times)")
