import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

broken_patterns = [
    re.compile(r'খি\s*-\s*ত'),
    re.compile(r'প\s*-\s*িত'),
    re.compile(r'প\s*-\s*ী'),
    re.compile(r'ম\s*-\s*ল'),
    re.compile(r'ভা\s*-\s*ার'),
    re.compile(r'গা\s*-\s*ীব'),
    re.compile(r'দ\s*-\s*ায়মান'),
    re.compile(r'বিখ\s*-\s*াত'),
    re.compile(r'বি\s*-\s*ু'),
    re.compile(r'(\b[ক-হ]ি?\s*-\s*[ক-হ][া-ৌ]?)'),
    re.compile(r'(?<![a-zA-Z])([ি]{1,3}\s*[\.,])'),
    re.compile(r'\b(ি\s+ও\s+িি|িি\s+ও\s+িিি)\b'),
]

for root, dirs, files in sorted(os.walk(base)):
    for f in sorted(files):
        if not f.endswith('.json'): continue
        p = os.path.join(root, f)
        with open(p, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        for q in data.get('questions', []):
            qid = q.get('id')
            items = [('q', q.get('question', ''))] + [(f'opt{i}', o) for i, o in enumerate(q.get('options', []))]
            for field, text in items:
                if not isinstance(text, str): continue
                for pat in broken_patterns:
                    m = pat.findall(text)
                    if m:
                        print(f"[{f}] Q{qid} {field}: match={m} in text: {text[:100]}")
