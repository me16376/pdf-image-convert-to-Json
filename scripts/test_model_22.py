import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_25 = [
    {
        "id": 1,
        "question": "শুদ্ধ বানান কোনটি?",
        "options": ["অপরাহ্ন", "অপরাহ্ণ", "অপরাণ্য", "অপরান্য"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "‘উগ্র’ এর বিপরীত শব্দ?",
        "options": ["অনূগ্র", "সৌম্য", "ধীর", "স্থির"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "বাংলা উপসর্গ সংখ্যা কত?",
        "options": ["বিশটি", "একুশটি", "বাইশটি", "তেইশটি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "কোনটি কৃৎ প্রত্যয়ের উদাহরণ?",
        "options": ["ঢাকা + ই", "মিশ্ + উক", "চোর + আ", "সোনা + আলি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "‘ঋজু’ শব্দের বিপরীত-",
        "options": ["সোজা", "বাঁকা", "কঠিন", "তরল"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "‘দ্যুলোক’ শব্দের অর্থ-",
        "options": ["আকাশ", "বাতাস", "পৃথিবী", "পাতাল"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "কারক নির্ণয় করুন - লোভে পাপ পাপে মৃত্যু ।",
        "options": ["কর্মকারক", "সম্প্রদান কারক", "অপাদান কারক", "অধিকরণ কারক"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "সমাস নির্ণয় করুন- বেআইনি",
        "options": ["অব্যয়ীভাব", "নঞ তৎপুরুষ", "উপপদ তৎপুরুষ", "নিত্য সমাস"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "কোনটি প্রান্তিক বিরাম চিহ্ন-",
        "options": ["দাঁড়ি", "কমা", "কোলন", "ড্যাস"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "‘গাড়ী স্টেশন ছাড়লো’-কোন কারক?",
        "options": ["অধিকরণ কারক", "করণ কারক", "অপাদান কারক", "কর্মকারক"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "‘একাদশে বৃহস্পতি’ অর্থ-",
        "options": ["সুসময়", "দুঃসময়", "অলীক বস্তু", "শেষ রক্ষা"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "ব্যক্তিগত পত্রে কতটি অংশ থাকে?",
        "options": ["চার", "পাঁচ", "ছয়", "সাত"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "কাজী নজরুল ইসলাম সম্পাদিত পত্রিকা কোনটি?",
        "options": ["ধূমকেতু", "সবুজপত্র", "ভারতী", "সওগাত"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "বাংলা গদ্যের জনক কে?",
        "options": [
            "রবীন্দ্রনাথ ঠাকুর",
            "বঙ্কিমচন্দ্র চট্টোপাধ্যায়",
            "ঈশ্বরচন্দ্র বিদ্যাসাগর",
            "বিহারীলাল চক্রবর্তী"
        ],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "‘ঘরের শত্রু বিভীষণ’ বাগধারাটির অর্থ কী?",
        "options": [" বন্ধুত্বপূর্ণ", "শত্রু", "রাবণের ভাই", "যে গৃহ বিবাদ করে"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "‘টীকা ভাষ্য’ অর্থ-",
        "options": ["ব্যাখ্যা বিশ্লেষণ", "সারকথা", "উৎস খোঁজা", "নির্ঘন্ট"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "কণ্ঠ থেকে উৎস ধ্বনি-",
        "options": ["ক", "ঙ", "হ", "য়"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 18,
        "question": "ভারতবর্ষে মুসলিম শাসনামলে রাজভাষা ছিল-",
        "options": ["বাংলা", "সংস্কৃত", "আরবি", "ফারসি"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 19,
        "question": "ড. মুহাম্মদ শহীদুল্লাহর মতে বাংলা ভাষার উদ্ভব –",
        "options": [
            "সংস্কৃত থেকে",
            "গৌড়ীয় প্রাকৃত থেকে",
            "মাগধী প্রাকৃত থেকে",
            "মৈথিলি থেকে"
        ],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 20,
        "question": "কোনটি চলিত ভাষার বৈশিষ্ট্য?",
        "options": [
            "গাম্ভীর্য",
            "প্রমিত উচ্চারণ",
            "তৎসম শব্দের বহুল ব্যবহার",
            "ব্যাকরণ অনুসরণ করে চলে"
        ],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 21,
        "question": "‘হাতি’ শব্দের প্রতি শব্দ কোনটি?",
        "options": ["কুরঙ্গ", "ভুজঙ্গ", "করী", "কেশরী"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 22,
        "question": "কোন শব্দ যুগল সমার্থক নয়?",
        "options": [
            "অটবি, বিটপী",
            "হেম, সুবর্ণ",
            "তটিনী, ঝর্ণা",
            "ধরা, মেদিনী"
        ],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 23,
        "question": "শুদ্ধ শব্দ কোনটি?",
        "options": ["ব্যাকারণবিদ", "বৈয়াকরণ", "ব্যাকারণিক", "বৈয়াকরণিক"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 24,
        "question": "‘ইউনেস্কো ‘কত সালে ২১ শে ফেব্রুয়ারিকে আন্তর্জাতিক মাতৃভাষা দিবস হিসেবে স্বীকৃতি দেয়?",
        "options": ["১৯৯৮", "১৯৯৯", "২০০০", "২০০৫"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 25,
        "question": "কোনটি ‘সূর্য’ এর সমার্থক শব্দ নয়?",
        "options": ["তপন", "প্রভাকর", "অর্ক", "অর্ণব"],
        "answer": "ঘ",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-২২",
    "subject": "Bangla",
    "model_test": "Model Test-22",
    "total_questions": len(q1_25),
    "questions": q1_25
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-22.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_25)} questions.")
