# -*- coding: utf-8 -*-
import json
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

def parse_file(filepath):
    results = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line_str = line.strip()
            m = re.search(r'Q(\d+)[^:]*:\*{0,2}\s*`([^`]+)`\s*->\s*opts:\s*(?:`?(\[[^\]]+\])`?),\s*ans:\s*`([^`]+)`,\s*expl:\s*`([^`]+)`', line_str)
            if m:
                q_num = int(m.group(1))
                q_text = m.group(2)
                raw_opts = m.group(3)
                ans = m.group(4)
                expl = m.group(5)
                try:
                    opts = json.loads(raw_opts)
                except Exception as e:
                    print(f"Error parsing opts for Q{q_num}: {e}")
                    opts = []
                results[q_num] = {
                    "id": q_num,
                    "question": q_text,
                    "options": opts,
                    "answer": ans,
                    "explanation": expl.replace('\\n', '\n')
                }
    return results

all_qs = {}
all_qs.update(parse_file('scripts/checkpoint_1662.txt'))
all_qs.update(parse_file('scripts/step_1719_full.txt'))

# Q70
all_qs[70] = {
    "id": 70,
    "question": "A pump can fill a tank with water in 2 hours. Because of a leak, it took 2 1/3 hours to fill the tank. The leak can drain all the water of the tank in: [BCPCL-ME-18]",
    "options": ["4 1/3 hours", "7 hours", "8 hours", "14 hours"],
    "answer": "ঘ",
    "explanation": "Shortcut:- Work done by the leak, = {2⁻¹ - (2 1/3)⁻¹}⁻¹ = 14 (Ans.)\nOr, Let, total volume of tank = 1\nCase-1, Takes 2 hrs to fill 1 portion\nTakes 1 hrs to fill = 1/2 portion\nCase-2, Takes 7/3 hrs to fill 1 portion\nTakes 1 hrs to fill = 3/7 portion\nLeakage Contribution = 1/2 - 3/7 = 1/14 portion\nNow, 1/14 portion drain in 1 hr.\n∴ 1 protion drain in 1/(1/14) = 14 hrs. (Ans.)"
}

# Q71 to Q86
all_qs[71] = {
    "id": 71,
    "question": "ক ও খ এর মোট বেতন খ ও গ এর মোট বেতন অপেক্ষা ১২ টাকা বেশি। ক এর বেতন গ অপেক্ষা কত কম? [BGFCL-CT-17]",
    "options": ["১০", "১২", "১৪", "কোনোটিই নয়"],
    "answer": "*",
    "explanation": "ধরি, ক ও খ এর মোট বেতন = x টাকা।\nবা, ক + খ = x টাকা ----- (i)\nশর্তমতে, খ + গ = x - ১২ টাকা ------- (ii)\n(i) - (ii) করে পাই, ক + খ - খ - গ = x - x + 12\nNote: প্রশ্নে গ এর বেতন ক অপেক্ষা কত কম বললে উত্তর হত ১২।"
}

all_qs[72] = {
    "id": 72,
    "question": "একটি ক্রিকেট খেলায় যত জন রান আউট হয় তার দেড় গুণ কট আউট হয়। আবার মোট উইকেটের অর্ধেক স্ট্যাম্প আউট হলে কত জন কট আউট হয়েছে? [BGFCL-CT-17]",
    "options": ["২", "৩", "৪", "৫"],
    "answer": "খ",
    "explanation": "Let, রান আউট = x, ∴ কট আউট = 1.5x,\nসম্ভব আউট হওয়া মোট উইকেট সংখ্যা = 10 তাহলে, স্ট্যাম্প আউট = 10/2 = 5\nশর্তমতে, x + 1.5x + 5 = 10 ⇒ x = 2 ∴ কট আউট = 1.5 × 2 = 3 জন (Ans.)"
}

all_qs[73] = {
    "id": 73,
    "question": "একটি ক্লাসে ১৬ জন ছেলের গড় ওজন ৫০ কেজি এবং অবশিষ্ট ৮ জন ছেলের গড় ওজন ৪০ কেজি। ক্লাসের সকল ছেলের গড় ওজন কত? [BGFCL-CT-17]",
    "options": ["৫০", "৪৮", "৪২", "৪০"],
    "answer": "খ",
    "explanation": "গড় ওজন = (মোট ওজন) / (মোট সংখ্যা) = ((৫০ × ১৬) + (৮ × ৪০)) / (১৬ + ৮) = ৪৮ (Ans.)"
}

all_qs[74] = {
    "id": 74,
    "question": "একটি শিবিরে ৭২০ জন সৈন্যের ২০ দিনের খাবার মজুদ আছে। ১০ দিন পর কিছু নতুন সৈন্যের আগমনের কারণে অবশিষ্ট খাদ্য তাদের ৮ দিন চললে। শিবিরে কতজন নতুন সৈন্য এসেছিল? [BGFDC-CT-17]",
    "options": ["১৮০ জন", "১৯০ জন", "১৭০ জন", "২০০ জন"],
    "answer": "ক",
    "explanation": "অবশিষ্ট (২০ - ১০) = ১০ দিন খেতে পারতো = ৭২০ জন সৈন্য\n∴ ৮ দিনে খাবে = (৭২০ × ১০) / ৮ = ৯০০ জন সৈন্য\n∴ অতিরিক্ত লোক লাগবে = (৯০০ - ৭২০) = ১৮০ জন (Ans.)"
}

all_qs[75] = {
    "id": 75,
    "question": "If x% of y is 100 and y% of z is 200, find the relation between x and z. [NWPGCL-ME-17]",
    "options": ["z = x/2", "z = 2x", "z = x/4", "z = 4x"],
    "answer": "খ",
    "explanation": "Let, y × x% = 100, ⇒ y × x/100 = 100, ∴ xy = 10000 ............. (i)\nAnd, z × y/100 = 200, ⇒ yz = 20000 ∴ y = 20000/z\nFrom equation (i) x . (20000/z) = 10000, ⇒ 2x = z (Ans.)"
}

all_qs[76] = {
    "id": 76,
    "question": "একটি ছাত্রাবাসে যতজন ছাত্র আছে তাদের প্রত্যেকের মাসিক খরচ মোট ছাত্রের দ্বিগুণ। ওই ছাত্রাবাসে মাসিক খরচ মোট ৬২৫০ টাকা হলে মোট ছাত্রসংখ্যা কত? [GTCL-ET-16]",
    "options": ["৫০ জন", "৫৬ জন", "৬৫ জন", "৭০ জন"],
    "answer": "খ",
    "explanation": "Let, মোট ছাত্র সংখ্যা = x জন। তাহলে, প্রত্যেকের মাসিক খরচ = 2x টাকা\nশর্তমতে, x × 2x = 6250 ⇒ x = √3125 = 55.9 = 56 জন (Ans.)"
}

all_qs[77] = {
    "id": 77,
    "question": "৫০ জন লোক একটি কাজের অর্ধেক করে ৮০ দিনে। ঐ কাজ ৫০ দিনে করতে কতজন অতিরিক্ত লোক লাগবে? [BADC-MT-16]",
    "options": ["৮০", "১০০", "১১০", "১৬০"],
    "answer": "গ",
    "explanation": "(Men 1 × time 1) / Work 1 = (Men 2 × time 2) / work 2\n⇒ (50 × 80) / (1/2) = (men2 × 50) / 1 ⇒ men2 = 160 জন\n∴ অতিরিক্ত লাগবে = 160 - 50 = 110 জন। (Ans.)"
}

all_qs[78] = {
    "id": 78,
    "question": "ক ও খ এর গড় আয় 300, খ ও গ এর গড় আয় 350 এবং ক ও গ এর গড় আয় 352 হলে ক এর আয় কত? [BADC-MT-16]",
    "options": ["160", "145", "302", "130"],
    "answer": "গ",
    "explanation": "প্রশ্নমতে, (ক + খ) + (খ + গ) + (ক + গ) = (300 + 350 + 352) × 2\n⇒ 2(ক + খ + গ) = 2004 ⇒ ক + খ + গ = 1002 ⇒ ক = 1002 - 700 = 302 (Ans.)"
}

all_qs[79] = {
    "id": 79,
    "question": "একজন লোক ৩ মাসে যে টাকা আয় করে তা সে ৪ মাসে ব্যয় করে। এক বছরে সে ৪৫০০০ টাকা আয় করলো। এক বছরে সে কত টাকা জমা করবে? [BADC-MT-16]",
    "options": ["১৫০০০০", "১১২৫০", "১৮০০০০", "২৫০০০০"],
    "answer": "খ",
    "explanation": "Let, ৩ মাসে আয় = x টাকা ∴ ১২ মাসে আয় = ৪x টাকা\nআবার, ৪ মাসে ব্যয় = x টাকা ∴ ১২ মাসে ব্যয় = ৩x টাকা\n∴ ১ বছরে জমা = ৪x - ৩x = x টাকা\n৪x টাকায় জমা হয় = x টাকা\n∴ ৪৫০০০ টাকায় জমা হয় = (x × 45000) / 4x = ১১২৫০ টাকা (Ans.)"
}

all_qs[80] = {
    "id": 80,
    "question": "An English school has 4/5 of the student are boys. There are 200 girls. What is the total number of students in the school? [KGDCL-EEE-16]",
    "options": ["2000", "3000", "4000", "1000"],
    "answer": "ঘ",
    "explanation": "Let, মোট student সংখ্যা = x, যেহেতু ছেলের সংখ্যা = 4/5 x সুতরাং মেয়ের সংখ্যা x - 4/5 x = 1/5 x\n∴ 1/5 x = 200 ⇒ x = 1000 (Ans.)"
}

all_qs[81] = {
    "id": 81,
    "question": "A washed 500 plate in 2 hours and B washed 450 plate in 3 hour. If they work together what time require to washing 1000 plate? [KGDCL-EEE-16]",
    "options": ["2.5", "3.5", "2", "4"],
    "answer": "ক",
    "explanation": "A, 2 ঘণ্টায় পরিষ্কার করে 500 প্লেট\nA, 1 ঘণ্টায় পরিষ্কার করে 500/2 = 250 প্লেট\nB, 3 ঘণ্টায় পরিষ্কার করে 450 plate = 150 প্লেট\n∴ A ও B, 1 ঘণ্টায় পরিষ্কার করে = 250 + 150 = 400 প্লেট\nA ও B, 400 প্লেট পরিষ্কার করে 1 ঘণ্টায়\nA ও B, 1 প্লেট পরিষ্কার করে 1/400 ঘণ্টায়\nA ও B, 1000 প্লেট পরিষ্কার করে 1000/400 = 2.5 ঘণ্টায় (Ans.)\nOr, Using this formula directly, W₁/T₁ + W₂/T₂ = W(total)/T(total)\n⇒ 500/2 + 450/3 = 1000/T(total) ⇒ T(total) = 2.5 hours (Ans.)"
}

all_qs[82] = {
    "id": 82,
    "question": "চারটি সমানুপাতিক রাশির প্রান্তীয় রাশিদ্বয়ের গুণফল ৪৮ হলে মধ্য রাশিদ্বয়ের গুণফল কত? [BEPZA-CE-16]",
    "options": ["৪৫", "৫৫", "৪৮", "৬০"],
    "answer": "গ",
    "explanation": "a:b::b:c একটি চতুর্থ সমানুপাতিক\na/b = b/c\n⇒ b² = ac = 48 [এখানে দেখা যায় যে, প্রান্তীয় রাশিদ্বয়ের গুণফল মধ্যরাশিদ্বয়ের গুণফলের সমান]\n∴ 48 (Ans.)"
}

all_qs[83] = {
    "id": 83,
    "question": "Faruk has x more marbles than Sanwar has and together they have a total of y marbles. Which of the following represents the number of marbles that Sanwar has? [BADC-ME-16]",
    "options": ["(y - x)/2", "y - x/2", "y/2 - x", "2y - x"],
    "answer": "ক",
    "explanation": "Let, সানোয়ারের মারবেল আছে = m সংখ্যক, ফারুকের আছে = m + x\n∴ মোট y = m + (m + x) ⇒ m = (y - x) / 2 (Ans.)"
}

all_qs[84] = {
    "id": 84,
    "question": "If x books cost of TK 50 and y books cost of 80 each then the average cost in taka per book is equal to - [BADC, DPDC-ME-16]",
    "options": ["(50x + 80y)/xy", "(5x + 8y)/(0.1x + 0.1y)", "(50x + 80y)/130", "none of these"],
    "answer": "খ",
    "explanation": "Average cost = (50x + 80y) / (x + y) = (5x + 8y) / (0.1x + 0.1y) (Ans.) [লব ও হরকে 10 দ্বারা ভাগ করে]"
}

all_qs[85] = {
    "id": 85,
    "question": "The cost of x numbers of pens is equal to the cost of (x+ 2) number of pencils. If per unit costs of pen and pencil are 10 and 8 Tk. Respectively, then x = ? [BADC-ME-16]",
    "options": ["4", "6", "8", "none"],
    "answer": "গ",
    "explanation": "according to question, Cost of Pen = Cost of pencil\n⇒ x × 10 = (x + 2) × 8, ⇒ x = 8 (Ans.)"
}

all_qs[86] = {
    "id": 86,
    "question": "A shopkeeper expects a gain of 22.5% on his cost price. If in a week, his sale was of Tk. 392, what was his profit? [KGDCL-EEE-16]",
    "options": ["72", "100", "4.6", "28"],
    "answer": "ক",
    "explanation": "মনে করি, ক্রয়মূল্য = x ∴ ক্রয়মূল্য + লাভ = বিক্রয়মূল্য\n⇒ x + (x × 22.5%) = 392\n⇒ x = 392 / 1.225 = 320,\n∴ লাভ = 392 - 320 = 72 (Ans.)"
}

print(f"Total collected: {len(all_qs)} questions")
missing = [i for i in range(1, 87) if i not in all_qs]
if missing:
    print(f"MISSING IDs: {missing}")
else:
    print("ALL 86 QUESTIONS PRESENT!")

# Sort by ID
final_list = [all_qs[i] for i in range(1, 87)]

# Write to target file
target_path = os.path.join("JSON Data", "BUET Patern", "Math", "সরল সহসমীকরণ.json")
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(final_list, f, ensure_ascii=False, indent=2)

print(f"Successfully saved to {target_path}!")
