import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

def get_inverted_vowels():
    found = []
    for root, dirs, files in sorted(os.walk(base)):
        for f in sorted(files):
            if not f.endswith('.json'): continue
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
            for q in d.get('questions', []):
                qid = q.get('id')
                texts = [('q', q.get('question', ''))] + [(f'opt{i}', o) for i, o in enumerate(q.get('options', []))] + [('exp', q.get('explanation', ''))]
                for field, text in texts:
                    if not isinstance(text, str): continue
                    for m in re.finditer(r'([^\s\(\)\[\]\,\.\?\!]*[ুিা]{2}[^\s\(\)\[\]\,\.\?\!]*)', text):
                        w = m.group(1)
                        if any(pair in w for pair in ['ুি', 'াু', 'িু']):
                            found.append((f, qid, field, w, text[:70]))
    return found

inv = get_inverted_vowels()
print(f"Total inverted vowel words: {len(inv)}")
for it in inv:
    print(f"{it[0]} Q{it[1]} {it[2]}: '{it[3]}' in: {it[4]}")
