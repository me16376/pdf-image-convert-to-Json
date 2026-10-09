import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'JSON Data/Biddabari-NTRCA'

BANGLA_SPECIFIC = {
    ('Bangla', 'লেকচার-০১. বাংলা ভাষার উদ্ভব ও ক্রমবিকাশ, বাংলা লিপি, ধ্বনি ও বর্ণ, অক্ষর, যুক্তবর্ণ.json', 7): "কুটিল",
    ('Bangla', 'লেকচার-০২. বাংলা ভাষার রীতি ও বিভাজন, ধ্বনি পরিবর্তন.json', 5): "লেখ্যরীতি",
    ('Bangla', 'লেকচার-০৩. ণ-ত্ব বিধান এবং ষ-ত্ব বিধান, শব্দের শ্রেণিবিভাগ.json', 4): "তদ্ভব",
    ('Bangla', 'লেকচার-০৯. বানান শুদ্ধিকরণ, বাক্য শুদ্ধিকরণ, বাক্য ও বাক্য পরিবর্তন, পারিভাষিক শব্দ, অনুবাদ, যতি বা ছেদচিহ্ন.json', 13): "দরিদ্র বাংলাদেশের প্রধান সমস্যা",
    ('Bangla', 'লেকচার-০৯. বানান শুদ্ধিকরণ, বাক্য শুদ্ধিকরণ, বাক্য ও বাক্য পরিবর্তন, পারিভাষিক শব্দ, অনুবাদ, যতি বা ছেদচিহ্ন.json', 16): "সাধু, চলিত",
    ('Bangla', 'লেকচার-০৯. বানান শুদ্ধিকরণ, বাক্য শুদ্ধিকরণ, বাক্য ও বাক্য পরিবর্তন, পারিভাষিক শব্দ, অনুবাদ, যতি বা ছেদচিহ্ন.json', 94): "সুকেশী",
    ('Bangla', 'লেকচার-১০. কারক ও বিভক্তি, বাক্য সংকোচন, বাগ্‌ধারা.json', 82): "কেতাদুরস্ত",
    ('Bangla', 'লেকচার-১১. সমাস, চিঠিপত্র.json', 8): "একশেষ দ্বন্দ্ব",
    ('Bangla', 'লেকচার-১১. সমাস, চিঠিপত্র.json', 20): "অব্যয়ীভাব",
    ('Bangla', 'লেকচার-১১. সমাস, চিঠিপত্র.json', 30): "কর্মধারয়",
    ('Bangla', 'লেকচার-১১. সমাস, চিঠিপত্র.json', 38): "উদ্বেল",
    ('Bangla', 'লেকচার-১২. বাংলা সাহিত্যের প্রাচীন যুগ ও মধ্যযুগ (চর্যাপদ, শ্রীকৃষ্ণকীর্তন, মঙ্গলকাব্য).json', 11): "জয়নুল আবেদীন এর শিল্পকর্ম",
    ('Bangla', 'লেকচার-১২. বাংলা সাহিত্যের প্রাচীন যুগ ও মধ্যযুগ (চর্যাপদ, শ্রীকৃষ্ণকীর্তন, মঙ্গলকাব্য).json', 15): "গোবিন্দদাস",
    ('Bangla', 'লেকচার-১২. বাংলা সাহিত্যের প্রাচীন যুগ ও মধ্যযুগ (চর্যাপদ, শ্রীকৃষ্ণকীর্তন, মঙ্গলকাব্য).json', 24): "জমিদার নিজাম শাহ",
    ('Bangla', 'লেকচার-১৩. বাংলা সাহিত্যের আধুনিক যুগ (ফোর্ট উইলিয়াম কলেজ থেকে আধুনিক সাহিত্যিকগণ).json', 6): "রাজীবলোচন মুখোপাধ্যায়",
    ('Bangla', 'লেকচার-১৩. বাংলা সাহিত্যের আধুনিক যুগ (ফোর্ট উইলিয়াম কলেজ থেকে আধুনিক সাহিত্যিকগণ).json', 10): "মাইকেল মধুসূদন দত্ত",
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 38): "১৯৮০"
}

cleaned_count = 0

for subj in sorted(os.listdir(base)):
    subj_dir = os.path.join(base, subj)
    if not os.path.isdir(subj_dir): continue

    for fname in sorted(os.listdir(subj_dir)):
        if not fname.endswith('.json'): continue
        p = os.path.join(subj_dir, fname)
        with open(p, 'r', encoding='utf-8') as fp:
            d = json.load(fp)

        file_changed = False
        for q in d.get('questions', []):
            qid = q.get('id')
            opts = q.get('options', [])

            # Check specific Bangla fixes
            key = (subj, fname, qid)
            if key in BANGLA_SPECIFIC:
                opts[3] = BANGLA_SPECIFIC[key]
                q['options'] = opts
                file_changed = True
                cleaned_count += 1
                continue

            new_opts = []
            for o in opts:
                cleaned_o = o
                # Strip NTRCA / Gh-N-J-I-O header leak
                if 'ঘঞজঈ' in cleaned_o or 'চাকুরি প্রত্যাশীদের জন্য' in cleaned_o:
                    cleaned_o = re.split(r'\s*ঘঞজঈ\s*অ\s*চাকুরি\s*প্রত্যাশীদের\s*জন্য.*', cleaned_o)[0].strip()
                    cleaned_o = re.split(r'\s*চাকুরি\s*প্রত্যাশীদের\s*জন্য.*', cleaned_o)[0].strip()
                new_opts.append(cleaned_o)

            if new_opts != opts:
                q['options'] = new_opts
                file_changed = True
                cleaned_count += 1

        if file_changed:
            with open(p, 'w', encoding='utf-8') as fp:
                json.dump(d, fp, ensure_ascii=False, indent=2)
            print(f"Cleaned headers in {fname}")

print(f"Total options cleaned: {cleaned_count}")
