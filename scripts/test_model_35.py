import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_20 = [
    {
        "id": 1,
        "question": "বাংলা ভাষার অভিধান প্রথম কে রচনা করেন?",
        "options": ["উইলিয়াম কেরি", "ড.মুহাম্মদ শহীদুল্লাহ", "সুনীতিকুমার চট্টোপাধ্যায়", "ফাদার মানোয়েল"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "'বচন ও লিঙ্গ' ব্যাকরণে আলোচিত হয়?",
        "options": ["ভাষাতত্ত্বে", "ধ্বনিতত্ত্বে", "রূপতত্ত্বে", "বাক্যতত্ত্বে"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "'Lexicography' -এর বাংলা পারিভাষিক শব্দ কি?",
        "options": ["ভাষাতত্ত্ব", "অভিধানতত্ত্ব", "ধ্বনিতত্ত্ব", "বাক্যতত্ত্ব"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "'ষড়ঋতু' শব্দের সন্ধিবিচ্ছেদ কি?",
        "options": ["ষড়+ঋতু", "ছয়+ঋতু", "ষট্+ঋতু", "ষড়্+ঋতু"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "'চক্ষুদান করা ' বাগধারার অর্থ কি?",
        "options": ["সেবা করা", "অপরাধ করা", "চুরি করা", "নষ্ট করা"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "'ভবিষ্যত না ভেবে কাজ করে যে' তাকে এক কথায় বলে---",
        "options": ["অবিসংবাদী", "নির্বাবনা", "অপরিণামদর্শী", "অবিমৃষ্যকারী"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "নিচের কোন বানানটি শুদ্ধ?",
        "options": ["অত্যধিক", "আদ্যাক্ষর", "আবিষ্কার", "অদ্যাপি"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "'পদ্মের' সমার্থক শব্দ কোনটি?",
        "options": ["মনসিজ", "অঞ্জন", "অরবিন্দ", "জলধর"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "কোনটি তৎসম শব্দ?",
        "options": ["বাজনা", "দোকানদার", "মানব", "ব্যাঙ্গাঠি"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "কোনটি লিঙ্গান্তর হয়না?",
        "options": ["বেয়াই", "সাহেব", "কবিরাজ", "রজক"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "'দর্শনমাত্র' কোন ধরনের সমাসের উদাহরণ?",
        "options": ["প্রাদি সমাস", "নিত্য সমাস", "দ্বিগু সমাস", "অব্যয়ীভাব সমাস"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "'Idiolect' শব্দের অর্থ কি?",
        "options": ["কথ্যভাষা", "ব্যক্তিভাষা", "প্রমিতভাষা", "উপভাষা"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "বিশ্বকবি তার কোন কবিতাটি উৎসর্গ করেছিলেন বিদ্রোহী কবিকে?",
        "options": ["বসন্ত", "ঘরে বাইরে", "সাজা", "ডাকঘর"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "'জিজ্ঞাসিব জনে জনে' কোন কারকে কোন বিভক্তি?",
        "options": ["অধিকরণে ৭মী", "কর্মে ৭মী", "করণে ৭মী", "অপাদানে ৭মী"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "'অবিরাম যাত্রার চির সংঘর্ষে, একদিন সে- পাহাড় টলবেই ' । কবিতাংশটি কার রচনা?",
        "options": ["সিকান্দার আবু জাফর", "সামসুর রাহমান", "সুভাষ মুখোপাধ্যায়", "ফররুখ আহমদ"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "'কোথায় থাকা হয়?'বাক্যটি কোন বাচ্যের উদাহরণ?",
        "options": ["কর্তৃবাচ্য", "কর্মবাচ্য", "ভাববাচ্য", "কর্তৃ-কর্মবাচ্য"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "'অভি' কোন ভাষার উপসর্গ?",
        "options": ["বাংলা", "তৎসম", "আরবি", "ফারসি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 18,
        "question": "'কমলাকান্তের দপ্তর' বঙ্কিমচন্দ্রের কোন ধরনের রচনা?",
        "options": ["প্রবন্ধ রচনা", "কাব্যগ্রন্থ", "রম্যরচনা", "ঐতিহাসিক উপন্যাস"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 19,
        "question": "'কুসুম' শব্দের সঙ্গে বহুবচনের কোন রূপটি মানানসই?",
        "options": ["নিচয়", "মালা", "দাম", "রাজি"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 20,
        "question": "'যত্ন করিলে রত্ন মিলিবে' এখানে 'করিলে' কোন ক্রিয়ার উদাহরন?",
        "options": ["অনুক্ত", "দ্বিকর্মক", "সমাপিকা", "অসমাপিকা"],
        "answer": "ঘ",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৩৫",
    "subject": "Bangla",
    "model_test": "Model Test-35",
    "total_questions": len(q1_20),
    "questions": q1_20
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-35.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_20)} questions.")
