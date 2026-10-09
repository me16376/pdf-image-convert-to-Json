import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_12 = [
    {
        "id": 1,
        "question": "কোনটি সঠিক বানান?",
        "options": ["নিশিথিনি", "নিশিথিনী", "নীশিথিনী", "নিশীথিনী"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "কোন বাক্যটি শুদ্ধ?",
        "options": ["আপনি সপরিবারে আমন্ত্রিত", "তার কথা শুনে আমি আশ্চর্যান্বিত হলাম", "তোমার পরশীকাতরতায় আমি মুগ্ধ হলাম", "সেদিন থেকে তিনি সেখানে আর যায় না"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "'যে নারী পূর্বে অপরের বাগদত্তা ছিল' তাকে এক কথায় কী বলে?",
        "options": ["অভিসারিণী", "অন্যপূর্বা", "অন্যপূর্্বা", "প্রোষিতভর্তৃকা"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "সমাসের রীতি কোন ভাষা থেকে আগত?",
        "options": ["উর্দু", "ফার্সি", "সংস্কৃত", "বাংলা"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "বাংলা সাহিত্যের চলিত ভাষার প্রবর্তক কে?",
        "options": ["রবীন্দ্রনাথ ঠাকুর", "ঈশ্বরচন্দ্র বিদ্যাসাগর", "প্রমথ চৌধুরী", "রামসুন্দর ত্রিবেদী"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "'চাচা কাহিনী' এর লেখক কে?",
        "options": ["দিলারা হাশেম", "আবু জাফর শামসুদ্দিন", "সরদার জয়েন উদ্দীন", "সৈয়দ মুজতবা আলী"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "বাংলা ভাষার প্রথম সাময়িক পত্র কোনটি?",
        "options": ["বঙ্গদর্শন", "দিগদর্শন", "সংবাদ প্রভাকর", "তত্ত্ববোধিনী"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "ধৃষ্ট' এর বিপরীত শব্দ কোনটি?",
        "options": ["মুক্ত", "নিরীহ", "দুষ্ট", "বিনয়ী"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "'ab initio' এর বাংলা পরিভাষা কী?",
        "options": ["অনুপস্থিত", "অবিহার", "প্রারম্ভেই", "মধ্যবর্তী"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "'তোমার মার বাড়ি.. তুমি যাও, আমি আমার বাড়িতে থাকি। আবার আমাকে দেখতে এসো'। উক্তিটি কোন গ্রন্থ থেকে নেওয়া হয়েছে?",
        "options": ["রক্তাক্ত প্রান্তর", "অসমাপ্ত আত্মজীবনী", "কারাগারের রোজনামচা", "দৌলত কাজী"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "চের কোন শব্দ: ণ-ত্ব বিধান অনুসারে 'ণ' এ ব্যবহার হয়েছে",
        "options": ["নিরূপণ", "লবণ", "কল্যাণ", "ব্যাকরণ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "'নিষ্কর' এর সন্ধি বিচ্ছেদ কোনটি?",
        "options": ["নিষ+ কর", "নিস্+কর", "নিঃ+ কর", "নীঃ+কার"],
        "answer": "গ",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৪৫",
    "subject": "Bangla",
    "model_test": "Model Test-45",
    "total_questions": len(q1_12),
    "questions": q1_12
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-45.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_12)} questions.")
