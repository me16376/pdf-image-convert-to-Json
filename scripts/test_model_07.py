import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_25 = [
    {
        "id": 1,
        "question": "চলিতরীতির শব্দ নয় কোনটি?",
        "options": ["করিবার", "করার", "করিবার", "করে"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "'ভূষণ্ডির কাক' বাগধারাটির সঠিক অর্থ কোনটি?",
        "options": ["একই স্বভাবের", "মূর্খ", "কপট ব্যক্তি", "দীর্ঘজীবী"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "কোন বানানটি সঠিক?",
        "options": ["সমীচীন", "সসিচিন", "সমীচিন", "সমিচীন"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "বাড়ি বা রাস্তার নম্বরের পরে কোন চিহ্ন বসে?",
        "options": ["হাইফেন", "কমা", "দাঁড়ি", "লোপ চিহ্ন"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "ভাষার কোন রীতি তদ্ভব শব্দ বহুল?",
        "options": ["সাধুরীতি", "চলিতরীতি", "কথ্যরীতি", "বানানরীতি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "'For good' এর সঠিক অর্থ কোনটি?",
        "options": ["ভালো হওয়া", "গড়িমসি", "ক্ষণতরে", "চিরতরে"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "অনুবাদ কোনটির সহায়ক?",
        "options": ["ভাষার উন্নতি", "জ্ঞান চর্চার", "ভাষার শৃঙ্খলার", "কাব্য রচনার"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "Waste not, want not এর সঠিক অনুবাদ কোনটি?",
        "options": [
            "অপচয় করলে অভাবে পড়তে হয়",
            "অপচয় অভাবের মূল কারণ",
            "অপচয় করোনা অভাবও হবে না",
            "অভাব থেকে বাঁচার জন্য অপচয় রোধ জরুরি"
        ],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "'লবণ' শব্দের সঠিক সন্ধি-বিচ্ছেদ কোনটি?",
        "options": ["লো + অন", "লো + বন", "ল + বন", "লৌ + বন"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "নিপাতনে সিদ্ধ সন্ধির উদাহরণ কোনটি?",
        "options": ["নিষ্কর", "পরস্পর", "সন্তাপ", "ষষ্ঠ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "'চৌচালা' কোন সমাসের উদাহরণ?",
        "options": ["বহুব্রীহি", "দ্বিগু", "তৎপুরুষ", "কর্মধারয়"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "আমার যাওয়া হয়নি- 'আমার' কোন কারকে কোন বিভক্তি?",
        "options": ["কর্মে শূন্য", "কর্তায় শূন্য", "কর্তায় ষষ্ঠী", "কর্মে ষষ্ঠী"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "সমাসের রীতি কোন ভাষার হতে বাংলায় এসেছে?",
        "options": ["হিন্দি", "সংস্কৃত", "প্রাকৃত", "ইংরেজি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "ব্যতিহার কর্তায় উদাহরণ কোনটি?",
        "options": [
            "ছেলেরা ফুটবল খেলছে",
            "মুষলধারে বৃষ্টি পড়ছে",
            "বাঘে-মহিষে এক ঘাটে জল খায়",
            "শিক্ষক ছাত্রদের ব্যাকরণ পড়াচ্ছেন"
        ],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "নিম্নের কোনটিতে বৃত্তি অর্থে 'ঈ' প্রত্যয় যুক্ত হয়েছে?",
        "options": ["জমিদারী", "পোদ্দারী", "উমেদারী", "সরকারী"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "একটি অপূর্ণ বাক্যের পরে অন্য একটি বাক্যের অবতারণা করতে হলে কোন চিহ্ন বসে?",
        "options": ["কোলন", "সেমিকোলন", "ড্যাস", "কমা"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "'চাঁদ' এর সমর্থক শব্দ কোনটি?",
        "options": ["সবিতা", "তপন", "আদিত্য", "বিধু"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 18,
        "question": "'খাতক' শব্দের বিপরীত শব্দ কোনটি?",
        "options": ["মহাজন", "বাউল গান", "তিরোভাব", "শাঁস"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 19,
        "question": "'পর্বত' এর সমর্থক শব্দ নয় কোনটি?",
        "options": ["শৈল", "অদ্রি", "মেদিনী", "অচল"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 20,
        "question": "'দীপ্তি পাচ্ছে এমন' -এক কথায় কী হবে?",
        "options": ["দীপ্যমান", "দীপ্তমান", "দীপ্যমান", "দেদীপ্যমান"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 21,
        "question": "কোনটির স্ত্রীলিঙ্গ ভিন্ন শব্দ?",
        "options": ["বিদ্বান", "গায়ক", "কোকিল", "দাদা"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 22,
        "question": "কোনটির শুধুমাত্র স্ত্রীবাচক হয়?",
        "options": ["সন্তান", "সৎমা", "ঢাকী", "ঘোষজা"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 23,
        "question": "অনূঢ়া কোনটির বাক্য সংকোচন?",
        "options": [
            "যে নারীর কোনো সন্তান হয় না",
            "যে নারী বীর সন্তান প্রসব করে",
            "যে নারীর সন্তান বাঁচে না",
            "যে মেয়ের বিয়ে হয়নি"
        ],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 24,
        "question": "'হরতাল' কোন ভাষার শব্দ?",
        "options": ["গুজরাতি", "তুর্কি", "পর্তুগিজ", "বার্মিজ"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 25,
        "question": "উক্তি-এর প্রকৃতি ও প্রত্যয় কোনটি?",
        "options": ["বচ্ + ক্ত", "বচ্ + উক্তি", "√বচ্ + ক্তি", "বচ্ + তি"],
        "answer": "গ",
        "explanation": ""
    }
]

out = {
    "title": "বাংলা বুলেটিন-০৭",
    "subject": "Bangla",
    "model_test": 7,
    "total_questions": len(q1_25),
    "questions": q1_25
}

out_dir = "JSON Data/Saif Sir NTRCA Suggestion/Bangla"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "Model Test-07.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"Saved {out_file} successfully with {len(q1_25)} questions!")
