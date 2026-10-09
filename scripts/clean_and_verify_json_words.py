import os
import re
import json
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

try:
    from bijoy2unicode import converter
    b2u = converter.Unicode()
except ImportError:
    b2u = None

# 1. Exact string replacements (high-confidence whole-word / phrase corrections)
EXACT_REPLACEMENTS = {
    # SutonnyMJ Bijoy Acronyms
    'টঘওঈঊঋ': 'UNICEF',
    'টঘঐঈজ': 'UNHCR',
    'ডঞঙ': 'WTO',
    'ইওগঝঞঊঈ': 'BIMSTEC',
    'ইঅউঈ': 'BADC',
    'ইগউ': 'BMD',
    'উববঢ়ঝববশ': 'DeepSeek',
    'অইঈ': 'ABC',
    'অঘতটঝ': 'ADBS',
    'অঝওঝ': 'ASIS',

    # SutonnyMJ Bijoy Phrases
    'ডধংঃব হড়ঃ, ধিহঃ হড়ঃ': 'Waste not, want not',
    'অঢ়বহঃযবংরং': 'Epenthesis',
    'ঊঢ়বহঃযবংরং': 'Epenthesis',
    'ঝঃড়ঢ় এবহড়পরফব': 'Stop Genocide',
    'এৎধসসধৎ': 'Grammar',
    'গঁফ অৎপযরঃবপঃঁৎব': 'Mud Architecture',
    'গধৎরহব চৎড়ঃবপঃবফ অৎবধ': 'Marine Protected Area',
    'ঔধফফধঢ়র অসধৎ এঁৎঁ': 'Jaddapi Amar Guru',
    'ঞযব ভধসড়ঁং নড়ড়শ:রঃষবফ': 'The famous book titled',
    'ধিং ৎিরঃঃবহ নু': 'was written by',
    'ঞযব পড়সঢ়ঁঃবৎ পড়সসধহফ ড়ভ': 'The computer command of',
    'ংঃধহফং ভড়ৎ': 'stands for',
    'ঝঁষঃধহধ্থং': "Sultana's",
    'গরৎৎড়ৎ': 'Mirror',
    'ঞৎধহংষধঃরড়হ': 'Translation',
    'অ অনড়ৎরমরহধষ': 'Aboriginal',
    'অফলড়ঁৎহসবহঃ': 'Adjournment',
    'অহড়হুসড়ঁং': 'Anonymous',
    'অঃঃবংঃবফ': 'Attested',
    'অভভরফধারঃ': 'Affidavit',
    'ওঈ': 'IC',
    'ঈওঐ': 'CIH',
    'ঊ-ঈড়সসবৎপব': 'E-Commerce',
    'ঈঃৎষ + অষঃ + উবষবঃব': 'Ctrl + Alt + Delete',

    # Broken ণ্ড / ঙ্ক / ঙ্গ words
    'হত্যাকা': 'হত্যাকাণ্ড',
    'কর্মকা': 'কর্মকাণ্ড',
    'অগ্নিকা': 'অগ্নিকাণ্ড',
    'কারাদ': 'কারাদণ্ড',
    'হৃৎপি': 'হৃৎপিণ্ড',
    'ভূখ': 'ভূখণ্ড',
    'চ - ালী': 'চণ্ডালী',
    'চ-ালী': 'চণ্ডালী',
    'ভা - ার': 'ভাণ্ডার',
    'ভা-ার': 'ভাণ্ডার',
    'ঠা - া': 'ঠাণ্ডা',
    'ঠা-া': 'ঠাণ্ডা',
    'চ - ী': 'চণ্ডী',
    'চ-ী': 'চণ্ডী',
    'চ - ীদাস': 'চণ্ডীদাস',
    'চ-ীদাস': 'চণ্ডীদাস',
    'পু - ্র': 'পুণ্ড্র',
    'পু-্র': 'পুণ্ড্র',
    'দ - ায়মান': 'দণ্ডায়মান',
    'দ-ায়মান': 'দণ্ডায়মান',
    'দ - াদেশ': 'দণ্ডাদেশ',
    'দ-াদেশ': 'দণ্ডাদেশ',
    'দ - বিধির': 'দণ্ডবিধির',
    'দ-বিধির': 'দণ্ডবিধির',
    'কোমরব -': 'কোমরবন্ধ',
    'কোমরব-': 'কোমরবন্ধ',
    'অতিপি - ত': 'অতিপণ্ডিত',
    'অতিপি-ত': 'অতিপণ্ডিত',
    'মহাপি - ত': 'মহাপণ্ডিত',
    'মহাপি-ত': 'মহাপণ্ডিত',
    'পি - ত नेता': 'পণ্ডিত নেতা',
    'পি - ত নেতা': 'পণ্ডিত নেতা',
    'পি - ত': 'পণ্ডিত',
    'পি-ত': 'পণ্ডিত',
    'প - িত': 'পণ্ডিত',
    'প-িত': 'পণ্ডিত',
    'পি - তম্মন্য': 'পণ্ডিতম্মন্য',
    'পি-তম্মন্য': 'পণ্ডিতম্মন্য',
    'প-িতম্মন্য': 'পণ্ডিতম্মন্য',
    'প - িতম্মন্য': 'পণ্ডিতম্মন্য',
    'ট্রপোম - ল': 'ট্রপোমণ্ডল',
    'ট্রপোম-ল': 'ট্রপোমণ্ডল',
    'আয়নোম - ল': 'আয়নোমণ্ডল',
    'আয়নোম-ল': 'আয়নোমণ্ডল',
    'স্ট্রাটোম - ল': 'স্ট্রাটোমণ্ডল',
    'স্ট্রাটোম-ল': 'স্ট্রাটোমণ্ডল',
    'বায়ুম-ল': 'বায়ুমণ্ডল',
    'বায়ুম-লের': 'বায়ুমণ্ডলের',
    'ভূ-ম-ল': 'ভূমণ্ডল',
    'বারিম-ল': 'বারিমণ্ডল',

    # Ligature & Spelling Corrections
    'সাপস্নাই': 'সাপ্লাই',
    'চেকোশেস্নাভাকিয়া': 'চেকোস্লোভাকিয়া',
    'চেকোস্নোভাকিয়া': 'চেকোস্লোভাকিয়া',
    'যুগোস্নোভিয়া': 'যুগোস্লাভিয়া',
    'স্নোগান': 'স্লোগান',
    'স্নাইড': 'স্লাইড',
    'দৈর্ঘয': 'দৈর্ঘ্য',
    'বর্গেক্ষত্রের': 'বর্গক্ষেত্রের',
    'ন র্দান': 'নর্দান',
    'পরিক্ষার্থীর': 'পরীক্ষার্থীর',
    'সর্বেশষ': 'সর্বশেষ',
    'কপোের্রশন': 'কর্পোরেশন',
    'দপত্মর': 'দপ্তর',
    'দপত্মরের': 'দপ্তরের',
    'প্রস্তুুতে': 'প্রস্তুতিতে',

    # Trigonometry SutonnyMJ remnants
    'পড়ঃঅ': 'cotA',
    'ংরহঅ': 'sinA',
    'পড়ঃ': 'cot',
    'ংরহ': 'sin',
    'ঃধহ': 'tan',
    'পড়ং': 'cos',
    'ংবপ': 'sec',
    'পড়ংবপ': 'cosec',

    # Isolated header texts in options/questions
    'ঞবধপযবৎ্থং ডড়ৎশ': '',
    'ঞবধপযবৎ্থং': '',
    'ঝঃঁফবহঃং চৎধপঃরপব': '',
    'ঈষধংং ঞবংঃ': '',
}

# 2. Specific question fixes (for options that got merged with adjacent notes/tables)
SPECIFIC_Q_FIXES = {
    ('Bangla', 'লেকচার-০৯. বানান শুদ্ধিকরণ, বাক্য শুদ্ধিকরণ, বাক্য ও বাক্য পরিবর্তন, পারিভাষিক শব্দ, অনুবাদ, যতি বা ছেদচিহ্ন.json', 19): {
        'options': ["দোষ স্বীকার করলে তোমাকে শাস্তি দেওয়া হবে না।", "তিনি বেড়াতে এসে কেনাকাটা করলেন।", "মহৎ মানুষ বলে সবাই তাকে সম্মান করেন।", "ছেলেটি চঞ্চল তবে মেধাবী।"]
    },
    ('Bangla', 'লেকচার-০৯. বানান শুদ্ধিকরণ, বাক্য শুদ্ধিকরণ, বাক্য ও বাক্য পরিবর্তন, পারিভাষিক শব্দ, অনুবাদ, যতি বা ছেদচিহ্ন.json', 22): {
        'question': "'হৈমন্তী চুপ করিয়া রহিল'- বাক্যটির জটিল রূপ কী?",
        'options': ["সে হৈমন্তী চুপ করিয়া রহিল", "যে হৈমন্তী সে চুপ করিয়া রহিল", "হৈমন্তী বলিয়া সে চুপ করিয়া রহিল", "কিন্তু হৈমন্তী চুপ করিয়া রহিল"],
        'answer': 'খ',
        'explanation': "জটিল বাক্যে সাপেক্ষ সর্বনাম (যেমন: যে...সে) ব্যবহৃত হয়। সুতরাং 'হৈমন্তী চুপ করিয়া রহিল' বাক্যটির জটিল রূপ হলো 'যে হৈমন্তী সে চুপ করিয়া রহিল'।"
    },
    ('Bangla', 'লেকচার-০৯. বানান শুদ্ধিকরণ, বাক্য শুদ্ধিকরণ, বাক্য ও বাক্য পরিবর্তন, পারিভাষিক শব্দ, অনুবাদ, যতি বা ছেদচিহ্ন.json', 31): {
        'question': "Epenthesis এর অর্থ- [১৫তম শিক্ষক নিবন্ধন সহকারী শিক্ষক (স্কুল সমমান)-২০১৯]",
        'options': ["স্বরসঙ্গতি", "স্বরাগম", "অভিশ্রুতি", "অপিনিহিতি"]
    },
    ('Bangla', 'লেকচার-০৯. বানান শুদ্ধিকরণ, বাক্য শুদ্ধিকরণ, বাক্য ও বাক্য পরিবর্তন, পারিভাষিক শব্দ, অনুবাদ, যতি বা ছেদচিহ্ন.json', 39): {
        'question': "Waste not, want not এর সঠিক অনুবাদ কোনটি? [১২তম শিক্ষক নিবন্ধন সহকারী শিক্ষক (স্কুল/সমপর্যায়-২)-২০১৪]",
        'options': ["অপচয় করলে অভাবে পড়তে হয়", "অপচয় অভাবের মূল কারণ", "অপচয় করোনা অভাবও হবে না", "অভাব থেকে বাঁচার জন্য অপচয় রোধ জরুরি"]
    },
    ('Bangla', 'লেকচার-১১. সমাস, চিঠিপত্র.json', 4): {
        'options': ["সমস্ত পদ", "ব্যাসবাক্য", "উত্তর পদ", "সমস্যমান পদ"]
    },
    ('Bangla', 'লেকচার-১৩. বাংলা সাহিত্যের আধুনিক যুগ (ফোর্ট উইলিয়াম কলেজ থেকে আধুনিক সাহিত্যিকগণ).json', 13): {
        'options': ["বঙ্গদর্শন", "তত্ত্ববোধিনী", "ঢাকা প্রকাশ", "সংবাদ প্রভাকর"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 4): {
        'options': ["আমার জীবন", "আমার অতীত কথা", "আমার আত্মকথা", "আমার কথা"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 10): {
        'options': ["নবীন তপস্বিনী", "সধবার একাদশী", "লীলাবতী", "নীলদর্পণ"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 16): {
        'options': ["বীরবল", "ভানুসিংহ ঠাকুর", "পরশুরাম", "প্রমথনাথ বসু"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 29): {
        'options': ["বুদ্ধদেব বসু", "সুধীন্দ্রনাথ দত্ত", "অমিয় চক্রবর্তী", "অন্নদাশঙ্কর রায়"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 42): {
        'options': ["প্রেমের সমাধি", "এক রাতের মিলন", "অহমিকার পরিণতি", "বন্ধু বিচ্ছেদের করুণ কাহিনি"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 45): {
        'options': ["মুনীর চৌধুরী", "আখতারুজ্জামান ইলিয়াস", "আহমদ ছফা", "মুনতাসির মামুন"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 57): {
        'options': ["ইউসুফ জোলেখা - শাহ মুহম্মদ সগীর", "পদ্মাবতী - আলাওল", "মধুমালতী - সৈয়দ হামজা", "নূরনামা - আবদুল হাকিম"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 61): {
        'options': ["কাজী নজরুল ইসলাম", "গোলাম মোস্তফা", "বেনজীর আহমদ", "ফররুখ আহমদ"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 68): {
        'options': ["আলাউদ্দিন আল আজাদ", "শামসুর রাহমান", "রফিক আজাদ", "হাসান হাফিজুর রহমান"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 84): {
        'options': ["গীতিনাট্য", "উপন্যাস", "মহাকাব্য", "নাট্যকাব্য"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 87): {
        'options': ["দীনেশচন্দ্র সেন", "সুনীতিকুমার চট্টোপাধ্যায়", "মুহম্মদ শহীদুল্লাহ্", "মুহম্মদ এনামুল হক"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 90): {
        'options': ["আরেক ফাল্গুন", "একুশে ফেব্রুয়ারি", "স্মৃতিস্তম্ভ", "জীবন থেকে নেয়া"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 98): {
        'options': ["ঈশ্বরচন্দ্র গুপ্ত", "রবীন্দ্রনাথ ঠাকুর", "কাজী নজরুল ইসলাম", "আবুল হোসেন"]
    },
    ('Bangla', 'লেকচার-১৪. সাহিত্যিকদের পরিচিতি, বিখ্যাত গ্রন্থ, উপন্যাস, নাটক, মুক্তিযুদ্ধ ও ভাষা আন্দোলনভিত্তিক সাহিত্য.json', 104): {
        'options': ["আলতাফ মাহমুদ", "আব্দুল লতিফ", "মাহমুদুন্নবী", "আবদুল আলীম"]
    },
    ('English', 'লেকচার-১০. Narration.json', 5): {
        'options': [
            "Farida told that her mother that she would go to bed then.",
            "Farida told that her mother that she will go to bed then.",
            "Farida told that her mother that she will be going to bed then.",
            "Farida told her mother that she would go to bed then."
        ]
    },
    ('GK', 'লেকচার-০৭. বিশিষ্ট ব্যক্তিত্ব, গুরুত্বপূর্ণ স্থাপনা, ভাস্কর্য, কৃষ্টি ও সংস্কৃতি, শিক্ষা ব্যবস্থা.json', 38): {
        'options': ["আবুল কালাম মুহম্মদ আজাদ", "মুহাম্মদ এনামুল হক", "আবুল বাশার", "জাফর ওয়াজেদ"]
    },
    ('Math', 'লেকচার-১৬. ত্রিভুজ.json', 8): {
        'question': "একটি সমদ্বিবাহু সমকোণী ত্রিভুজের অতিভুজের দৈর্ঘ্য ১২ সে.মি. হলে ত্রিভুজটির ক্ষেত্রফল কত? [২৭তম বিসিএস]",
        'options': ["৩৬", "৪৮", "৫৬", "৭২"],
        'answer': 'ক',
        'explanation': "সমকোণী সমদ্বিবাহু ত্রিভুজের অতিভুজ h = ১২ সে.মি. হলে সমান বাহু a-এর জন্য a² + a² = ১২² ⇒ ২a² = ১৪৪ ⇒ a² = ৭২। ক্ষেত্রফল = ½ × a² = ½ × ৭২ = ৩৬ বর্গ সে.মি.।"
    }
}

def clean_text(text):
    if not isinstance(text, str) or not text:
        return text

    # Strip leaked watermark/explanation from option text
    text = re.split(r'\s*বিদ্যাবাড়ি\s*(?:✓|\u2713)?\s*ব্যাখ্যা\s*[:\.]?', text)[0].strip()
    text = re.split(r'\s*\[\s*ব্যাখ্যা\s*[:\.]?', text)[0].strip()

    # Exact string substitutions
    for k, v in EXACT_REPLACEMENTS.items():
        if k in text:
            text = text.replace(k, v)

    # General स्त্ম -> स्त
    text = re.sub(r'স্ত্ম', 'স্ত', text)

    # Degree symbol: (\d+)\s*ক্ক -> \1°
    text = re.sub(r'(\d+)\s*ক্ক', r'\1°', text)

    # Math multiplication symbol: (\d+)\s*দ্ধ\s*(\d+) -> \1 × \2
    text = re.sub(r'(\d+)\s*দ্ধ\s*(\d+)', r'\1 × \2', text)

    # Bijoy quotes ্তু...্থ -> "..."
    def decode_bijoy_quote(m):
        inner = m.group(1).strip()
        # If inner can be inverted back to english using b2u
        if b2u:
            try:
                en = b2u.convertUnicodeToBijoy(inner).strip()
                # If decoded english looks like genuine english words
                if re.match(r'^[a-zA-Z0-9\s\+\-\:\,\.\'\"]+$', en) and len(en) >= 2:
                    return f'"{en}"'
            except Exception:
                pass
        return f'"{inner}"'

    text = re.sub(r'্তু([^্থ]+)্থ', decode_bijoy_quote, text)

    # Isolated kar signs: consonant + space(s) + kar -> attach kar
    text = re.sub(r'([\u0985-\u09B9\u09DC-\u09DF])\s+([\u09BE-\u09CC])', r'\1\2', text)

    # Clean double spaces
    text = re.sub(r'[ \t]+', ' ', text).strip()

    return text

def process_file(subj, fname, fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    changed = False
    questions = data.get('questions', [])

    for q in questions:
        qid = q.get('id')
        specific_key = (subj, fname, qid)

        # Apply specific question fix if available
        if specific_key in SPECIFIC_Q_FIXES:
            fix = SPECIFIC_Q_FIXES[specific_key]
            for k, v in fix.items():
                q[k] = v
            changed = True

        # Clean question text
        old_q = q.get('question', '')
        new_q = clean_text(old_q)
        if new_q != old_q:
            q['question'] = new_q
            changed = True

        # Clean options
        opts = q.get('options', [])
        new_opts = []
        for opt in opts:
            cleaned_opt = clean_text(opt)
            new_opts.append(cleaned_opt)
        if new_opts != opts:
            q['options'] = new_opts
            changed = True

        # Clean explanation
        old_exp = q.get('explanation', '')
        new_exp = clean_text(old_exp)
        if new_exp != old_exp:
            q['explanation'] = new_exp
            changed = True

    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return len(questions)
    return 0

def main():
    base_dir = 'JSON Data/Biddabari-NTRCA'
    total_modified = 0
    total_q_modified = 0

    for subj in sorted(os.listdir(base_dir)):
        subj_dir = os.path.join(base_dir, subj)
        if not os.path.isdir(subj_dir): continue

        print(f"\n=================== Processing Subject: {subj} ===================")
        for fname in sorted(os.listdir(subj_dir)):
            if not fname.endswith('.json'): continue
            fpath = os.path.join(subj_dir, fname)
            q_cnt = process_file(subj, fname, fpath)
            if q_cnt > 0:
                print(f"  [UPDATED] {fname} ({q_cnt} questions processed)")
                total_modified += 1
                total_q_modified += q_cnt
            else:
                print(f"  [OK] {fname}")

    print(f"\nCompleted! Total files updated: {total_modified}, Total questions checked: {total_q_modified}")

if __name__ == '__main__':
    main()
