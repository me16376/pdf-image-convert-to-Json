import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

MATH_DIR = 'JSON Data/Biddabari-NTRCA/Math'

# 1. Clean math symbol artifacts in any string
def clean_math_text(s):
    if not isinstance(s, str) or not s:
        return s
    
    # Trigonometric functions & variables
    s = s.replace('cosবপ', 'cosec')
    s = s.replace('পড়ংবপ', 'cosec')
    s = s.replace('ঝবপ', 'sec')
    s = s.replace('ংবপ', 'sec')
    s = s.replace(':ধহ', 'tan')
    s = s.replace('ঃধহ', 'tan')
    s = s.replace('পড়ং', 'cos')
    s = s.replace('ংরহ', 'sin')
    s = s.replace('পড়ঃ', 'cot')

    # Trigo with A / B / C
    s = re.sub(r'\b(sin|cos|tan|cot|sec|cosec)অ\b', r'\1A', s)
    s = re.sub(r'\b(sin|cos|tan|cot|sec|cosec)ই\b', r'\1B', s)
    s = re.sub(r'\b(sin|cos|tan|cot|sec|cosec)ঈ\b', r'\1C', s)

    # θ (theta)
    s = s.replace('', 'θ')

    # Fake minus sign: SutonnyMJ 'ু' between terms
    s = re.sub(r'(\d+°|[a-zA-Zθ\)]|\b[০-৯]+)\s*ু\s*([a-zA-Zθ\(]|[০-৯]+)', r'\1 - \2', s)

    # Degree symbol: ক্ক or  -> °
    s = re.sub(r'(\d+)\s*ক্ক', r'\1°', s)
    s = re.sub(r'(\d+)\s*', r'\1°', s)

    # Multiplication: দ্ধ -> ×
    s = re.sub(r'(\d+)\s*দ্ধ\s*(\d+)', r'\1 × \2', s)

    # Clean double spaces
    s = re.sub(r'[ \t]+', ' ', s).strip()
    return s

def fix_lecture_03():
    fpath = os.path.join(MATH_DIR, 'লেকচার-০৩. ভগ্নাংশ.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        d = json.load(f)

    fixed_count = 0
    for q in d['questions']:
        opts = q.get('options', [])
        # If question has empty options
        if any(not opt or opt.strip() == '' for opt in opts):
            qtext = q.get('question', '')
            nums_q = re.findall(r'\b\d+\b', qtext)
            all_opt = ' '.join([o for o in opts if o])
            nums_opt = re.findall(r'\b\d+\b', all_opt)
            
            # Case A: 4 numerators at end of question and 4 denominators in options
            if len(nums_q) >= 4 and len(nums_opt) == 4:
                cand_nums = nums_q[-4:]
                cand_dens = nums_opt
                q['options'] = [f"{n}/{d}" for n, d in zip(cand_nums, cand_dens)]
                # Clean trailing numbers from question text
                trailing_pat = r'\s*' + r'\s+'.join(re.escape(n) for n in cand_nums) + r'\s*$'
                q['question'] = re.sub(trailing_pat, '', qtext).strip()
                fixed_count += 1
            # Case B: All 8 numbers in question or options
            elif len(nums_opt) >= 8:
                cand_nums = nums_opt[:4]
                cand_dens = nums_opt[4:8]
                q['options'] = [f"{n}/{d}" for n, d in zip(cand_nums, cand_dens)]
                fixed_count += 1
            elif q['id'] == 1:
                q['question'] = "৫/১২, ৬/১৩, ১১/২৪, ৩/৮ এর মধ্যে বড় ভগ্নাংশটি কোনটি? [৪১তম বিসিএস]"
                q['options'] = ["৫/১২", "৬/১৩", "১১/২৪", "৩/৮"]
                fixed_count += 1
            elif q['id'] == 6:
                q['question'] = "২/৩ × ৩/৪ = ? [পরিবার পরিকল্পনা অধিদপ্তরের বিভিন্ন পদে নিয়োগ- ২০১৪]"
                q['options'] = ["১/২", "২/৩", "৩/৪", "১/৪"]
                fixed_count += 1
            elif q['id'] == 8:
                q['question'] = "১/৫ + ০.১ + ০.০৫ = কত? [উপজেলা পরিসংখ্যান কর্মকর্তা- ২০১০]"
                q['options'] = ["৭/২০", "১৩/২০", "৭/১৫", "১৭/২০"]
                fixed_count += 1
            elif q['id'] == 17:
                q['question'] = "কোনটি ক্ষুদ্রতম ভগ্নাংশ? [২৪তম বিসিএস]"
                q['options'] = ["৩/৫", "৩/১১", "৮/৫", "২/২৭"]
                fixed_count += 1
            elif q['id'] == 22:
                q['question'] = "নিচের কোন ভগ্নাংশটি সবচেয়ে ছোট? [১৫তম বিসিএস]"
                q['options'] = ["৩/৪", "৪/৯", "৭/৯", "৯/১৩"]
                fixed_count += 1
            elif q['id'] == 25:
                q['question'] = "০.৪৭ পৌনঃপুনিক ভগ্নাংশটির সাধারণ ভগ্নাংশ কোনটি? [২৪তম বিসিএস]"
                q['options'] = ["৪৭/৯০", "৪৭/১০০", "৪৩/৯০", "১৯/৪০"]
                fixed_count += 1
            elif q['id'] == 39:
                q['question'] = "১১/১৪ এবং ১৪/১৭ এর মধ্যে কোনটি বড়? [১৭তম বিসিএস]"
                q['options'] = ["১১/১৪", "১৪/১৭", "উভয়টি সমান", "কোনোটিই নয়"]
                fixed_count += 1
            elif q['id'] == 40:
                q['question'] = "৩/৫ এবং ৪/৭ এর মধ্যে পার্থক্য কত?"
                q['options'] = ["১/৩৫", "২/৩৫", "৩/৩৫", "১/৭"]
                fixed_count += 1
            elif q['id'] == 42:
                q['question'] = "নিচের কোন ভগ্নাংশটি বৃহত্তম? [৩৪তম বিসিএস]"
                q['options'] = ["২/৩", "৩/৭", "৫/৯", "২/৫"]
                fixed_count += 1
            elif q['id'] == 43:
                q['question'] = "কোনটি সবচেয়ে বড় ভগ্নাংশ? [২৮তম বিসিএস]"
                q['options'] = ["২/৩", "৪/৭", "৫/৮", "৭/১১"]
                fixed_count += 1
            elif q['id'] == 44:
                q['question'] = "কোন ভগ্নাংশটি ক্ষুদ্রতম? [২৮তম বিসিএস]"
                q['options'] = ["১/৪", "৫/৮", "৭/১১", "১২/১৫"]
                fixed_count += 1
            elif q['id'] == 48:
                q['question'] = "৭/৯, ১৬/১৯, ১১/১৩ এর মধ্যে কোনটি বৃহত্তম? [১৬তম বিসিএস]"
                q['options'] = ["৭/৯", "১৬/১৯", "১১/১৩", "সবগুলো সমান"]
                fixed_count += 1
            elif q['id'] == 50:
                q['question'] = "৩/৪, ৪/৯, ৭/৮, ৯/১১ এর মধ্যে কোনটি বড়?"
                q['options'] = ["৩/৪", "৪/৯", "৭/৮", "৯/১১"]
                fixed_count += 1
            elif q['id'] == 55:
                q['question'] = "নিচের কোনটি ক্ষুদ্রতম ভগ্নাংশ?"
                q['options'] = ["৩/৫", "৭/১০", "৭/৮", "১২/১৫"]
                fixed_count += 1
            elif q['id'] == 64:
                q['question'] = "৪/৫, ২/৩, ১/২, ১/৪ এর মধ্যে কোনটি বৃহত্তম?"
                q['options'] = ["৪/৫", "২/৩", "১/২", "১/৪"]
                fixed_count += 1
            elif q['id'] == 78:
                q['question'] = "১/২ এবং ১/৩ এর যোগফল কত?"
                q['options'] = ["৫/৬", "২/৫", "৩/৫", "১/৫"]
                fixed_count += 1
            elif q['id'] == 79:
                q['question'] = "০.২ × ০.০২ = কত?"
                q['options'] = ["০.০০৪", "০.০৪", "০.৪", "০.০০২"]
                fixed_count += 1
            elif q['id'] == 82:
                q['question'] = "৭/৮ এবং ৫/৬ এর বিয়োগফল কত?"
                q['options'] = ["১/২৪", "২/২৪", "১/১২", "১/৬"]
                fixed_count += 1
            elif q['id'] == 86:
                q['question'] = "কোনটি ক্ষুদ্রতম ভগ্নাংশ?"
                q['options'] = ["৪/৫", "১২/১৫", "১১/১৪", "১৭/২১"]
                fixed_count += 1
            elif q['id'] == 87:
                q['question'] = "কোন ভগ্নাংশটি বড়?"
                q['options'] = ["৪/২৭", "৩/৩৬", "১১/৪৫", "২/৯"]
                fixed_count += 1
            elif q['id'] == 88:
                q['question'] = "১/৪, ১/১২, ১/১৬, ১/২০ এর মধ্যে কোনটি বৃহত্তম?"
                q['options'] = ["১/৪", "১/১২", "১/১৬", "১/২০"]
                fixed_count += 1
            elif q['id'] == 91:
                q['question'] = "১/৩ এবং ২/৩ এর যোগফল কত?"
                q['options'] = ["১", "২/৩", "৪/৩", "১/২"]
                fixed_count += 1
            elif q['id'] == 95:
                q['question'] = "১/৩, ৩/৭, ২/৪, ৫/৯ এর মধ্যে কোনটি বৃহত্তম?"
                q['options'] = ["১/৩", "৩/৭", "২/৪", "৫/৯"]
                fixed_count += 1
            elif q['id'] == 96:
                q['question'] = "৩/৪, ৪/৯, ৭/৯, ৯/১৩ এর মধ্যে কোনটি ক্ষুদ্রতম?"
                q['options'] = ["৩/৪", "৪/৯", "৭/৯", "৯/১৩"]
                fixed_count += 1
            elif q['id'] == 102:
                q['question'] = "১/৩ + ১/৪ = কত?"
                q['options'] = ["৭/১২", "২/৭", "১/১২", "৫/১২"]
                fixed_count += 1
            elif q['id'] == 105:
                q['question'] = "৫/৬, ১২/১৫, ১১/১৪, ১৭/২১ এর মধ্যে ক্ষুদ্রতম কোনটি?"
                q['options'] = ["৫/৬", "১২/১৫", "১১/১৪", "১৭/২১"]
                fixed_count += 1

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Fixed {fixed_count} questions in Lecture 03 (Fractions)")

def fix_lecture_19():
    fpath = os.path.join(MATH_DIR, 'লেকচার-১৯. ত্রিকোণমিতি, পরিমাপ ও একক.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        d = json.load(f)

    fixed_count = 0
    L19_SPECIFIC = {
        2: {
            'question': "৩ cotA = ৪ হলে, sinA এর মান কত? [১৬তম প্রভাষক নিবন্ধন- ২০১৯]",
            'options': ["৪/৫", "৩/৫", "৩/৪", "৪/৩"],
            'answer': "খ"
        },
        3: {
            'question': "tan θ = ১/√৩ হলে, cos θ = কত? [১৪ তম প্রভাষক নিবন্ধন পরীক্ষা-২০১৭]",
            'options': ["১/২", "১/√২", "√৩/২", "১"],
            'answer': "গ"
        },
        5: {
            'question': "cosec (৯০° - θ) = ২ হলে, cos θ = কত? [১০ম প্রভাষক নিবন্ধন পরীক্ষা-২০১৪]",
            'options': ["১", "√৩/২", "১/২", "১/√২"],
            'answer': "গ"
        },
        7: {
            'question': "(sec θ + tan θ) = ৭/৫ হলে, (sec θ - tan θ) এর মান কত? [১৫তম শিক্ষক নিবন্ধন সহকারী শিক্ষক-২০১৯]",
            'options': ["৫/৭", "৭/৫", "৩/৫", "১/৫"],
            'answer': "ক"
        },
        32: {
            'question': "sinA = ১/২ হলে, cosA = কত?",
            'options': ["১/২", "১/√২", "√৩/২", "২/√৩"],
            'answer': "গ"
        },
        33: {
            'question': "secA + tanA = ৫/২ হলে, secA - tanA = ? [৪২তম বিসিএস (বিশেষ)]",
            'options': ["১/২", "১/৫", "২/৫", "৫/২"],
            'answer': "গ"
        },
        35: {
            'question': "tan θ = ১/√৩ হলে, cos θ = কত?",
            'options': ["১/২", "১/√২", "√৩/২", "√৩"],
            'answer': "গ"
        },
        36: {
            'question': "tan θ = ৩/৪ হলে, cosec θ এর মান কত?",
            'options': ["৩/৫", "৫/৩", "৪/৫", "৫/৪"],
            'answer': "খ"
        },
        37: {
            'question': "যদি cot θ = ৫/১২ হয়, তবে cosec θ এর মান কত?",
            'options': ["৫/১৩", "১৩/১২", "১২/১৩", "১৩/৫"],
            'answer': "খ"
        },
        38: {
            'question': "৩ cotA = ৪ হলে, sinA এর মান কত?",
            'options': ["৪/৫", "৩/৫", "৩/৪", "৪/৩"],
            'answer': "খ"
        },
        44: {
            'question': "B = ৬০° হলে, (১ - tan²B) / (১ + tan²B) এর মান কত? [জাতীয় রাজস্ব বোর্ডের সহকারী রাজস্ব কর্মকর্তা- ২০১৭]",
            'options': ["১/২", "-১/২", "০", "১"],
            'answer': "খ"
        },
        45: {
            'question': "sec θ + tan θ = ৫/৩ হলে, sec θ - tan θ এর মান কত? [গৃহায়ণ ও গণপূর্ত মন্ত্রণালয়ের আবাসন পরিদপ্তরের সহকারী পরিচালক-'০৬]",
            'options': ["৫/৩", "-৫/৩", "৩/৫", "-৩/৫"],
            'answer': "গ"
        },
        56: {
            'question': "(sin θ + cos θ) / (sin θ - cos θ) = ৭ হলে, tan θ এর মান কত? [বিশেষ শিক্ষক নিবন্ধন (স্কুল/সমপর্যায়)'১০]",
            'options': ["৩/৪", "৪/৩", "৭/৮", "৮/৭"],
            'answer': "খ"
        },
        65: {
            'question': "৩ cotA = ৪ হলে, sinA এর মান কত?",
            'options': ["৪/৫", "৩/৫", "৩/৪", "৪/৩"],
            'answer': "খ"
        },
        66: {
            'question': "sin θ = ৪/৫ হলে, tan θ = কত?",
            'options': ["৪/৩", "৩/৪", "৩/৫", "৫/৪"],
            'answer': "ক"
        },
        67: {
            'question': "tan θ = -৫/১২, π/২ < θ < π হলে cosec θ এর মান-",
            'options': ["-১৩/৫", "৫/১৩", "-৫/১৩", "১৩/৫"],
            'answer': "ঘ"
        },
        68: {
            'question': "(sec θ + tan θ) = ৭/৫ হলে, (sec θ - tan θ) এর মান কত?",
            'options': ["৫/৭", "৭/৫", "৩/৫", "১/৫"],
            'answer': "ক"
        }
    }

    for q in d['questions']:
        qid = q.get('id')
        if qid in L19_SPECIFIC:
            fix = L19_SPECIFIC[qid]
            q['question'] = fix['question']
            q['options'] = fix['options']
            q['answer'] = fix['answer']
            fixed_count += 1
        else:
            q['question'] = clean_math_text(q.get('question', ''))
            q['options'] = [clean_math_text(o) for o in q.get('options', [])]
            q['explanation'] = clean_math_text(q.get('explanation', ''))

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Fixed {fixed_count} questions in Lecture 19 (Trigonometry)")

def fix_all_math_files():
    for fname in sorted(os.listdir(MATH_DIR)):
        if not fname.endswith('.json'): continue
        fpath = os.path.join(MATH_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)

        changed = False
        for q in d['questions']:
            old_q = q.get('question', '')
            new_q = clean_math_text(old_q)
            if new_q != old_q:
                q['question'] = new_q
                changed = True

            old_opts = q.get('options', [])
            new_opts = [clean_math_text(o) for o in old_opts]
            if new_opts != old_opts:
                q['options'] = new_opts
                changed = True

            old_exp = q.get('explanation', '')
            new_exp = clean_math_text(old_exp)
            if new_exp != old_exp:
                q['explanation'] = new_exp
                changed = True

        if changed:
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
            print(f"Cleaned symbols in {fname}")

if __name__ == '__main__':
    fix_lecture_03()
    fix_lecture_19()
    fix_all_math_files()
