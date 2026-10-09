import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_20 = [
    {
        "id": 1,
        "question": "কোনটি অপিনিহিতির উদাহরণ?",
        "options": ["শুনিয়া", "রাইত", "চলো", "চলতি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "\"মনে মনে তুলনা করে দেখলাম\"- এখানে দ্বিরুক্তি ব্যবহৃত হয়েছে-",
        "options": ["বিশেষ্য", "ক্রিয়া-বিশেষণ রূপে", "ব্যাপ্তি অর্থে", "আধিক্য বোঝাতে"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "'শরতের শিশির'- বাগধারা শব্দটির অর্থ কী?",
        "options": ["সুসময়ের সঞ্চয়", "সুসময়", "শরতের শিউলি ফুল", "সুসময়ের বন্ধু"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "কোনটি যোগরূঢ় শব্দ?",
        "options": ["গৃহিণী", "পঙ্কজ", "সন্দেশ", "গৃহিণী"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "\"দেখে যেন মনে হয় চিনি উহারে\"- পঙ্ক্তির 'যেন' কোন পদ?",
        "options": ["ভাব বিশেষণ", "পদান্বয়ী অব্যয়", "সংযোজক অব্যয়", "অনন্বয়ী অব্যয়"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "'খনার বচন' - এর মূলভাব কি?",
        "options": ["শুদ্ধ জীবনযাপন রীতি", "সামাজিক মূল্যবোধ", "রাষ্ট্র পরিচালনা রীতি", "লৌকিক প্রণয় সঙ্গীত"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "'জয় বাংলা বাংলার জয়' গানটির গীতিকার কে?",
        "options": ["সিকান্দার আবু জাফর", "নজরুল ইসলাম বাবু", "গোবিন্দ হালদার", "গাজী মাজহারুল আনোয়ার"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "'এটা আমার সাধ্যাতীত' বাক্যটির সঠিক ইংরেজি অনুবাদ কোনটি?",
        "options": ["This is out of my power.", "This is beyond of my ability.", "This is beyond of my reach.", "This is out of my function."],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "'ডাক্তার ডাক' বাক্যটির ইংরেজি অনুবাদ হবে?",
        "options": ["Call a doctor", "Call for doctor", "Call in a doctor", "Call in doctor"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "কোন দুটি রচনা একই শ্রেণির?",
        "options": ["নীলদর্পণ ও বিষাদ-সিন্ধু", "লালসালু ও বলাকা", "গীতাঞ্জলি ও অগ্নিবীণা", "ডাকঘর ও শ্রীকান্ত"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "কোন বানানটি খাঁটি ষ-ত্ব বিধানের উদাহরণ?",
        "options": ["ষোড়শ", "ভূষণ", "স্পষ্ট", "বিশেষণ"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "স্বরভক্তির অপর নাম কি?",
        "options": ["অভিশ্রুতি", "অন্ত্যস্বরাগম", "অপিনিহিত", "বিপ্রকর্ষ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "'উদাসীন পথিকের মনের কথা' - কোন জাতীয় রচনা?",
        "options": ["নাটক", "কাব্য", "গীতি কবিতা", "উপন্যাস"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "'দারিদ্র্যতা' শব্দটি অশুদ্ধ কেন?",
        "options": ["প্রত্যয়জনিত কারণে", "উপসর্গজনিত কারণে", "কারকজনিত কারণে", "অনুসর্গজনিত কারণে"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "\"আমাদের দেশে হবে সেই ছেলে কবে, কথায় না বড় হয়ে কাজে বড় হবে\"- চরণ দু'টির রচয়িতা কে?",
        "options": ["সুকান্ত ভট্টাচার্য", "কামিনী রায়", "ঈশ্বরী পাটনী", "কুসুমকুমারী দাশ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "ব্যাধিকরণ বহুব্রীহি সমাস কোনটি?",
        "options": ["সুশ্রী", "নিরুপায়", "সহোদর", "কথাসর্বস্ব"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "'কপোল' শব্দটির অর্থ কী?",
        "options": ["গাল", "গলা", "ঠোঁট", "কপাল"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 18,
        "question": "ডেসমন্ড টুটু কত সালে, কি বিষয়ে নোবেল পুরস্কার লাভ করেছিলেন?",
        "options": ["১৯৮৪ সালে, শান্তিতে", "১৯৯৬ সালে, রসায়নে", "১৯৮৫ সালে, অর্থনীতিতে", "১৯৮৪ সালে, সাহিত্যে"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 19,
        "question": "ব্যঞ্জন বর্ণের সংক্ষিপ্ত রূপকে বলে-",
        "options": ["রেফ", "হসন্ত", "কার", "ফলা"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 20,
        "question": "\"হে বঙ্গ, ভাণ্ডারে তব বিবিধ রতন, পর-ধন-লোভে মত্ত, করিনু ভ্রমণ পরদেশে, ভিক্ষাবৃত্তি কুক্ষণে আচরি।\" এ কবিতাংশটির রচয়িতা কে?",
        "options": ["কাজী নজরুল ইসলাম", "জীবনানন্দ দাশ", "রবীন্দ্রনাথ ঠাকুর", "মাইকেল মধুসূদন দত্ত"],
        "answer": "ঘ",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৩৯",
    "subject": "Bangla",
    "model_test": "Model Test-39",
    "total_questions": len(q1_20),
    "questions": q1_20
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-39.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_20)} questions.")
