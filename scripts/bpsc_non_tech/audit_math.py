import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('JSON Data/BPSC Non Tech/Math/Math.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total Math Questions: {len(data)}")

# 1. Check ID sequence
ids = [q['id'] for q in data]
expected_ids = list(range(1, len(data) + 1))
if ids != expected_ids:
    print("ID sequence mismatch!")
else:
    print("ID sequence is 1..1003 continuous.")

# 2. Check duplicate options
dup_options = []
for q in data:
    opts = [str(o).strip() for o in q.get('options', [])]
    if len(opts) != len(set(opts)):
        dup_options.append((q['id'], q.get('page'), opts))

print(f"Questions with duplicate options: {len(dup_options)}")
for qid, page, opts in dup_options:
    print(f"  Q{qid} (page {page}): {opts}")

# 3. Check for Devanagari
devanagari_pattern = re.compile(r'[\u0900-\u097F]')
dev_matches = []
for q in data:
    text = json.dumps(q, ensure_ascii=False)
    m = devanagari_pattern.findall(text)
    if m:
        dev_matches.append((q['id'], q.get('page'), set(m)))
print(f"Devanagari found: {len(dev_matches)}")
for issue in dev_matches:
    print("  Devanagari:", issue)

# 4. Check for odd LaTeX / KaTeX issues (unbalanced $ signs)
katex_issues = []
for q in data:
    for field in [q.get('question', ''), q.get('explanation', '')] + q.get('options', []):
        if not isinstance(field, str): continue
        dollars = [m.start() for m in re.finditer(r'(?<!\\)\$', field)]
        if len(dollars) % 2 != 0:
            katex_issues.append((q['id'], q.get('page'), 'Unbalanced $', field[:80]))
            break

print(f"Unbalanced $ count: {len(katex_issues)}")
for issue in katex_issues:
    print("  KaTeX:", issue)

# 5. Check for empty options or empty questions
empty_issues = []
for q in data:
    if not q.get('question', '').strip():
        empty_issues.append((q['id'], 'Empty question'))
    if len(q.get('options', [])) < 4:
        empty_issues.append((q['id'], f"Fewer than 4 options ({len(q.get('options', []))})"))
    for opt in q.get('options', []):
        if not str(opt).strip():
            empty_issues.append((q['id'], 'Empty option'))
print(f"Empty issues: {len(empty_issues)}")
for issue in empty_issues:
    print("  Empty:", issue)

# 6. Check common Bengali broken words / split kars / OCR artifacts
broken_patterns = [
    (r'\u09C7[\u09BE\u09D7]', 'Split O-kar / Ou-kar'),
    (r'[ক-হ][\u09BE-\u09CD]{2,}', 'Double vowel kars'),
    (r'(\b[ক-হ]\b\s+){3,}', 'Isolated single characters chain'),
]

for pat, desc in broken_patterns:
    matches = []
    for q in data:
        full_text = json.dumps(q, ensure_ascii=False)
        m = re.findall(pat, full_text)
        if m:
            matches.append((q['id'], q.get('page'), m[:3]))
    print(f"Pattern '{desc}' matches: {len(matches)}")
    for item in matches[:5]:
        print("   ", item)
