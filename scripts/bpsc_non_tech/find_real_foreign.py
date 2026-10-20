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

# Devanagari (excluding 0964 and 0965 which are Danda/Double Danda used in Bengali)
RE_DEV_REAL = re.compile(r'[\u0900-\u0963\u0966-\u097F\u0D80-\u0DFF\u0600-\u06FF\u4E00-\u9FFF]')

print("=== REAL FOREIGN SCRIPT CHARACTERS AUDIT ===")
found_count = 0
for name, fpath in SUBJECTS:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for q in data:
        qid = q.get("id")
        page = q.get("page")
        all_texts = [("question", q.get("question", ""))] + \
                    [(f"opt_{i+1}", opt) for i, opt in enumerate(q.get("options", []))] + \
                    [("explanation", q.get("explanation", ""))]
        for field, txt in all_texts:
            if not isinstance(txt, str):
                continue
            matches = RE_DEV_REAL.findall(txt)
            if matches:
                found_count += 1
                chars = "".join(set(matches))
                print(f"[{name}] ID: {qid} (p.{page}) Field: {field} | Chars: '{chars}'")
                print(f"   Context: {txt}")
                print("-" * 60)

print(f"Total instances of real foreign script characters: {found_count}")
