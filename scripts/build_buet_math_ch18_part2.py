# -*- coding: utf-8 -*-
import json
import os

from build_buet_math_ch18 import q_data

# ==============================================================================
# Q33 to Q75 (Pages 434-441)
# ==============================================================================

q_data.append({
    "id": 33,
    "question": "How many degrees does hour hand of a clock move from 8.00 AM to 2.00 PM? [RNPL-ME,EEE-25]",
    "options": ["180°", "120°", "90°", "270°"],
    "answer": "a",
    "explanation": "সময়ের ব্যবধান = 8.00 AM থেকে 2.00 PM = 6 ঘণ্টা। 1 ঘণ্টায় ঘণ্টা কাঁটা ঘুরে = 30° ∴ 6 ঘণ্টায় ঘুরে = 30° × 6 = 180°।"
})

q_data.append({
    "id": 34,
    "question": "A husband and wife have 6 married children, and each of them has a children. How many total number of family members: [RNPL-ME,EEE-25]",
    "options": ["24", "28", "20", "22"],
    "answer": "c",
    "explanation": "স্বামী ও স্ত্রী = ২ জন, ৬ বিবাহিত সন্তান ও তাদের সঙ্গী = ১২ জন, এবং প্রতি পরিবারে ১ জন করে সন্তান = ৬ জন। মোট সদস্য = ২ + ১২ + ৬ = ২০ জন।"
})

q_data.append({
    "id": 35,
    "question": "তিন ক্রমের ম্যাজিক সংখ্যা কোনটি? [DPDC-AE-25]",
    "options": ["15", "25", "33", "20"],
    "answer": "ক",
    "explanation": "তিন ক্রমের ম্যাজিক সংখ্যা হলো 15। 3×3 ক্রমের ম্যাজিক বর্গের প্রতিটি সারি, কলাম ও কর্ণের যোগফল 15 হয়।"
})

q_data.append({
    "id": 36,
    "question": "A cube is colored red on all 6 faces. It is cut into 64 identical smaller cubes of equal size. How many cubes have three faces painted? [CPGCBL-EEE/ME/CE-24]",
    "options": ["4", "8", "10", "16"],
    "answer": "b",
    "explanation": "একটি ঘনকের ৮টি কোণায় অবস্থিত ছোট ঘনকগুলোরই ৩টি তল রঙ করা থাকে। সুতরাং সঠিক উত্তর ৮টি।"
})

q_data.append({
    "id": 37,
    "question": "Five houses A to E are standing in a series. If house A is standing right to the B, E is at the end of the series, C is to the left of E, D is to the left of the B, then which house is in the middle. [CPGCBL-EEE/ME/CE-24]",
    "options": ["B", "D", "A", "E"],
    "answer": "c",
    "explanation": "শর্তানুসারে সারিটি হলো: D - B - A - C - E। সুতরাং সারির ঠিক মাঝখানে রয়েছে বাড়ি A।"
})

q_data.append({
    "id": 38,
    "question": "Which part will fit in the picture- [CPGCBL-EEE/ME/CE-24]",
    "options": ["1", "2", "3", "4"],
    "answer": "b",
    "explanation": "চিত্রের জ্যামিতিক বিন্যাস ও প্যাটার্ন অনুসারে বিকল্প 2 উপযুক্তভাবে মিলে যায়।"
})

q_data.append({
    "id": 39,
    "question": "How many triangles are present in the figure below? [CPGCBL-EEE/ME/CE-25]",
    "options": ["10", "12", "14", "16"],
    "answer": "c",
    "explanation": "প্রদত্ত চিত্রে মোট ১৪টি ত্রিভুজ রয়েছে।"
})

q_data.append({
    "id": 40,
    "question": "[Diagram with 8 branches: 5 & 25, 8 & 64, 4 & ?, 1 & 2] [CPGCBL-EEE/ME/CE-25]",
    "options": ["1", "3", "5", "6"],
    "answer": "b",
    "explanation": "প্রদত্ত চিত্রটিতে দুটি ধারা রয়েছে: 5-এর বর্গ 25, 8-এর বর্গ 64 এবং পর্যায়ক্রমিক সংখ্যা 1, 2, 3, 4... ∴ প্রশ্নবোধক স্থানে 3 হবে।"
})

q_data.append({
    "id": 41,
    "question": "Which one is the water image of ADVANCE? [APSCL-ME/EEE-24]",
    "options": ["∀ꓷV∀NƆE", "∀ꓷᴧ∀NƆƎ", "ADVANCE", "None"],
    "answer": "b",
    "explanation": "পানিতে ADVANCE শব্দের উলম্ব প্রতিফলন (water image) হলো ∀ꓷᴧ∀NƆƎ।"
})

q_data.append({
    "id": 42,
    "question": "A, P, R, X, S and Z are sitting in a row. S and Z are in the centre and A and P are at the ends. R is sitting on the left of A. Then who is sitting on the right of P? [APSCL-ME/EEE-24]",
    "options": ["S", "X", "A", "Z"],
    "answer": "b",
    "explanation": "সারির বিন্যাস: P X S Z R A। সুতরাং P-এর ডান পাশে X বসেছে।"
})

q_data.append({
    "id": 43,
    "question": "Arrange the words given below in a meaningful sequence. [APSCL-ME/EEE-24]\n1. Presentation, 2. Recommendation, 3. Arrival, 4. Discussion, 5. Introduction",
    "options": ["5, 3, 4, 1, 2", "3, 5, 4, 2, 1", "3, 5, 1, 4, 2", "5, 3, 1, 2, 4"],
    "answer": "c",
    "explanation": "যৌক্তিক ক্রম: 3. Arrival -> 5. Introduction -> 1. Presentation -> 4. Discussion -> 2. Recommendation (3, 5, 1, 4, 2)।"
})

q_data.append({
    "id": 44,
    "question": "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z. Which letter in this alphabet is the eighth letter to the right of the letter and which is tenth letter to the left of the last but one letter of the alphabet? [APSCL-ME/EEE-24]",
    "options": ["X", "W", "I", "H"],
    "answer": "b",
    "explanation": "Last but one letter হলো Y (25th)। Y এর বামে ১০ম অক্ষর হলো O (15th)। O এর ডানে ৮ম অক্ষর হলো W (23rd)।"
})

q_data.append({
    "id": 45,
    "question": "What is the number of straight lines and the number of triangles in the given figure. [APSCL-ME/EEE-24]",
    "options": [
        "10 straight lines and 34 triangles",
        "9 straight lines and 34 triangles",
        "9 straight lines and 36 triangles",
        "10 straight lines and 36 triangles"
    ],
    "answer": "c",
    "explanation": "প্রদত্ত চিত্রে 9 straight lines and 36 triangles বিদ্যমান।"
})

q_data.append({
    "id": 46,
    "question": "Given, ● + ▲ = 8, ★ - ◼ = 4, ● - ▲ = 0, ★ + ◼ = 12. ● + ▲ - ★ + ◼ = ? [CPGCBL-ET/MT-24]",
    "options": ["2", "4", "8", "0"],
    "answer": "b",
    "explanation": "● + ▲ - ★ + ◼ = (● + ▲) - (★ - ◼) = 8 - 4 = 4।"
})

q_data.append({
    "id": 47,
    "question": "C L R T B Q S M A P D I N F J K G Y X. LBT, IJF, PID এবং BMS চারটির মধ্যে কোনটি ব্যতিক্রম? [CPGCBL-ET/MT-24]",
    "options": ["BMS", "LBT", "IJF", "PDI"],
    "answer": "d",
    "explanation": "সিরিজে LBT এর মাঝে R; IJF এর মাঝে N; BMS এর মাঝে Q রয়েছে। কিন্তু PDI এর মাঝে কোনো letter নেই।"
})

q_data.append({
    "id": 48,
    "question": "আজ সোমবার হলে, ৬১ দিন পর কি বার হবে? [CPGCBL-ET/MT-24]",
    "options": ["Saturday", "Monday", "Sunday", "Thursday"],
    "answer": "ক",
    "explanation": "৬১ ÷ ৭ = ভাগশেষ ৫। ৫৬তম দিন সোমবার এবং ৫ দিন পর শনিবার (Saturday)।"
})

q_data.append({
    "id": 49,
    "question": "নিচের চিত্রে কয়টি ত্রিভুজ আছে? [PGCB-MT-20, BRPL-ME/ET/PT-24, NWPGCL-MT/ET/RAC-24, CPGCBL-ET/MT-24]",
    "options": ["5", "6", "8", "10"],
    "answer": "ঘ",
    "explanation": "পঞ্চকোণ তারকায় মোট ১০টি ত্রিভুজ থাকে।"
})

q_data.append({
    "id": 50,
    "question": "একটি জিরাফের দুটি চোখ, একটি বানরের দুটি চোখ এবং একটি হাতির দুটি চোখ থাকলে, আমার কয়টি চোখ আছে? [CPGCBL-ET/MT-24]",
    "options": ["3", "4", "1", "2"],
    "answer": "ঘ",
    "explanation": "মানুষের দুটি চোখ থাকে, সুতরাং উত্তর ২।"
})

q_data.append({
    "id": 51,
    "question": "1. Presentation, 2. Recommendation, 3. Arrival, 4. Discussion, 5. Introduction. নিচের কোন ক্রমটি সঠিক? [CPGCBL-ET/MT-24]",
    "options": ["5, 3, 4, 1, 2", "3, 5, 4, 2, 1", "3, 5, 1, 4, 2", "5, 3, 1, 2, 4"],
    "answer": "c",
    "explanation": "সঠিক ক্রম: 3. Arrival -> 5. Introduction -> 1. Presentation -> 4. Discussion -> 2. Recommendation।"
})

q_data.append({
    "id": 52,
    "question": "A, P, R, X, S ও Z পাশাপাশি আছে। S এবং Z মাঝখানে আছে, A এবং P শেষে আছে, A এর বামদিকে R থাকলে, P এর ডান দিকে কোনটি আছে? [CPGCBL-ET/MT-24]",
    "options": ["S", "X", "A", "Z"],
    "answer": "খ",
    "explanation": "সারিটি হলো: P X S Z R A। সুতরাং P এর ডান দিকে X আছে।"
})

q_data.append({
    "id": 53,
    "question": "[Diagram: four diamonds with 7,6,4,2; 9,9,8,1; 5,3,1,5; 6,2,1,?] [CPGCBL-ET/MT-24]",
    "options": ["2", "8", "4", "1"],
    "answer": "ক",
    "explanation": "7 × 6 = 42; 9 × 9 = 81; 5 × 3 = 15; 6 × 2 = 12 ∴ প্রশ্নবোধক স্থানে 2 হবে।"
})

q_data.append({
    "id": 54,
    "question": "AB = 3, BC = 5, CD = 7 হলে, AD = কত? [NWPGCL-MT/ET/RAC-24]",
    "options": [],
    "answer": "5",
    "explanation": "A = 1, B = 2, C = 3, D = 4 ∴ AD = 1 + 4 = 5।"
})

q_data.append({
    "id": 55,
    "question": "'ক' খ এর পশ্চিমে এবং 'খ' গ এর উত্তরে অবস্থিত। 'ঘ' ক এর দক্ষিণে হলে ঘ থেকে গ এর অবস্থান কোন দিকে? [NWPGCL-MT/ET/RAC-24]",
    "options": [],
    "answer": "পূর্ব দিকে",
    "explanation": "ঘ থেকে গ এর অবস্থান সরাসরি পূর্ব দিকে।"
})

q_data.append({
    "id": 56,
    "question": "আসাদ সাহেবের ৪ জন ছেলে আছে, প্রত্যেক ছেলের একজন করে বোন আছে। আসাদ সাহেবের মোট কতজন সন্তান? [NWPGCL-MT/ET/RAC-24]",
    "options": [],
    "answer": "৫ জন",
    "explanation": "৪ ছেলে এবং ১ মেয়ে। মোট সন্তান = ৫ জন।"
})

q_data.append({
    "id": 57,
    "question": "ভাই ও বোনের বর্তমান বয়স যথাক্রমে ২২ বছর ও ১৮ বছর। ভাইয়ের বয়স যখন দ্বিগুণ হবে তখন বোনের বয়স কত হবে? [NWPGCL-MT/ET/RAC-24]",
    "options": [],
    "answer": "৪০ বছর",
    "explanation": "ভাইয়ের বয়স দ্বিগুণ হলে ৪৪ বছর হবে (২২ বছর পর)। বোনের বয়স হবে ১৮ + ২২ = ৪০ বছর।"
})

q_data.append({
    "id": 58,
    "question": "D, K, G, N, ____, Q, M, T শূন্যস্থান এ কোন letter বসবে? [NWPGCL-MT/ET/RAC-24]",
    "options": [],
    "answer": "J",
    "explanation": "D (+7) -> K (-4) -> G (+7) -> N (-4) -> J (+7) -> Q (-4) -> M (+7) -> T ∴ J।"
})

q_data.append({
    "id": 59,
    "question": "বিকাল ৪.০০ টার সময় ঘড়িতে ঘণ্টা ও মিনিটের কাঁটা কত ডিগ্রি কোণে অবস্থান করে? [NWPGCL-MT/ET/RAC-24]",
    "options": [],
    "answer": "১২০°",
    "explanation": "|(60H - 11M)/2| = |(60×4 - 0)/2| = 120°।"
})

q_data.append({
    "id": 60,
    "question": "2 × 4 = 10, 3 × 5 = 18, 4 × 6 = 28 হলে 6 × 8 = কত? [NWPGCL-MT/ET/RAC-24]",
    "options": [],
    "answer": "53",
    "explanation": "2×4 + 2 = 10; 3×5 + 3 = 18; 4×6 + 4 = 28; 6×8 + 5 = 53।"
})

q_data.append({
    "id": 61,
    "question": "2, 3, 5, 8, 12, 17,- সিরিজটির পরবর্তী সংখ্যা কত? [NWPGCL-MT/ET/RAC-24]",
    "options": [],
    "answer": "23",
    "explanation": "+1, +2, +3, +4, +5, +6 => 17 + 6 = 23।"
})

q_data.append({
    "id": 62,
    "question": "১ নটিক্যাল mile কত কিঃমিঃ? [BTCL-CMT/MT-24]",
    "options": ["১.৮৫২", "১.৮৫৫", "১.৮১৬", "১.৮০২"],
    "answer": "ক",
    "explanation": "১ নটিক্যাল মাইল = ১.৮৫২ কি.মি., ১ মাইল = ১.৬২ কি.মি.।"
})

q_data.append({
    "id": 63,
    "question": "What is the meaning of 1 million? [BTCL-ET/ENT-24]",
    "options": ["One lakh", "Ten lakh", "Five lakh", "none"],
    "answer": "খ",
    "explanation": "1 Million = 10 lakh."
})

q_data.append({
    "id": 64,
    "question": "A man went 10m to the south then turn right and covered 12m distance then turn left, in which direction is he face? [BRPL-CSE/ME/EEE-24]",
    "options": ["North", "South", "East", "West"],
    "answer": "b",
    "explanation": "Initially went south, turned right (facing west), then turned left (facing south)."
})

q_data.append({
    "id": 65,
    "question": "Find the unknown value. [Diagram: 9, 28, ?, 126, 217] [BRPL-CSE/ME/EEE-24]",
    "options": ["96", "65", "56", "102"],
    "answer": "b",
    "explanation": "2³ + 1 = 9, 3³ + 1 = 28, 4³ + 1 = 65, 5³ + 1 = 126, 6³ + 1 = 217 ∴ 65।"
})

q_data.append({
    "id": 66,
    "question": "X talks with Y, Y is the brother of X's grandmothers dauther, then what is the relation of X with Y. [BRPL-CSE/ME/EEE-24]",
    "options": ["Grandfather", "Father", "Brother", "None"],
    "answer": "b",
    "explanation": "Y is Father (or maternal uncle)."
})

q_data.append({
    "id": 67,
    "question": "যদি সাদা মানে কালো, কালো মানে লাল, লাল মানে হলুদ, হলুদ মানে কমলা, কমলা মানে সবুজ, সবুজ মানে বেগুনি, বেগুনি মানে নীল হয় তাহলে, মানুষের রক্তের রং কি? [BRPL-ME/PT/ET-24]",
    "options": ["গোলাপি", "হলুদ", "নীল", "সবুজ"],
    "answer": "খ",
    "explanation": "রক্তের স্বাভাবিক রং লাল। প্রশ্নে 'লাল মানে হলুদ' বলা হয়েছে, তাই রক্তের রং হলুদ।"
})

q_data.append({
    "id": 68,
    "question": "সাড়ে ছয়টার সময় ঘণ্টা ও মিনিটের কাঁটার মধ্যে ক্ষুদ্রতম কোণের পরিমাণ কত? [PGCB-CE/EEE/ME/CSE-24]",
    "options": ["৭.৫°", "১৫°", "২২.৫°", "৩০°"],
    "answer": "খ",
    "explanation": "|(60×6 - 11×30)/2| = 30/2 = 15°।"
})

q_data.append({
    "id": 69,
    "question": "একটি বানর তৈলাক্ত বাঁশ বেয়ে ১ মিনিটে ৪ ফুট ওঠে, পরের মিনিটে ১ ফুট নামে। এভাবে ২২ ফুট লম্বা বাঁশের শীর্ষে পৌঁছাতে কত সময় লাগবে? [PGCB-CE/EEE/ME/CSE-24]",
    "options": ["১৫ মিনিট", "১১ মিনিট", "১৩ মিনিট", "১৪ মিনিট"],
    "answer": "গ",
    "explanation": "২ মিনিটে ৩ ফুট ওঠে। ১২ মিনিটে ১৮ ফুট + পরবর্তী ১ মিনিটে ৪ ফুট উঠে ২২ ফুটের শীর্ষে পৌঁছে যাবে। মোট সময় = ১২ + ১ = ১৩ মিনিট।"
})

q_data.append({
    "id": 70,
    "question": "........., 13, .......3. সিরিজের শূন্যস্থানের বসবে- [BGDCL-CT/ET/MT/CMT-24]",
    "options": ["12, 20", "12, 6", "18, 8", "12, 5"],
    "answer": "গ",
    "explanation": "18 - 5 = 13, 13 - 5 = 8, 8 - 5 = 3 ∴ 18, 8।"
})

q_data.append({
    "id": 71,
    "question": "How many daughters A have? A and B are brothers. C, D and E are nephews of A. F and G are son of A and niece of B respectively. [EGCB-ICT-24]",
    "options": ["1", "2", "3", "4"],
    "answer": "ক",
    "explanation": "G হলো A এর মেয়ে, সুতরাং ১ জন কন্যা সন্তান রয়েছে।"
})

q_data.append({
    "id": 72,
    "question": "A is taller than B amongst A, B, C, D, E. C is shorter than E and D is greater than A. Who is next to tallest? [EGCB-ICT-24]",
    "options": ["A", "B", "C", "D"],
    "answer": "ক",
    "explanation": "D > A > B; সবচেয়ে লম্বা D, তার ঠিক পরের জন A।"
})

q_data.append({
    "id": 73,
    "question": "A person has 6th birthday in 6th January, 2000. When will he celebrate his 40th birth anniversary? [EGCB-ICT-24]",
    "options": ["6 January 2034", "6 January 2035", "6 January 2040", "none of this"],
    "answer": "ক",
    "explanation": "জন্ম সাল = 2000 - 6 = 1994। 40তম বার্ষিকী = 1994 + 40 = 2034 (6 January 2034)।"
})

q_data.append({
    "id": 74,
    "question": "Now the time is 4.25 pm on the 24th of February and 11th of the Bengali month Falgun. Which date will be of Falgun on 25th of February at 6 am considering the sunrise at 6.30 am? [EGCB-ICT-24]",
    "options": ["12", "11", "10", "13"],
    "answer": "খ",
    "explanation": "সূর্যোদয়ের আগে তারিখ পরিবর্তন হয় না, তাই সকাল ৬:০০ টায় ১১ ফাল্গুন বহাল থাকবে।"
})

q_data.append({
    "id": 75,
    "question": "In 2024, there are months with 30 and 31 days in them. How many months will only have 28 days in them? [EGCB-ICT-24]",
    "options": ["0", "1", "1", "3"],
    "answer": "ক",
    "explanation": "2024 লিপ ইয়ার হওয়ায় ফেব্রুয়ারি ২৯ দিনের এবং কোনো মাসেই শুধুমাত্র ২৮ দিন নেই ∴ 0।"
})

print(f"Loaded {len(q_data)} questions so far.")
