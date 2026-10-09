import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

q1_20 = [
    {
        "id": 1,
        "question": "'কন্যা' শব্দের সমার্থক শব্দ কোনটি?",
        "options": ["অনুজা", "অবলা", "সুত", "তনয়া"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 2,
        "question": "'বগুড়ার চিনিপাতা দই সুস্বাদু।' - বাক্যটির 'চিনিপাতা' কোন কারক?",
        "options": ["অধিকরণ", "অপাদান", "করণ", "কর্ম"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 3,
        "question": "'ভানুমতির খেল' প্রবচটি বোঝায়-",
        "options": ["চালবাজি", "ভেলকিবাজি", "ফটকাবাজি", "ফেরেব্বাজি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 4,
        "question": "'ছেলে তো নয় যেন ননীর পুতুল'- এখানে 'যেন' -",
        "options": ["অব্যয়", "বিশেষ্য", "বিশেষণ", "সর্বনাম"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 5,
        "question": "কোনটি ভুল বাক্য ?",
        "options": ["দীনতা সব সময় ভাল নয়", "দেশের দারিদ্র দূর করতে হবে", "সময় বড় সংক্ষিপ্ত", "এখানে প্রবেশ নিষিদ্ধ"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 6,
        "question": "কোনটি শুদ্ধ বানান?",
        "options": ["প্রত্যুদগমন", "প্রত্যূদ্গমন", "প্রত্যুতগমন", "প্রত্যুদগমন"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 7,
        "question": "অবীরা বলতে কোন নারীকে বোঝায়?",
        "options": ["যে স্বামীর বশীভূত", "যার পুত্র হয়নি", "যার স্বামী, পুত্র নেই", "যার বিয়ে হয়নি"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 8,
        "question": "তুর্কি ভাষার শব্দ কোনগুলি?",
        "options": ["চা, চিনি", "হজ, ওজু", "চাকু, তোপ", "চশমা, রশদ"],
        "answer": "গ",
        "explanation": ""
    },
    {
        "id": 9,
        "question": "বাংলা ভাষায় প্রথম সনেট লেখেন-",
        "options": ["ঈশ্বর গুপ্ত", "মধুসূদন দত্ত", "রবীন্দ্রনাথ ঠাকুর", "নবীন সেন"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 10,
        "question": "'পরীক্ষায় সফল হও' - এটি কোন ধরনের বাক্য?",
        "options": ["বিবৃতিমূলক", "আদেশমূলক", "বিস্ময়সূচক", "ইচ্ছাসূচক"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 11,
        "question": "নিপাতনে সিদ্ধ সন্ধি কোনটি?",
        "options": ["পরিষ্কৃত", "পতঞ্জলি", "উত্থান", "সংস্কৃত"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 12,
        "question": "'মৌনাক'- ছদ্মনামে কে লিখতেন?",
        "options": ["শামসুর রাহমান", "ঈশ্বরচন্দ্র গুপ্ত", "বঙ্কিমচন্দ্র চট্টোপাধ্যায়", "সৈয়দ মুজতবা আলী"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 13,
        "question": "বিদেশি ধাতু কোনটি?",
        "options": ["গড্", "বুধ", "ছাম্", "ডর্"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 14,
        "question": "'পূর্ব বাংলার ভাষা আন্দোলন ও তৎকালীন রাজনীতি' গ্রন্থের রচয়িতা কে?",
        "options": ["ভাষা সৈনিক মাহবুবুল আলম চৌধুরী", "আহমদ ছফা", "আলি আহাদ", "বদরুদ্দীন উমর"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 15,
        "question": "'সব ভাল যার শেষ ভাল তার' - সঠিক ইংরেজি অনুবাদ কোনটি?",
        "options": ["All well that ends well.", "All are well that are well.", "All one well when all finish well.", "All well that end well."],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 16,
        "question": "কর্মধারায় সমাস কোনটি?",
        "options": ["মুখচন্দ্র", "মধুমখা", "কদাচার", "মহারাজ"],
        "answer": "ক",
        "explanation": ""
    },
    {
        "id": 17,
        "question": "'আলপিন' কোন ভাষার শব্দ?",
        "options": ["ওলন্দাজ", "গুজরাটি", "তুর্কি", "পর্তুগিজ"],
        "answer": "ঘ",
        "explanation": ""
    },
    {
        "id": 18,
        "question": "কোনটি মুক্তিযুদ্ধের প্রভাবে রচিত গল্পগ্রন্থ?",
        "options": ["দুধভাতে উৎপাত", "নামহীন গোত্রহীন", "অরক্ষিত জনপদ", "অবিনাশী আয়োজন"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 19,
        "question": "কোন ধ্বনি উচ্চারণের সময় স্বরতন্ত্রী বেশি অনুরণিত হয়?",
        "options": ["মহাপ্রাণ ধ্বনি", "ঘোষ ধ্বনি", "অঘোষ ধ্বনি", "অল্পপ্রাণ ধ্বনি"],
        "answer": "খ",
        "explanation": ""
    },
    {
        "id": 20,
        "question": "'ব্যাপ্তি' অর্থে সম্বন্ধ পদ কোনটি?",
        "options": ["রাজার রাজ্য", "বাটির দুধ", "দেশের লোক", "রোজার ছুটি"],
        "answer": "ঘ",
        "explanation": ""
    }
]

model_test_data = {
    "title": "বাংলা বুলেটিন-৪০",
    "subject": "Bangla",
    "model_test": "Model Test-40",
    "total_questions": len(q1_20),
    "questions": q1_20
}

output_path = "JSON Data/Saif Sir NTRCA Suggestion/Bangla/Model Test-40.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(model_test_data, f, ensure_ascii=False, indent=2)

print(f"Saved {output_path} successfully with {len(q1_20)} questions.")
