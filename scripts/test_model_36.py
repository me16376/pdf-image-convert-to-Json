import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_24 = [
    {
        "id": 1,
        "question": "নামাজ, রোজা কোন ভাষার শব্দ?",
        "options": ["আরবি", "ফারসি", "উর্দু", "তুর্কি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "নিচের কোনটি একটি দেশী শব্দ?",
        "options": ["আনারস", "চন্দ্র", "কষ্ট", "কুলা"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "কেন্দ্রীয় শহীদ মিনারের স্থপতি কে?",
        "options": ["তানবীর কবীর", "হামিদুর রহমান", "হামিদুজ্জামান", "অস্কার বাদল"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "কোন নদীটি বঙ্গ জনপদের উত্তরাঞ্চলের সীমানা ছিল?",
        "options": ["পদ্মা", "মেঘনা", "যমুনা", "সুরমা"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "\"পদ্মরাগ\" উপন্যাসটির রচয়িতা কে?",
        "options": ["কাজী নজরুল ইসলাম", "দৌলত কাজী", "মীর মোশাররফ হোসেন", "বেগম রোকেয়া"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "\"একুশে ফেব্রুয়ারি\" প্রথম সংকলনের সম্পাদক কে?",
        "options": ["শওকত ওসমান", "জহির রায়হান", "দৌলত কাজী", "হাসান হাফিজুর রহমান"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "দক্ষিণ এশিয়ার দীর্ঘতম সেতু ঢোলা-সাদিয়া কোন দেশে অবস্থিত?",
        "options": ["বাংলাদেশ", "ভারত", "পাকিস্তান", "শ্রীলংকা"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "ক্যালকুলাস কে আবিষ্কার করেন?",
        "options": ["কোলার", "নিউটন", "গ্যালিলিও", "আর্কিমিডিস"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "\"টপ্পা\" কী?",
        "options": ["এক ধরনের গান", "নাচের মুদ্রা", "এক ধরনের বাদ্যযন্ত্র", "বিশেষ ধরনের খেলা"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "\"নিষ্ঠা\" শব্দের সঠিক সন্ধি বিচ্ছেদ কোনটি?",
        "options": ["নিস্ + ঠা", "নিঃ + ঠা", "নিঃ + ঠা", "কোনোটিই নয়"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "\"ঐচ্ছিক\" এর বিপরীতার্থক শব্দ কোনটি?",
        "options": ["আবশ্যক", "আবশ্যকীয়", "আবশ্যিক", "অত্যাবশ্যক"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "একটি দেশে উৎপাদন বাড়লে কি হবে?",
        "options": ["দারিদ্র্য বেড়ে যাবে", "বেকারত্ব বাড়বে", "মানুষের ক্রয়ক্ষমতা বাড়বে", "কর্মসংস্থানের সুযোগ বাড়বে"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "খাঁটি বাংলা উপসর্গ কয়টি?",
        "options": ["২০টি", "২১টি", "২২টি", "২৫টি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "কোনটি নিত্য স্ত্রীবাচক বাংলা শব্দ?",
        "options": ["সতীন", "বিধবা", "সপত্নী", "বিপত্নী"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "\"বিস্ময়\" এর সঠিক উচ্চারণ কোনটি",
        "options": ["বিস্শয়", "বিস্শয়", "বিশ্শায়", "বিশ্ময়"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "\"বন্ধুর\" শব্দের বিপরীত শব্দ কোনটি",
        "options": ["মিষ্টি", "মসৃণ", "অমসৃণ", "সমতল"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "\"শরতের শিশির\" বাগধারাটির অর্থ কী?",
        "options": ["সচেতন হওয়া", "কাশফুলের শিশির", "দুঃসময়ে বন্ধু", "ক্ষণস্থায়ী"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 18,
        "question": "কর্মে ক্লান্তি নেই এই বাক্যাংশের সংক্ষিপ্ত রূপ কী?",
        "options": ["ক্লান্তিহীন", "অক্লান্ত", "অক্লান্ত কর্মী", "অবিশ্রাম"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 19,
        "question": "বাংলা বর্ণমালায় মাত্রাবিহীন বর্ণের সংখ্যা কত?",
        "options": ["৮", "৯", "১০", "১১"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 20,
        "question": "সন্ধি এর সন্ধি বিচ্ছেদ কী?",
        "options": ["সম + ধি", "সম্ + ধি", "সম + ন্ধি", "সন + ধি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 21,
        "question": "শুদ্ধ বানান কোনটি?",
        "options": ["পিপীলিকা", "বুদ্ধিজীবি", "অগ্নাশয়", "অন্তঃস্বত্তা"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 22,
        "question": "\"ক্ষ্ম\" যুক্তাক্ষরটি কোন কোন অক্ষরের যুক্তরূপ?",
        "options": ["ক+খ", "খ+স+ম", "ক+খ+ম", "ক+ষ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 23,
        "question": "আমি শব্দটি কোন লিঙ্গ?",
        "options": ["পুংলিঙ্গ", "স্ত্রী লিঙ্গ", "ক্লীব লিঙ্গ", "উভয় লিঙ্গ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 24,
        "question": "নিচের কোনটি সর্বনাম?",
        "options": ["করিম", "কী", "বালক", "এবং"],
        "answer": "খ",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৩৬",
    "subject": "Bangla",
    "model_test": "Model Test-36",
    "total_questions": len(q1_24),
    "questions": q1_24
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-36.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_24)} questions.")
