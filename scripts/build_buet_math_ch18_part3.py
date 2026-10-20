# -*- coding: utf-8 -*-
import json
import os

from build_buet_math_ch18_part2 import q_data

# ==============================================================================
# Q76 to Q115 (Pages 441-447)
# ==============================================================================

q_data.append({
    "id": 76,
    "question": "'ক' থেকে 'ছ' পর্যন্ত দূরত্বের সমান দূরত্বে 'ড' অবস্থিত হলে Reverse order-এ 'ড' পর্যন্ত বর্ণ কী হবে? [EGCB-ICT-24]",
    "options": ["ছ", "প", "ড", "ল"],
    "answer": "ক",
    "explanation": "বর্ণমালার অবস্থান ও Reverse order অনুসারে সঠিক উত্তর (ক) ছ।"
})

q_data.append({
    "id": 77,
    "question": "What is the 4th Number of this series 2, 16, 54, ----- [EGCB-EEE/ME/CE-24]",
    "options": ["76", "64", "128", "112"],
    "answer": "গ",
    "explanation": "2 × 1³ = 2, 2 × 2³ = 16, 2 × 3³ = 54, 2 × 4³ = 128 (Ans.)"
})

q_data.append({
    "id": 78,
    "question": "'Three idiots' is a _ [EGCB-EEE/ME/CE-24]",
    "options": ["Poetry", "Novel", "Literature", "Movie"],
    "answer": "ঘ",
    "explanation": "'3 Idiots' একটি বিখ্যাত চলচ্চিত্র (Movie)।"
})

q_data.append({
    "id": 79,
    "question": "At which with the horizontal a projectile is to be projected to cover maximum horizontal distance? [EGCB-EEE/ME/CE-24]",
    "options": ["slightly lower than 45 degrees", "Slightly higher than 45 degrees", "Exactly 45 degrees", "Right angle"],
    "answer": "গ",
    "explanation": "প্রাস সর্বোচ্চ অনুভূমিক পাল্লা অতিক্রম করে যখন নিক্ষেপণ কোণ ঠিক ৪৫ ডিগ্রি (Exactly 45 degrees) হয়।"
})

q_data.append({
    "id": 80,
    "question": "একজন ব্যক্তি তার অবস্থান থেকে 10m দক্ষিণে যায় তারপর ডানদিকে ঘুরে 10m যায় আবার ডানদিকে ঘুরে 10m যায় তারপর ২য় ব্যক্তির সাথে মুখোমুখি দেখা হয়। তাহলে ২য় ব্যক্তি কোন দিকে মুখ আছে? [EGCB-EEE/ME/CE-24]",
    "options": ["দক্ষিণ", "উত্তর", "পূর্ব", "পশ্চিম"],
    "answer": "ক",
    "explanation": "১ম ব্যক্তি দক্ষিণে গিয়ে ডানে (পশ্চিমে) ঘুরে আবার ডানে (উত্তরে) যায়। অর্থাৎ সে উত্তর দিকে মুখ করে রয়েছে। তার সাথে মুখোমুখি হতে হলে ২য় ব্যক্তিকে দক্ষিণ দিকে মুখ করে থাকতে হবে।"
})

q_data.append({
    "id": 81,
    "question": "Terminator II is a ------- [NWPGCL-ICT/CSE-24]",
    "options": ["Movie", "book", "poem", "Drama"],
    "answer": "ক",
    "explanation": "Terminator II একটি বিখ্যাত সিনেমা (Movie)।"
})

q_data.append({
    "id": 82,
    "question": "a, 52, c, 48, f, 42, j, ? [NWPGCL-ICT/CSE-24]",
    "options": ["34", "44", "54", "64"],
    "answer": "ক",
    "explanation": "সংখ্যার ধারা: 52 - 4 = 48, 48 - 6 = 42, 42 - 8 = 34।"
})

q_data.append({
    "id": 83,
    "question": "Write the next term of each of the following sequences: 1, 5, 14, 30, 55 ........ [NWPGCL-ICT/CSE-24]",
    "options": ["91", "96", "97", "98"],
    "answer": "ক",
    "explanation": "1, 1+2²=5, 5+3²=14, 14+4²=30, 30+5²=55, 55+6²=55+36=91।"
})

q_data.append({
    "id": 84,
    "question": "0.125, 0.2, 0.5, 0.8... complete the series. [BCPCL-EEE-24]",
    "options": ["1", "2", "6", "8"],
    "answer": "খ",
    "explanation": "0.125 × 4 = 0.5; 0.5 × 4 = 2 (Ans.)"
})

q_data.append({
    "id": 85,
    "question": "Heart: Human: : Car [BSTI-CE/Physics/EEE-24]",
    "options": ["Engine", "Fuel", "wheel", "Lubricant"],
    "answer": "a",
    "explanation": "মানুষের শরীরের মূল চালিকাশক্তি যেমন হৃদপিণ্ড (Heart), গাড়ির মূল যন্ত্র তেমনি ইঞ্জিন (Engine)।"
})

q_data.append({
    "id": 86,
    "question": "'Top gun' is related to [CPGCBL-EEE/ME/CE-23]",
    "options": ["Revolver", "Rifle", "Aircraft", "none"],
    "answer": "গ",
    "explanation": "'Top Gun' ফাইটার বিমান (Aircraft) চালনা ও নৌবাহিনীর বিমানচালকদের সাথে সম্পর্কিত।"
})

q_data.append({
    "id": 87,
    "question": "A 52 C 48 f 42 j? Which one is the next. [CPGCBL-EEE/ME/CE-23]",
    "options": ["40", "34", "38", "None of the above"],
    "answer": "খ",
    "explanation": "সংখ্যার পার্থক্য: 52 - 4 = 48, 48 - 6 = 42, 42 - 8 = 34।"
})

q_data.append({
    "id": 88,
    "question": "What will come next in the series- 3, 7, 13, 21? [CPGCBL-EEE/ME/CE-23]",
    "options": ["29", "30", "31", "32"],
    "answer": "গ",
    "explanation": "ব্যবধান: 7 - 3 = 4, 13 - 7 = 6, 21 - 13 = 8, পরবর্তী ব্যবধান 10। ∴ 21 + 10 = 31।"
})

q_data.append({
    "id": 89,
    "question": "একটি গাছকে উপড়ে ফেলার জন্য 10 নিউটন বল প্রয়োজন। যদি গাছটিকে দড়ি বেঁধে উপর দিক থেকে 6 নিউটন বলে টানা হয় এবং পূর্বদিক থেকে আরেকটি দড়ি বেঁধে টানা হয় তাহলে পূর্ব দিকের দড়ির বল কত হবে? [CPGCBL-ET/MT/CT-23]",
    "options": ["2 N", "8 N", "4 N", "10 N"],
    "answer": "খ",
    "explanation": "লব্ধি বল F = √(F₁² + F₂²) => 10 = √(6² + F₂²) => F₂² = 100 - 36 = 64 => F₂ = 8 N।"
})

q_data.append({
    "id": 90,
    "question": "এক ব্যক্তি A অবস্থান থেকে 12 মিটার উত্তর দিকে যায় এবং পরে 5 মিটার পূর্ব দিকে গিয়ে B অবস্থানে পৌঁছায়। A হতে তাঁর দূরত্ব কত? [BCPCL-ET-23]",
    "options": [],
    "answer": "13 মিটার",
    "explanation": "দূরত্ব = √(12² + 5²) = √(144 + 25) = √169 = 13 মিটার।"
})

q_data.append({
    "id": 91,
    "question": "মি. ক 17 দিন আগে বলেছিলেন তার জন্মদিন আগামীকাল। আজ 23 তারিখ হলে তার জন্মদিন কত তারিখে ছিলো? [DESCO-ET-23]",
    "options": ["18 তারিখ", "7 তারিখ", "5 তারিখ", "24 তারিখ"],
    "answer": "খ",
    "explanation": "17 দিন আগে ছিল 23 - 17 = 6 তারিখ। সেদিন তিনি বলেছিলেন জন্মদিন আগামীকাল, সুতরাং জন্মদিন ছিল 6 + 1 = 7 তারিখ।"
})

q_data.append({
    "id": 92,
    "question": "A farmer has some hens and some cows. If the total number of animal heads is 40 and the total number of animal legs is 100, what is the number of cows? [BIWTA-EEE/ME/CE-22]",
    "options": ["10", "20", "30", "cannot be determined"],
    "answer": "ক",
    "explanation": "H + C = 40 এবং 2H + 4C = 100 => 2(40 - C) + 4C = 100 => 2C = 20 => C = 10। সুতরাং গরুর সংখ্যা 10।"
})

q_data.append({
    "id": 93,
    "question": "The mode and mean is given by 7 and 8, respectively. Then the median is: [BCIC-EEE/ME-22]",
    "options": ["1/13", "13/3", "23/3", "33"],
    "answer": "c",
    "explanation": "mode = 3 × median - 2 × mean => 7 = 3 × median - 2 × 8 => 3 × median = 23 => median = 23/3 (Ans.)"
})

q_data.append({
    "id": 94,
    "question": "একজন সৈন্য ট্রেনিং করছে। একজন লোক সৈন্যদলের একজনকে জিজ্ঞাসা করলো তোমরা কতজন? উত্তরে সৈন্যটি বললো- আছি যত আসবে তত, তার অর্ধেক, তার সিকি এবং তোমাকে নিয়ে শতজন। কতজন সৈন্য ট্রেনিং নিচ্ছিল? [PGCB-ET-18, MT-20, BADC-MT-20, BPDB-CT-21, BPDB-ET-21, CPGCBL-ET/MT-22]",
    "options": ["১৮ জন", "৩৬ জন", "৪০ জন", "৪৮ জন"],
    "answer": "খ",
    "explanation": "ধরি সৈন্য সংখ্যা x। প্রশ্নমতে, x + x + x/2 + x/4 + 1 = 100 => 11x/4 = 99 => x = 36 জন।"
})

q_data.append({
    "id": 95,
    "question": "A series is given with one term missing. Choose the correct alternative from the given ones that will complete the series. ABC, ZYX, DEF, WVU........ [KGDCL-EEE/ME/CE-21]",
    "options": ["GHI", "IJK", "MNO", "EFG"],
    "answer": "a",
    "explanation": "ABC, DEF এর পরবর্তী পদ ক্রমানুসারে GHI হবে।"
})

q_data.append({
    "id": 96,
    "question": "If x and y are negative, then which of the following statement is/are always true? [BPDB-EEE/CE/CSE-21]",
    "options": ["xy is positive", "x + y is positive", "x - y is positive", "none of these"],
    "answer": "ক",
    "explanation": "দুটি ঋণাত্মক সংখ্যার গুণফল সর্বদা ধনাত্মক (positive) হয়। সুতরাং xy is positive সবসময় সত্য।"
})

q_data.append({
    "id": 97,
    "question": "A ও B দুই ভাই, C ও D দুই বোন, A-এর ছেলে D-এর ভাই হলে B ও C এর মধ্যে সম্পর্ক কী? [KGDCL-MT-21]",
    "options": ["বাবা", "দাদা", "চাচা", "ভাই"],
    "answer": "গ",
    "explanation": "A এর ছেলে D এর ভাই, আবার C ও D দুই বোন। সুতরাং C হলো A এর মেয়ে। যেহেতু B হলো A এর ভাই, তাই B হলো C এর চাচা।"
})

q_data.append({
    "id": 98,
    "question": "ঢাকা থেকে রাজশাহী যাবার চারটি পথ রয়েছে। কত সংখ্যক উপায়ে ঢাকা থেকে রাজশাহী গিয়ে রাজশাহী থেকে আবার ঢাকায় ফেরত আসা যাবে? [APSCL-ET-21]",
    "options": ["4", "16", "24", "32"],
    "answer": "খ",
    "explanation": "যাওয়ার উপায় ৪টি এবং ফেরত আসার উপায় ৪টি। মোট উপায়ের সংখ্যা = ৪ × ৪ = ১৬টি।"
})

q_data.append({
    "id": 99,
    "question": "2 feet : 4 yard = ? [DESCO-ET-19, BPDB-MT-21]",
    "options": ["1:9", "1:8", "1:7", "1:6"],
    "answer": "ঘ",
    "explanation": "1 yard = 3 ft। ∴ 2 ft : 4 yard = 2 ft : (4 × 3) ft = 2 : 12 = 1 : 6 (Ans.)"
})

q_data.append({
    "id": 100,
    "question": "মাসুদ রাশেদের থেকে লম্বা, কাশেম মাসুদের থেকে লম্বা, জাবির খবিরের থেকে লম্বা, খবির রাশেদের থেকে লম্বা। এদের মধ্যে বেটে কে? [BR Power-PT-21]",
    "options": [],
    "answer": "রাশেদ",
    "explanation": "কাশেম > মাসুদ > রাশেদ এবং জাবির > খবির > রাশেদ। সুতরাং এদের মধ্যে সবচেয়ে বেটে রাশেদ।"
})

q_data.append({
    "id": 101,
    "question": "একজন লোক একটি লাইনের ১ম থেকে গণনা করলেও ১১ তম হয় এবং শেষ থেকে গণনা করলেও ১১ তম হয়, তবে লাইনে মোট কয়জন ছিল? [BR Power-PT-21]",
    "options": ["২৪", "২১", "৩০", "৪২"],
    "answer": "খ",
    "explanation": "মোট লোকসংখ্যা = ১১ + ১১ - ১ = ২১ জন।"
})

q_data.append({
    "id": 102,
    "question": "এই সিরিজে কোনটি ভুল? ১ ২ ৩ ৪ ৫ ৬ ৭ ৯ [BR Power-PT-21]",
    "options": ["৬", "৭", "৫", "৮"],
    "answer": "ঘ",
    "explanation": "সিরিজে দেখা যাচ্ছে ১ থেকে ৯ এর স্বাভাবিক সংখ্যার মধ্যে ৮ নেই। সুতরাং ভুল ৮।"
})

q_data.append({
    "id": 103,
    "question": "৬ জন বালক ৬ মিনিটে ৬ পৃষ্ঠা লিখে। ১ জন ১ পৃষ্ঠা কত মিনিটে লিখবে? [BR Power-PT-21]",
    "options": ["১", "২১", "৬", "১২"],
    "answer": "গ",
    "explanation": "(M₁ × T₁)/W₁ = (M₂ × T₂)/W₂ => (6 × 6)/6 = (1 × T₂)/1 => T₂ = 6 মিনিট।"
})

q_data.append({
    "id": 104,
    "question": "দুইটি বিন্দুর মধ্যে দিয়ে কয়টি রেখা অঙ্কন করা যাবে? [PGCB-CT-21]",
    "options": [],
    "answer": "১টি",
    "explanation": "দুইটি বিন্দুর মধ্য দিয়ে শুধুমাত্র একটিই নির্দিষ্ট সরলরেখা অঙ্কন করা যায়।"
})

q_data.append({
    "id": 105,
    "question": "\"A+B\" means A is the son of B. \"A-B\" means A is the wife of B. Then what does P+R-Q? [NESCO-CSE-21]",
    "options": [
        "P is the son of Q",
        "P is the wife of Q",
        "P is the father of Q",
        "P is the brother of Q"
    ],
    "answer": "a",
    "explanation": "R - Q অর্থ R হলো Q এর স্ত্রী। P + R অর্থ P হলো R এর ছেলে। সুতরাং P হলো Q এর ছেলে (P is the son of Q)।"
})

q_data.append({
    "id": 106,
    "question": "How many times are the hands of a clock at right angle in a day? [SGCL-EEE/ME-20]",
    "options": ["22", "24", "44", "48"],
    "answer": "c",
    "explanation": "প্রতি ঘণ্টায় ঘণ্টার ও মিনিটের কাঁটা ২ বার লম্বভাবে অবস্থান করে। কিন্তু ২-৪টা এবং ৮-১০টায় ৪ বারের বদলে ৩ বার করে সমকোণে আসে। ফলে প্রতি ১২ ঘণ্টায় ২২ বার এবং ২৪ ঘণ্টায় মোট ৪৪ বার সমকোণে থাকে।"
})

q_data.append({
    "id": 107,
    "question": "[Diagram: Three triangles with vertices and centers; 1st with 7, 6, 2 and center 19; 2nd with 1, 8, 4 and center 33; 3rd with 5, 2, ? and center 23] প্রশ্নবোধক স্থানে সংখ্যাটি কত হবে? [PGCB-ET, CMT-18]",
    "options": ["7", "8", "9", "10"],
    "answer": "গ",
    "explanation": "(6 × 2) + 7 = 19; (8 × 4) + 1 = 33; (2 × 9) + 5 = 23 ∴ ? = 9 (Ans.)"
})

q_data.append({
    "id": 108,
    "question": "যদি ২চ = ৩ছ = ৪জ হয়, তবে চ : ছ : জ = ? [PGCB-ET-19]",
    "options": ["২৪ : ৮ : ৬", "১৬ : ৮ : ৬", "১২ : ৮ : ৬", "১২ : ৮ : ৪"],
    "answer": "গ",
    "explanation": "২চ = ৩ছ => চ/ছ = ৩/২ = ৬/৪ = ১২/৮; আবার ৩ছ = ৪জ => ছ/জ = ৪/৩ = ৮/৬। ∴ চ : ছ : জ = ১২ : ৮ : ৬।"
})

q_data.append({
    "id": 109,
    "question": "42 + |4| + |-4| - 42 = ? [SGCL-MT-20]",
    "options": ["12", "18", "8", "16"],
    "answer": "c",
    "explanation": "42 + |4| + |-4| - 42 = 42 + 4 + 4 - 42 = 8 [এখানে, |-4| = 4 ধরে]।"
})

q_data.append({
    "id": 110,
    "question": "How many days are there in x weeks and x days? [PGCB-MT-20]",
    "options": ["7 x²", "14 x", "8x", "7"],
    "answer": "c",
    "explanation": "Total days = x weeks + x days = (x × 7) + x = 8x (Ans.)"
})

q_data.append({
    "id": 111,
    "question": "If 2nd term is 27 and 5th term is 84 at constant rate then what is the 1st term? [EGCB-ME-20]",
    "options": ["12", "16", "8", "20"],
    "answer": "c",
    "explanation": "ধরি first term = a, constant difference = d। a + d = 27 এবং a + 4d = 84 => 3d = 57 => d = 19 ∴ a = 27 - 19 = 8 (Ans.)"
})

q_data.append({
    "id": 112,
    "question": "[Diagram: Triangle divided into 3 vertical sectors and 3 horizontal layers] চিত্রে কতটি ত্রিভুজ বিদ্যমান? [BCMCL-ME-20]",
    "options": ["9", "18", "13", "12"],
    "answer": "খ",
    "explanation": "মোট ত্রিভুজের সংখ্যা = (1 + 2 + 3) × 3 = 6 × 3 = 18 (Ans.)"
})

q_data.append({
    "id": 113,
    "question": "If South-East becomes North and North-East become west and rest of the directions are changed in the same manner, then what will be the direction for west? [BCMCL-ME-20]",
    "options": ["North-East", "South", "South-East", "South-West"],
    "answer": "c",
    "explanation": "দিক পরিবর্তনের নিয়ম অনুযায়ী পশ্চিম দিকের নতুন অবস্থান হবে South-East।"
})

q_data.append({
    "id": 114,
    "question": "[Diagram: Triangle with all three medians intersecting at centroid] How many triangles are there in the following figure? [BCMCL-20]",
    "options": ["9", "13", "16", "18"],
    "answer": "c",
    "explanation": "একটি ত্রিভুজের তিনটি মধ্যমা পরস্পরকে ছেদ করলে মোট ১৬টি ত্রিভুজ গঠিত হয়।"
})

q_data.append({
    "id": 115,
    "question": "F2, -, D8, C16, B32 ......... ? [BIFPCL-ME-19]",
    "options": ["E4", "E3", "E2", "E6"],
    "answer": "a",
    "explanation": "Letter F থেকে A এর দিকে অগ্রসর হচ্ছে এবং সংখ্যা দ্বিগুণ হচ্ছে: 2, 4, 8, 16, 32। সুতরাং উত্তর E4।"
})

print(f"Loaded {len(q_data)} questions so far.")
