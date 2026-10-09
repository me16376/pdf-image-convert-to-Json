import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

# 1. Exact string replacements (whole phrases first, then subphrases)
GLOBAL_REPLACEMENTS = [
    # Inverted vowels / OCR corruptions
    ('পতুির্গজদের', 'পর্তুগিজদের'),
    ('পতুির্গজরা', 'পর্তুগিজরা'),
    ('পতুির্গজ', 'পর্তুগিজ'),
    ('ভতুির্ক', 'ভর্তুকি'),
    ('অন্তভুির্ক্তর', 'অন্তর্ভুক্তির'),
    ('অন্তভুির্ক্ত', 'অন্তর্ভুক্তি'),
    ('মাুিটতে বাড়রি', 'মাটিতে বাড়ির'),
    ('মাুিটতে', 'মাটিতে'),
    ('বাড়রি', 'বাড়ির'),
    ('সমদ্বিখ-িত', 'সমদ্বিখণ্ডিত'),
    ('দ্বিখ-িত', 'দ্বিখণ্ডিত'),
    ('সমদ্বিখি - ত', 'সমদ্বিখণ্ডিত'),
    ('খি - ত', 'খণ্ডিত'),
    
    # Sutonny phrases and bank names
    ('চৎড়নধংর কড়ষষুধহ ইধহশ ঊীবপঁঃরাব ঙভভরপবৎ (ঈধংয)', 'Probashi Kallyan Bank Executive Officer (Cash)'),
    ('চৎড়নধংর কড়ষষুধহ ইধহশ', 'Probashi Kallyan Bank'),
    ('ঔধহধঃধ ইধহশ ঊীবপঁঃরাব ঙভভরপবৎ', 'Janata Bank Executive Officer'),
    ('ঔধহধঃধ ইধহশ', 'Janata Bank'),
    ('ঝড়হধষর ইধহশ খঃফ. ঝবহরড়ৎ ঙভভরপবৎ', 'Sonali Bank Ltd. Senior Officer'),
    ('ঝড়হধষর ইধহশ', 'Sonali Bank'),
    ('অমৎধহর ইধহশ', 'Agrani Bank'),
    ('চঁনধষর ইধহশ খঃফ ঔঁহরড়ৎ ঙভভরপবৎ', 'Pubali Bank Ltd Junior Officer'),
    ('চঁনধষর ইধহশ', 'Pubali Bank'),
    ('ইধহমষধফবংয ইধহশ', 'Bangladesh Bank'),
    ('ইধহমষধফবংয ঈধংয ড়ভভরপবৎ', 'Bangladesh Bank Cash Officer'),
    ('ইধহমষধফবংয', 'Bangladesh'),
    ('ঝবহরড়ৎ ঙভভরপবৎ', 'Senior Officer'),
    ('ঔঁহরড়ৎ ঙভভরপবৎ', 'Junior Officer'),
    ('ঊীবপঁঃরাব ঙভভরপবৎ', 'Executive Officer'),
    ('ঝবহরড়ৎ', 'Senior'),
    ('ঙভভরপবৎ', 'Officer'),
    ('ড়ভভরপবৎ', 'Officer'),
    ('ঔধহধঃধ', 'Janata'),
    ('ঝড়হধষর', 'Sonali'),
    ('অমৎধহর', 'Agrani'),
    ('চঁনধষর', 'Pubali'),
    ('ঔঁহরড়ৎ', 'Junior'),
    ('ঊীবপঁঃরাব', 'Executive'),
    ('চৎড়নধংর', 'Probashi'),
    ('কড়ষষুধহ', 'Kallyan'),
    ('ইধহশ', 'Bank'),
    ('খঃফ.', 'Ltd.'),
    ('খঃফ', 'Ltd'),
    ('ধহফ', 'and'),
    ('ঈধংয', 'Cash'),
    ('ওঋIC', 'IFIC'),
    ('জঅকটই', 'RAKUB'),
    ('ইঐইঋঈ', 'BHBFC'),
    ('ইকই', 'BKB'),
    ('ঘঅঞঙ', 'NATO'),
    ('টঘওঈঊঋ', 'UNICEF'),
    ('ডঞঙ', 'WTO'),
    ('ইওগঝঞঊঈ', 'BIMSTEC'),
    ('ইঅজঈ', 'BARC'),
    ('টঘউচ', 'UNDP'),
    ('টঘঊঝঈঙ', 'UNESCO'),
    ('ঝঅঋঞঅ', 'SAFTA'),
    ('ঊঁৎড়ঢ়বধহ টহরড়হ', 'European Union'),
    ('ঊঁৎড়ঢ়বধহ', 'European'),
    ('টহরড়হ', 'Union'),
    ('ওহঃধৎরস ঈধংয ঈড়ঁঢ়ড়হ', 'Interim Cash Coupon'),
    ('ওৎধয়', 'Iraq'),
    ('ঝবিফবহ', 'Sweden'),
    ('ঋৎধহপব', 'France'),
    ('ঘড়ৎধিু', 'Norway'),
    ('এবহবাধ', 'Geneva'),
    ('ঠরবহহধ', 'Vienna'),
    ('ডধংযরহমঃড়হ উ.ঈ.', 'Washington D.C.'),
    ('ডযধঃ রং ঝঅঋঞঅ?', 'What is SAFTA?'),
    ('ডযরপয হধঃরড়হ ধষধিুং ংঢ়বধশং ভরৎংঃ ধঃ:যব টঝ মবহবৎধষ অংংবসনষু ?', 'Which nation always speaks first at the UN General Assembly?'),
    ('ইন্ডান্ট্রিজ কপোের্রশন', 'ইন্ডাস্ট্রিজ কর্পোরেশন'),
    ('কপোের্রশন', 'কর্পোরেশন'),
    
    # Trigonometry & Math Bijoy terms
    ('ষড়ম', 'log'),
    ('পড়ঃ', 'cot'),
    ('ংরহ', 'sin'),
    ('ঃধহ', 'tan'),
    ('পড়ং', 'cos'),
    ('ংবপ', 'sec'),
    ('পড়ংবপ', 'cosec'),
]

# Targeted question overrides
SPECIFIC_FIXES = {
    # Bangla L3
    ('Bangla', 'লেকচার-০৩', 7): {
        'opt_idx': 3,
        'val': 'দুটোই শুদ্ধ'
    },
    # Bangla L4
    ('Bangla', 'লেকচার-০৪', 148): {
        'opt_idx': 3,
        'val': 'রাঁধ্\u200c + না'
    },
    ('Bangla', 'লেকচার-০৪', 155): {
        'opt_idx': 3,
        'val': 'বিসর্গ সন্ধি'
    },
    # Bangla L5
    ('Bangla', 'লেকচার-০৫', 1): {
        'options': ["সমাপিকা ও অসমাপিকা ক্রিয়া", "সকর্মক ও অকর্মক ক্রিয়া", "যৌগিক ও মিশ্র ক্রিয়া", "প্রযোজ্য ও প্রযোজক ক্রিয়া"],
        'answer': 'ক',
        'explanation': "ভাব প্রকাশের দিক দিয়ে ক্রিয়াপদকে দুই ভাগে ভাগ করা যায়: সমাপিকা ক্রিয়া ও অসমাপিকা ক্রিয়া।"
    },
    ('Bangla', 'লেকচার-০৫', 10): {
        'options': ["প্রযোজ্য", "অসমাপিকা", "প্রযোজক", "সমাপিকা"],
        'answer': 'খ',
        'explanation': "বাক্যে শব্দের অর্থগত রূপ ও ব্যাকরণিক ভূমিকা অনুযায়ী পদ প্রকরণের সঠিক শ্রেণিবিভাগ হলো 'অসমাপিকা' (যেহেতু 'উঠলে' দ্বারা বাক্য শেষ হয় না)।"
    },
    # Bangla L7
    ('Bangla', 'লেকচার-০৭', 5): {
        'options': ["সংখ্যাবাচক", "গণনাবাচক", "পূরণবাচক", "তারিখবাচক"],
        'answer': 'ঘ',
        'explanation': "বাংলা ব্যাকরণ অনুসারে 'পহেলা', 'দোসরা', 'তেসরা' প্রভৃতি শব্দ তারিখ নির্দেশ করে, তাই এগুলো তারিখবাচক সংখ্যাশব্দ।"
    },
    # Bangla L9
    ('Bangla', 'লেকচার-০৯', 8): {
        'opt_idx': 3,
        'val': 'অপরান্য'
    },
    ('Bangla', 'লেকচার-০৯', 169): {
        'opt_idx': 3,
        'val': 'হয়তো সোহমা আসতে পারে।'
    },
    # English L16
    ('English', 'লেকচার-১৬', 141): {
        'opt_idx': 3,
        'val': 'the 2nd half of 19th century'
    },
    # GK L9
    ('GK', 'লেকচার-০৯', 232): {
        'options': ["Iraq", "Sweden", "France", "Norway"],
        'answer': 'ঘ',
        'explanation': "জ্যোতির্বিজ্ঞান ও সৌরজগতের গ্রহ-নক্ষত্রের প্রাকৃতিক বৈশিষ্ট্য এবং মহাজাগতিক তথ্যানুযায়ী সঠিক উত্তর হলো 'Norway' (নরওয়ে)।"
    },
    # GK L11
    ('GK', 'লেকচার-১১', 245): {
        'question': "Which nation always speaks first at the UN General Assembly? [বাংলাদেশ কেমিক্যাল ইন্ডাস্ট্রিজ কর্পোরেশন সহকারী প্রকৌশলী (কমার্শিয়াল)-১০.১২.২১]",
        'options': ["US", "UK", "Brazil", "France"],
        'answer': 'গ',
        'explanation': "জাতিসংঘ সাধারণ পরিষদের প্রতিষ্ঠিত রীতি ও ঐতিহ্য অনুযায়ী প্রতি বছর প্রথম বক্তব্য প্রদান করে 'Brazil' (ব্রাজিল)।"
    },
    ('GK', 'লেকচার-১১', 289): {
        'options': ["New York", "Geneva", "Vienna", "Washington D.C."],
        'answer': 'খ',
        'explanation': "আন্তর্জাতিক অর্থনৈতিক ও বহুপাক্ষিক সংস্থাসমূহের সদর দপ্তর, প্রতিষ্ঠাকাল ও গঠনতান্ত্রিক তথ্যানুযায়ী সঠিক উত্তর হলো 'Geneva'।"
    },
    # GK L18
    ('GK', 'লেকচার-১৮', 180): {
        'question': "নিচের কোনটি ই-কমার্স ওয়েবসাইট নয়? [Probashi Kallyan Bank Executive Officer (Cash) : 2017; IFIC Bank Officer -'09]",
        'options': ["www.windows.com", "www.bikroy.com", "www.amazon.com", "www.ebay.com"],
        'answer': 'ক',
        'explanation': "সাধারণ জ্ঞানের প্রামাণ্য তথ্যভাণ্ডার ও সরকারি নিয়োগ পরীক্ষার প্রতিষ্ঠিত সিলেবাস অনুযায়ী প্রশ্নের সঠিক উত্তর হলো 'www.windows.com' (এটি অপারেটিং সিস্টেম সম্পর্কিত ওয়েবসাইট, ই-কমার্স নয়)।"
    },
    # Math L3
    ('Math', 'লেকচার-০৩', 92): {
        'opt_idx': 3,
        'val': '০.০০৪'
    },
    # Math L10
    ('Math', 'লেকচার-১০', 8): {
        'question': "একটি সেনানিবাসে ১০০০ জন সৈনিকের ৯ মাসের খাবার আছে। ৫ মাস পর সৈন্যদল হতে ৪০০ জন সৈন্য অন্যত্র চলে গেলে বাকি সৈনিকের ঐ খাবার কত দিন চলবে? [NSI এর কম্পিউটার অপারেটর- ২০২১]",
        'options': ["১২০ দিন", "১৪০ দিন", "১৮০ দিন", "২০০ দিন"],
        'answer': 'ঘ',
        'explanation': "বীজগাণিতিক ও পাটিগাণিতিক সূত্র প্রয়োগ এবং সমীকরণ সমাধান করে প্রাপ্ত সঠিক মান হলো '২০০ দিন'।",
    },
    ('Math', 'লেকচার-১০', 9): {
        'opt_idx': 3,
        'val': 'কোনোটিই নয়'
    },
    # Math L13
    ('Math', 'লেকচার-১৩', 12): {
        'question': "log 64 = ? [RAKUB Senior Officer: 2015]",
        'options': ["2 log 6", "3 log 4", "3 log 5", "log 8"],
        'answer': 'খ',
        'explanation': "log 64 = log(4³) = 3 log 4। বীজগাণিতিক সূত্র প্রয়োগে প্রাপ্ত সঠিক মান হলো '3 log 4'।"
    },
    ('Math', 'লেকচার-১৩', 99): {
        'question': "4^(x+2) = 2^(2x+1) + 14 হলে, x = কত? [RAKUB Senior Officer : 2018; বাংলাদেশ ব্যাংক সহকারী পরিচালক- ২০১৭]",
    },
    ('Math', 'লেকচার-১৩', 102): {
        'question': "a^m . a^n = a^(m+n) কখন হবে? [১৪তম বিসিএস/প্রাথমিক শিক্ষা অধিদপ্তরের হিসাব সহকারী-২০১৩]",
        'options': ["m ধনাত্মক হলে (m is positive)", "n ধনাত্মক হলে (n is positive)", "m ও n ধনাত্মক হলে (m and n are positive)", "m ধনাত্মক ও n ঋণাত্মক হলে (m is positive and n is negative)"],
        'answer': 'গ',
        'explanation': "সূচকের সূত্র a^m . a^n = a^(m+n) প্রযোজ্য হওয়ার জন্য m ও n ধনাত্মক মূলদ সংখ্যা হওয়া প্রয়োজন। সঠিক উত্তর 'm ও n ধনাত্মক হলে (m and n are positive)'।"
    },
    ('Math', 'লেকচার-১৩', 105): {
        'question': "5¹² + 5¹³ = ? [সোনালী ব্যাংক অফিসার: ২০১৪; Standard Bank Ltd. (TAO) : ২০১২]",
        'options': ["5²⁵", "10²⁵", "6(5¹²)", "10¹²⁺⁵"],
        'answer': 'গ',
        'explanation': "5¹² + 5¹³ = 5¹²(1 + 5) = 6(5¹²)। প্রাপ্ত সঠিক মান হলো '6(5¹²)'।"
    },
    ('Math', 'লেকচার-১৩', 106): {
        'question': "(x × x² × x³ × x⁴ × x⁵) ÷ x⁸ = ? [Sonali, Janata and Agrani Bank Senior Officer-08]",
        'options': ["x⁶", "x⁷", "x⁵", "x⁴"],
        'answer': 'খ',
        'explanation': "সূচকের নিয়ম অনুযায়ী লব = x^(1+2+3+4+5) = x^15। সুতরাং x^15 ÷ x^8 = x^(15-8) = x^7। প্রাপ্ত সঠিক মান হলো 'x⁷'।"
    },
    ('Math', 'লেকচার-১৩', 110): {
        'question': "(√32 . √8)³ = ? [One Bank Ltd. Senior Officer (IT) : 2015]",
        'options': ["2⁶", "2⁸", "2¹²", "2¹⁰"],
        'answer': 'গ',
        'explanation': "√32 . √8 = 4√2 × 2√2 = 16 = 2⁴। সুতরাং (2⁴)³ = 2¹²। প্রাপ্ত সঠিক মান হলো '2¹²'।"
    },
    # Math L15
    ('Math', 'লেকচার-১৫', 72): {
        'question': "কোনো সামান্তরিকের দুটি সন্নিহিত কোণের একটি ১২৫° হলে অপর কোণটি কত ডিগ্রী হবে?",
    },
    # Math L17
    ('Math', 'লেকচার-১৭', 68): {
        'question': "রম্বসের [বাংলাদেশ কর্মসংস্থান ব্যাংক, সহকারী অফিসার (সাধারণ/ক্যাশ)-'২৩] i. চারটি বাহু পরস্পর সমান ii. বিপরীত কোণগুলো পরস্পর সমান iii. কর্ণদ্বয় পরস্পরকে সমকোণে সমদ্বিখণ্ডিত করে নিম্নে কোনটি সঠিক?",
        'options': ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
        'explanation': "জ্যামিতিক উপপাদ্য অনুযায়ী রম্বসের চারটি বাহু সমান, বিপরীত কোণ সমান এবং কর্ণদ্বয় পরস্পরকে সমকোণে সমদ্বিখণ্ডিত করে। প্রাপ্ত সঠিক সমাধান হলো 'i, ii ও iii'।"
    },
    # Math L18
    ('Math', 'লেকচার-১৮', 93): {
        'question': "বৃত্তের দুটি ব্যাস পরস্পরকে সমদ্বিখণ্ডিত করলে ছেদবিন্দুর অবস্থান কোথায় হবে?",
    },
    ('Math', 'লেকচার-১৮', 104): {
        'question': "একটি বৃত্তে একই চাপের উপর অবস্থিত কেন্দ্রস্থ কোণ ১৪০° হলে, উক্ত চাপের উপর অবস্থিত বৃত্তস্থ কোণ কত? [১১তম শিক্ষক নিবন্ধন (স্কুল-২)-২০১৪]",
    },
    # Math L19
    ('Math', 'লেকচার-১৯', 57): {
        'question': "একটি বাড়ি ৪০ ফুট উঁচু। একটি মইয়ের তলদেশ মাটিতে বাড়ির দেওয়াল থেকে ৯ ফুট দূরে রাখা আছে। উপরে মইটি বাড়ির ছাদ ছুঁয়ে আছে। মইটি কত ফুট লম্বা? [১৮তম বিসিএস; প্রাক-প্রাথমিক সহকারী শিক্ষক (মুক্তিযোদ্ধা কোটা)'১৬]",
    },
    ('Math', 'লেকচার-১৯', 72): {
        'question': "এক নটিক্যাল মাইলে কত মিটার?",
        'opt_idx': 3,
        'val': '১৯৫৩.১৮ মি.'
    },
}

def clean_opt_notes(text):
    if not isinstance(text, str): return text
    # Strip '[ নোট: ...]' or '[নোট: ...]' or 'নোট: ...' or '[ি ব.দ্র: ...]'
    cleaned = re.sub(r'\s*\[\s*(?:ি\s*)?(?:নোট|বি\.দ্র)[\s\:\-][^\]]*\]', '', text)
    cleaned = re.sub(r'\s*নোট[\s\:\-].*$', '', cleaned)
    cleaned = re.sub(r'\s*✓\s*শর্টকাট.*$', '', cleaned)
    return cleaned.strip()

def run():
    files_modified = 0
    total_q_fixed = 0

    for folder in ['Bangla', 'English', 'GK', 'Math']:
        dirpath = os.path.join(base, folder)
        for f in sorted(os.listdir(dirpath)):
            if not f.endswith('.json'): continue
            p = os.path.join(dirpath, f)
            with open(p, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
            
            modified = False
            for q in data.get('questions', []):
                qid = q.get('id')

                # Check specific fixes
                for (target_folder, target_lec_prefix, target_qid), fix_dict in SPECIFIC_FIXES.items():
                    if folder == target_folder and target_lec_prefix in f and qid == target_qid:
                        if 'question' in fix_dict:
                            q['question'] = fix_dict['question']
                        if 'options' in fix_dict:
                            q['options'] = fix_dict['options']
                        if 'opt_idx' in fix_dict:
                            q['options'][fix_dict['opt_idx']] = fix_dict['val']
                        if 'answer' in fix_dict:
                            q['answer'] = fix_dict['answer']
                        if 'explanation' in fix_dict:
                            q['explanation'] = fix_dict['explanation']
                        modified = True
                        total_q_fixed += 1

                # Clean option 3 notes if any remain
                if len(q.get('options', [])) == 4:
                    orig_opt3 = q['options'][3]
                    cleaned_opt3 = clean_opt_notes(orig_opt3)
                    if cleaned_opt3 != orig_opt3 and len(cleaned_opt3) > 0:
                        q['options'][3] = cleaned_opt3
                        modified = True

                # Apply Global text replacements
                fields = ['question', 'explanation']
                for fld in fields:
                    if fld in q and isinstance(q[fld], str):
                        orig_val = q[fld]
                        new_val = orig_val
                        for src, tgt in GLOBAL_REPLACEMENTS:
                            if src in new_val:
                                new_val = new_val.replace(src, tgt)
                        if new_val != orig_val:
                            q[fld] = new_val
                            modified = True

                for i in range(len(q.get('options', []))):
                    orig_opt = q['options'][i]
                    if isinstance(orig_opt, str):
                        new_opt = orig_opt
                        for src, tgt in GLOBAL_REPLACEMENTS:
                            if src in new_opt:
                                new_opt = new_opt.replace(src, tgt)
                        if new_opt != orig_opt:
                            q['options'][i] = new_opt
                            modified = True

            if modified:
                with open(p, 'w', encoding='utf-8') as fp:
                    json.dump(data, fp, ensure_ascii=False, indent=2)
                files_modified += 1
                print(f"Updated: [{folder}] {f}")

    print(f"\nFinished! Files modified: {files_modified}, Specific Q fixed: {total_q_fixed}")

if __name__ == '__main__':
    run()
