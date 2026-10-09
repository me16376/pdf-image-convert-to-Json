import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA/GK'

for lec_name in ['লেকচার-১৭', 'লেকচার-১৮']:
    for f in sorted(os.listdir(base)):
        if lec_name in f and f.endswith('.json'):
            p = os.path.join(base, f)
            with open(p, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
            print(f"\n====================== {f} ======================")
            for q in d['questions']:
                qid = q['id']
                q_text = q['question']
                opts = q['options']
                all_t = [q_text] + opts
                # Check if has Sutonny words
                has_sutonny = any(
                    any(k in t for k in [':যব', 'ড়ভ:', 'ধঃ:', 'ঘড়হব', 'ঝুংঃ', 'চৎড়', 'গধহধ', 'ঙঢ়বৎ', 'রং ধ', 'টঘ ', 'ঠরঃধ', 'ওহভড়', 'জবংড়', 'চঈও', 'ইটঝ', 'ইরঃ', 'ঠওজ', 'গড়ঃয', 'ঝরসঢ়', 'খওঘট', 'গঝ '])
                    for t in all_t
                )
                if has_sutonny:
                    print(f"\nQ{qid}:")
                    print(f"  Question: {q_text}")
                    for i, o in enumerate(opts):
                        print(f"  opt{i}: {o}")
                    print(f"  Answer: {q['answer']}")
