# -*- coding: utf-8 -*-
"""
Word-by-word audit of all JSON files in JSON Data/BPSC ICT Wizard/
Checks for:
1. Detached vowel marks / kars (e.g. ' ি', ' া')
2. Unnatural Latin/Bengali script mixing (e.g. without hyphen)
3. Consecutive whitespace or trailing/leading whitespace
4. Broken words / hanging punctuation (e.g. ' ?', ' ,')
5. Known typos and broken technical terms
"""
import glob
import json
import re
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('JSON Data/BPSC ICT Wizard/*.json'))

total_issues = 0

for fpath in files:
    fname = fpath.replace('\\', '/').split('/')[-1]
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    
    file_issues = []
    
    for item in data:
        qid = item.get('id')
        q_text = item.get('question', '')
        options = item.get('options', [])
        
        # Check question and each option
        all_texts = [('Question', q_text)] + [(f'Option {idx}', opt) for idx, opt in enumerate(options)]
        
        for field, text in all_texts:
            # 1. Detached kar
            for m in re.finditer(r'\s([\u09be-\u09cc\u09cd])', text):
                file_issues.append((qid, field, f'Detached vowel/hasant: {repr(m.group(0))}', text))
            
            # 2. Dangling hasant at end of Bengali word (unless followed by valid char)
            for m in re.finditer(r'[\u0980-\u09ff]\u09cd(?=[\s,\.?!;:\'\"\)\]\-]|$)', text):
                # Some words validly end in hasant, but let's inspect
                file_issues.append((qid, field, f'Trailing hasant: {repr(m.group(0))}', text))
            
            # 3. Double vowel marks
            for m in re.finditer(r'([\u09be\u09bf\u09c0\u09c1\u09c2\u09c3\u09c7\u09c8\u09cb\u09cc]{2,})', text):
                file_issues.append((qid, field, f'Double vowel mark: {repr(m.group(0))}', text))
            
            # 4. Leading / trailing spaces
            if text != text.strip():
                file_issues.append((qid, field, 'Untrimmed whitespace', text))
            
            # 5. Multiple spaces inside text
            if '  ' in text:
                file_issues.append((qid, field, 'Consecutive spaces', text))
            
            # 6. Space before question mark or comma
            if re.search(r'\s[?,;:]', text):
                file_issues.append((qid, field, 'Space before punctuation', text))
            
            # 7. Unnatural English-Bengali glued (e.g. 'CPUএর' instead of 'CPU এর' or 'CPU-এর')
            for m in re.finditer(r'([A-Za-z]{2,}[\u0985-\u09ff]+)', text):
                matched = m.group(1)
                # Check if hyphen is missing, like 'OSএর' or 'LANএর'
                file_issues.append((qid, field, f'Glued English-Bengali: {matched}', text))
                
            # 8. Unnatural Bengali-English glued
            for m in re.finditer(r'([\u0985-\u09ff]+[A-Za-z]{2,})', text):
                matched = m.group(1)
                file_issues.append((qid, field, f'Glued Bengali-English: {matched}', text))

    print(f'=== {fname}: {len(file_issues)} potential issues found ===')
    total_issues += len(file_issues)
    for issue in file_issues[:15]:
        print(f'  [Q{issue[0]} {issue[1]}] {issue[2]} -> {issue[3]}')
    if len(file_issues) > 15:
        print(f'  ... and {len(file_issues) - 15} more.')

print('=' * 60)
print(f'Total issues across all files: {total_issues}')
