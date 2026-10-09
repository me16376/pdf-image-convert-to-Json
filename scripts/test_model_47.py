import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_10 = [
    {
        "id": 1,
        "question": "'মেঘের আচ্ছন্ন হওয়ার ফলে স্নিগ্ধ' এর বাক্য সংকোচন কী?",
        "options": ["মেঘলা", "মেঘাচ্ছন্ন", "মেঘমেদুর", "মেঘস্নিগ্ধ"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "'বিরানব্বই' কোন সমাস?",
        "options": ["প্রাদি সমাস", "নিত্য সমাস", "অলুক তৎপুরুষ", "অব্যয়ীভাব"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "একেই কি বলে সভ্যতা' কোন ধরনের রচনা?",
        "options": ["প্রহসন", "উপন্যাস", "প্রবন্ধ", "নাটক"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "কোনটি সাধিত ধাতু?",
        "options": ["পড়", "কাটা", "রাখা", "পড়া"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "বাক্যে বিধেয় বিশেষণ কোথায় বসে?",
        "options": ["বিশেষণের পূর্বে", "বিশেষ্যের পূর্বে", "প্রথমে", "শেষে"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "ভাষার মূল উপকরণ কী?",
        "options": ["বাক্যাংশ", "শব্দ", "অর্থ", "বাক্য"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "বাংলা ভাষায় যৌগিক স্বরধ্বনি সংখ্যাটি কোনটি?",
        "options": ["২৪ টি", "২৫ টি", "২৭ টি", "২৩ টি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "বর্ণচোরা' কোন ধরনের সমাস?",
        "options": ["অলুক তৎপুরুষ", "নঞ তৎপুরুষ", "ষষ্ঠী তৎপুরুষ", "উপপদ তৎপুরুষ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "কোনটি নিত্য সম্বন্ধীয় অব্যয় ?",
        "options": ["যখন-তখন", "শন শন", "অথবা", "অধিকন্তু"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "'তুমি অধম, তাই বলিয়া আমি উত্তম হইব না কেন? কার উক্তি ?",
        "options": ["বঙ্কিমচন্দ্র চট্টোপাধ্যায়", "কাজী নজরুল ইসলাম", "রবীন্দ্রনাথ ঠাকুর", "ঈশ্বরচন্দ্র বিদ্যাসাগর"],
        "answer": "ক",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৪৭",
    "subject": "Bangla",
    "model_test": "Model Test-47",
    "total_questions": len(q1_10),
    "questions": q1_10
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-47.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_10)} questions.")
