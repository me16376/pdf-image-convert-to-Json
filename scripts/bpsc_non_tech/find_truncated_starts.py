import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\bdCalling\Downloads\Mosabber\pdf-image-convert-to-Json\JSON Data\BPSC Non Tech"
SUBJECTS = [
    ("Bangla", os.path.join(BASE_DIR, "Bangla", "Bangla.json")),
    ("English", os.path.join(BASE_DIR, "English", "English.json")),
    ("Bangladesh Affairs", os.path.join(BASE_DIR, "Bangladesh Affairs", "Bangladesh_Affairs.json")),
    ("International Affairs", os.path.join(BASE_DIR, "International Affairs", "International_Affairs.json")),
    ("Science", os.path.join(BASE_DIR, "Science", "Science.json")),
    ("ICT", os.path.join(BASE_DIR, "ICT", "ICT.json")),
    ("Math", os.path.join(BASE_DIR, "Math", "Math.json")),
]

# A kar or hasanta at the start of a string:
RE_START_WITH_KAR = re.compile(r'^\s*[\(\[\{‘“\'\"]?([ািীুূৃেৈোৌ্্য্র])')

print("=== CHECKING FOR TRUNCATED QUESTION STARTS ===")

all_truncated = []

for name, fpath in SUBJECTS:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for q in data:
        qid = q.get("id")
        page = q.get("page", 0)
        q_text = q.get("question", "").strip()
        
        # Check if question starts with a kar
        m = RE_START_WITH_KAR.search(q_text)
        if m:
            all_truncated.append({
                "subject": name, "id": qid, "page": page,
                "type": "STARTS_WITH_KAR", "char": m.group(1), "question": q_text[:80]
            })
            continue
            
        # Check if options start with a kar
        for oi, opt in enumerate(q.get("options", [])):
            om = RE_START_WITH_KAR.search(opt.strip())
            if om:
                all_truncated.append({
                    "subject": name, "id": qid, "page": page,
                    "type": "OPT_STARTS_WITH_KAR", "opt_idx": oi+1, "char": om.group(1), "text": opt[:50]
                })

print(f"Total truncated start issues found: {len(all_truncated)}")
for t in all_truncated:
    print(f"[{t['subject']}] ID {t['id']} (p.{t['page']}) [{t['type']}]: char='{t.get('char')}'")
    print(f"   text: {t.get('question') or t.get('text')}")
