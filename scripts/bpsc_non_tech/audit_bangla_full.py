import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

fpath = r"c:\Users\bdCalling\Downloads\Mosabber\pdf-image-convert-to-Json\JSON Data\BPSC Non Tech\Bangla\Bangla.json"
with open(fpath, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total Bangla MCQs: {len(data)}")

issues = []

for q in data:
    qid = q["id"]
    page = q.get("page", 0)
    q_text = q.get("question", "")
    options = q.get("options", [])
    ans = q.get("answer", "")
    exp = q.get("explanation", "")
    
    # 1. Check answer validity
    if ans not in ["ক", "খ", "গ", "ঘ", "ঙ", "নোট"]:
        issues.append((qid, page, "INVALID_ANSWER", f"Answer is '{ans}'"))
        
    # 2. Check options count and duplicates
    if len(options) < 4:
        issues.append((qid, page, "FEW_OPTIONS", f"Only {len(options)} options"))
    if len(set(options)) < len(options):
        # find duplicate option
        seen = set()
        dups = [x for x in options if x in seen or seen.add(x)]
        issues.append((qid, page, "DUPLICATE_OPTIONS", f"Duplicate options: {dups}"))
        
    # 3. Check for empty options
    for oi, opt in enumerate(options):
        if not opt.strip():
            issues.append((qid, page, "EMPTY_OPTION", f"Option {oi+1} is empty"))
            
    # 4. Check for leading option markers in options
    for oi, opt in enumerate(options):
        if re.match(r'^\s*[\(\[\{]?[ক-ঙa-eA-E][\)\]\}\.\-–]\s*', opt):
            issues.append((qid, page, "OPT_MARKER_IN_OPTION", f"Opt {oi+1}: '{opt}'"))
            
    # 5. Check question endings: should usually end in ?, :, ।, or quotes
    clean_q = q_text.strip()
    if not clean_q:
        issues.append((qid, page, "EMPTY_QUESTION", ""))
    elif clean_q[-1] not in ["?", "!", "।", ":", "’", "'", "”", '"', ")", "-", "—"]:
        issues.append((qid, page, "QUESTION_ENDING", f"Ends with '{clean_q[-1]}': {clean_q[-30:]}"))
        
    # 6. Specific typos in Bangla
    all_txt = q_text + " " + " ".join(options) + " " + exp
    if "শহীদুল্লাহ্ র" in all_txt:
        issues.append((qid, page, "TYPO_SHAHIDULLAH", "Found 'শহীদুল্লাহ্ র'"))
    if "ই ইন্দ্রিয়কে" in all_txt:
        issues.append((qid, page, "TYPO_INDRIA", "Found 'ই ইন্দ্রিয়কে'"))
    if "পদে পদের" in all_txt:
        issues.append((qid, page, "TYPO_PODE_PODER", "Found 'পদে পদের'"))

print(f"Total Bangla issues found: {len(issues)}")
for iss in issues:
    print(f"QID {iss[0]} (p.{iss[1]}) [{iss[2]}]: {iss[3]}")
