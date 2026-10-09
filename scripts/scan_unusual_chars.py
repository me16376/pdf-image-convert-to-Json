import os
import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

allowed_ranges = [
    (0x0020, 0x007E), # ASCII printable
    (0x0980, 0x09FF), # Bengali block
    (0x00A0, 0x00BF), # Latin-1 symbols (like ° etc)
    (0x2000, 0x206F), # General punctuation (curly quotes, dashes, etc)
    (0x2200, 0x22FF), # Math operators
    (0x0370, 0x03FF), # Greek letters (theta, pi, etc)
    (0x2070, 0x209F), # Superscripts / subscripts
    (0x2700, 0x27BF), # Dingbats (checkmark ✓ etc)
    (0x25A0, 0x25FF), # Geometric shapes (■, ▲, ➢, etc)
]

def is_allowed(c):
    code = ord(c)
    for r_start, r_end in allowed_ranges:
        if r_start <= code <= r_end:
            return True
    return False

weird_chars = []

for root, dirs, files in os.walk(base):
    for f in sorted(files):
        if not f.endswith('.json'): continue
        p = os.path.join(root, f)
        with open(p, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        for q in data.get('questions', []):
            texts = [('q', q.get('question', ''))] + [(f'opt{i}', o) for i, o in enumerate(q.get('options', []))] + [('exp', q.get('explanation', ''))]
            for field, t in texts:
                if not isinstance(t, str): continue
                for c in t:
                    if not is_allowed(c):
                        weird_chars.append((f, q.get('id'), field, c, hex(ord(c)), t[:60]))

print(f"Total non-standard character occurrences found: {len(weird_chars)}")
seen_codes = set()
for item in weird_chars:
    if item[4] not in seen_codes:
        seen_codes.add(item[4])
        print(f"File: {item[0]} Q{item[1]} {item[2]} -> char: {repr(item[3])} (code: {item[4]}) in text: \"{item[5]}\"")
