# scripts/bpsc_non_tech/math/p1009.py

PAGE_NUM = 1009

QUESTIONS = [
    {
        "id": 48,
        "page": PAGE_NUM,
        "question": "Which two pairs of x satisfies the equation (x + 3)² = (x + 5) [BB-2026]",
        "options": [
            "1, 4",
            "1, -4",
            "-1, -4",
            "-1, 4"
        ],
        "answer": "গ",
        "explanation": "Given that,\n(x + 3)² = (x + 5)\n⇒ x² + 6x + 9 = x + 5\n⇒ x² + 6x - x + 9 - 5 = 0\n⇒ x² + 5x + 4 = 0\n⇒ x² + 4x + x + 4 = 0\n⇒ (x + 4) + 1(x + 4) = 0\n⇒ (x + 4)(x + 1) = 0\n∴ x = -1, -4 (Ans.)"
    },
    {
        "id": 49,
        "page": PAGE_NUM,
        "question": "The HCF and LCM of two numbers are 12 and 288 respectively. If one of the numbers is 96, find the other. [BB-2026]",
        "options": [
            "34",
            "36",
            "38",
            "40"
        ],
        "answer": "খ",
        "explanation": "Given that,\nHCF of two numbers = 12\nLCM of two numbers = 288\nOne number = 96\nLet the other number = x\nWe know the relation between HCF, LCM and two numbers.\n∴ Product of the two numbers = HCF × LCM\n⇒ 96 × x = 12 × 288\n⇒ x = (12 × 288) / 96\n∴ x = 36 (Ans.)"
    },
    {
        "id": 50,
        "page": PAGE_NUM,
        "question": "tan45° এর মান কত? [WZPDCL-2026]",
        "options": [
            "0",
            "1",
            "√3",
            "1/√3"
        ],
        "answer": "খ",
        "explanation": "tan45° = sin45° / cos45° = (1/√2) / (1/√2) = 1/√2 × √2/1 = 1 (Ans.)"
    },
    {
        "id": 51,
        "page": PAGE_NUM,
        "question": "sin²θ + cos²θ = কত? [WZPDCL-2026]",
        "options": [
            "0",
            "1",
            "sin2θ",
            "cos2θ"
        ],
        "answer": "খ",
        "explanation": "আমরা জানি, sin²θ + cos²θ = 1"
    },
    {
        "id": 52,
        "page": PAGE_NUM,
        "question": "কমপ্লেক্স সংখ্যা i² কত? [WZPDCL-2026]",
        "options": [
            "1",
            "-1",
            "0",
            "i³"
        ],
        "answer": "খ",
        "explanation": "কমপ্লেক্স সংখ্যাসমূহ:\n* i⁰ = √(-1)\n* i² = -1\n* i³ = -i\n* i⁴ = 1"
    },
    {
        "id": 53,
        "page": PAGE_NUM,
        "question": "যদি x = 2 হয়, 3x² - 4x + 1 এর মান কত? [WZPDCL-2026]",
        "options": [
            "5",
            "7",
            "9",
            "11"
        ],
        "answer": "ক",
        "explanation": "দেওয়া আছে, x = 2\n∴ প্রদত্ত রাশি = 3x² - 4x + 1\n= 3 × (2)² - 4 × 2 + 1\n= 3 × 4 - 8 + 1\n= 13 - 8\n= 5\n∴ নির্ণেয় মান 5 (Ans.)"
    },
    {
        "id": 54,
        "page": PAGE_NUM,
        "question": "একটি বৃত্তের ব্যাস ১২ সেমি হলে এর পরিসীমা কত সেমি হবে? [WZPDCL-2026]",
        "options": [
            "৩৭.৭০",
            "৭৫.৪০",
            "১১৩.১০",
            "৫৯.২১"
        ],
        "answer": "ক",
        "explanation": "দেওয়া আছে,\nবৃত্তের ব্যাস = ১২ সেমি\n∴ বৃত্তের ব্যাসার্ধ, r = ১২/২ = ৬ সেমি\nআমরা জানি,\nবৃত্তের পরিসীমা = ২πr\n= ২ × ৩.১৪১৬ × ৬ = ৩৭.৭০ সেমি\n∴ নির্ণেয় পরিসীমা ৩৭.৭০ সেমি।"
    },
    {
        "id": 55,
        "page": PAGE_NUM,
        "question": "একটি সমদ্বিবাহু ত্রিভুজের অতিভুজের দৈর্ঘ্য ১২ সেমি হলে ত্রিভুজটির ক্ষেত্রফল কত বর্গ সেমি? [WZPDCL-2026]",
        "options": [
            "√৭৬",
            "√৪৪",
            "৩৬",
            "৭২"
        ],
        "answer": "গ",
        "explanation": "সমকোণ সংলগ্ন প্রতিটি বাহুর দৈর্ঘ্য = a সেমি\nএখন, a² + a² = 12²\nবা, 2a² = 144\nবা, a² = 72\n∴ a = √72\n∴ ত্রিভুজটির ক্ষেত্রফল = 1/2 × (√72) × (√72)\n= 1/2 × (√72)²\n= 1/2 × 72\n= 36 বর্গ সেমি\n∴ নির্ণেয় ক্ষেত্রফল 36 বর্গ সেমি।"
    },
    {
        "id": 56,
        "page": PAGE_NUM,
        "question": "২, ৬, ১২, ২০, ৩০ এর সিরিজটির সঙ্গে কোনটির মিল আছে? [GDA-2025]",
        "options": [
            "৩৮, ৫২, ৬৮, ৮০",
            "২৭, ৪৮, ৬৮, ৭৮",
            "৪২, ৫৬, ৭২, ৯০",
            "৩৮, ৫০, ৬২, ৭৪"
        ],
        "answer": "গ",
        "explanation": "প্রদত্ত ধারাটি লক্ষ করি,\n২, ৬, ১২, ২০, ৩০\nএখানে পরপর দুটি পদের পার্থক্য বা ব্যবধান নির্ণয় করি।\n৬ - ২ = ৪\n১২ - ৬ = ৬\n২০ - ১২ = ৮\n৩০ - ২০ = ১০\nঅর্থাৎ, প্রতি পদের পার্থক্য ক্রমানুসারে, ৪, ৬, ৮, ১০ এভাবে ২ করে বৃদ্ধি পাচ্ছে।\nতাহলে,\n৩০ এর পরবর্তী পদ = ৩০ + (১০ + ২) = ৪২\n৪২ এর পরবর্তী পদ = ৪২ + (১২ + ২) = ৫৬\n৫৬ এর পরবর্তী পদ = ৫৬ + (১৪ + ২) = ৭২\nএবং ৭২ এর পরবর্তী পদ = ৭২ + (১৬ + ২) = ৯০\nসুতরাং, সঠিক ধারাটি হলো: ৪২, ৫৬, ৭২, ৯০ (উত্তর)"
    }
]
