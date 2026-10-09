import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

def check_all():
    for folder in ['Bangla', 'English', 'GK', 'Math']:
        dirpath = os.path.join(base, folder)
        files = sorted([f for f in os.listdir(dirpath) if f.endswith('.json')])
        print(f"\n==========================================")
        print(f"Scanning folder: {folder} ({len(files)} files)")
        print(f"==========================================")
        for f in files:
            p = os.path.join(dirpath, f)
            with open(p, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
            
            file_issues = []
            for q in d.get('questions', []):
                qid = q.get('id')
                texts = [('q', q.get('question', ''))] + [(f'opt{i}', o) for i, o in enumerate(q.get('options', []))]
                for field, text in texts:
                    if not isinstance(text, str): continue
                    
                    # 1. Inverted vowels: ুি, াু
                    for m in re.finditer(r'([^\s\(\)\[\]\,\.\?\!]*[ুিা]{2}[^\s\(\)\[\]\,\.\?\!]*)', text):
                        w = m.group(1)
                        if 'ুি' in w or 'াু' in w:
                            file_issues.append((qid, field, 'inverted_vowel', w, text[:70]))

                    # 2. Broken ligature hyphens: e.g. খি - ত
                    for m in re.finditer(r'([^\s\(\[\{]{1,5}\s*-\s*[^\s\)\]\}\,\.\?\!]{1,5})', text):
                        w = m.group(1)
                        if any(ch in w for ch in ['খি', 'চ', 'ভা', 'ঠা', 'প', 'দ', 'ম']) and any(ch in w for ch in ['ত', 'ালী', 'ার', 'া', 'িত', 'ায়মান', 'ল', 'লী']):
                            if not any(good in w for good in ['মা-বাবা', 'ভাই-বোন', 'আশা-আকাঙ্ক্ষা']):
                                file_issues.append((qid, field, 'broken_hyphen', w, text[:70]))

                    # 3. Sutonny Bijoy gibberish words
                    for m in re.finditer(r'\b([অ-হ]{0,3}[ড়ঃংৎবভধহশষসঢ়য়ঁ]{3,}[অ-হ]{0,3})\b', text):
                        w = m.group(1)
                        # Check if looks like Sutonny English
                        if any(w.startswith(prefix) for prefix in ['ঝবহর', 'ঙভভর', 'ঔধহ', 'ইধহ', 'ঝড়হ', 'ঘঅঞ', 'অমৎ', 'ঊঁৎ', 'টহর', 'চঁন', 'ঔঁহ', 'ঊীব', 'ঈধং', 'চৎড়', 'কড়ষ', 'জঅক', 'ইঐ', 'ইক', 'ডযধ']):
                            file_issues.append((qid, field, 'sutonny_word', w, text[:70]))

                    # 4. Stray roman numeral
                    if re.search(r'(?<![ক-হA-Za-z0-9])(?:[ি]{1,3}\.|\bি\s+ও\s+িি\b|\bি\s+ও\s+িিি\b|\bিি\s+ও\s+িিি\b)', text):
                        if not any(unit in text for unit in ['মি.', 'সে.মি.', 'কি.মি.', 'লি.']):
                            file_issues.append((qid, field, 'roman_glitch', text, text[:70]))

                    # 5. Answer leaks at end of question
                    if field == 'q':
                        if m := re.search(r'[\?।]\s*([০-৯\d]{1,3}\s*[কখগঘa-dA-D])\s*$', text):
                            file_issues.append((qid, field, 'answer_leak', m.group(1), text[-40:]))

            if file_issues:
                print(f"\n--- File: {f} ({len(file_issues)} issues) ---")
                for iss in file_issues:
                    print(f"  Q{iss[0]} {iss[1]} [{iss[2]}]: '{iss[3]}' in: {iss[4]}")

if __name__ == '__main__':
    check_all()
