import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

def apply_fixes():
    # 1. GK L8 Q55: 'গ - ার' -> 'গণ্ডার'
    for f in os.listdir(os.path.join(base, 'GK')):
        if '০৮' in f:
            p = os.path.join(base, 'GK', f)
            with open(p, 'r', encoding='utf-8') as fp: d = json.load(fp)
            for q in d['questions']:
                if q['id'] == 55:
                    q['options'][1] = 'গণ্ডার'
            with open(p, 'w', encoding='utf-8') as fp: json.dump(d, fp, ensure_ascii=False, indent=2)

    # 2. GK L9 Q160: '"Man is a political animal" - who said this?'
    for f in os.listdir(os.path.join(base, 'GK')):
        if '০৯' in f:
            p = os.path.join(base, 'GK', f)
            with open(p, 'r', encoding='utf-8') as fp: d = json.load(fp)
            for q in d['questions']:
                if q['id'] == 160:
                    q['question'] = '"Man is a political animal" - who said this? [৩৬তম বিসিএস] "মানুষ সামাজিক ও রাজনৈতিক জীব" কে বলেছেন?'
            with open(p, 'w', encoding='utf-8') as fp: json.dump(d, fp, ensure_ascii=False, indent=2)

    # 3. GK L11 Q127 & Q353: 'Bretton Woods Institutions'
    for f in os.listdir(os.path.join(base, 'GK')):
        if '১১' in f:
            p = os.path.join(base, 'GK', f)
            with open(p, 'r', encoding='utf-8') as fp: d = json.load(fp)
            for q in d['questions']:
                if q['id'] == 127:
                    q['question'] = 'কোনটি Bretton Woods Institutions এর অন্তর্ভুক্ত?'
                elif q['id'] == 353:
                    q['question'] = 'কোনটি Bretton Woods Institutions এর অন্তর্ভুক্ত? [৪২তম বিসিএস]'
            with open(p, 'w', encoding='utf-8') as fp: json.dump(d, fp, ensure_ascii=False, indent=2)

    # 4. GK L14 Q243: Olympic rings
    for f in os.listdir(os.path.join(base, 'GK')):
        if '১৪' in f:
            p = os.path.join(base, 'GK', f)
            with open(p, 'r', encoding='utf-8') as fp: d = json.load(fp)
            for q in d['questions']:
                if q['id'] == 243:
                    q['options'] = [
                        "Blue, Yellow, Black, Green and Red",
                        "Red, Blue, Green, White and Black",
                        "Red, Yellow, Green, Violet and Black",
                        "Blue, Red, Green, Violet and Black"
                    ]
                    q['answer'] = "ক"
                    q['explanation'] = "অলিম্পিক পতাকার ৫টি বলয় ৫টি মহাদেশকে নির্দেশ করে, যার রং হলো নীল, হলুদ, কালো, সবুজ ও লাল (Blue, Yellow, Black, Green, Red)।"
            with open(p, 'w', encoding='utf-8') as fp: json.dump(d, fp, ensure_ascii=False, indent=2)

    # 5. GK L16 Q73 opt3: 'Axillary vein'
    for f in os.listdir(os.path.join(base, 'GK')):
        if '১৬' in f:
            p = os.path.join(base, 'GK', f)
            with open(p, 'r', encoding='utf-8') as fp: d = json.load(fp)
            for q in d['questions']:
                if q['id'] == 73:
                    q['options'][3] = 'Axillary vein'
            with open(p, 'w', encoding='utf-8') as fp: json.dump(d, fp, ensure_ascii=False, indent=2)

    # 6. GK L18 Q81 q: 'File, Edit, View'
    for f in os.listdir(os.path.join(base, 'GK')):
        if '১৮' in f:
            p = os.path.join(base, 'GK', f)
            with open(p, 'r', encoding='utf-8') as fp: d = json.load(fp)
            for q in d['questions']:
                if q['id'] == 81:
                    q['question'] = 'মাইক্রোসফট ওয়ার্ড ডকুমেন্টের File, Edit, View ইত্যাদি শব্দ বিশিষ্ট লাইনটিকে বলা হয়-'
            with open(p, 'w', encoding='utf-8') as fp: json.dump(d, fp, ensure_ascii=False, indent=2)

    # 7. Math files: replace isolated ু with minus in powers/numbers
    math_dir = os.path.join(base, 'Math')
    for f in os.listdir(math_dir):
        if not f.endswith('.json'): continue
        p = os.path.join(math_dir, f)
        with open(p, 'r', encoding='utf-8') as fp: d = json.load(fp)
        mod = False
        for q in d['questions']:
            # Replace ু in math questions/options
            for fld in ['question', 'explanation']:
                orig = q[fld]
                new = orig
                new = re.sub(r'ু([০-৯\d])', r'-\1', new)
                new = new.replace(' ু১', ' -1').replace(' ু২', ' -2').replace(' ু৩', ' -3').replace(' ু৫', ' -5').replace(' ু৭', ' -7')
                new = new.replace(' ু', ' -')
                if new != orig:
                    q[fld] = new
                    mod = True
            for i in range(len(q['options'])):
                orig = q['options'][i]
                new = orig
                new = re.sub(r'ু([০-৯\d])', r'-\1', new)
                new = new.replace(' ু১', ' -1').replace(' ু২', ' -2').replace(' ু৩', ' -3').replace(' ু৫', ' -5').replace(' ু৭', ' -7')
                new = new.replace(' ু', ' -')
                if new != orig:
                    q['options'][i] = new
                    mod = True
        if mod:
            with open(p, 'w', encoding='utf-8') as fp:
                json.dump(d, fp, ensure_ascii=False, indent=2)
            print(f"Updated Math minus in: {f}")

    print("Completed isolated kar & math minus fixes!")

if __name__ == '__main__':
    apply_fixes()
