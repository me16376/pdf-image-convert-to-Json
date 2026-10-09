import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

def analyze_corpus():
    issues = {
        'hyphen_broken': [],
        'roman_i_glitch': [],
        'answer_leak_in_q': [],
        'inverted_vowels': [],
        'sutonny_english_words': [],
        'truncated_bracket_words': [],
        'isolated_symbols': []
    }
    
    # Regexes
    re_hyphen_broken = re.compile(r'([^\s\(\[\{]{1,5})\s*-\s*([^\s\)\]\}\,\.\?\!]{1,5})')
    re_roman = re.compile(r'(?<![a-zA-Z])(?:\b[ি]{1,3}\.|\bি\s+ও\s+িি\b|\bি\s+ও\s+িিি\b|\bিি\s+ও\s+িিি\b|\bি,\s*িি\s+ও\s+িিি\b)')
    re_ans_leak = re.compile(r'[\?।]\s*([০-৯\d]{1,3}\s*[কখগঘa-dA-D])\s*$')
    re_inv_vowel = re.compile(r'[\u09BE\u09BF\u09C0\u09C1\u09C2\u09C7\u09C8\u09CB\u09CC]{2,}')
    # Common Sutonny-mapped English words
    re_sutonny_en = re.compile(r'\b(ষড়ম|পড়ঃ|ংরহ|ঃধহ|পড়ং|ংবপ|পড়ংবপ|জঅকটই|ঝবহরড়ৎ|ঙভভরপবৎ|টঘওঈঊঋ|ডঞঙ|ইওগঝঞঊঈ|ইঅজঈ|ঘঅঞঙ|টঘউচ|টঘঊঝঈঙ)\b')
    re_trunc_bracket = re.compile(r'\[[^\]]*\b(?:সংস্থ|প্রকৌ|অধিদ|মন্ত্রণাল|পরীক্ষ|সহকা|অফিসা)\b')

    file_count = 0
    q_count = 0

    for root, dirs, files in sorted(os.walk(base)):
        for f in sorted(files):
            if not f.endswith('.json'): continue
            file_count += 1
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
            for q in data.get('questions', []):
                q_count += 1
                qid = q.get('id')
                q_text = q.get('question', '')
                opts = q.get('options', [])
                
                # Check question
                if m := re_ans_leak.search(q_text):
                    issues['answer_leak_in_q'].append((f, qid, 'q', m.group(0), q_text[-30:]))
                
                if m := re_roman.findall(q_text):
                    issues['roman_i_glitch'].append((f, qid, 'q', m, q_text[:80]))
                
                if m := re_trunc_bracket.findall(q_text):
                    issues['truncated_bracket_words'].append((f, qid, 'q', m, q_text[-60:]))

                all_texts = [('q', q_text)] + [(f'opt{i}', o) for i, o in enumerate(opts)]
                for field, text in all_texts:
                    if not isinstance(text, str): continue
                    
                    if m := re_sutonny_en.findall(text):
                        issues['sutonny_english_words'].append((f, qid, field, m, text[:60]))
                    
                    if m := re_roman.findall(text):
                        if field != 'q': # already added
                            issues['roman_i_glitch'].append((f, qid, field, m, text[:60]))
                    
                    # Inverted vowels
                    for vmatch in re_inv_vowel.finditer(text):
                        pair = vmatch.group(0)
                        # Filter out compound vowels like ৌ (ে + ৗ is ৌ in single codepoint U+09CC, but sometimes decomposed)
                        # Also ো is U+09CB
                        # Real double vowels like ুি, াু, িা are suspicious
                        if pair in ('ুি', 'াু', 'িু', 'িে', 'েি', 'ুে', 'েু'):
                            issues['inverted_vowels'].append((f, qid, field, pair, text[:60]))
                    
                    # Hyphen breaks: check if it's broken letters
                    for hmatch in re_hyphen_broken.finditer(text):
                        w1, w2 = hmatch.group(1), hmatch.group(2)
                        # if either side is 1 char or looks like broken ligature
                        if any(c in 'খিমপচভঠদগঝ' for c in w1) and any(c in 'তলারীীবদ' for c in w2):
                            if '-' in hmatch.group(0):
                                issues['hyphen_broken'].append((f, qid, field, hmatch.group(0), text[:60]))

    print(f"Scanned {file_count} files, {q_count} questions.")
    print("=" * 60)
    for cat, items in issues.items():
        print(f"Category: {cat} -> {len(items)} issues found")
        for it in items[:8]:
            print(f"  {it[0]} Q{it[1]} {it[2]}: {it[3]} | Context: {it[4]}")
        if len(items) > 8:
            print(f"  ... and {len(items) - 8} more")
        print("-" * 60)

if __name__ == '__main__':
    analyze_corpus()
