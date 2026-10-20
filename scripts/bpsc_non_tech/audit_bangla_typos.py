import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

fpath = r"c:\Users\bdCalling\Downloads\Mosabber\pdf-image-convert-to-Json\JSON Data\BPSC Non Tech\Bangla\Bangla.json"
with open(fpath, "r", encoding="utf-8") as f:
    data = json.load(f)

VALID_REDUPLICATED = {
    "ধীরে", "বার", "পলে", "শন", "কন", "মাঝে", "কাছে", "ভয়ে", "হাতে", "মুখে",
    "দিনে", "মনে", "ছোট", "বড়", "যে", "যা", "কে", "কার", "নতুন", "পিছু",
    "সাথে", "চোখে", "ঘরে", "দেশে", "গ্রামে", "যুগে", "কালে", "পথে", "ঘাটে",
    "গায়ে", "পায়ে", "টাকা", "এক", "দুই", "কথা", "কেঁদে", "হেসে", "মুহূর্তে",
    "জ্বর", "কোন", "বেশ", "ভিন্ন", "প্রধান", "সময়"
}

RE_DUPLICATE_WORDS = re.compile(r'\b([\u0980-\u09FF]{2,})\s+\1\b')
RE_LINE_START_STRAY = re.compile(r'(?:^|\n)\s*([ক-হড়-য়])\s+([\u0980-\u09FF]{2,})')

findings = []

for q in data:
    qid = q["id"]
    page = q.get("page", 0)
    all_texts = [("question", q.get("question", ""))] + \
                [(f"opt_{i+1}", opt) for i, opt in enumerate(q.get("options", []))] + \
                [("explanation", q.get("explanation", ""))]
    for field, txt in all_texts:
        if not txt:
            continue
            
        for m in RE_DUPLICATE_WORDS.finditer(txt):
            w = m.group(1)
            if w not in VALID_REDUPLICATED:
                findings.append({
                    "id": qid, "page": page, "field": field, "type": "DUPLICATE_WORD",
                    "word": w, "context": txt[max(0, m.start()-20):min(len(txt), m.end()+20)]
                })
                
        for m in RE_LINE_START_STRAY.finditer(txt):
            letter = m.group(1)
            word = m.group(2)
            if letter not in {"ও", "এ", "বা", "ড", "ন"}:
                findings.append({
                    "id": qid, "page": page, "field": field, "type": "STRAY_LINE_START",
                    "letter": letter, "context": txt[max(0, m.start()-5):min(len(txt), m.end()+35)]
                })

print(f"Total filtered findings in Bangla: {len(findings)}")
for i, f in enumerate(findings):
    print(f"#{i+1} QID {f['id']} (p.{f['page']}) [{f['field']}] {f['type']}: '{f.get('word') or f.get('letter')}'")
    print(f"   Context: \"{f.get('context')}\"")
