import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_20 = [
    {
        "id": 1,
        "question": "বঙ্কিমচন্দ্র চট্টোপাধ্যায় রচিত প্রথম বাংলা উপন্যাস কোনটি?",
        "options": ["কপালকুণ্ডলা", "বিষবৃক্ষ", "দুর্গেশনন্দিনী", "মৃণালিনী"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "বাংলাদেশের জাতীয় সংগীতের রচয়িতা নাম কি?",
        "options": ["রবীন্দ্রনাথ ঠাকুর", "কাজী নজরুল ইসলাম", "শামসুর রহমান", "আল মাহমুদ"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "বাংলা সাহিত্যের আদি নিদর্শন কোনটি?",
        "options": ["বেদ", "শ্রীকৃষ্ণ কীর্তন", "রসুল বিজয়", "চর্যাপদ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "বাংলা সাহিত্যে বিদ্রোহী কবি কে?",
        "options": ["রবীন্দ্রনাথ ঠাকুর", "কাজী নজরুল ইসলাম", "শামসুর রহমান", "আল মাহমুদ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "\"নকশী কাঁথার মাঠ\" এর রচয়িতা কে?",
        "options": ["কাজী নজরুল ইসলাম", "শামসুর রহমান", "জসীমউদ্দিন", "ফররুখ আহমেদ"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "বাংলা লিপির উৎপত্তি কোন লিপি থেকে?",
        "options": ["খরোষ্ঠী লিপি", "ব্রাহ্মী লিপি", "অশোক লিপি", "প্রাকৃত লিপি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "এক কথায় প্রকাশ করুন : \"যা অবশ্যই ঘটবে\"-",
        "options": ["সম্ভাবনা ময়", "দুর্নিবার", "অবশ্যম্ভাবী", "সম্ভাব্য"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "এক কথায় প্রকাশ করুন : \"যার চক্ষু লজ্জা নেই\"-",
        "options": ["চশমখোর", "নির্লজ্জ", "চাক্ষুষ", "চোষ্য"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "এক কথায় প্রকাশ করুন : \"কোথাও উন্নত কোথাও অবনত\"-",
        "options": ["অনুন্নত", "বন্ধুর", "উন্নত-অবনত", "অবনত"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "বাগধারার অর্থ নির্ণয় করুন : \"বক ধার্মিক\"-",
        "options": ["অতি ধার্মীক", "উচ্ছৃঙ্খল", "প্রাচীন পন্থি", "ভন্ড"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "বাগধারার অর্থ নির্ণয় করুন : \"কানকাটা\"-",
        "options": ["ধার্মীক", "ভন্ড সাধু", "বেহায়া", "পক্ষপাত দুষ্ট"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "বাগধারার অর্থ নির্ণয় করুন : \"ইতর বিশেষ\"-",
        "options": ["আবোল তাবোল", "অর্থহীন কথা", "খারাপ ব্যক্তি", "ভেদাভেদ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "নিচের কোন বানানটি শুদ্ধ?",
        "options": ["গীতাঞ্জলী", "গীতাঞ্জলি", "গিতাঞ্জলি", "গিতাঞ্জলী"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "নিচের কোন বানানটি শুদ্ধ?",
        "options": ["সুশ্রূষা", "শুশ্রুশা", "শুশ্রূষা", "শুশ্রূষা"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "\"চাঁদ\"- এর সমার্থক শব্দ কোনটি?",
        "options": ["শশী", "পতঙ্গ", "অরুণ", "বহ্নি"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "\"আকাশ\"- এর সমার্থক শব্দ কোনটি ?",
        "options": ["পাথার", "গগন", "বারি", "খেচর"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "নিচের কোন পুরুষবাচক শব্দের স্ত্রীবাচক শব্দ নেই?",
        "options": ["চৌধুরী", "কবিরাজ", "নবীন", "কুলটা"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 18,
        "question": "\"উদ্ধত\" এর বিপরীত শব্দ কোনটি?",
        "options": ["অবনত", "বিনীত", "আনত", "নত"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 19,
        "question": "\"সে বলতে চায় তথাপি বলে না\"- এটি কোন শ্রেণীর বাক্য?",
        "options": ["সরল বাক্য", "জটিল বাক্য", "যৌগিক বাক্য", "ব্যাস বাক্য"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 20,
        "question": "নিচের কোনটি একটি স্বরবর্ণ?",
        "options": ["ক", "ঙ", "এ", "চ"],
        "answer": "গ",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৪৮",
    "subject": "Bangla",
    "model_test": "Model Test-48",
    "total_questions": len(q1_20),
    "questions": q1_20
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-48.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_20)} questions.")
