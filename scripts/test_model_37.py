import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_20 = [
    {
        "id": 1,
        "question": "বাংলাদেশ ছাড়া কোন অঞ্চলের মানুষের ভাষা বাংলা?",
        "options": ["উড়িষ্যা", "তামিল", "নাগপুর", "মিজোরাম"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "তারিখ শব্দটি কোন ভাষা থেকে বাংলায় এসেছে?",
        "options": ["ফরাসি", "আরবি", "তুর্কি", "পর্তুগিজ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "রিক্সা কোন ভাষার শব্দ?",
        "options": ["গুজরাটি", "পাঞ্জাবি", "তুর্কি", "জাপানি"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "প্রচলিত বিদেশি শব্দের ভাবানুমূলক প্রতিশব্দকে কী বলে?",
        "options": ["অপিনিহিত", "পারিভাষিক শব্দ", "রূঢ়ি শব্দ", "তৎসম শব্দ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "বাংলা ভাষায় যৌগিক স্বরধ্বনির সংখ্যা কয়টি?",
        "options": ["১১টি", "২৫টি", "৪০টি", "৫০টি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "ব্রহ্মপুত্র শব্দের 'হ্ম' যুক্ত বর্ণটি কোন কোন বর্ণের সংযুক্ত রূপ?",
        "options": ["ম+হ", "হ্+ম", "ক্+ষ", "ষ্+ণ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "উপরিউক্ত সন্ধিবদ্ধ শব্দ কোনটি?",
        "options": ["উপরিউক্ত", "উপরোপরি", "উপর্‍যুক্ত", "উপরোক্ত"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "নিচের কোনটি রূপক কর্মধারয় সমাসের উদাহরণ?",
        "options": ["মনমরা", "মনহড়া", "মনমাঝি", "পরাণপ্রিয়া"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "আছো তুমি জগৎ মাঝারে। এখানে মাঝারে শব্দটি কোন অর্থে ব্যবহৃত?",
        "options": ["বাইরে", "ব্যাপ্তি", "মধ্যে", "সঙ্গে"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "বিশ্বজনের হিতকর এককথায় কী বলে?",
        "options": ["হিতকর", "বিশ্বজনহিত", "বিশ্বজননীন", "বিশ্বজনক"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "তামার বিষ বাগধারাটির অর্থ কী?",
        "options": ["ক্ষণস্থায়ী বস্তু", "অর্থের কুপ্রভাব", "তীব্রজ্বালা", "অসম্ভব বস্তু"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "একটি অপূর্ণ বাক্যের শেষে অন্য বাক্যের অবতারণা করতে কী চিহ্ন বসে?",
        "options": ["ড্যাস", "কোলন", "সেমিকোলন", "পূর্ণচ্ছেদ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "'অন্ধবধূ' কবিতায় কোন পাখির চেঁচিয়ে সারা হওয়ার কথা উল্লেখ আছে?",
        "options": ["কাক", "চোখ গেল", "কোকিল", "শালিক"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "'বন্যেরা বনে সুন্দর, শিশুরা মাতৃক্রোড়ে' এটি কী?",
        "options": ["প্রবাদ", "ডাকের বচন", "খনার বচন", "ছড়াংশ"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "কাজী নজরুল ইসলামের প্রথম কাব্যগ্রন্থের নাম কী?",
        "options": ["অগ্নিবীণা", "বিষের বাশি", "ছায়ানট", "চক্রবাক"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "প্রবাসের দিনগুলি' গ্রন্থের রচয়িতা কে?",
        "options": ["সৈয়দ মুজতবা আলী", "সুফিয়া কামাল", "জাহানারা ইমাম", "মলয় খান"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "'ভানু সিংহ কার ছদ্মনাম?",
        "options": ["রবীন্দ্রনাথ ঠাকুর", "প্রমথ চৌধুরী", "শরৎচন্দ্র", "গোলাম মোস্তফা"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 18,
        "question": "অন্নদামঙ্গল কাব্য কোন যুগের কাব্য?",
        "options": ["প্রাচীনযুগ", "মধ্যযুগ", "অন্ধকার যুগ", "আধুনিক যুগ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 19,
        "question": "অমিত্রাক্ষর ছন্দের প্রবর্তক -",
        "options": ["মাইকেল মধুসূদন", "বঙ্কিমচন্দ্র", "রবীন্দ্রনাথ", "বিহারীলাল"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 20,
        "question": "'যদ্যপি ' এর সন্ধিবিচ্ছেদ কী?",
        "options": ["যদ+পি", "যদি+অপি", "যদ+অপি", "যদ্য+অপি"],
        "answer": "খ",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৩৭",
    "subject": "Bangla",
    "model_test": "Model Test-37",
    "total_questions": len(q1_20),
    "questions": q1_20
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-37.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_20)} questions.")
