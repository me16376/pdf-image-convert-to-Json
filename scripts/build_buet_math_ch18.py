# -*- coding: utf-8 -*-
import json
import os

q_data = []

# ==============================================================================
# Q1 to Q32 (Pages 428-433)
# ==============================================================================

q_data.append({
    "id": 1,
    "question": "নিচের সিরিজের ফাঁকা জায়গায় কোন সংখ্যা হবে? [47th BCS]\n243, 81, ----, 9, 3, 1",
    "options": ["3", "27", "12", "6"],
    "answer": "খ",
    "explanation": "243 ÷ 3 = 81, 81 ÷ 3 = 27, 27 ÷ 3 = 9, 9 ÷ 3 = 3, 3 ÷ 3 = 1। ∴ ফাঁকা জায়গায় 27 হবে।"
})

q_data.append({
    "id": 2,
    "question": "Seed: Sapling :: Egg: ? [47th BCS]",
    "options": ["Omlette", "Chicken", "Yolk", "Chick"],
    "answer": "d",
    "explanation": "Seed থেকে Sapling (চারাগাছ) উৎপন্ন হয়, তেমনি Egg থেকে Chick (মুরগির ছানা) উৎপন্ন হয়।"
})

q_data.append({
    "id": 3,
    "question": "MENPO অর্থ \"Lemon\" হলে NBOHP অর্থ কী? [47th BCS]",
    "options": ["Mango", "Table", "Light", "Shirt"],
    "answer": "ক",
    "explanation": "প্রতিটি অক্ষরের মান -1 করে পিছন দিকে গিয়ে গঠিত হয়েছে:\nN - 1 = M, B - 1 = A, O - 1 = N, H - 1 = G, P - 1 = O => MANGO।"
})

q_data.append({
    "id": 4,
    "question": "প্রদত্ত চিত্রে ত্রিভুজের সংখ্যা নির্ণয় করুন? [47th BCS]",
    "options": ["১৫", "১৬", "৭", "৯"],
    "answer": "খ",
    "explanation": "১টি করে ছোট ত্রিভুজ = ৬টি, ২টি করে যুক্ত ত্রিভুজ = ৩টি, ৩টি করে যুক্ত ত্রিভুজ = ৬টি, সম্পূর্ণ বড় ত্রিভুজ = ১টি। মোট ত্রিভুজ = ১৬টি।"
})

q_data.append({
    "id": 5,
    "question": "[Diagram: Three tree branch figures with leaves; 1st has 18, 12, 20 and trunk 5; 2nd has 16, 14, 30 and trunk 6; 3rd has 45, 18, 27 and trunk ?] কোনটি প্রশ্নবোধক চিহ্নের স্থলাভিষিক্ত হবে? [47th BCS]",
    "options": ["১৮", "১২", "৯", "৬"],
    "answer": "গ",
    "explanation": "(১৮ + ১২ + ২০)/১০ = ৫; (১৬ + ১৪ + ৩০)/১০ = ৬; (৪৫ + ১৮ + ২৭)/১০ = ৯। ∴ উত্তর ৯।"
})

q_data.append({
    "id": 6,
    "question": "পানিতে প্রদত্ত প্রতিচ্ছবিগুলোর সাথে কোনটি ইংরেজিতে একটি শব্দের সাথে সাদৃশ্যপূর্ণ? [47th BCS]",
    "options": ["Ⅎ∀WI⅂ʎ", "ʎ⅂IW∀Ⅎ", "ʎ⅂IM∀Ⅎ", "Ⅎ∀WI⅂⅄"],
    "answer": "ঘ",
    "explanation": "FAMILY শব্দটির পানিতে প্রতিবিম্ব হলো Ⅎ∀WI⅂⅄।"
})

q_data.append({
    "id": 7,
    "question": "একজন ব্যক্তি চার মাইল উত্তরে, ১২ মাইল পূর্বে এবং তারপরে ১২ মাইল উত্তরে ভ্রমণ করেন। তিনি শুরুর বিন্দু থেকে কত দূরে আছেন? [47th BCS]",
    "options": ["২৮ মাইল", "২৪ মাইল", "২১ মাইল", "২০ মাইল"],
    "answer": "ঘ",
    "explanation": "মোট উত্তর দূরত্ব = ৪ + ১২ = ১৬ মাইল, পূর্ব দূরত্ব = ১২ মাইল।\nদূরত্ব = √(১৬² + ১২²) = √(২৫৬ + ১৪৪) = √৪০০ = ২০ মাইল।"
})

q_data.append({
    "id": 8,
    "question": "পাঁচজন ব্যক্তি গোল হয়ে বসে আছে এবং মাঝখানে তাকিয়ে তাস খেলছে। রাজিবের বাম দিকে রয়েছে মুকুল, বিজয় রয়েছে অনিক ও নুরুলের মাঝখানে এবং অনিকের ডান দিকে। তাহলে নুরুলের ডান দিকে কে রয়েছে? [47th BCS]",
    "options": ["অনিক", "বিজয়", "মুকুল", "রাজিব"],
    "answer": "গ",
    "explanation": "নুরুলের ডান দিকে রয়েছে মুকুল।"
})

q_data.append({
    "id": 9,
    "question": "যদি A এর সাথে B খাপ খায় যেমনভাবে C, D এর সাথে তাহলে নিচের জোড়াগুলোর মধ্যে কোন জোড়া যুক্তিযুক্তভাবে খাপ খায়? [47th BCS]",
    "options": [
        "পাখিকে যেমন দৌড়াতে হয়, মাছকে তেমন সাঁতার কাটতে হয়",
        "আঁধারের বিপরীত যেমন উজ্জ্বল, তেমনি নিরবতার বিপরীত হলো উচ্চশব্দ",
        "খাদ্য যেমন খাবারের জন্য, পানি তেমনি পান করার জন্য",
        "রঙ যেমন ছায়ায়ুক্ত হয়, গতি তেমনি দ্রুত হয়"
    ],
    "answer": "গ",
    "explanation": "খাদ্য যেমন খাবারের জন্য, পানি তেমনি পান করার জন্য।"
})

q_data.append({
    "id": 10,
    "question": "হাত চোখ ও মস্তিষ্কের কার্যাবলি এতটাই যে, শৈশবকালের প্রথম দিকে হাতের ব্যবহার সম্পূর্ণ বিকাশকে ত্বরান্বিত করতে সাহায্য করে? [47th BCS]",
    "options": [
        "অপরিবর্তনীয়-বুদ্ধিসম্পর্কিত",
        "রহস্যময়-মনস্তাত্ত্বিক",
        "নিয়ন্ত্রিত-কিশোর",
        "ঘনিষ্ঠভাবে যুক্ত- প্রত্যক্ষনমূলক"
    ],
    "answer": "ঘ",
    "explanation": "হাত, চোখ ও মস্তিষ্কের কার্যাবলি যদি ঘনিষ্ঠভাবে যুক্ত হয়ে থাকে তবে শিশুর প্রত্যক্ষনমূলক বিকাশ ত্বরান্বিত হয়।"
})

q_data.append({
    "id": 11,
    "question": "নিচে উল্লেখিত শব্দগুলোর মধ্যে কোন বানানটি সঠিক খুঁজে বের করুন। [47th BCS]",
    "options": ["Randezvos", "Rendezvous", "Rondezvous", "Rendavous"],
    "answer": "খ",
    "explanation": "সঠিক বানান Rendezvous, যার অর্থ মিলনমেলা।"
})

q_data.append({
    "id": 12,
    "question": "একটি গিয়ার ট্রেনে তিনটি গিয়ার আছে, গিয়ার 'এ' এর ১২টি দাঁত, গিয়ার 'বি' এর ৩৬টি দাঁত, এবং গিয়ার 'সি' এর ২৪টি দাঁত আছে। যদি গিয়ার 'এ' কে ঘড়ির কাঁটা যেদিকে ঘোরে সেদিকে ঘোরানো হয়, তাহলে গিয়ার 'সি' কোন দিকে ঘুরবে? [47th BCS]",
    "options": [
        "ঘড়ির কাঁটার দিকে",
        "ঘড়ির কাঁটার বিপরীত দিকে",
        "স্থির",
        "একেবারে ঘুরবে না"
    ],
    "answer": "ক",
    "explanation": "গিয়ার A ঘড়ির কাঁটার দিকে ঘুরলে গিয়ার B ঘড়ির কাঁটার বিপরীত দিকে ঘুরবে এবং গিয়ার C ঘড়ির কাঁটার দিকে ঘুরবে।"
})

q_data.append({
    "id": 13,
    "question": "যখন দুটি বস্তুর সংঘর্ষ হয় এবং তারা একসাথে লেগে থাকে, তখন তাকে কোন ধরনের সংঘর্ষ বলে? [47th BCS]",
    "options": ["স্থিতিস্থাপক সংঘর্ষ", "প্লাস্টিক সংঘর্ষ", "অস্থিতিস্থাপক সংঘর্ষ", "ঘর্ষণীয় সংঘর্ষ"],
    "answer": "গ",
    "explanation": "যখন দুটি বস্তু সংঘর্ষের পর একসাথে লেগে থাকে, তখন তাকে অস্থিতিস্থাপক সংঘর্ষ বলে।"
})

q_data.append({
    "id": 14,
    "question": "নিচের ছবিগুলোর পাশের প্রশ্নবোধক চিহ্নের স্থানে কোন বিকল্পটি বসবে? [47th BCS]",
    "options": ["১", "২", "৩", "৪"],
    "answer": "গ",
    "explanation": "চিত্রের ঘূর্ণন অনুযায়ী সঠিক বিকল্পটি ৩।"
})

q_data.append({
    "id": 15,
    "question": "পৃথিবীর কক্ষপথের বিভিন্ন বিন্দু থেকে দেখলে কোন ঘটনার কারণে এটি নক্ষত্রের অবস্থানের আপাত পরিবর্তন ঘটে? [47th BCS]",
    "options": ["ডপলার ইফেক্ট", "রেডশিফট", "কসমিক", "প্যারালেক্স"],
    "answer": "ঘ",
    "explanation": "পৃথিবীর কক্ষপথের বিভিন্ন বিন্দু থেকে দেখলে নক্ষত্রের আপাত অবস্থানের পরিবর্তন ঘটে প্যারালেক্স (Parallax) ঘটনার কারণে।"
})

q_data.append({
    "id": 16,
    "question": "[Grid: 17, 8, 5, 5; 13, 7, 5, 4; 6, 12, 6, 3; 10, 6, 4, ?] প্রশ্নবোধক চিহ্নিত ঘরে কোন সংখ্যাটি বসবে? [47th BCS]",
    "options": ["৪", "৫", "৬", "৭"],
    "answer": "ক",
    "explanation": "17 + 8 = 25 = 5 × 5; 13 + 7 = 20 = 5 × 4; 6 + 12 = 18 = 6 × 3; 10 + 6 = 16 = 4 × 4 ∴ প্রশ্নবোধক স্থানে ৪ বসবে।"
})

q_data.append({
    "id": 17,
    "question": "What is the next number in the series 9, 18, 29, 42, 57, ? [BCRECL-CE, ME, EEE-25]",
    "options": ["70", "74", "64", "72"],
    "answer": "b",
    "explanation": "ব্যবধান: 18 - 9 = 9, 29 - 18 = 11, 42 - 29 = 13, 57 - 42 = 15, পরবর্তী ব্যবধান 17। ∴ 57 + 17 = 74।"
})

q_data.append({
    "id": 18,
    "question": "What is the least number should be added to 6558 so the number will be a perfect square number? [BCRECL-CE, ME, EEE-25]",
    "options": ["3", "2", "4", "None"],
    "answer": "a",
    "explanation": "81² = 6561। সুতরাং যোগ করতে হবে = 6561 - 6558 = 3।"
})

q_data.append({
    "id": 19,
    "question": "ঘড়িতে ১০.৫০ বাজলে ঘণ্টা ও মিনিটের কাঁটার মধ্যে কত ডিগ্রি কোণ তৈরি হবে? [DESCO-CT, MT, ET-25]",
    "options": ["১৫", "৩০", "২৫", "৫৫"],
    "answer": "গ",
    "explanation": "কোণ, θ = |(60H - 11M)/2| = |(60×10 - 11×50)/2| = |(600 - 550)/2| = 50/2 = 25°।"
})

q_data.append({
    "id": 20,
    "question": "একটি মাসের প্রথম দিন শুক্রবার এবং শেষ দিন শুক্রবার হলে মাসটি কত দিনের? [DESCO-CT, MT, ET-25]",
    "options": ["২৮", "২৯", "৩০", "৩১"],
    "answer": "খ",
    "explanation": "১, ৮, ১৫, ২২, ২৯ তারিখ শুক্রবার হবে। সুতরাং মাসটি ২৯ দিনের।"
})

q_data.append({
    "id": 21,
    "question": "a - c = 2 হলে abc - cba = কত? (এখানে a = 1, b = 2, c = 3 তাহলে abc = 1 2 3 এইভাবে ধরে করুন) [DESCO-CT, MT, ET-25]",
    "options": ["198", "444", "298", "200"],
    "answer": "ক",
    "explanation": "ধরি a = 3, b = 2, c = 1, তবে a - c = 2। তাহলে abc = 321 এবং cba = 123। ∴ abc - cba = 321 - 123 = 198।"
})

q_data.append({
    "id": 22,
    "question": "একটি জায়গায় ১৫টি প্রাণী (গরু, বিড়াল, কুকুর) ১০টি গরু নয়, ৮টি বিড়াল নয়, কুকুর কয়টি? [DESCO-CT, MT, ET-25]",
    "options": ["২", "৩", "৪", "১"],
    "answer": "খ",
    "explanation": "গরু নয় এমন প্রাণী = 10টি (বিড়াল + কুকুর)। ∴ গরুর সংখ্যা = 15 - 10 = 5টি। আবার বিড়াল নয় 8টি প্রাণী (কুকুর + গরু)। ∴ কুকুরের সংখ্যা = 8 - 5 = 3টি।"
})

q_data.append({
    "id": 23,
    "question": "শিশির ও তুষার সকাল বেলা মুখোমুখি দাঁড়াল। শিশিরের ছায়া তুষারের ডানে হলে শিশির কোন দিকে দাঁড়িয়েছিল? [DESCO-CT, MT, ET-25]",
    "options": [],
    "answer": "উত্তর দিকে",
    "explanation": "সকালে সূর্য পূর্বে থাকে, ছায়া পশ্চিমে পড়ে। তুষারের ডান পাশ যদি পশ্চিম হয়, তবে তুষার দক্ষিণ মুখী এবং তার মুখোমুখি শিশির উত্তর দিকে মুখ করে দাঁড়িয়েছিল।"
})

q_data.append({
    "id": 24,
    "question": "একটি আয়তক্ষেত্র ও বর্গক্ষেত্র সর্বোচ্চ কয়টি বিন্দুতে ছেদ করবে? [DESCO-CT, MT, ET-25]",
    "options": ["৪", "৬", "৮", "২"],
    "answer": "ক",
    "explanation": "একটি আয়তক্ষেত্র এবং একটি বর্গক্ষেত্র পরস্পরকে সর্বোচ্চ ৪টি বিন্দুতে ছেদ করতে পারে।"
})

q_data.append({
    "id": 25,
    "question": "একটি কেক-কে ৪টি সরলরেখা দ্বারা কাটলে সর্বোচ্চ কয়টি টুকরা হবে? [DESCO-CT, MT, ET-25]",
    "options": ["১০", "১৫", "১১", "১৩"],
    "answer": "গ",
    "explanation": "সর্বোচ্চ টুকরা সংখ্যা = n(n + 1)/2 + 1 = 4(5)/2 + 1 = 10 + 1 = 11টি।"
})

q_data.append({
    "id": 26,
    "question": "R এবং J একটি সারিতে আছে যেখানে R এর ডানে ৩য় সিটে J বসেছে। R ডান পাশ থেকে 6th এবং বামপাশ থেকে 10th হলে ডান থেকে J কত নং সিটে আছে? [DESCO-CT, MT, ET-25]",
    "options": ["৩য়", "৫ম", "৬ষ্ঠ", "১০ম"],
    "answer": "ক",
    "explanation": "R ডান দিক থেকে ৬ নং সিটে। যেহেতু J, R-এর ডানদিকে ৩য় সিটে আছে, তাই J ডান প্রান্তের আরও কাছে থাকবে। সুতরাং ডান দিক থেকে গণনা করলে J-এর অবস্থান হবে ৬ - ৩ = ৩য়।"
})

q_data.append({
    "id": 27,
    "question": "If the word BATHE is coded as 23541. What is the code for the word TEA? [RNPL-ME,EEE-25]",
    "options": ["123", "415", "513", "153"],
    "answer": "c",
    "explanation": "B=2, A=3, T=5, H=4, E=1। ∴ TEA = 513।"
})

q_data.append({
    "id": 28,
    "question": "Which word best fits with hours, minutes, seconds? [RNPL-ME,EEE-25]",
    "options": ["year", "month", "week", "day"],
    "answer": "d",
    "explanation": "Day is composed of hours, minutes, and seconds."
})

q_data.append({
    "id": 29,
    "question": "How many times does the digit 9 appear when writing all the numbers from 0 to 99? [RNPL-ME,EEE-25]",
    "options": ["21", "19", "22", "20"],
    "answer": "d",
    "explanation": "9, 19, 29, 39, 49, 59, 69, 79, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99 এ মোট ২০ বার digit 9 আসে।"
})

q_data.append({
    "id": 30,
    "question": "How many triangles are there in the below diagram? [RNPL-ME,EEE-25]",
    "options": ["10", "12", "14", "8"],
    "answer": "b",
    "explanation": "প্রদত্ত চিত্রে মোট ১২টি ত্রিভুজ রয়েছে।"
})

q_data.append({
    "id": 31,
    "question": "In a MCQ exam there are 80 questions, a correct answer gives 1 marks but a wrong answer deduct 0.25 marks and if a question is not attempted there is no deduction in marks. If a student attempted 75% the question and got 45 marks, then how many questions did he answer incorrectly? [RNPL-ME,EEE-25]",
    "options": [],
    "answer": "12",
    "explanation": "Number of answered questions = 75% of 80 = 60. Total marks obtained = 45. Difference = 60 - 45 = 15. Net loss per wrong answer = 1 + 0.25 = 1.25 marks. ∴ Number of wrong answer = 15/1.25 = 12 (Ans.)"
})

q_data.append({
    "id": 32,
    "question": "How many ways are there to divide 50 people into 3 groups so that each group contains members equal to a prime number? [RNPL-ME, EEE-25]",
    "options": [],
    "answer": "5 ways",
    "explanation": "The sum of 3 prime numbers is 50. Since 50 is even, one prime must be 2. The other two must sum to 48: (5, 43), (7, 41), (11, 37), (17, 31), (19, 29). There are 5 ways."
})

print(f"Loaded {len(q_data)} questions so far.")
