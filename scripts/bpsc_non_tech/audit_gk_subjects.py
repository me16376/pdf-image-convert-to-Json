import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\bdCalling\Downloads\Mosabber\pdf-image-convert-to-Json\JSON Data\BPSC Non Tech"
GK_SUBJECTS = [
    ("Bangladesh Affairs", os.path.join(BASE_DIR, "Bangladesh Affairs", "Bangladesh_Affairs.json")),
    ("International Affairs", os.path.join(BASE_DIR, "International Affairs", "International_Affairs.json")),
    ("Science", os.path.join(BASE_DIR, "Science", "Science.json")),
    ("ICT", os.path.join(BASE_DIR, "ICT", "ICT.json")),
]

# Patterns
RE_OPT_MARKER = re.compile(r'^\s*[\(\[\{]?[ক-ঙa-eA-E][\)\]\}\.\-–]\s+')
RE_ISOLATED_KAR = re.compile(r'(?:^|\s)([\u09BE-\u09CC\u09CD])')
RE_DOUBLE_KAR = re.compile(r'([\u09BE-\u09CC\u09CD])\1+')
RE_REPEATED_WORD = re.compile(r'\b([\u0980-\u09FF]{2,})\s+\1\b')

VALID_REPEATS = {"ধীরে", "বার", "পলে", "শন", "কন", "মাঝে", "কাছে", "ভয়ে", "হাতে", "মুখে", "যে", "যা", "কে", "কোন", "বেশ", "ভিন্ন", "প্রধান", "সময়", "এক", "দুই"}

all_gk_issues = []

for name, fpath in GK_SUBJECTS:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    print(f"\n--- Scanning {name} ({len(data)} MCQs) ---")
    subj_issues = 0
    
    for q in data:
        qid = q.get("id")
        page = q.get("page", 0)
        q_text = q.get("question", "")
        options = q.get("options", [])
        ans = q.get("answer", "")
        exp = q.get("explanation", "")
        
        # 1. Answer validity
        if ans not in ["ক", "খ", "গ", "ঘ", "ঙ", "নোট"]:
            all_gk_issues.append((name, qid, page, "INVALID_ANSWER", f"Ans: {ans}"))
            subj_issues += 1
            
        # 2. Options validity
        if len(options) not in (4, 5):
            all_gk_issues.append((name, qid, page, "OPTIONS_COUNT", f"{len(options)} opts"))
            subj_issues += 1
        else:
            for oi, opt in enumerate(options):
                if not opt.strip():
                    all_gk_issues.append((name, qid, page, "EMPTY_OPTION", f"Opt {oi+1} empty"))
                    subj_issues += 1
                elif RE_OPT_MARKER.match(opt):
                    all_gk_issues.append((name, qid, page, "OPT_MARKER", f"Opt {oi+1}: '{opt}'"))
                    subj_issues += 1
                    
            if len(set(options)) < len(options):
                seen = set()
                dups = [x for x in options if x in seen or seen.add(x)]
                all_gk_issues.append((name, qid, page, "DUPLICATE_OPTIONS", f"Dups: {dups}"))
                subj_issues += 1
                
        # 3. Text checks (isolated kars, double kars, duplicate words)
        all_texts = [("question", q_text)] + [(f"opt_{i+1}", opt) for i, opt in enumerate(options)] + [("explanation", exp)]
        for field, txt in all_texts:
            if not txt:
                continue
            iso = RE_ISOLATED_KAR.findall(txt)
            if iso:
                all_gk_issues.append((name, qid, page, "ISOLATED_KAR", f"Field: {field} | chars: {iso} in '{txt[:60]}'"))
                subj_issues += 1
            dk = RE_DOUBLE_KAR.findall(txt)
            if dk:
                all_gk_issues.append((name, qid, page, "DOUBLE_KAR", f"Field: {field} | chars: {dk} in '{txt[:60]}'"))
                subj_issues += 1
            for m in RE_REPEATED_WORD.finditer(txt):
                w = m.group(1)
                if w not in VALID_REPEATS:
                    all_gk_issues.append((name, qid, page, "REPEATED_WORD", f"Field: {field} | word: '{w}' in '{txt[max(0, m.start()-15):min(len(txt), m.end()+15)]}'"))
                    subj_issues += 1
                    
    print(f"Issues in {name}: {subj_issues}")

print(f"\nTotal GK issues across 4 subjects: {len(all_gk_issues)}")
for iss in all_gk_issues[:30]:
    print(f"[{iss[0]}] QID {iss[1]} (p.{iss[2]}) [{iss[3]}]: {iss[4]}")
if len(all_gk_issues) > 30:
    print(f"... and {len(all_gk_issues)-30} more.")
