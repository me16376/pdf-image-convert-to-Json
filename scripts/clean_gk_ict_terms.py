import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA/GK'

GK_ICT_MAPPINGS = [
    # Full questions
    ('ডযরপয ড়হব ড়ভ:যব ভড়ষষড়রিহম রং হড়ঃ ধহ বীধসঢ়ষব ড়ভ ড়ঢ়বৎধঃরহম ংুংঃবস ভড়ৎ ঢ়বৎংড়হধষ পড়সঢ়ঁঃবৎং?',
     'Which one of the following is not an example of operating system for personal computers?'),
    ('ডযরপয ড়ভ:যব ভড়ষষড়রিহম রং হড়ঃ পড়সঢ়ঁঃবৎ যধৎফধিৎব?',
     'Which of the following is not computer hardware?'),
    ('ওহ গঝ চড়বিৎ চড়রহঃ, যিরপয ভঁহপঃরড়হ শবু রহ:যব শবুনড়ধৎফ রং ঁংবফ ধং ধ ংযড়ৎঃপঁঃ ভড়ৎ ংঃধৎঃরহম ংষরফবংযড়?ি',
     'In MS Power Point, which function key in the keyboard is used as a shortcut for starting slideshow?'),
    ('ঞযব নুঁরহম and ংবষষরহম ড়ভ মড়ড়ফং ড়াবৎ:যব রহঃবৎহবঃ রং শহড়হি ধং-',
     'The buying and selling of goods over the internet is known as-'),
    ('অ পড়সঢ়ঁঃবৎ পধহহড়ঃ ড়িৎশ রিঃযড়ঁঃ- / কম্পিউটার কাজ যা ছাড়া করতে পারে না-',
     'A computer cannot work without- / কম্পিউটার যা ছাড়া কাজ করতে পারে না-'),
    ('ডযরপয ড়হব ড়ভ:যব ভড়ষষড়রিহমং রং হড়ঃ ধ ভঁহপঃরড়হ ড়ভ ধহ ঙঢ়বৎধঃরহম ঝুংঃবসং (ঙঝ)?',
     'Which one of the followings is not a function of an Operating Systems (OS)?'),
    ('ডযরপয ড়ভ:যব ভড়ষষড়রিহম ফধঃধ ংঃৎঁপঃঁৎবং ভড়ষষড়ংি:যব খওঋঙ ঢ়ৎরহপরঢ়ষব?',
     'Which of the following data structures follows the LIFO principle?'),
    ("অ ঝঃধপশ রং ধষংড় পধষষবফু", "A Stack is also called-"),
    ("ওহ গঝ ড়িৎফ, যিরপয ড়ভ:যব ভড়ষষড়রিহম ংযড়ৎঃপঁঃ শবুং ধৎব ঁংবফ ভড়ৎ ধষরমহরহম:বীঃ:ড় পবহঃবৎ?",
     "In MS Word, which of the following shortcut keys are used for aligning text to center?"),
    ('গড়ঃযবৎনড়ধৎফ- এ চঈও ইটঝ কত ইরঃ- এ কাজ করে?', 'Motherboard-এ PCI BUS কত Bit-এ কাজ করে?'),
    ('ডরহফড়ংি ঘঞ- এর পূর্ণরূপ-', 'Windows NT- এর পূর্ণরূপ-'),
    ('চড়ংঃ- এর পূর্ণরূপ-', 'POST- এর পূর্ণরূপ-'),
    ('ঠওজটঝ এর পূর্ণরূপ-', 'VIRUS এর পূর্ণরূপ-'),
    ('ঠওজটঝ হচ্ছে-', 'VIRUS হচ্ছে-'),
    ('জঅগ রং ধ-', 'RAM is a-'),
    ('"IC" stands for-', '"IC" stands for-'),
    ('নিচের কোন সাইবার আক্রমণ সংঘটিত হলে গ্রাহক নিজ ঈড়সঢ়ঁঃবৎ ঝুংঃবস ব্যবহার করতে পারেন না এবং ঈড়সঢ়ঁঃবৎ ঝুংঃবস কে ব্যবহার উপযোগী করতে অর্থ দাবি করা হয়?',
     'নিচের কোন সাইবার আক্রমণ সংঘটিত হলে গ্রাহক নিজ Computer System ব্যবহার করতে পারেন না এবং Computer System কে ব্যবহার উপযোগী করতে অর্থ দাবি করা হয়?'),
    ("গঝ ঙভভরপব -এর কোন সফটওয়্যারটি ডাটাবেস নিয়ে কাজ করে ?", "MS Office -এর কোন সফটওয়্যারটি ডাটাবেস নিয়ে কাজ করে?"),
    ("গঝ ডড়ৎফ -এ ঃধনষব ড়ভ পড়হঃবহঃং তৈরি করার অপশন নিচের কোন ট্যাব এ পাওয়া যায়?", "MS Word -এ Table of contents তৈরি করার অপশন নিচের কোন ট্যাবে পাওয়া যায়?"),
    ("গঝ ডড়ৎফ এ কোন মেনুতে প্রিন্ট কমান্ড থাকে?", "MS Word-এ কোন মেনুতে প্রিন্ট কমান্ড থাকে?"),
    ("কোনটি 'অ্যাপিস্নকেশন সফটওয়্যার?", "কোনটি অ্যাপ্লিকেশন সফটওয়্যার?"),

    # Phrasing / options
    ('ঠরঃধষ ওহভড়ৎসধঃরড়হ জবংড়ঁৎপবং ঁহফবৎ ঝবরুব', 'Vital Information Resources under Seize'),
    ('ঠরঃধষ ওহভড়ৎসধঃরড়হ জবংড়ঁৎপবং ংবরুব', 'Vital Information Resources seize'),
    ('ঠরঃধষ ওহভড়ৎসধঃরড়হ জবযঁনরষধঃরড়হ ঝবৎারপব', 'Vital Information Rehabilitation Service'),
    ('ঝরসঢ়ষব গবংংধমব ঞৎধহংসরংংরড়হ চৎড়ঃড়পড়ষ', 'Simple Message Transmission Protocol'),
    ('ঝঃৎধঃবমরপ গধরষ ঞৎধহংভবৎ চৎড়ঃড়পড়ষ', 'Strategic Mail Transfer Protocol'),
    ('ঝঃৎধঃবমরপ গধরষ ঞৎধহংসরংংরড়হ চৎড়ঃড়পড়ষ', 'Strategic Mail Transmission Protocol'),
    ('ঝরসঢ়ষব গধরষ ঞৎধহংভবৎ চৎড়ঃড়পড়ষ', 'Simple Mail Transfer Protocol'),
    ('উবহরধষ ড়ভ ঝবৎারপব', 'Denial of Service'),
    ('গধহ-রহ-ঃযব-গরফফষব', 'Man-in-the-middle'),
    ('চৎড়ারফব ধ ঁংবৎ রহঃবৎভধপব', 'Provide a user interface'),
    ('গধহধমব যধৎফধিৎব ফবারপবং', 'Manage hardware devices'),
    ('ঈড়ঢ়ু ভরষবং ভৎড়স:যব হবঃড়িৎশ ধঁঃড়সধঃরপধষষু', 'Copy files from the network automatically'),
    ('ওহঃবৎহধঃরড়হধষ ঈড়সসঁহরঃু', 'International Community'),
    ('ওহঃবমৎধঃবফ ঈরৎপঁরঃ', 'Integrated Circuit'),
    ('ওহঃবৎহষ ঈরৎপঁরঃ', 'Internal Circuit'),
    ('ঝবপড়হফধৎু গবসড়ৎু', 'Secondary Memory'),
    ('চৎরসধৎু গবসড়ৎু', 'Primary Memory'),
    ('চৎড়পবংsinম টহরঃ', 'Processing Unit'),
    ('চৎড়পবংংরহম টহরঃ', 'Processing Unit'),
    ('চযরংযরহম', 'Phishing'),
    ('জধহংড়সধিৎব', 'Ransomware'),
    ('ঙঢ়বৎধঃরহম ঝুংঃবস', 'Operating System'),
    ('চড়বিৎ ড়হ ংবষভ:বংঃ', 'Power on self test'),
    ('চড়বিৎ ড়ভ ংবষভ:বংঃ', 'Power of self test'),
    ('চড়বিৎ ড়ভভ ংবষভ:বংঃ', 'Power off self test'),
    ('ডরহফড়ংি ঘবি ঞবপযহড়logু', 'Windows New Technology'),
    ('ডরহফড়ংি ঘবি ঋবপ', 'Windows New Fec'),
    ('এৎধঢ়যরপধষ ঁংবৎ ওহঃবৎভধপব', 'Graphical User Interface'),
    ('জবভৎবংয ৎধঃব', 'Refresh rate'),
    ('উড়ঃ ঢ়রঃপয', 'Dot pitch'),
    ('জবংড়ষঁঃরড়হ', 'Resolution'),
    ('ঞড়ঁপয ঝপৎববহ', 'Touch Screen'),
    ('ওসধমব ঝপধহহবৎ', 'Image Scanner'),
    ('চযুংরপধষ ংরিঃপযবং', 'Physical switches'),
    ('অ সধমহবঃ', 'A magnet'),
    ('খধংবৎং', 'Lasers'),
    ('ঐধৎফ উরংশ', 'Hard Disk'),
    ('ঋষড়ঢ়ঢ়ু উরংশ', 'Floppy Disk'),
    ('ঐধৎফ ফরংশ', 'Hard disk'),
    ('গড়ঁংব', 'Mouse'),
    ('কবুনড়ধৎফ', 'Keyboard'),
    ('গড়হরঃড়ৎ', 'Monitor'),
    ('চৎড়পবংংড়ৎ', 'Processor'),
    ('টঘ উবাবষড়ঢ়সবহঃ চৎড়মৎধসসব', 'UN Development Programme'),
    ('টঘ উবংঃৎড়ু চধংঃং', 'UN Destroy Pasts'),
    ('টঘ উবারষ চঁনষরপ', 'UN Devil Public'),
    ('টঘঙ', 'UNO'),
    ('টঘ', 'UN'),
    ('ঠরঃধসরহ ক', 'Vitamin K'),
    ('ঠরঃধসরহ অ', 'Vitamin A'),
    ('ঠরঃধসরহ ই', 'Vitamin B'),
    ('ঠরঃধসরহ ঈ', 'Vitamin C'),
    ('গঝ ডড়ৎফ', 'MS Word'),
    ('গঝ চড়বিৎ চড়রহঃ', 'MS PowerPoint'),
    ('গঝ চড়বিৎচড়রহঃ', 'MS PowerPoint'),
    ('গঝ অপপবংং', 'MS Access'),
    ('গঝ ঊীপবষ', 'MS Excel'),
    ('গঝ উঙঝ', 'MS DOS'),
    ('গঝ ঙভভরপব ঢচ', 'MS Office XP'),
    ('গঝ ঙভভরপব', 'MS Office'),
    ('গঝ উড়ং', 'MS DOS'),
    ('গঝ ঙঁঃষড়ড়শ', 'MS Outlook'),
    ('গঝ চড়রহঃ', 'MS Paint'),
    ('ডরহফড়ংি ঠরংঃধ', 'Windows Vista'),
    ('ডরহফড়ংি ঢচ', 'Windows XP'),
    ('ডরহফড়ংি ৯৮', 'Windows 98'),
    ('ডরহফড়ংি ৭', 'Windows 7'),
    ('ডরহফড়ংি', 'Windows'),
    ('জবফ যধঃ খরহীঁ', 'Red Hat Linux'),
    ('খওঘটঢ', 'LINUX'),
    ('খরহীঁ', 'Linux'),
    ('টহরী', 'Unix'),
    ('চড়বিৎ চড়রহঃ', 'PowerPoint'),
    ('ঋড়ী চৎড়', 'FoxPro'),
    ('ঙৎধপষব', 'Oracle'),
    ('ওহংবৎঃ', 'Insert'),
    ('জবভবৎবহপব', 'Reference'),
    ('জবারবি', 'Review'),
    ('ঠরবি', 'View'),
    ('ঋরষব', 'File'),
    ('ঋড়ৎসধঃ', 'Format'),
    ('ঊফরঃ', 'Edit'),
    ('১৬ ইরঃং', '১৬ Bits'),
    ('৮ ইরঃং', '৮ Bits'),
    ('৩২ ইরঃং', '৩২ Bits'),
    ('৬৪ ইরঃং', '৬৪ Bits'),
    ('১৬ ইরঃ', '১৬ Bit'),
    ('৮ ইরঃ', '৮ Bit'),
    ('৩২ ইরঃ', '৩২ Bit'),
    ('৬৪ ইরঃ', '৬৪ Bit'),
    ('চঈও ইটঝ', 'PCI BUS'),
    ('চঈও', 'PCI'),
    ('ইটঝ', 'BUS'),
    ('ইরঃ', 'Bit'),
    ('ঝঢ়ববফ', 'Speed'),
    ('ঙঈজ', 'OCR'),
    ('জঅগ', 'RAM'),
    ('জঙগ', 'ROM'),
    ('ইওঙঝ', 'BIOS'),
    ('ঊ-নুঁরহম', 'E-buying'),
    ('ঊ-পড়সসবৎপব', 'E-commerce'),
    ('ঊ-ংবষষরহম', 'E-selling'),
    ('ঊ-নঁsinবংং', 'E-business'),
    ('ঊ-নঁংরহবংং', 'E-business'),
    ('ওহঃবৎহবঃ', 'Internet'),
    ('ঝড়িৎফ', 'Sword'),
    ('উড়পঃড়ৎ', 'Doctor'),
    ('অষষ ( সবগুলো)', 'All (সবগুলো)'),
    ('অষষ', 'All'),
    ('ঋ২', 'F2'),
    ('ঋ৩', 'F3'),
    ('ঋ৫', 'F5'),
    ('ঈঃৎষ + গ', 'Ctrl + M'),
    ('ঈঃৎষ + ঈ', 'Ctrl + C'),
    ('ঈঃৎষ + ঊ', 'Ctrl + E'),
    ('ঈঃৎ + গ', 'Ctrl + M'),
    ('ঈঃৎ + ঈ', 'Ctrl + C'),
    ('ঈঃৎ + ঊ', 'Ctrl + E'),
    ('ঈঃৎষ', 'Ctrl'),
    ('অষষ ড়ভ:যবংব', 'All of these'),
    ('ঘড়হব ড়ভ:যবংব', 'None of these'),
    ('ঘড়হব ড়ভ:যবস', 'None of them'),
    ('ঘড়হব', 'None'),
    ('টঝঅওউ', 'USAID'),
    ('টঝঅ', 'USA'),
    ('অটকটঝ', 'AUKUS'),
    ('ঔটঝঞ', 'JUST'),
    ('ইৎধপশ Bank Ltd. চৎড়নধঃরড়হধৎু Officer', 'BRAC Bank Ltd. Probationary Officer'),
    ('ঝড়ঁঃযবধংঃ Bank Ltd.', 'Southeast Bank Ltd.'),
    ('ওহাবংঃসবহঃ ঈড়ঢ়বৎধঃরড়হ ড়ভ Bangladesh (ICই)', 'Investment Corporation of Bangladesh (ICB)'),
    ('চকঝঋ অংংরংtanঃ গধহধমবৎ', 'PKSF Assistant Manager'),
    ('অই Bank Ltd. গধহধমবসবহঃ ঞৎধরহবব', 'AB Bank Ltd. Management Trainee'),
    ('টঝ', 'US'),
    ('টক', 'UK'),
    ('ডযধঃ রং:যব नवহমধষর সবধহরহম ড়ভ- "time is up"', 'What is the Bengali meaning of "time is up"'),
    ('ডযধঃ রং:যব নবহমধষর সবধহরহম ড়ভ- "time is up"', 'What is the Bengali meaning of "time is up"'),
    ('ঞযব ড়িৎষফ্থং ষধৎমবংঃ রহঃবৎহধঃরড়হধষ ড়ৎমধহরুধঃরড়হ and ধ ংঁপপবংংড়ৎ:ড়:যব খবমঁব ড়ভ ঘধঃরড়হং রং-',
     "The world's largest international organization and a successor to the League of Nations is-"),
]

def clean_gk():
    modified_files = 0
    for root, dirs, files in sorted(os.walk('JSON Data/Biddabari-NTRCA')):
        for f in sorted(files):
            if not f.endswith('.json'): continue
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
            
            modified = False
            for q in data.get('questions', []):
                fields = ['question', 'explanation']
                for fld in fields:
                    if fld in q and isinstance(q[fld], str):
                        orig = q[fld]
                        new = orig
                        for src, tgt in GK_ICT_MAPPINGS:
                            if src in new:
                                new = new.replace(src, tgt)
                        if new != orig:
                            q[fld] = new
                            modified = True

                for i in range(len(q.get('options', []))):
                    orig_opt = q['options'][i]
                    if isinstance(orig_opt, str):
                        new_opt = orig_opt
                        for src, tgt in GK_ICT_MAPPINGS:
                            if src in new_opt:
                                new_opt = new_opt.replace(src, tgt)
                        if new_opt != orig_opt:
                            q['options'][i] = new_opt
                            modified = True

            if modified:
                with open(p, 'w', encoding='utf-8') as fp:
                    json.dump(data, fp, ensure_ascii=False, indent=2)
                modified_files += 1
                print(f"Cleaned ICT/Sutonny in: {f}")

    print(f"Total files updated: {modified_files}")

if __name__ == '__main__':
    clean_gk()
