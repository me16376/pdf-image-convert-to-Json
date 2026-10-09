import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_11 = [
    {
        "id": 1,
        "question": "'মর্সিয়া ' শব্দের অর্থ কী?",
        "options": ["সাগর", "গান", "শোক", "সাহিত্য"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "কবি সুফিয়া কামালের জন্ম কোন জেলায়?",
        "options": ["কুমিল্লা", "যশোহর", "কোলকাতা", "বরিশাল"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "কোন বাক্যাংশটির গুরুচন্ডালী দোষমুক্ত?",
        "options": ["ঘটকের গাড়ি", "মড়াপোড়া", "ঘোড়ার গাড়ি", "শবদাহ"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "'যে নারী প্রিয় বলে' এক কথায় প্রকাশ করুন-",
        "options": ["প্রিয়া", "প্রিয়ংবদা", "শ্রীমতি", "সুহাসিনী"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "ছড়া কোন ছন্দে রচিত হয়?",
        "options": ["স্বরবৃত্ত", "পয়ার", "অমিত্রাক্ষর", "ত্রিপদী"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "'হাঁড়ি হাঁড়ি সন্দেশ' এখানে কোন পদযোগে বহুবচন হয়েছে?",
        "options": ["বিশেষ্য ও বিশেষণ", "বিশেষণ ও ক্রিয়া", "বিশেষ্য ও বিশেষ্য", "বিশেষণ ও বিশেষণ"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "'নদী ও নারী ' উপন্যাসের রচয়িতা কে?",
        "options": ["মীর মশাররফ হোসেন", "রবীন্দ্রনাথ ঠাকুর", "সৈয়দ আবুল ফজল", "হুমায়ুন কবির"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "'ছোটটি কোথায়?' বাক্যে ছোট শব্দের শেষে 'টি এর ব্যাকরণিক পরিচয় কী?",
        "options": ["পদাশ্রিত নির্দেশক", "অনুসর্গ", "বিভক্তি", "শব্দ প্রত্যয়"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "হাইফেন (-) এর পর কতক্ষণ থামতে হয়?",
        "options": ["১ সেকেন্ড", "২ সেকেন্ড", "১.৫ সেকেন্ড", "থামার প্রয়োজন নেই।"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "'শোনো একটি মুজিবরের কণ্ঠস্বরের ধ্বনি' - গানটি রচয়িতা কে?",
        "options": ["শাহেদ মাহমুদ", "মুকুন্দ দাস", "গৌরীপ্রসন্ন মজুমদার", "গোবিন্দ হালদার"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "'মুজিব -লেনিন -ইন্দিরা' কাব্যগ্রন্থের লেখক কে?",
        "options": ["নির্মলেন্দু গুণ", "আসাদ চৌধুরী", "শওকত আলী", "মহাদেব সাহা"],
        "answer": "ক",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৪৩",
    "subject": "Bangla",
    "model_test": "Model Test-43",
    "total_questions": len(q1_11),
    "questions": q1_11
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-43.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_11)} questions.")
