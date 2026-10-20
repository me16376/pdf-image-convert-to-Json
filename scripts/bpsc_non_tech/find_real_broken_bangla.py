import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

fpath = r"c:\Users\bdCalling\Downloads\Mosabber\pdf-image-convert-to-Json\JSON Data\BPSC Non Tech\Bangla\Bangla.json"
with open(fpath, "r", encoding="utf-8") as f:
    data = json.load(f)

# Punctuation or operator tokens that separate legitimate items
PUNCT = {",", ";", ":", "+", "-", "—", "–", "।", "?", "!", "/", "=", "(", ")", "[", "]", "{", "}", "'", "\"", "‘", "’", "“", "”"}

STANDALONE_VALID = {"ও", "এ", "বা", "তা", "যা", "না", "কি", "কী", "সে", "যে", "কে", "তু", "হা", "হাঁ", "ছ", "টি", "টা"}

real_broken_candidates = []

for q in data:
    qid = q["id"]
    page = q.get("page", 0)
    all_texts = [("question", q.get("question", ""))] + \
                [(f"opt_{i+1}", opt) for i, opt in enumerate(q.get("options", []))] + \
                [("explanation", q.get("explanation", ""))]
    for field, txt in all_texts:
        if not txt:
            continue
            
        tokens = txt.split()
        for i, token in enumerate(tokens):
            # Strip outer punctuation
            clean_tok = re.sub(r'^[^\u0980-\u09FF]+|[^\u0980-\u09FF]+$', '', token)
            if len(clean_tok) == 1 and clean_tok not in STANDALONE_VALID and not clean_tok.isdigit():
                # Check preceding and following
                prev_tok = tokens[i-1] if i > 0 else ""
                next_tok = tokens[i+1] if i < len(tokens)-1 else ""
                
                # Check if preceded or followed by punctuation or math symbols
                has_punct = False
                for p in PUNCT:
                    if p in token or (prev_tok and prev_tok.endswith(p)) or (next_tok and next_tok.startswith(p)):
                        has_punct = True
                        break
                if has_punct:
                    continue
                    
                # If either prev_tok or next_tok is a Bengali word
                prev_clean = re.sub(r'^[^\u0980-\u09FF]+|[^\u0980-\u09FF]+$', '', prev_tok)
                next_clean = re.sub(r'^[^\u0980-\u09FF]+|[^\u0980-\u09FF]+$', '', next_tok)
                
                if (len(prev_clean) >= 2 or len(next_clean) >= 2):
                    ctx = " ".join(tokens[max(0, i-2):min(len(tokens), i+3)])
                    real_broken_candidates.append({
                        "id": qid, "page": page, "field": field, "letter": clean_tok,
                        "prev": prev_tok, "next": next_tok, "context": ctx
                    })

print(f"Total potential real broken words in Bangla: {len(real_broken_candidates)}")
for cand in real_broken_candidates:
    print(f"QID {cand['id']} (p.{cand['page']}) [{cand['field']}] Letter: '{cand['letter']}' | Context: \"{cand['context']}\"")
