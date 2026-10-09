import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_10 = [
    {
        "id": 1,
        "question": "'পরার্থ' শব্দের বিপরীত শব্দ কি?",
        "options": ["স্বার্থ", "অনুগ্রহ", "স্বার্থপর", "স্বার্থন্বেষী"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "ভাষার কোন রীতি নাটকে ও বক্তৃতায় অনুপযোগ?",
        "options": ["কথ্যভাষা", "উপভাষা", "সাধুভাষা", "চলিতভাষা"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "সব ভাষার ব্যাকারণের কয়টি মৌলিক অংশ থাকে?",
        "options": ["৫টি", "৬টি", "১০টি", "৪টি"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "নিষ্কর শব্দের সন্ধি বিচ্ছেদ কোনটি",
        "options": ["নীহ+কর", "নি:+কর", "নিষ+কর", "নিস+কর"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "নিচের কোন বানানটি শুদ্ধ?",
        "options": ["মরিচিকা", "মরীচিকা", "মৌরিচিকা", "মরীচীকা"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "মুক্ত শব্দের প্রকৃতি-প্রত্যয় কোনটি",
        "options": ["√মু+ক্ত", "√মুক+ত", "√মুহ+ক্ত", "√মুচ+ত"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "কোনটি উভইলিঙ্গ?",
        "options": ["শিশু", "বৃদ্ধ", "নাবালক", "পৌঢ়"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "তুমি মহারাজ সাধু হলে আজ ,আমি আজ চোর বটে,-কোন কবিতার অংশ?",
        "options": ["দুই বিঘা জমি", "পুরাতন ভৃত্য", "চিত্রা", "আবেদন"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "বুদ্ধিমান আর এর বিশেষণ পদ কোনটি?",
        "options": ["বৃদ্ধি", " বুদ্ধিত্ব", "বুদ্ধিমত্তা", "বোদ্ধা"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "'propaganda' এর বাংলা পরিভাষা কোনটি?",
        "options": ["ষড়যন্ত্র", "অপপ্রচার", "প্রসার", "গুজব"],
        "answer": "খ",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৩৪",
    "subject": "Bangla",
    "model_test": "Model Test-34",
    "total_questions": len(q1_10),
    "questions": q1_10
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-34.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_10)} questions.")
