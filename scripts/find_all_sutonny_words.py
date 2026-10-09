import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

# Mapping of known Sutonny words
SUTONNY_MAP = {
    'ঝবহরড়ৎ ঙভভরপবৎ': 'Senior Officer',
    'ঝবহরড়ৎ': 'Senior',
    'ঙভভরপবৎ': 'Officer',
    'ড়ভভরপবৎ': 'Officer',
    'ঔধহধঃধ ইধহশ': 'Janata Bank',
    'ঔধহধঃধ': 'Janata',
    'ইধহশ': 'Bank',
    'ঝড়হধষর ইধহশ': 'Sonali Bank',
    'ঝড়হধষর': 'Sonali',
    'অমৎধহর ইধহশ': 'Agrani Bank',
    'অমৎধহর': 'Agrani',
    'চঁনধষর ইধহশ': 'Pubali Bank',
    'চঁনধষর': 'Pubali',
    'ঔঁহরড়ৎ ঙভভরপবৎ': 'Junior Officer',
    'ঔঁহরড়ৎ': 'Junior',
    'ঊীবপঁঃরাব ঙভভরপবৎ': 'Executive Officer',
    'ঊীবপঁঃরাব': 'Executive',
    'চৎড়নধংর কড়ষষুধহ ইধহশ': 'Probashi Kallyan Bank',
    'চৎড়নধংর': 'Probashi',
    'কড়ষষুধহ': 'Kallyan',
    'ইধহমষধফবংয ইধহশ': 'Bangladesh Bank',
    'ইধহমষধফবংয': 'Bangladesh',
    'খঃফ.': 'Ltd.',
    'খঃফ': 'Ltd',
    'ধহফ': 'and',
    'ঈধংয': 'Cash',
    'ওঋIC': 'IFIC',
    'জঅকটই': 'RAKUB',
    'ইঐইঋঈ': 'BHBFC',
    'ইকই': 'BKB',
    'ঘঅঞঙ': 'NATO',
    'টঘওঈঊঋ': 'UNICEF',
    'ডঞঙ': 'WTO',
    'ইওগঝঞঊঈ': 'BIMSTEC',
    'ইঅজঈ': 'BARC',
    'টঘউচ': 'UNDP',
    'টঘঊঝঈঙ': 'UNESCO',
    'ঝঅঋঞঅ': 'SAFTA',
    'ঊঁৎড়ঢ়বধহ টহরড়হ': 'European Union',
    'ঊঁৎড়ঢ়বধহ': 'European',
    'টহরড়হ': 'Union',
    'ওহঃধৎরস ঈধংয ঈড়ঁঢ়ড়হ': 'Interim Cash Coupon',
    'ওৎধয়': 'Iraq',
    'ঝবিফবহ': 'Sweden',
    'ঋৎধহপব': 'France',
    'ঘড়ৎধিু': 'Norway',
    'এবহবাধ': 'Geneva',
    'ঠরবহহধ': 'Vienna',
    'ডধংযরহমঃড়হ উ.ঈ.': 'Washington D.C.',
    'টঝ': 'US',
    'টক': 'UK',
    'ইৎধুরষ': 'Brazil',
    'ডযধঃ রং ঝঅঋঞঅ?': 'What is SAFTA?',
    'ডযধঃ': 'What',
    'রং': 'is',
    'ডযরপয হধঃরড়হ ধষধিুং ংঢ়বধশং ভরৎংঃ ধঃ:যব টঝ মবহবৎধষ অংংবসনষু ?': 'Which nation always speaks first at the UN General Assembly?',
}

total_found = 0
for root, dirs, files in sorted(os.walk(base)):
    for f in sorted(files):
        if not f.endswith('.json'): continue
        p = os.path.join(root, f)
        with open(p, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        for q in d.get('questions', []):
            qid = q.get('id')
            texts = [('q', q.get('question', ''))] + [(f'opt{i}', o) for i, o in enumerate(q.get('options', []))] + [('exp', q.get('explanation', ''))]
            for field, text in texts:
                if not isinstance(text, str): continue
                for k in sorted(SUTONNY_MAP.keys(), key=lambda x: -len(x)):
                    if k in text:
                        total_found += 1
                        print(f"[{f}] Q{qid} {field}: found '{k}' -> '{SUTONNY_MAP[k]}'")
                        break

print(f"\nTotal occurrences found: {total_found}")
