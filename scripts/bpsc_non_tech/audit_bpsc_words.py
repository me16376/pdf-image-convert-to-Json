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

# Regex patterns for anomalies
RE_FOREIGN = re.compile(r'[\u0900-\u097F\u0D80-\u0DFF\u0600-\u06FF\u4E00-\u9FFF]') # Devanagari, Sinhala, Arabic, CJK
RE_ISOLATED_KAR = re.compile(r'(?:^|\s)([ািীুূৃেৈোৌ্্য্র])')
RE_DOUBLE_KAR = re.compile(r'([ািীুূৃেৈোৌ্])\1+')
RE_PIPE_DARI = re.compile(r'(?<=[^\d\s])\|(?=[^\d\s]|$)')
RE_QUESTION_MARK_GLITCH = re.compile(r'\?{2,}|\!{2,}')
RE_LEADING_OPT_MARKER = re.compile(r'^\s*[\(\[\{]?[a-eA-Eক-ঙ][\)\]\}\.\-–]\s*')
RE_DOUBLE_SPACE = re.compile(r'[^\S\r\n]{2,}')

# Broken Bengali word: single consonant followed by or preceded by a Bengali word
# Valid standalone 1-letter Bengali words: ও, এ, আ, বা, তা, যা, না, কি, সে, যে, কে, টু
VALID_SINGLE_LETTERS = set(["ও", "এ", "আ", "বা", "তা", "যা", "না", "কি", "সে", "যে", "কে", "টু", "x", "y", "z", "a", "b", "c", "p", "q"])

RE_SPLIT_BENGALI_PREFIX = re.compile(r'\b([ক-হড়-য়])\s+([ক-হড়-য়]{2,})\b')
RE_SPLIT_BENGALI_SUFFIX = re.compile(r'\b([ক-হড়-য়]{2,})\s+([ক-হড়-য়])\b')

# Misplaced hyphen splits e.g. "ই - মেইল", "দক্ষিণ - পূর্ব"
RE_SPLIT_HYPHEN = re.compile(r'([\u0980-\u09FF\w])\s*[-–]\s*([\u0980-\u09FF\w])')

def audit_subject(name, fpath):
    print(f"\n=======================================================")
    print(f"AUDITING: {name} ({fpath})")
    print(f"=======================================================")
    
    if not os.path.exists(fpath):
        print(f"ERROR: File not found: {fpath}")
        return []
    
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    print(f"Total MCQs: {len(data)}")
    issues = []
    
    for idx, q in enumerate(data):
        qid = q.get("id", idx + 1)
        page = q.get("page", 0)
        q_text = q.get("question", "")
        options = q.get("options", [])
        answer = q.get("answer", "")
        exp = q.get("explanation", "")
        
        # 1. Missing or suspicious fields
        if not q_text.strip():
            issues.append({"id": qid, "page": page, "type": "EMPTY_QUESTION", "text": ""})
        if not options or len(options) < 4:
            issues.append({"id": qid, "page": page, "type": "FEW_OPTIONS", "count": len(options)})
        if not answer:
            issues.append({"id": qid, "page": page, "type": "NO_ANSWER", "text": ""})
            
        all_texts = [("question", q_text)] + [(f"opt_{i+1}", opt) for i, opt in enumerate(options)] + [("explanation", exp)]
        
        for field, txt in all_texts:
            if not isinstance(txt, str):
                continue
                
            # Leading option markers in options
            if field.startswith("opt_") and RE_LEADING_OPT_MARKER.match(txt):
                issues.append({"id": qid, "page": page, "type": "LEADING_OPT_MARKER", "field": field, "text": txt[:40]})
                
            # Foreign script characters
            foreign = RE_FOREIGN.findall(txt)
            if foreign:
                issues.append({"id": qid, "page": page, "type": "FOREIGN_SCRIPT", "field": field, "chars": foreign, "sample": txt[:80]})
                
            # Isolated Kar (dependent vowel without consonant)
            iso = RE_ISOLATED_KAR.findall(txt)
            if iso:
                issues.append({"id": qid, "page": page, "type": "ISOLATED_KAR", "field": field, "chars": iso, "sample": txt[:80]})

            # Double kars
            dk = RE_DOUBLE_KAR.findall(txt)
            if dk:
                issues.append({"id": qid, "page": page, "type": "DOUBLE_KAR", "field": field, "chars": dk, "sample": txt[:80]})
                
            # Pipe used as dari
            if RE_PIPE_DARI.search(txt):
                issues.append({"id": qid, "page": page, "type": "PIPE_DARI", "field": field, "sample": txt[:80]})
                
            # Repeated punctuation
            if RE_QUESTION_MARK_GLITCH.search(txt):
                issues.append({"id": qid, "page": page, "type": "PUNCT_GLITCH", "field": field, "sample": txt[:80]})
                
            # Double spaces
            if RE_DOUBLE_SPACE.search(txt):
                issues.append({"id": qid, "page": page, "type": "DOUBLE_SPACE", "field": field, "sample": txt[:80]})
                
            # Broken Bengali words (single consonant prefix/suffix split by space)
            for m in RE_SPLIT_BENGALI_PREFIX.finditer(txt):
                c1, w2 = m.groups()
                if c1 not in VALID_SINGLE_LETTERS:
                    # check if likely broken word
                    issues.append({"id": qid, "page": page, "type": "BROKEN_BENGALI_PREFIX", "field": field, "match": m.group(0), "sample": txt[max(0, m.start()-15):min(len(txt), m.end()+15)]})
                    
            for m in RE_SPLIT_BENGALI_SUFFIX.finditer(txt):
                w1, c2 = m.groups()
                if c2 not in VALID_SINGLE_LETTERS:
                    issues.append({"id": qid, "page": page, "type": "BROKEN_BENGALI_SUFFIX", "field": field, "match": m.group(0), "sample": txt[max(0, m.start()-15):min(len(txt), m.end()+15)]})

            # Check unbalanced parentheses (excluding math LaTeX where parenthesis might be in escaped syntax)
            if name != "Math":
                if txt.count('(') != txt.count(')'):
                    # Only flag if not a common emoticon or smiley
                    issues.append({"id": qid, "page": page, "type": "UNBALANCED_PARENS", "field": field, "sample": txt[:80]})

    print(f"Total issues found: {len(issues)}")
    # Summarize issue types
    types = {}
    for issue in issues:
        t = issue["type"]
        types[t] = types.get(t, 0) + 1
    for t, c in types.items():
        print(f"  - {t}: {c}")
        
    return issues

if __name__ == "__main__":
    all_issues = {}
    total_all = 0
    for name, fpath in SUBJECTS:
        issues = audit_subject(name, fpath)
        all_issues[name] = issues
        total_all += len(issues)
        
    out_file = r"scripts\bpsc_non_tech\audit_report.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_issues, f, ensure_ascii=False, indent=2)
    print(f"\n=======================================================")
    print(f"GRAND TOTAL ANOMALIES ACROSS ALL 7 SUBJECTS: {total_all}")
    print(f"Wrote full report to {out_file}")
    print(f"=======================================================")
