import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_17 = [
    {
        "id": 1,
        "question": "‘বিমুগ্ধ’ শব্দটি ব্যাকরণের কোন নিয়মে গঠিত হয়েছে?",
        "options": ["উপসর্গযোগে", "সন্ধিযোগে", "প্রত্যয়যোগে", "সমাসযোগে"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "কোন বানানটি শুদ্ধ?",
        "options": ["মনঃকষ্ট", "মনকষ্ট", "মনকষ্ট", "মনোকষ্ট"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "বঙ্গবন্ধুর 'অসমাপ্ত আত্মজীবনী' কবে প্রথম প্রকাশিত হয়?",
        "options": ["জুন, ২০১১", "জুলাই, ২০১১", "জুন, ২০১২", "জানুয়ারি, ২০১৩"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "১৯৭১ সালে মুজিবনগর সরকার কর্তৃক প্রকাশিত পত্রিকার নাম ছিল-",
        "options": ["মুক্তির ডাক", "জয় বাংলা", "মুক্তবার্তা", "স্বাধীনতা"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "'বাংলাদেশ স্বপ্ন দ্যাখে' কাব্যগ্রন্থের রচয়িতা কে?",
        "options": ["আল মাহমুদ", "নির্মলেন্দু গুণ", "শামসুর রাহমান", "হুমায়ূন আহমেদ"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "'ইকা' - প্রত্যয় কোন শব্দে ক্ষুদ্রার্থে ব্যবহৃত হয়েছে?",
        "options": ["নায়িকা", "সেবিকা", "মালিকা", "শ্যালিকা"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "'স্বর্গ' - এর সমার্থক শব্দ কোনটি?",
        "options": ["ভূঙ্গ", "ত্রিদিব", "সবিতা", "উদধি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "'পাতিসনে শিলাতলে পদ্মপাতা' কি অর্থে অনুজ্ঞার ব্যবহার হয়েছে?",
        "options": ["আদেশ", "প্রার্থনা", "অনুরোধ", "উপদেশ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "জসীমউদ্দীন রচিত 'নিমন্ত্রণ' কবিতাটি কোন গ্রন্থের অন্তর্ভুক্ত?",
        "options": ["মাটির কান্না", "ধানক্ষেত", "বালুচর", "রাখালী"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "কোনটি তৎপুরুষ সমাসের উদাহরণ?",
        "options": ["বাগদত্তা ( বাক্ দ্বারা দত্তা )", "জীবনবীমা ( জীবন রক্ষার বীমা )", "গমনাগমন ( গমন ও আগমন )", "নদীমাতৃক ( নদী মাতা যার )"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "কোনটি সঠিক?",
        "options": ["কুসুমপুঞ্জ", "বৃক্ষপুঞ্জ", "মেঘপুঞ্জ", "তরঙ্গপুঞ্জ"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "যৌগিক ক্রিয়ার উদাহরণ কোনটি?",
        "options": ["আজগরটি ফোঁসাচ্ছে", "তরকারি বাসি হলে টক", "সাইরেন বেজে উঠল", "মাথা ঝিম ঝিম করছে"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "'সবুজ' কোন ভাষার থেকে আগত শব্দ?",
        "options": ["ফারসি", "দেশি", "সংস্কৃত", "পর্তুগিজ"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "কোনটি সরল বাক্য?",
        "options": ["সত্য কথা বলিনি, তাই বিপদে পড়েছি।", "মেঘ গর্জন করলে, ময়ূর নৃত্য করে।", "বিপদ এবং দুঃখ এক সময়ে আসে।", "যতই করিবে দান, তত যাবে বেড়ে।"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "'গ্রন্থগার' শব্দটি -",
        "options": ["নিপাতনে সিদ্ধ সন্ধি", "স্বরসন্ধি", "ব্যঞ্জন সন্ধি", "বিসর্গ সন্ধি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "বিভক্তিযুক্ত শব্দ ও ধাতুকে বলে-",
        "options": ["কারক", "পদ", "ক্রিয়াপদ", "শব্দ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "কোন শব্দটি দ্বন্দ্ব সমাস?",
        "options": ["দম্পতি", "সিংহাসন", "রাজপথ", "প্রভাত"],
        "answer": "ক",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৪১",
    "subject": "Bangla",
    "model_test": "Model Test-41",
    "total_questions": len(q1_17),
    "questions": q1_17
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-41.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_17)} questions.")
