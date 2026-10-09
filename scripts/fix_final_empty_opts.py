import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

FIXES = {
    ('JSON Data/Biddabari-NTRCA/Bangla/লেকচার-০৯. বানান শুদ্ধিকরণ, বাক্য শুদ্ধিকরণ, বাক্য ও বাক্য পরিবর্তন, পারিভাষিক শব্দ, অনুবাদ, যতি বা ছেদচিহ্ন.json', 20): {
        'question': '"ছোট কিন্তু রসে ভরা" -বাক্যটিকে সরল বাক্যে রূপান্তরিত করলে কী হবে? [ঢাবি (খ- ইউনিট): ২০১৪-১৫]',
        'options': ["যদিও ছোট, তবু রসে ভরা", "রসে ভরা ছোট চিঠি", "ছোট ও রসে ভরা", "ছোট হলেও রসে ভরা"],
        'answer': "ঘ",
        'explanation': "যৌগিক বাক্যকে সরল বাক্যে রূপান্তরের সময় একটিমাত্র সমাপিকা ক্রিয়া বজায় রেখে রূপান্তর করা হয়। সুতরাং সঠিক উত্তর 'ছোট হলেও রসে ভরা'।"
    },
    ('JSON Data/Biddabari-NTRCA/Bangla/লেকচার-০৯. বানান শুদ্ধিকরণ, বাক্য শুদ্ধিকরণ, বাক্য ও বাক্য পরিবর্তন, পারিভাষিক শব্দ, অনুবাদ, যতি বা ছেদচিহ্ন.json', 21): {
        'question': "'লোকটি দরিদ্র হলেও সৎ' -বাক্যটির যৌগিক রূপ কী?",
        'options': ["লোকটি দরিদ্র এবং সৎ", "লোকটি দরিদ্র কিন্তু সৎ", "লোকটি যদিও দরিদ্র তবুও সৎ", "যদিও লোকটি দরিদ্র বটে তথাপি সৎ"],
        'answer': "খ",
        'explanation': "যৌগিক বাক্যে দুটি স্বাধীন খণ্ডবাক্য সংযোজক বা বিয়োজক অব্যয় (এবং, কিন্তু, বা) দ্বারা যুক্ত থাকে। সুতরাং সঠিক উত্তর 'লোকটি দরিদ্র কিন্তু সৎ'।"
    },
    ('JSON Data/Biddabari-NTRCA/English/লেকচার-১১. Word Formation, Degree.json', 11): {
        'question': "What is the adjective form of the word ‘People’? [প্রাথমিক সহকারী শিক্ষক নিয়োগ পরীক্ষা (৩য় পর্যায়)-২০২২]",
        'options': ["Popular", "Popularity", "Popularize", "Populous"],
        'answer': "ঘ",
        'explanation': "The noun 'People' has the adjective form 'Populous' (ঘনবসতিপূর্ণ)।"
    },
    ('JSON Data/Biddabari-NTRCA/English/লেকচার-১১. Word Formation, Degree.json', 12): {
        'question': "The adjective form of ‘decision’ is --- [প্রাথমিক সহকারী শিক্ষক নিয়োগ পরীক্ষা (৪র্থ পর্যায় : ৩)-২০১৯]",
        'options': ["decisive", "deceived", "decide", "decisiveness"],
        'answer': "ক",
        'explanation': "The noun 'decision' has the adjective form 'decisive' (চূড়ান্ত/সিদ্ধান্তমূলক)।"
    },
    ('JSON Data/Biddabari-NTRCA/English/লেকচার-১১. Word Formation, Degree.json', 33): {
        'question': "Choose the correct sentence.",
        'options': [
            "The house of our village is better than yours.",
            "The houses of our village are better than those of yours.",
            "The houses our village is good than yours.",
            "The house of our village are better than those of yours."
        ],
        'answer': "খ",
        'explanation': "তুলনার ক্ষেত্রে বহুবচনে 'those of' ব্যবহৃত হয়। সুতরাং সঠিক বাক্য 'The houses of our village are better than those of yours.'।"
    },
    ('JSON Data/Biddabari-NTRCA/English/লেকচার-১৬. Different Authors & Their Literary Works, Figure of Speech.json', 8): {
        'question': "Who is the central character of ‘Wuthering Heights’– [৪০তম বিসিএস]",
        'options': ["Mr. Earnshaw", "Catherine", "Heathcliff", "Hindley Earnshaw"],
        'answer': "গ",
        'explanation': "In Emily Bronte's novel 'Wuthering Heights', the central protagonist is Heathcliff."
    },
    ('JSON Data/Biddabari-NTRCA/English/লেকচার-১৬. Different Authors & Their Literary Works, Figure of Speech.json', 88): {
        'question': "Who is the author of ‘Jane Eyre’? [৪৩তম বিসিএস; বাংলাদেশ পল্লী বিদ্যুতায়ন বোর্ড (BREB)- এর সহকারী জেনারেল ম্যানেজার-২০২৪; বাংলাদেশ রেলওয়ের উপসহকারী প্রকৌশলী-২০২৪]",
        'options': ["Charlotte Bronte", "Emily Bronte", "Mary Shelley", "Jane Austen"],
        'answer': "ক",
        'explanation': 'The famous Victorian novel Jane Eyre was written by Charlotte Bronte.'
    },
    ('JSON Data/Biddabari-NTRCA/English/লেকচার-১৬. Different Authors & Their Literary Works, Figure of Speech.json', 109): {
        'question': "‘Vanity Fair’ is a novel written by- [৪১ তম বিসিএস]",
        'options': ["D. H. Lawrence", "William Makepeace Thackeray", "Virginia Woolf", "Joseph Conrad"],
        'answer': "খ",
        'explanation': "Vanity Fair is a renowned English satirical novel written by William Makepeace Thackeray."
    }
}

for (fpath, qid), fix in FIXES.items():
    with open(fpath, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for q in d['questions']:
        if q['id'] == qid:
            for k, v in fix.items():
                q[k] = v
            break
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Fixed {os.path.basename(fpath)} Q{qid}")

print("All remaining empty options fixed successfully!")
