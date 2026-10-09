import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

# Final targeted question updates:
def apply_final_updates():
    # 1. GK L18 Q113
    for f in os.listdir(os.path.join(base, 'GK')):
        if '১৮' in f and f.endswith('.json'):
            p = os.path.join(base, 'GK', f)
            with open(p, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
            for q in d['questions']:
                if q['id'] == 113:
                    q['options'] = ["http", "www", "URL", "HTML"]
                    q['answer'] = "গ"
                    q['explanation'] = "একটি প্রতিষ্ঠানের পূর্ণাঙ্গ ওয়েব ঠিকানাকে নির্দেশ করে 'URL' (Uniform Resource Locator)।"
            with open(p, 'w', encoding='utf-8') as fp:
                json.dump(d, fp, ensure_ascii=False, indent=2)

    # 2. Math L12 Q37
    for f in os.listdir(os.path.join(base, 'Math')):
        if '১২' in f and f.endswith('.json'):
            p = os.path.join(base, 'Math', f)
            with open(p, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
            for q in d['questions']:
                if q['id'] == 37:
                    q['question'] = "16x² - 25y² - 8x + 10y এর উৎপাদক কত? [৩৩তম বিসিএস লিখিত]"
                    q['options'] = [
                        "(4x + 5y)(4x + 5y - 2)",
                        "(4x - 5y)(4x - 5y + 2)",
                        "(4x - 5y)(4x + 5y - 2)",
                        "(4x + 5y)(4x + 5y + 2)"
                    ]
                    q['answer'] = "গ"
                    q['explanation'] = "16x² - 25y² - 8x + 10y = (4x - 5y)(4x + 5y) - 2(4x - 5y) = (4x - 5y)(4x + 5y - 2)। সঠিক মান হলো '(4x - 5y)(4x + 5y - 2)'।"
            with open(p, 'w', encoding='utf-8') as fp:
                json.dump(d, fp, ensure_ascii=False, indent=2)

    # 3. Math L14 Q106
    for f in os.listdir(os.path.join(base, 'Math')):
        if '১৪' in f and f.endswith('.json'):
            p = os.path.join(base, 'Math', f)
            with open(p, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
            for q in d['questions']:
                if q['id'] == 106:
                    q['question'] = "অজানা সংখ্যাটি কত? ৪, ৬, ৯, ৬, ১৪, ৬, ... ?"
            with open(p, 'w', encoding='utf-8') as fp:
                json.dump(d, fp, ensure_ascii=False, indent=2)

    # 4. Bangla L9 Q55
    for f in os.listdir(os.path.join(base, 'Bangla')):
        if '০৯' in f and f.endswith('.json'):
            p = os.path.join(base, 'Bangla', f)
            with open(p, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
            for q in d['questions']:
                if q['id'] == 55:
                    q['question'] = "শুদ্ধ বাক্যটি চিহ্নিত করুন-"
            with open(p, 'w', encoding='utf-8') as fp:
                json.dump(d, fp, ensure_ascii=False, indent=2)

    # 5. Bangla L10 Q107 & Q231
    for f in os.listdir(os.path.join(base, 'Bangla')):
        if '১০' in f and f.endswith('.json'):
            p = os.path.join(base, 'Bangla', f)
            with open(p, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
            for q in d['questions']:
                if q['id'] == 107:
                    q['options'][0] = "পাণ্ডিত্যপূর্ণ কথা"
                elif q['id'] == 231:
                    q['options'][0] = "পাণ্ডিত্যের দ্বারা যিনি মূর্খ"
                    q['options'][2] = "পাণ্ডিত্যে যিনি মূর্খ"
            with open(p, 'w', encoding='utf-8') as fp:
                json.dump(d, fp, ensure_ascii=False, indent=2)

    # 6. Global Decomposed O-kar replacements across all files
    REPLACEMENTS = [
        ('খোঁজা', 'খোঁজা'),
        ('খোঁজার', 'খোঁজার'),
        ('খোঁচা', 'খোঁচা'),
        ('গোঁফে', 'গোঁফে'),
        ('দাড়ি-গোঁফ', 'দাড়ি-গোঁফ'),
        ('নিখোঁজ', 'নিখোঁজ'),
        ('ছোঁয়ার', 'ছোঁয়ার'),
        ('কানছোঁয়া', 'কানছোঁয়া'),
        ('কানাসোঁআ', 'কানায়-কানায়'),
        ('গোঁড়া', 'গোঁড়া'),
        ('গোঁয়ার', 'গোঁয়ার'),
        ('রোঁ', 'রোঁয়া'),
        ('মার্কো', 'মার্কো'),
        ('পাি - ত্য', 'পাণ্ডিত্য'),
    ]

    for root, dirs, files in os.walk(base):
        for f in files:
            if not f.endswith('.json'): continue
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
            mod = False
            for q in data.get('questions', []):
                for fld in ['question', 'explanation']:
                    if fld in q and isinstance(q[fld], str):
                        orig = q[fld]
                        new = orig
                        for src, tgt in REPLACEMENTS:
                            if src in new:
                                new = new.replace(src, tgt)
                        if new != orig:
                            q[fld] = new
                            mod = True
                for i in range(len(q.get('options', []))):
                    orig = q['options'][i]
                    if isinstance(orig, str):
                        new = orig
                        for src, tgt in REPLACEMENTS:
                            if src in new:
                                new = new.replace(src, tgt)
                        if new != orig:
                            q['options'][i] = new
                            mod = True
            if mod:
                with open(p, 'w', encoding='utf-8') as fp:
                    json.dump(data, fp, ensure_ascii=False, indent=2)
                print(f"Updated decomposed o-kar in: {f}")

    print("Completed final updates successfully!")

if __name__ == '__main__':
    apply_final_updates()
