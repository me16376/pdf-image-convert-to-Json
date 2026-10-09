import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

findings = []

for root, dirs, files in sorted(os.walk(base)):
    for f in sorted(files):
        if not f.endswith('.json'): continue
        p = os.path.join(root, f)
        with open(p, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        for q in d.get('questions', []):
            qid = q.get('id')
            for i, opt in enumerate(q.get('options', [])):
                if not isinstance(opt, str): continue
                # Check for leaked marks or notes in options
                if any(kw in opt for kw in ['✓', 'শর্টকাট', 'নোট:', 'নোট ঃ', 'ব্যাখ্যা:', 'সূত্র :']):
                    findings.append((f, qid, f'opt{i}', opt))
                elif len(opt) > 100:
                    findings.append((f, qid, f'opt{i}', opt))

print(f"Total suspicious options found: {len(findings)}")
for f, qid, field, opt in findings:
    print(f"[{f}] Q{qid} {field} (len {len(opt)}): {repr(opt[:80])} ...")
