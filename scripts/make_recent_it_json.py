import json

recent_it_mcqs = [
  {
    "id": 1,
    "question": "নিচের কোনটি ক্লাউড কম্পিউটিং-এর প্রধান বৈশিষ্ট্য?",
    "options": [
      "অন-ডিমান্ড সেল্ফ-সার্ভিস",
      "ব্যক্তিগত ডেটা সেন্টার",
      "ফিক্সড হার্ডওয়্যার কনফিগারেশন",
      "অফলাইন অ্যাক্সেস"
    ],
    "answer": "ক"
  },
  {
    "id": 2,
    "question": "IaaS এর পূর্ণরূপ কী?",
    "options": [
      "Internet as a Service",
      "Infrastructure as a Service",
      "Information as a Service",
      "Integration as a Service"
    ],
    "answer": "খ"
  },
  {
    "id": 3,
    "question": "Gmail, Microsoft 365 কোন সার্ভিস মডেলের উদাহরণ?",
    "options": [
      "IaaS",
      "PaaS",
      "SaaS",
      "CaaS"
    ],
    "answer": "গ"
  },
  {
    "id": 4,
    "question": "অ্যাপ্লিকেশন তৈরি এবং ডেপ্লয়মেন্টের জন্য একটি প্ল্যাটফর্ম সরবরাহ করে কোনটি?",
    "options": [
      "IaaS",
      "PaaS",
      "SaaS",
      "Public Cloud"
    ],
    "answer": "খ"
  },
  {
    "id": 5,
    "question": "একাধিক ক্লাউড সরবরাহকারীর সংমিশ্রণকে কী বলা হয়?",
    "options": [
      "Public Cloud",
      "Private Cloud",
      "Hybrid Cloud",
      "Community Cloud"
    ],
    "answer": "গ"
  },
  {
    "id": 6,
    "question": "ক্লাউড মডেলের মধ্যে ব্যবহারকারীর সার্ভার এবং অপারেটিং সিস্টেমে সর্বাধিক নিয়ন্ত্রণ থাকে কোনটিতে?",
    "options": [
      "SaaS",
      "PaaS",
      "IaaS",
      "Community Cloud"
    ],
    "answer": "গ"
  },
  {
    "id": 7,
    "question": "ক্লাউড কম্পিউটিং-এ 'পে-অ্যাস-ইউ-গো' মডেলের মূল কারণ কী?",
    "options": [
      "ব্যাপক নেটওয়ার্ক অ্যাক্সেস",
      "পরিমাপ করা সার্ভিস",
      "রিসোর্স পুলিং",
      "দ্রুত স্কেলেবিলিটি"
    ],
    "answer": "খ"
  },
  {
    "id": 8,
    "question": "নিচের কোনটি ক্লাউড কম্পিউটিং-এর একটি অসুবিধা?",
    "options": [
      "খরচ হ্রাস",
      "স্কেলেবিলিটি",
      "বিক্রেতা লক-ইন",
      "স্বয়ংক্রিয় আপডেট"
    ],
    "answer": "গ"
  },
  {
    "id": 9,
    "question": "AI-এর সেই শাখা কোনটি যা কম্পিউটারকে ডেটা থেকে শেখার এবং প্রোগ্রামিং ছাড়াই ভবিষ্যদ্বাণী করার ক্ষমতা দেয়?",
    "options": [
      "ডিপ লার্নিং",
      "মেশিন লার্নিং (ML)",
      "নিউরাল নেটওয়ার্ক",
      "ন্যাচারাল ল্যাঙ্গুয়েজ প্রসেসিং"
    ],
    "answer": "খ"
  },
  {
    "id": 10,
    "question": "টিউরিং টেস্ট কী পরিমাপ করে?",
    "options": [
      "মেশিনের ডেটা স্টোরেজ ক্ষমতা",
      "মেশিনের প্রসেসিং গতি",
      "মেশিনের মানুষের মতো আচরণ করার ক্ষমতা",
      "মেশিনের প্রোগ্রামিং ভাষা বোঝার ক্ষমতা"
    ],
    "answer": "গ"
  },
  {
    "id": 11,
    "question": "Siri, Alexa এবং Google Assistant কোন ধরনের AI-এর উদাহরণ?",
    "options": [
      "Strong AI",
      "General AI",
      "Weak AI",
      "Super AI"
    ],
    "answer": "গ"
  },
  {
    "id": 12,
    "question": "মেশিন লার্নিং-এ যখন ডেটা Labeled থাকে এবং প্রত্যাশিত আউটপুট জানা থাকে, তখন তাকে কী বলে?",
    "options": [
      "Unsupervised Learning",
      "Reinforcement Learning",
      "Supervised Learning",
      "Deep Learning"
    ],
    "answer": "গ"
  },
  {
    "id": 13,
    "question": "Clustering কোন ধরনের মেশিন লার্নিং-এর প্রধান কাজ?",
    "options": [
      "Supervised Learning",
      "Reinforcement Learning",
      "Unsupervised Learning",
      "Evolutionary Learning"
    ],
    "answer": "গ"
  },
  {
    "id": 14,
    "question": "কৃত্রিম বুদ্ধিমত্তার জনক হিসেবে কাকে বিবেচনা করা হয়?",
    "options": [
      "জন ভন নিউম্যান",
      "অ্যালান টিউরিং",
      "জন ম্যাকার্থি",
      "বিল গেটস"
    ],
    "answer": "গ"
  }
]

with open('JSON Data/BPSC ICT Wizard/10. Recent IT Advancement.json', 'w', encoding='utf-8') as f:
    json.dump(recent_it_mcqs, f, ensure_ascii=False, indent=2)

print('Saved 10. Recent IT Advancement.json with', len(recent_it_mcqs), 'MCQs')
