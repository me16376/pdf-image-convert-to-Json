import json

# Questions 1 to 50 from pages 10-13, and Questions 1 to 21 from pages 20-21
with open('JSON Data/Ict-wizard-NTRCA-313-and-325/অধ্যায়- ক. কম্পিউটার বেসিক.json', encoding='utf-8') as f:
    ref_data = json.load(f)

# Questions 1-50
fundamental_mcqs = []
for i in range(50):
    item = ref_data[i]
    fundamental_mcqs.append({
        "id": i + 1,
        "question": item["question"],
        "options": item["options"],
        "answer": item["answer"]
    })

# Questions 51-71 corresponding to Page 20 Q1-14 and Page 21 Q15-21
# Map to exact items in ref_data
# Page 20 Q1 -> ref_data index 50 (id 51: নিচের কোনটি আউটপুট ডিভাইস নয়?)
# Page 20 Q2 -> ref_data index 52 (id 53: হার্ড কপি প্রস্তুত করতে নিচের কোন ডিভাইসটি ব্যবহৃত হয়?)
# Page 20 Q3 -> ref_data index 53 (id 54: কোন ডিভাইসের মাধ্যমে ডেটা কম্পিউটারে প্রবেশ করানো হয়?)
# Page 20 Q4 -> ref_data index 54 (id 55: OMR-এর পূর্ণরূপ কী?)
# Page 20 Q5 -> ref_data index 55 (id 56: নিচের কোনটি একটি পয়েন্টটিং ডিভাইস?)
# Page 20 Q6 -> ref_data index 56 (id 57: MICR সাধারণত কোন ক্ষেত্রে ব্যবহৃত হয়?)
# Page 20 Q7 -> ref_data index 57 (id 58: কোন প্রিন্টারটি ইমপ্যাক্ট প্রিন্টারের উদাহরণ?)
# Page 20 Q8 -> ref_data index 58 (id 59: প্লটারের প্রধান ব্যবহার কীসের জন্য?)
# Page 20 Q9 -> ref_data index 59 (id 60: প্রতি ইঞ্চিতে ডটের সংখ্যা দ্বারা...)
# Page 20 Q10 -> ref_data index 60 (id 61: নিচের কোন ডিভাইসটি সফট কপিকে...)
# Page 20 Q11 -> ref_data index 61 (id 62: নিচের কোনটি ইনপুট এবং আউটপুট উভয় ডিভাইস হিসেবে ব্যবহৃত হয়?)
# Page 20 Q12 -> ref_data index 62 (id 63: কম্পিউটার পরিচালনার জন্য আবশ্যকীয় প্রোগ্রামকে কী বলা হয়?)
# Page 20 Q13 -> ref_data index 63 (id 64: নিচের কোনটি একটি অপারেটিং সিস্টেম নয়?)
# Page 20 Q14 -> ref_data index 64 (id 65: MS Word কী ধরনের সফটওয়্যার?)
# Page 21 Q15 -> ref_data index 65 (id 66: মেমরি ম্যানেজমেন্ট, ফাইল ম্যানেজমেন্ট...)
# Page 21 Q16 -> ref_data index 66 (id 67: নিচের কোনটি ডেটাবেজ সফটওয়্যারের উদাহরণ?)
# Page 21 Q17 -> ref_data index 67 (id 68: অ্যান্টিভাইরাস সফটওয়্যার কোন ধরনের سافٹওয়্যারের উদাহরণ?)
# Page 21 Q18 -> ref_data index 67 (id 69: GUI-এর মাধ্যমে নির্দেশ গ্রহণ করে কোনটি?)
# Page 21 Q19 -> ref_data index 69 (id 70: ব্যবহারকারীর নির্দিষ্ট প্রয়োজন পূরণের জন্য তৈরি سافٹওয়্যার কোনটি?)
# Page 21 Q20 -> ref_data index 70 (id 71: MS Excel হলো একটি -)
# Page 21 Q21 -> ref_data index 71 (id 72: অপারেটিং সিস্টেম কম্পিউটার চালু করার সময় सर्वप्रथम কোন কাজটি করে?)

page20_21_indices = [50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]

for idx in page20_21_indices:
    item = ref_data[idx]
    fundamental_mcqs.append({
        "id": len(fundamental_mcqs) + 1,
        "question": item["question"],
        "options": item["options"],
        "answer": item["answer"]
    })

# Exact updates matching original text on page 20 & 21
# Q53: কোন ডিভাইসটির মাধ্যমে ডেটা ও ইনস্ট্রাকশন কম্পিউটারে প্রবেশ করানো হয়?
fundamental_mcqs[52]["question"] = "কোন ডিভাইসটির মাধ্যমে ডেটা ও ইনস্ট্রাকশন কম্পিউটারে প্রবেশ করানো হয়?"
# Q57: কোন প্রিন্টারটি ইমপ্যাক্ট (Impact) প্রিন্টারের উদাহরণ?
fundamental_mcqs[56]["question"] = "কোন প্রিন্টারটি ইমপ্যাক্ট (Impact) প্রিন্টারের উদাহরণ?"
# Q59: প্রতি ইঞ্চিতে ডটের সংখ্যা (DPI) দ্বারা কোনটির রেজোলিউশন পরিমাপ করা হয়?
fundamental_mcqs[58]["question"] = "প্রতি ইঞ্চিতে ডটের সংখ্যা (DPI) দ্বারা কোনটির রেজোলিউশন পরিমাপ করা হয়?"
# Q68: গ্রাফিক্যাল ইউজার ইন্টারফেস (GUI)-এর মাধ্যমে নির্দেশ গ্রহণ করে কোনটি?
fundamental_mcqs[67]["question"] = "গ্রাফিক্যাল ইউজার ইন্টারফেস (GUI)-এর মাধ্যমে নির্দেশ গ্রহণ করে কোনটি?"

with open('JSON Data/BPSC ICT Wizard/1. Compter Fundamental.json', 'w', encoding='utf-8') as f:
    json.dump(fundamental_mcqs, f, ensure_ascii=False, indent=2)

print('Saved 1. Compter Fundamental.json with', len(fundamental_mcqs), 'MCQs')
