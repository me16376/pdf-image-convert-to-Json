# -*- coding: utf-8 -*-
import json
import os

from build_buet_math_ch18_part3 import q_data

# ==============================================================================
# Q116 to Q148 (Pages 448-453)
# ==============================================================================

q_data.append({
    "id": 116,
    "question": "1  2  3\n1  4  9\n2  ?  12\n[DESCO-ME-19]",
    "options": ["6", "5", "8", "10"],
    "answer": "a",
    "explanation": "পূর্ববর্তী সংখ্যা যোগ করে পরবর্তী সংখ্যা হবে। সুতরাং ২ এবং ৪ যোগ করে ৬ হবে।"
})

q_data.append({
    "id": 117,
    "question": "A man is standing in front of a painting man. The man says, Brothers and sisters I have none and the man's father is my father's son. How the related the man to the painting man. [B-R Power-ME-19]",
    "options": ["His son", "His father", "His Nephew", "His uncle"],
    "answer": "a",
    "explanation": "ছবির মানুষকে বলছে যে, তার বাবা আমার বাবার পুত্র। যেহেতু তার আর কোন ভাই বা বোন নেই। তাই ছবির লোকটি তার পুত্র।"
})

q_data.append({
    "id": 118,
    "question": "What number will be for question mark? [Diagram with 3 circles: 50 with 16, 26; 25 with 8, 13; ? with 32, 52] [B-R Power-ME-19]",
    "options": ["48", "40", "86", "26"],
    "answer": "c",
    "explanation": "16 + 26 = 42 + 8 = 50; 13 + 8 = 21 + 4 = 25; 32 + 52 = 84 + 2 = 86 (Ans: 86)"
})

q_data.append({
    "id": 119,
    "question": "A woman walking with a boy meets another woman and on being asked her relationship with the boy, she says, 'My maternal uncle and his maternal uncle's maternal uncle are brothers.' How is the boy related to the woman? [APSCL-ME-19]",
    "options": ["Nephew", "Brother-in-law", "Son", "Grandson"],
    "answer": "c",
    "explanation": "মহিলাটি সঙ্গে থাকা ছেলের উদ্দেশ্য বলছে যে, আমার মামা এবং তার মামার মামা পরস্পর ভাই। সুতরাং ছেলেটি তার সন্তান।"
})

q_data.append({
    "id": 120,
    "question": "In a room there are some birds and cats. There are total 50 legs and 15 heads in that room. How many cats were there? [APSCL-ME-19]",
    "options": ["30", "20", "10", "10"],
    "answer": "c",
    "explanation": "15 টি মাথা এবং 50 টি পা আছে। পাখির পা থাকে 2 টি করে। বিড়ালের পা থাকে 4 টি করে। মনে করি, বিড়ালের সংখ্যা = 10 টি, পাখির সংখ্যা = 5 টি। বিড়ালের পা = 4 × 10 = 40, পাখির পা = 2 × 5 = 10, মোট 50 টি পা। সুতরাং 10 টি বিড়াল আছে।"
})

q_data.append({
    "id": 121,
    "question": "29th February 2016 Rahim celebrated his 16th birthday. In which year he was born. [APSCL-ME-19]",
    "options": [],
    "answer": "29, Feb, 2000",
    "explanation": "29 Feb. 2016 -> 15th birthday, ∴ সে জন্মগ্রহণ করেছে = 29 Feb, 2001 (অথবা লিপ ইয়ার হিসাব অনুযায়ী ২০০০)।"
})

q_data.append({
    "id": 122,
    "question": "A workman starts his work on Monday works for 8 days and takes every 9th day as his holiday. His 12th holiday will fall on? [APSCL-ME-19]",
    "options": ["Monday", "Tuesday", "Wednesday", "Friday"],
    "answer": "c",
    "explanation": "1st day -> Monday, 8th day -> Monday, 9th day -> Tuesday (Holiday)। 12th holiday is = 9 × 12 = 108 ÷ 7 সুতরাং ভাগশেষ = 3। সুতরাং, Monday প্রথম দিন হলে ৩য় দিন হবে Wednesday (Ans.)"
})

q_data.append({
    "id": 123,
    "question": "Choose the missing terms out of the given alternatives: AZ, GT, MN, ?, YB [DPDC-19]",
    "options": ["JH", "SH", "SK", "TS"],
    "answer": "b",
    "explanation": "First letters: A -> G(+6), G -> M(+6), M -> S(+6), S -> Y(+6); Second letters: Z -> T(-6), T -> N(-6), N -> H(-6), H -> B(-6) ∴ SH (Ans.)"
})

q_data.append({
    "id": 124,
    "question": "B is lighter than A. D is heavier than B but lighter than A. C is heavier than A. Who is the lightest? [APSCL-19]",
    "options": ["A", "B", "C", "D"],
    "answer": "b",
    "explanation": "B < A, B < D, D < A, A < C সুতরাং B সবচেয়ে হালকা (Ans.)"
})

q_data.append({
    "id": 125,
    "question": "B is stronger than C, C is stronger than A, D is stronger than B, E is stronger than D. Who is stronger? [APSCL-19]",
    "options": ["B", "C", "D", "E"],
    "answer": "d",
    "explanation": "B > C, C > A, D > B, E > D সুতরাং E সবচেয়ে শক্তিশালী।"
})

q_data.append({
    "id": 126,
    "question": "A man from point A starts his journey goes 1 km north. He turns 2 km east, then 3 km south, from that point he goes 4km west, finally 2 km north and reaches point B. Minimum distance between A and B. [B-R Power-ME-19]",
    "options": ["4 km", "1 km", "2 km", "3 km"],
    "answer": "c",
    "explanation": "A to B = 2 km (Ans.)"
})

q_data.append({
    "id": 127,
    "question": "11 (r - 1) = 13 (s - 1); r + s ? [DESCO-ME-19]",
    "options": ["89", "26", "86", "91"],
    "answer": "b",
    "explanation": "যেহেতু সমীকরণটির দুইপাশ সমান, তাই বামপাশে 11 এর সাথে গুণ আকারে 13 আনতে হবে আর ডানপাশে 13 এর সাথে গুণ আকারে 11 আনতে হবে। তাই r - 1 = 13 ∴ r = 14 এবং s - 1 = 11 ∴ s = 12 অতএব r + s = 14 + 12 = 26 (Ans.)"
})

q_data.append({
    "id": 128,
    "question": "যদি 'ক' এবং 'খ' উভয়ই জোড় সংখ্যা হয়, তাহলে নিচের কোনটি অবশ্যই বিজোড় সংখ্যা হবে? [BADC-CT-18]",
    "options": ["ক + ২ খ", "কখ + ১", "ক + খ", "২ ক + খ"],
    "answer": "খ",
    "explanation": "জোড় সংখ্যার সাথে জোড় গুন করলে জোড় সংখ্যাই হবে এবং এর সাথে ১ যোগ করলে বিজোড় সংখ্যাই হবে। সঠিক উত্তর (খ)।"
})

q_data.append({
    "id": 129,
    "question": "A is lighter than B. C is lighter than B. D is heavier than B and E is heavier than D. Who is the heaviest? [NWPGCL-ME-18]",
    "options": ["E", "B", "C", "D"],
    "answer": "a",
    "explanation": "A < B, C < B, B < D, D < E সুতরাং E সবচেয়ে ভারি।"
})

q_data.append({
    "id": 130,
    "question": "Neela's age was 15 years and 11 months at 11th November 2006. Her birthday was - [BPDB-ME-16]",
    "options": [],
    "answer": "11-12-1990",
    "explanation": "11th November 2006 থেকে 15 বছর 11 মাস বিয়োগ করলে জন্মদিন দাঁড়ায় 11-12-1990।"
})

q_data.append({
    "id": 131,
    "question": "একটি ঘড়ির ঘণ্টার কাঁটা ও মিনিটের কাঁটা ঘণ্টায় কতবার সমকোণে থাকবে? [BR Power-PT-21]",
    "options": [],
    "answer": "২ বার",
    "explanation": "ঘণ্টা ও মিনিটের কাঁটা ঘণ্টায় ২ বার সমকোণে থাকে।"
})

q_data.append({
    "id": 132,
    "question": "How many degrees are between the hands of a clock at 3 : 30? [APSCL-CE-20]",
    "options": ["75°", "90°", "105°", "70°"],
    "answer": "a",
    "explanation": "Angle, θ = |(60H - 11M)/2| = |(60×3 - 11×30)/2| = 75° (Ans.)"
})

q_data.append({
    "id": 133,
    "question": "A clock is started at noon by 10 minutes past 5, the hour hand has turned through angle of - [DPDC-19, EGCB-ME-20]",
    "options": ["120°", "150°", "155°", "180°"],
    "answer": "c",
    "explanation": "At noon অর্থ 12:00 PM। 12 টা হতে 5 টা 10 মিনিট পর্যন্ত ঘণ্টার কাটা ঘুরছে 5 ঘণ্টা 10 মিনিট। ঘণ্টার কাঁটার ক্ষেত্রে, 60 মিনিট = 30° সুতরাং, 1 ঘণ্টা = 30°, বা, 1 মিনিট = 1/2° ∴ 5 ঘণ্টা 10 মিনিটে = (5 × 30) + (10 × 1/2) = 155° (Ans.)"
})

q_data.append({
    "id": 134,
    "question": "ঘড়িতে যখন ৮ টা বাজে তখন ঘণ্টা ও মিনিটের কাঁটার মধ্যবর্তী কোণ কত হবে? [BR Power-PT-21, BCS -39th]",
    "options": ["140°", "160°", "120°", "110°"],
    "answer": "গ",
    "explanation": "θ = |(60H - 11M)/2| = |(60×8 - 11×0)/2| = 240° ∴ প্রকৃতকোণ = 360 - 240 = 120° (Ans.) অথবা, প্রত্যেক ঘণ্টার angle = 360/12 = 30° ∴ 8 বাজলে ঘণ্টা ও মিনিটের মধ্যে angle = 30° × 4 = 120°"
})

q_data.append({
    "id": 135,
    "question": "দেয়াল ঘড়িতে রাত নয়টা বাজে। ঘণ্টা ও মিনিটের কাঁটার মধ্যকার কোনটির মাপ কত? [BEPZA-CE-16]",
    "options": ["90°", "150°", "120°", "110°"],
    "answer": "ক",
    "explanation": "θ = |(60H - 11M)/2| = |(60×9 - 11×0)/2| = 270° ∴ প্রকৃতকোণ = 360 - 270 = 90°।"
})

q_data.append({
    "id": 136,
    "question": "City B is 8 miles east of city A. City C is 6 miles north of city B. City D is 16 miles east of city C and city E is 12 miles north of city D. What is the distance from city A to city E? [NESCO-CE-18]",
    "options": ["10 miles", "20 miles", "24 miles", "30 miles"],
    "answer": "d",
    "explanation": "AE = √((6 + 12)² + (8 + 16)²) = √(18² + 24²) = 30 miles (Ans.)"
})

q_data.append({
    "id": 137,
    "question": "একজন লোক উত্তর-পশ্চিম দিকে মুখ করে আছে। সে ঘড়ির কাঁটার দিকে ৯০° ঘুরে, তারপর ঘড়ির কাঁটার বিপরীত দিকে ১৮০° ঘুরে এবং তারপর একই দিকে আরো ৯০° ঘুরে। এখন সে কোন দিকে মুখ করে আছে? [46th BCS]",
    "options": ["দক্ষিণ", "দক্ষিণ-পশ্চিম", "দক্ষিণ-পূর্ব", "পূর্ব"],
    "answer": "গ",
    "explanation": "ঘড়ির কাঁটার দিকে ৯০°, বিপরীত দিকে ১৮০° + ৯০° = ২৭০°। নেট ১৮০° বিপরীত দিকে ঘূর্ণন, সুতরাং উত্তর-পশ্চিমের বিপরীতে দক্ষিণ-পূর্ব দিক।"
})

q_data.append({
    "id": 138,
    "question": "নিম্নের শব্দগুলো অভিধানে যে ক্রমে আছে সেভাবে সাজান- 1. Protect 2. Pragmatic 3. Pastel 4. Postal 5. Pebble [46th BCS]",
    "options": ["43521", "35421", "34512", "43512"],
    "answer": "খ",
    "explanation": "অভিধান অনুযায়ী, Pastel (3) -> Pebble (5) -> Postal (4) -> Pragmatic (2) -> Protect (1) ∴ 35421 (Ans.)"
})

q_data.append({
    "id": 139,
    "question": "একটি ছবিতে একজন পুরুষের দিকে ইঙ্গিত করে একজন মহিলা বলেন, “তার ভাইয়ের বাবা আমার দাদার একমাত্র ছেলে।” ছবির পুরুষের সঙ্গে উক্ত মহিলার সম্পর্ক কী? [46th BCS]",
    "options": ["মা", "খালা", "বোন", "কন্যা"],
    "answer": "গ",
    "explanation": "মহিলা ও সেই পুরুষ হল ভাই-বোন। সুতরাং ছবির পুরুষের সাথে মহিলার সম্পর্ক বোন।"
})

q_data.append({
    "id": 140,
    "question": "যদি E = 10, J = 20, O = 30 এবং T = 40 হয়, তাহলে B + E + S + T = ? [46th BCS]",
    "options": ["71", "82", "90", "92"],
    "answer": "ঘ",
    "explanation": "Here, E = 5 × 2 = 10, J = 10 × 2 = 20, O = 15 × 2 = 30, T = 20 × 2 = 40. ∴ B = 2 × 2 = 4, E = 5 × 2 = 10, S = 19 × 2 = 38, T = 20 × 2 = 40 ∴ B + E + S + T = (4 + 10 + 38 + 40) = 92 (Ans.)"
})

q_data.append({
    "id": 141,
    "question": "নিচের কোন শব্দটি অন্যদের থেকে আলাদা? [46th BCS]",
    "options": ["kiwi", "Eagle", "Emu", "Ostrich"],
    "answer": "খ",
    "explanation": "প্রদত্ত অপশনে- kiwi, Emu, Ostrich পাখি গুলো উড়তে পারে না। অপরদিকে Eagle উড়তে পারে তাই Eagle আলাদা।"
})

q_data.append({
    "id": 142,
    "question": "একজন মহিলা বলেছেন, “আপনি যদি আমার নিজের বয়সকে উল্টে দেন তাহলে তা আমার স্বামীর বয়সকে নির্দেশ করে। তিনি আমার থেকে বয়সে বড় এবং আমাদের বয়সের পার্থক্য আমাদের বয়সের যোগফলের এগারো ভাগের একভাগ।” মহিলার বয়স কত? [46th BCS]",
    "options": ["২৩ বছর", "৩৪ বছর", "৪৫ বছর", "কোনটিই নয়"],
    "answer": "গ",
    "explanation": "অপশন থেকে পাই, মহিলার বয়স = ৪৫ বছর ∴ স্বামীর বয়স = ৫৪ বছর ∴ পার্থক্য = ৯ বছর। তাদের বয়সের যোগফল = (৪৫ + ৫৪) = ৯৯ বছর। এগারো (১১) ভাগের একভাগ = ৯৯/১১ = ৯ বছর ∴ মহিলার বয়স = ৪৫ বছর।"
})

q_data.append({
    "id": 143,
    "question": "যদি একটি কামান থেকে নিম্নলিখিত ৪ টি বস্তুকে অনুভূমিক ভাবে নিক্ষেপ করা হয়, তবে কোনটি সবচেয়ে বেশি দূরে উড়ে যাবে? [46th BCS]",
    "options": ["[আয়তাকার বস্তু]", "[সিলিন্ডার আকৃতির বস্তু]", "[গোলাকার বস্তু]", "[কৌণিক বস্তু]"],
    "answer": "গ",
    "explanation": "Aerodynamics-এর নিয়ম অনুযায়ী, যে বস্তুর Drag of Co-efficient কম সে বস্তু বাতাসে বা যেকোন Fluid এর বাধা অতিক্রম করে খুব সহজেই বেশি দূরত্ব অতিক্রম করবে। প্রদত্ত অপশনের গোলাকৃতি বস্তুর Drag Co-efficient সবচেয়ে কম।"
})

q_data.append({
    "id": 144,
    "question": "সেই জুটি নির্বাচন করুন যা “Children : pediatrician” জুটির মধ্যে প্রকাশিত সম্পর্কটির মতো একটি সম্পর্ককে সর্বোত্তমভাবে প্রকাশ করে। [46th BCS]",
    "options": ["Adult : Orthopedist", "Kidney : Nephrologist", "Females : Gynecologist", "Skin : Darmatologist"],
    "answer": "গ",
    "explanation": "শিশুদের চিকিৎসার জন্য - শিশুরোগ বিশেষজ্ঞ (Pediatrician), অনুরূপভাবে মহিলাদের চিকিৎসার জন্য - স্ত্রীরোগ বিশেষজ্ঞ (Gynecologist) অর্থাৎ উভয়দিকে person এর সাথে related হবে।"
})

q_data.append({
    "id": 145,
    "question": "[চিত্র: ৩x৩ গ্রিড প্যাটার্ন ক্রম] কোন চিত্রটি সিরিজটি সম্পূর্ণ করে? [46th BCS]",
    "options": ["[চিত্র ক]", "[চিত্র খ]", "[চিত্র গ]", "[চিত্র ঘ]"],
    "answer": "ক",
    "explanation": "প্যাটার্ন ঘূর্ণন ও শেডিং অনুযায়ী চিত্র (ক) সিরিজটি পূর্ণ করে।"
})

q_data.append({
    "id": 146,
    "question": "[Diagram: Triangles with sides 4, 8, base 9, center 108; sides 5, 4, base 12, center ?] নিম্নের প্রশ্নবোধক চিহ্নে কোন সংখ্যাটি বসবে? [46th BCS]",
    "options": ["৮০", "১১৪", "১০৮", "কোনটিই নয়"],
    "answer": "গ",
    "explanation": "চিত্র-০১: ৪ + ৮ = ১২ & ১২ × ৯ = ১০৮; চিত্র-০২: ৫ + ৪ = ৯ & ৯ × ১২ = ১০৮ ∴ ১০৮ (Ans.)"
})

q_data.append({
    "id": 147,
    "question": "সঠিক বানান কোনটি, চিহ্নিত করুন। [46th BCS]",
    "options": ["Conscicncious", "Conscienctious", "Consciencitious", "Conscientious"],
    "answer": "ঘ",
    "explanation": "Conscientious অর্থ ন্যায়বান, বিবেকবান।"
})

q_data.append({
    "id": 148,
    "question": "'Ubiquitous' [46th BCS]",
    "options": ["Scarce", "Abundant", "Widespread", "Limited"],
    "answer": "গ",
    "explanation": "Ubiquitous অর্থ সর্বব্যাপী; Widespread- বিস্তৃত; Scarce- দুর্লভ; Abundant- প্রচুর; Limited- সীমিত। সুতরাং ubiquitous এর সমার্থক Widespread।"
})

# ==============================================================================
# Save final Chapter 18 JSON
# ==============================================================================

out_path = os.path.join("JSON Data", "BUET Patern", "Math", "মানসিক দক্ষতা.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(q_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated Chapter 18 JSON with {len(q_data)} MCQs!")
