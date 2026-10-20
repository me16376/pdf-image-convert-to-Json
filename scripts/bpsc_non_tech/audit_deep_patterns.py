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

# 1. Invalid kar sequences (e.g. াা, েে, োা, etc., but excluding valid conjunct hasanta sequences like ক্ত = ক + ্ + ত)
RE_INVALID_KARS = re.compile(r'([ািীুূৃেৈোৌ]){2,}|[ািীুূৃেৈোৌ][্]|[্]{2,}')

# 2. Space before kar (isolated dependent vowel sign after space)
RE_SPACE_BEFORE_KAR = re.compile(r'(?<=[\s\(\[\{,\.\?!:;\-\"\'“‘])([ািীুূৃেৈোৌ্])')

# 3. Latin letter embedded in Bengali word: e.g. [ক-হ] + [a-zA-Z] + [ক-হ] or vice-versa
RE_LATIN_IN_BENGALI = re.compile(r'[\u0980-\u09FF][a-zA-Z]+[\u0980-\u09FF]|[\u0980-\u09FF][a-zA-Z]|[a-zA-Z][\u0980-\u09FF]')

# 4. Pipe character
RE_PIPE = re.compile(r'\|')

# 5. Split conjuncts: consonant + space + hasanta + consonant e.g. "ক ্ত" or "ক ্ ত"
RE_SPLIT_HASANTA = re.compile(r'[\u0985-\u09B9]\s+্|্\s+[\u0985-\u09B9]')

print("=== DEEP PATTERN AUDIT ===")

findings = []

for name, fpath in SUBJECTS:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\n--- Scanning {name} ({len(data)} MCQs) ---")
    subj_issues = 0
    for q in data:
        qid = q.get("id")
        page = q.get("page")
        all_texts = [("question", q.get("question", ""))] + \
                    [(f"opt_{i+1}", opt) for i, opt in enumerate(q.get("options", []))] + \
                    [("explanation", q.get("explanation", ""))]
        for field, txt in all_texts:
            if not isinstance(txt, str):
                continue
                
            # Check invalid kars
            for m in RE_INVALID_KARS.finditer(txt):
                subj_issues += 1
                findings.append({
                    "subject": name, "id": qid, "page": page, "field": field,
                    "type": "INVALID_KAR_SEQUENCE", "match": m.group(0),
                    "context": txt[max(0, m.start()-20):min(len(txt), m.end()+20)]
                })
                
            # Check space before kar
            for m in RE_SPACE_BEFORE_KAR.finditer(txt):
                subj_issues += 1
                findings.append({
                    "subject": name, "id": qid, "page": page, "field": field,
                    "type": "SPACE_BEFORE_KAR", "match": m.group(0),
                    "context": txt[max(0, m.start()-20):min(len(txt), m.end()+20)]
                })
                
            # Check split hasanta
            for m in RE_SPLIT_HASANTA.finditer(txt):
                subj_issues += 1
                findings.append({
                    "subject": name, "id": qid, "page": page, "field": field,
                    "type": "SPLIT_HASANTA", "match": m.group(0),
                    "context": txt[max(0, m.start()-20):min(len(txt), m.end()+20)]
                })
                
            # Check pipe
            if '|' in txt and name != "Math": # Math might use |x|
                subj_issues += 1
                findings.append({
                    "subject": name, "id": qid, "page": page, "field": field,
                    "type": "PIPE_DARI", "match": "|",
                    "context": txt[max(0, txt.find('|')-20):min(len(txt), txt.find('|')+20)]
                })
                
            # Check Latin in Bengali (filter out legitimate English acronyms in parens or with hyphens)
            for m in RE_LATIN_IN_BENGALI.finditer(txt):
                # Check if it's hyphenated like e-কমার্স, or HTML-এর
                sub = txt[max(0, m.start()-5):min(len(txt), m.end()+5)]
                if '-' in sub or '—' in sub:
                    continue
                # If Latin letter is directly adjacent to Bengali letter
                subj_issues += 1
                findings.append({
                    "subject": name, "id": qid, "page": page, "field": field,
                    "type": "LATIN_BENGALI_MERGE", "match": m.group(0),
                    "context": txt[max(0, m.start()-20):min(len(txt), m.end()+20)]
                })
                
    print(f"Issues in {name}: {subj_issues}")

print(f"\nTOTAL DEEP PATTERN ISSUES: {len(findings)}")

out_path = r"scripts\bpsc_non_tech\deep_pattern_report.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(findings, f, ensure_ascii=False, indent=2)
print(f"Saved report to {out_path}")
