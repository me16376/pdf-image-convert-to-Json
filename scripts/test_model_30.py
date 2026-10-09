import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_20 = [
    {
        "id": 1,
        "question": "‘দুই বিঘা জমি’ কবিতাটি কার লেখা?",
        "options": ["কাজী নজরুল ইসলাম", "রবীন্দ্রনাথ ঠাকুর", "মাইকেল মধুসূদন দত্ত", "কায়কোবাদ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "ছেলেটি দ্রুত দৌড়ায়। ‘দ্রুত’ কোন পদের উদাহরণ?",
        "options": ["বিশেষণ", "ক্রিয়া", "ক্রিয়া বিশেষণ", "বিশেষ্য"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "মন রূপ মাঝি= মনমাঝি কোন সমাসের উদাহরণ?",
        "options": ["বহুব্রীহি", "তৎপুরুষ", "রূপক কর্মধারয়", "দ্বন্দ্ব"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "শুদ্ধ বানান কোনটি?",
        "options": ["মুমূর্ষূ", "মুমূর্ষ", "মুমূর্ষু", "মৃমূর্ষু"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "সূর্য শব্দের সমার্থক শব্দ কোনটি?",
        "options": ["অর্ণব", "অর্ক", "প্রসুন", "পল্লব"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "বাংলা বর্ণমালায় মাত্রাহীন বর্ণ কয়টি?",
        "options": ["১০টি", "৭টি", "৮টি", "৬টি"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "স্বরবর্ণের সংক্ষিপ্ত রূপকে কী বলে?",
        "options": ["কার", "ফলা", "স্বরলিপি", "সম্প্রসারণ"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "যা ক্রিয়া সম্পাদন করে তাকে কী বলে?",
        "options": ["বিভক্তি", "উপসর্গ", "অনুসর্গ", "কারক"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "বাংলা উপসর্গ কয়টি?",
        "options": ["২০টি", "২১টি", "১৯টি", "১২টি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "সংখ্যা গণনার মূল একক-",
        "options": ["শূন্য", "এক", "ক্রম", "তারিখ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "চোখের বালি বাগধারাটির অর্থ কী?",
        "options": ["প্রিয় বস্তু", "বিরক্তিকর বস্তু", "আকর্ষণ", "চোখের রোগ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "উভয় সংকট বাগধারাটির অর্থ কী?",
        "options": ["দুই দিকে পথ", "আসন্ন সংকট", "দুইদিকে বিপদ", "ভুলপথে গমন"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "বাংলা লিপির উৎস কী?",
        "options": ["সংস্কৃত লিপি", "চীনা লিপি", "আরবি লিপি", "ব্রাহ্মী লিপি"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "বাংলাদেশের জাতীয় কবি কে?",
        "options": ["কাজী নজরুল ইসলাম", "জীবনানন্দ দাশ", "রবীন্দ্রনাথ ঠাকুর", "জসীমউদ্দীন"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "বাক্যে যতিচিহ্ন দাঁড়ি ( । ) থাকলে কতক্ষণ থামতে হয়?",
        "options": ["এক সেকেন্ড", "এক বলতে যে সময় প্রয়োজন", "এক বলার দ্বিগুণ", "থামার প্রয়োজন নেই"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "কোন পুরুষবাচক শব্দের দুইটি স্ত্রীবাচক শব্দ আছে?",
        "options": ["রাষ্ট্রপতি", "যোদ্ধা", "দেবর", "কেরানি"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "তারিখ কোন ভাষার শব্দ?",
        "options": ["আরবি", "ফারসি", "পর্তুগিজ", "তুর্কি"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 18,
        "question": "কবর কবিতাটি কে লিখেছেন?",
        "options": ["কায়কোবাদ", "জসীম উদ্দীন", "রবীন্দ্রনাথ ঠাকুর", "মাইকেল মধুসূদন দত্ত"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 19,
        "question": "রবীন্দ্র - এর সঠিক সন্ধি বিচ্ছেদ কোনটি?",
        "options": ["রবি + ইন্দ্র", "রবী+ ইন্দ্র", "রবি + ঈন্দ্র", "রবি+ ঈন্দ্র"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 20,
        "question": "ক্রিয়ার কাল প্রধানত কত প্রকার?",
        "options": ["৩", "২", "৪", "৬"],
        "answer": "ক",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৩০",
    "subject": "Bangla",
    "model_test": "Model Test-30",
    "total_questions": len(q1_20),
    "questions": q1_20
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-30.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_20)} questions.")
