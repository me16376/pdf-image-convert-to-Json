import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

# Common prefixes that take hyphen:
VALID_PREFIXES = {'উপ', 'আর্থ', 'মা', 'ভাই', 'পিতা', 'নন', 'প্রাক', 'পোস্ট', 'ই', 'ইলেকট্রনিক', 'আধেক', 'আধা', 'কো', 'খণ্ড', 'দশক'}

broken_words = []

for root, dirs, files in sorted(os.walk(base)):
    for f in sorted(files):
        if not f.endswith('.json'): continue
        p = os.path.join(root, f)
        with open(p, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        for q in d.get('questions', []):
            qid = q.get('id')
            texts = [('q', q.get('question', ''))] + [(f'opt{i}', o) for i, o in enumerate(q.get('options', []))]
            for field, text in texts:
                if not isinstance(text, str): continue
                # Match word - word
                for m in re.finditer(r'([^\s\(\)\[\]\,\.\?\!\'\"\/]+)\s*-\s*([^\s\(\)\[\]\,\.\?\!\'\"\/]+)', text):
                    w1, w2 = m.group(1), m.group(2)
                    full = m.group(0)
                    # Filter out English hyphens like non-formal, well-known
                    if re.match(r'^[a-zA-Z0-9]+$', w1) and re.match(r'^[a-zA-Z0-9]+$', w2):
                        continue
                    # Filter out years like ২০১৬-২০১৭, dates, etc.
                    if re.match(r'^[০-৯\d]+$', w1) or re.match(r'^[০-৯\d]+$', w2):
                        continue
                    # Filter out single-letter options or prefixes
                    if w1 in VALID_PREFIXES:
                        continue
                    # If either part is short or has known ligature fragment:
                    if len(w1) <= 2 or len(w2) <= 2 or any(k in full for k in ['খি', 'ত', 'প', 'ম', 'ভা', 'ঠা', 'চ', 'দ', 'ল', 'লী', 'িত']):
                        # Check if it's suspicious
                        broken_words.append((f, qid, field, full, text[:80]))

print(f"Total potential broken hyphen words: {len(broken_words)}")
for bw in broken_words[:35]:
    print(f"[{bw[0]}] Q{bw[1]} {bw[2]}: '{bw[3]}' in: {bw[4]}")
