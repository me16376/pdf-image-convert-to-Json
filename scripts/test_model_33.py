import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_20 = [
    {
        "id": 1,
        "question": "জন্ম এর বিশেষণ রূপ কোনটি?",
        "options": ["জনম", "জাত", "সৃষ্টি", "জান্ম"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "'আয়না' আবুল মনসুর আহমেদ কোন ধরণের রচনা?",
        "options": ["প্রবন্ধ", "কাব্যগ্রন্থ", "রম্য রচনা", "নাটক"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "সময়ের অনেক গভীরে ডুব দিয়ে /আমি আমার স্বদেশ দেখছি ' কবিতা কার রচনা?",
        "options": ["শামসুর রাহমান", "সৈয়দ আলী আহসান", "সুভাষ মুখপদ্দই", "সিকান্দার আবু জাফর"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "Lexicography এর বাংলা পারিভাষিক শব্দ কি?",
        "options": ["ভাষাতত্ত্ব", "অভিধানতত্ত্ব", "ধ্বনিতত্ত্ব", "বাক্য তত্ত্ব"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "জন্ম এর বিশেষণ রূপ কোনটি?",
        "options": ["জনম", "জাত", "সৃষ্টি", "জান্ম"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "'আয়না' আবুল মনসুর আহমেদ কোন ধরণের রচনা?",
        "options": ["প্রবন্ধ", "কাব্যগ্রন্থ", "রম্য রচনা", "নাটক"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "সময়ের অনেক গভীরে ডুব দিয়ে /আমি আমার স্বদেশ দেখছি ' কবিতা কার রচনা?",
        "options": ["শামসুর রাহমান", "সৈয়দ আলী আহসান", "সুভাষ মুখপদ্দই", "সিকান্দার আবু জাফর"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "Phonology এর বাংলা পারিভাষিক শব্দ কি?",
        "options": ["ভাষাতত্ত্ব", "অভিধানতত্ত্ব", "ধ্বনিতত্ত্ব", "বাক্য তত্ত্ব"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "জন্ম এর বিশেষণ রূপ কোনটি?",
        "options": ["জনম", "জাত", "সৃষ্টি", "জান্ম"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "'আয়না' আবুল মনসুর আহমেদ কোন ধরণের রচনা?",
        "options": ["প্রবন্ধ", "কাব্যগ্রন্থ", "রম্য রচনা", "নাটক"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "সময়ের অনেক গভীরে ডুব দিয়ে /আমি আমার স্বদেশ দেখছি ' কবিতা কার রচনা?",
        "options": ["শামসুর রাহমান", "সৈয়দ আলী আহসান", "সুভাষ মুখপদ্দই", "সিকান্দার আবু জাফর"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "Lexicography এর বাংলা পারিভাষিক শব্দ কি?",
        "options": ["ভাষাতত্ত্ব", "অভিধানতত্ত্ব", "ধ্বনিতত্ত্ব", "বাক্য তত্ত্ব"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "জন্ম এর বিশেষণ রূপ কোনটি?",
        "options": ["জনম", "জাত", "সৃষ্টি", "জান্ম"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "'আয়না' আবুল মনসুর আহমেদ কোন ধরণের রচনা?",
        "options": ["প্রবন্ধ", "কাব্যগ্রন্থ", "রম্য রচনা", "নাটক"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "সময়ের অনেক গভীরে ডুব দিয়ে /আমি আমার স্বদেশ দেখছি ' কবিতা কার রচনা?",
        "options": ["শামসুর রাহমান", "সৈয়দ আলী আহসান", "সুভাষ মুখপদ্দই", "সিকান্দার আবু জাফর"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "Lexicography এর বাংলা পারিভাষিক শব্দ কি?",
        "options": ["ভাষাতত্ত্ব", "অভিধানতত্ত্ব", "ধ্বনিতত্ত্ব", "বাক্য তত্ত্ব"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "জন্ম এর বিশেষণ রূপ কোনটি?",
        "options": ["জনম", "জাত", "সৃষ্টি", "জান্ম"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 18,
        "question": "'আয়না' আবুল মনসুর আহমেদ কোন ধরণের রচনা?",
        "options": ["প্রবন্ধ", "কাব্যগ্রন্থ", "রম্য রচনা", "নাটক"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 19,
        "question": "সময়ের অনেক গভীরে ডুব দিয়ে /আমি আমার স্বদেশ দেখছি ' কবিতা কার রচনা?",
        "options": ["শামসুর রাহমান", "সৈয়দ আলী আহসান", "সুভাষ মুখপদ্দই", "সিকান্দার আবু জাফর"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 20,
        "question": "Lexicography এর বাংলা পারিভাষিক শব্দ কি?",
        "options": ["ভাষাতত্ত্ব", "অভিধানতত্ত্ব", "ধ্বনিতত্ত্ব", "বাক্য তত্ত্ব"],
        "answer": "খ",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৩৩",
    "subject": "Bangla",
    "model_test": "Model Test-33",
    "total_questions": len(q1_20),
    "questions": q1_20
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-33.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_20)} questions.")
