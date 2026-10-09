import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

for folder in ['Bangla', 'English', 'GK', 'Math']:
    dirpath = os.path.join(base, folder)
    print(f"\n=================== {folder} ===================")
    for f in sorted(os.listdir(dirpath)):
        if not f.endswith('.json'): continue
        with open(os.path.join(dirpath, f), 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        for q in d.get('questions', []):
            qid = q.get('id')
            for i, opt in enumerate(q.get('options', [])):
                if not isinstance(opt, str): continue
                # We want options that are abnormally long (len > 70)
                # In English/Bangla, normal options rarely exceed 80 unless they are sentences
                if len(opt) > 70:
                    # Let's inspect
                    print(f"[{f}] Q{qid} opt{i} (len={len(opt)}): {repr(opt[:80])}")
