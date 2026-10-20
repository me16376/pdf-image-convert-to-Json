import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect English texts in English and ICT subjects
files = [
    r"JSON Data\BPSC Non Tech\English\English.json",
    r"JSON Data\BPSC Non Tech\ICT\ICT.json",
]

# Patterns for broken English words
broken_english_patterns = [
    # 1. Lowercase letter followed by uppercase (camelCase that might be unspaced words)
    (re.compile(r'\b[a-z]+[A-Z][a-z]+\b'), 'Possible unspaced English words (camelCase)'),
    # 2. English word with punctuation inside that shouldn't be there (e.g. w.ord)
    (re.compile(r'\b[a-zA-Z]+[0-9]+[a-zA-Z]+\b'), 'Letters with digits inside'),
    # 3. Rogue single letters (e.g. 't he', 'w ould', 'b ut')
    (re.compile(r'\b[b-hj-zB-HJ-Z]\s+[a-z]{2,}\b'), 'Rogue single letter before word'),
    (re.compile(r'\b[a-z]{2,}\s+[b-hj-z]\b'), 'Rogue single letter after word'),
]

for fpath in files:
    data = json.load(open(fpath, encoding='utf-8'))
    fname = os.path.basename(fpath)
    print(f"\nChecking {fname} for broken English words...")
    
    for q in data:
        qid = q.get('id')
        p = q.get('page')
        
        texts = [('question', q.get('question', '')),
                 ('explanation', q.get('explanation', ''))]
        for idx, opt in enumerate(q.get('options', [])):
            texts.append((f'option_{idx}', str(opt)))
            
        for fld, text in texts:
            if not text: continue
            for pat, desc in broken_english_patterns:
                for m in pat.finditer(text):
                    m_str = m.group(0)
                    # Exclude known programming terms like IPv6, 4G, 5G, HTML5, etc.
                    if m_str in {'IPv4', 'IPv6', 'UTF8', 'MP3', 'MP4', 'H2O', 'CO2'}:
                        continue
                    s = max(0, m.start() - 20)
                    e = min(len(text), m.end() + 20)
                    print(f"  [Q{qid} p.{p} {fld}] {desc}: '{m_str}' in \"...{text[s:e]}...\"")
