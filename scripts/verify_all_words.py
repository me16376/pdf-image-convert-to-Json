import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

patterns = {
    'স্ত্ম': re.compile(r'স্ত্ম'),
    'broken_ondo': re.compile(r'(?<![ক-হA-Za-z])(হত্যাকা|কর্মকা(?!রক)|অগ্নিকা|কারাদ|হৃৎপি|ভূখ)(?![ণণ্ডA-Za-z])'),
    'broken_hyphens': re.compile(r'চ\s*-\s*ালী|ভা\s*-\s*ার|ঠা\s*-\s*া|চ\s*-\s*ী|পু\s*-\s*্র|দ\s*-\s*ায়মান|ম\s*-\s*ল|প\s*-\s*িত|পি\s*-\s*ত|খি\s*-\s*ত'),
    'watermark_leaks': re.compile(r'বিদ্যাবাড়ি\s*(?:✓|\u2713)?\s*ব্যাখ্যা'),
    'header_leaks': re.compile(r'ঞবধপযবৎ|Teacher’s Work|Student Practice|Class Test'),
    'isolated_kar': re.compile(r'(?<![\.\d])\s+[\u09BE-\u09CC]\b'),
    'sutonny_bank': re.compile(r'\b(ঝবহরড়ৎ|ঙভভরপবৎ|ঔধহধঃধ|ইধহশ|ঝড়হধষর|ঘঅঞঙ|অমৎধহর|টহরড়হ)\b'),
}

findings = {k: [] for k in patterns}
total_words = 0
total_questions = 0

for root, dirs, files in os.walk(base):
    for f in sorted(files):
        if not f.endswith('.json'): continue
        p = os.path.join(root, f)
        with open(p, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        for q in data.get('questions', []):
            total_questions += 1
            qid = q.get('id')
            texts = [('q', q.get('question', ''))] + [(f'opt{i}', o) for i, o in enumerate(q.get('options', []))]
            for field, text in texts:
                if not isinstance(text, str): continue
                total_words += len(text.split())
                for pat_name, regex in patterns.items():
                    m = regex.findall(text)
                    if m:
                        findings[pat_name].append((f, qid, field, m, text[:80]))

print(f"Total questions scanned: {total_questions}")
print(f"Total words scanned: {total_words}")
print("-" * 50)
all_clean = True
for pat_name, items in findings.items():
    print(f"Pattern [{pat_name}]: {len(items)} occurrences")
    if items:
        all_clean = False
        for item in items[:5]:
            print(f"   {item[0]} Q{item[1]} {item[2]}: {item[3]} | \"{item[4]}\"")

if all_clean:
    print("\n ALL PATTERNS PASSED 100% CLEAN! NO CORRUPTIONS FOUND!")
