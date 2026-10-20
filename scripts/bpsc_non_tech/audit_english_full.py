import json
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

fpath = r"c:\Users\bdCalling\Downloads\Mosabber\pdf-image-convert-to-Json\JSON Data\BPSC Non Tech\English\English.json"
with open(fpath, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total English MCQs: {len(data)}")

issues = []

# Known English OCR misreads or typos in job solution books
COMMON_ENGLISH_TYPOS = [
    (r'\bmaintainance\b', 'maintenance'),
    (r'\bgrammer\b', 'grammar'),
    (r'\boccured\b', 'occurred'),
    (r'\brecieve\b', 'receive'),
    (r'\bseperate\b', 'separate'),
    (r'\buntill\b', 'until'),
    (r'\bwritting\b', 'writing'),
    (r'\btruly\b', 'truly'),
    (r'\bdefination\b', 'definition'),
    (r'\bAblenesos\b', 'Ableness'),
    (r'\bdiffcrent\b', 'different'),
    (r'\bcompletly\b', 'completely'),
    (r'\bposibly\b', 'possibly'),
    (r'\bnecesary\b', 'necessary'),
    (r'\bcolleague\b', 'colleague'),
    (r'\bcommittee\b', 'committee'),
    (r'\blieutenant\b', 'lieutenant'),
    (r'\bquestionaire\b', 'questionnaire'),
]

for q in data:
    qid = q["id"]
    page = q.get("page", 0)
    q_text = q.get("question", "")
    options = q.get("options", [])
    ans = q.get("answer", "")
    exp = q.get("explanation", "")
    
    # 1. Answer validity
    if ans not in ["ক", "খ", "গ", "ঘ", "ঙ", "নোট"]:
        issues.append((qid, page, "INVALID_ANSWER", f"Ans is '{ans}'"))
        
    # 2. Options format and count
    if not isinstance(options, list):
        issues.append((qid, page, "NOT_LIST_OPTIONS", f"Type: {type(options)}"))
    elif len(options) not in (4, 5):
        issues.append((qid, page, "OPTIONS_COUNT", f"{len(options)} options"))
    else:
        # Check empty or duplicates
        for oi, opt in enumerate(options):
            if not isinstance(opt, str) or not opt.strip():
                issues.append((qid, page, "EMPTY_OPTION", f"Option {oi+1} empty"))
            elif re.match(r'^\s*[\(\[\{]?[ক-ঙa-eA-E][\)\]\}\.\-–]\s+[A-Za-z\u0980-\u09FF]', opt):
                # Only flag if followed by letter (avoid e-mail, e-book)
                m = re.match(r'^\s*[\(\[\{]?([a-eA-E])[\)\]\}\.\-–]\s+', opt)
                if m and m.group(1).lower() not in ['e']: # e.g. e-mail
                    issues.append((qid, page, "LEADING_OPT_MARKER", f"Opt {oi+1}: '{opt}'"))
                    
        if len(set(options)) < len(options):
            # If the question asks for spelling, check if duplicates exist
            seen = set()
            dups = [x for x in options if x in seen or seen.add(x)]
            issues.append((qid, page, "DUPLICATE_OPTIONS", f"Duplicate options: {dups}"))
            
    # 3. Check for OCR letter mergers or broken English words
    # e.g. words containing digits like 'th1s', '1n'
    for oi, opt in enumerate(options):
        if isinstance(opt, str):
            for m in re.finditer(r'\b[a-zA-Z]+[0-9]+[a-zA-Z]+\b', opt):
                issues.append((qid, page, "ALPHANUM_WORD", f"Opt {oi+1}: '{m.group(0)}' in '{opt}'"))
                
    # 4. Check known typos
    all_txt = q_text + " " + " ".join(options if isinstance(options, list) else []) + " " + (exp or "")
    if "Ablenesos" in all_txt:
        issues.append((qid, page, "TYPO_ABLENESOS", "Found 'Ablenesos'"))
    if "diffcrent" in all_txt:
        issues.append((qid, page, "TYPO_DIFFCRENT", "Found 'diffcrent'"))

print(f"Total English issues found: {len(issues)}")
for iss in issues[:30]:
    print(f"QID {iss[0]} (p.{iss[1]}) [{iss[2]}]: {iss[3]}")
if len(issues) > 30:
    print(f"... and {len(issues)-30} more.")
