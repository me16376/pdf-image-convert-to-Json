import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_25 = [
    {
        "id": 1,
        "question": "বাংলা ভাষা কোন ভাষাস্তর থেকে এসেছে?",
        "options": ["সংস্কৃত", "গৌড়ীয় প্রাকৃত", "হিন্দি", "আসামি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "কোনটি মৌলিক স্বরধ্বনি?",
        "options": ["ঔ", "ঈ", "ঐ", "এ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "বাংলা ভাষারীতির কয়টি রূপ?",
        "options": ["দুইটি", "তিনটি", "পাঁচটি", "চারটি"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "‘ষষ্ঠ’ এর সন্ধি- বিচ্ছেদ কোনটি?",
        "options": ["ষট+ থ", "ষষ্ঠ+ থ", "ষষ্+ থ", "ষষ্+ ঠ"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "নিচের কোনটি যোগরূঢ় শব্দ?",
        "options": ["পঙ্কজ", "তৈল", "মধুর", "নবাবী"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "‘অদ্য’ শব্দটি কোন ভাষারীতির উদাহরণ?",
        "options": ["চলিত", "সাধু", "প্রাকৃত", "কোল"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "কোনটি ওষ্ঠ্য ধ্বনি?",
        "options": ["ম", "ঙ", "চ", "র"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "চন্দ্রের প্রতিশব্দ নয়?",
        "options": ["সোম", "হিমাংশু", "সবিতা", "দ্বিজরাজ"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "কোন বানানটি শুদ্ধ?",
        "options": ["মুমূর্ষ", "মুমূর্ষু", "মূমূর্ষু", "মূমূর্ষ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "কোনটি তৎপুরুষ সমাস?",
        "options": ["ভালোমন্দ", "মধুমখা", "যথাসাধ্য", "সত্যনিষ্ঠ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "‘পাখির নীড়ের মত চোখ তুলে নাটোরের বনলতা সেন’ -এখানে ‘নীড়’ শব্দটি কী অর্থে ব্যবহৃত হয়?",
        "options": ["নান্দনিক", "আশ্রয়", "রহস্যময়", "পাখির বাসা"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "শুদ্ধ বানান কোনটি?",
        "options": ["নিরপরাধী", "দারিদ্রতা", "স্বার্থকতা", "প্রাণিকুল"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "‘গোবর গণেশ’ বাগধারাটির অর্থ কী?",
        "options": ["অপদার্থ", "নিরেট মূর্খ", "অত্যন্ত অলস", "অপটু"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "কোন গুলো দন্ত ধ্বনি?",
        "options": ["ক খ গ ঘ", "প ফ ব ভ", "ত থ দ ধ", "চ ছ জ ঝ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "কোনটি দেশি শব্দ?",
        "options": ["রিকসা", "চা", "কিতাব", "কুলা"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "কোনটি ধ্বনি বিপর্যয়ের উদাহরণ?",
        "options": ["শরীর", "হংস > হাঁস", "লাফ > ফাল", "দুর্গা > দুগ্গা"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "পতাকা এর সমার্থক শব্দ কোনটি?",
        "options": ["কেতন", "নলিন", "মার্গ", "ভাজন"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 18,
        "question": "‘নয়ন’ শব্দটির সঠিক প্রত্যয় কোনটি?",
        "options": ["নী + অন", "নে + অন", "নৌ + অন", "নয় + ন"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 19,
        "question": "বাক্য বিস্ময়সূচক (!) চিহ্ন থাকলে, কতক্ষণ থামতে হয়?",
        "options": ["দুই সেকেন্ড", "এক সেকেন্ড", "তিন সেকেন্ড", "চার সেকেন্ড"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 20,
        "question": "অলীক এর বিপরীত শব্দ-",
        "options": ["বাস্তব", "কল্পনা", "উন্নতি", "আয়াত্ব"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 21,
        "question": "‘পড়ায় মন বসে না’-এখানে ‘পড়ায়’ কোন কারকে কোন বিভক্তি?",
        "options": [
            "কর্ম কারকে ৭মী বিভক্তি",
            "অধিকারে ৭মী বিভক্তি",
            "অপাদান কারকে ৭মী বিভক্তি",
            "করণ কারকে ৭মী বিভক্তি"
        ],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 22,
        "question": "কোনটি দ্বিগু সমাস?",
        "options": ["সপ্তাহ", "পরিভ্রমণ", "আমরণ", "মনগড়া"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 23,
        "question": "নদী এর সমার্থক শব্দ কোনটি?",
        "options": ["সরিৎ", "নগ", "গিরি", "বিহগ"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 24,
        "question": "‘নাদ’ শব্দের অর্থ কী?",
        "options": ["মেঘের ডাক", "বাঘের ডাক", "সিংহের নাম", "ময়ূরের ডাক"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 25,
        "question": "অনুবাদ কত প্রকার?",
        "options": ["২ প্রকার", "৩ প্রকার", "৪ প্রকার", "৫ প্রকার"],
        "answer": "ক",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-২৫",
    "subject": "Bangla",
    "model_test": "Model Test-25",
    "total_questions": len(q1_25),
    "questions": q1_25
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-25.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_25)} questions.")
