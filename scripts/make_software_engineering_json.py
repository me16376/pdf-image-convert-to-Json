import json

soft_eng_mcqs = [
  {
    "id": 1,
    "question": "SDLC-এর পূর্ণরূপ কী?",
    "options": [
      "Software Design Life Cycle",
      "System Development Logic Cycle",
      "Software Development Life Cycle",
      "Standard Development Life Cycle"
    ],
    "answer": "গ"
  },
  {
    "id": 2,
    "question": "SDLC-এর প্রথম ধাপ কোনটি?",
    "options": [
      "Design",
      "Requirement Analysis",
      "Coding",
      "Testing"
    ],
    "answer": "খ"
  },
  {
    "id": 3,
    "question": "কোন ধাপে সফটওয়্যারটির আর্কিটেকচার এবং ডেটাবেস স্কিমা তৈরি করা হয়?",
    "options": [
      "Feasibility Study",
      "Design",
      "Implementation",
      "Maintenance"
    ],
    "answer": "খ"
  },
  {
    "id": 4,
    "question": "SDLC-এর কোন ধাপে সফটওয়্যারকে ত্রুটিমুক্ত (Bug-free) করা হয়?",
    "options": [
      "Coding",
      "Deployment",
      "Testing",
      "Requirement Analysis"
    ],
    "answer": "গ"
  },
  {
    "id": 5,
    "question": "SDLC-এর শেষ ধাপ কোনটি?",
    "options": [
      "Testing",
      "Maintenance",
      "Implementation",
      "Design"
    ],
    "answer": "খ"
  },
  {
    "id": 6,
    "question": "কোন মডেলটি Linear Sequential মডেল নামে পরিচিত?",
    "options": [
      "Agile Model",
      "Waterfall Model",
      "Spiral Model",
      "RAD Model"
    ],
    "answer": "খ"
  },
  {
    "id": 7,
    "question": "Waterfall মডেলের প্রধান অসুবিধা কী?",
    "options": [
      "এটি খুব বেশি সময় নেয়।",
      "এর জন্য কম ডকুমেন্টেশন প্রয়োজন।",
      "এটি পুনরাবৃত্তিমূলক নয়।",
      "পরিবর্তন দক্ষতার সাথে গ্রহণ করতে পারে না।"
    ],
    "answer": "ঘ"
  },
  {
    "id": 8,
    "question": "কোন মডেলে ঝুঁকি বিশ্লেষণ সবচেয়ে বেশি গুরুত্বপূর্ণ?",
    "options": [
      "V-Model",
      "Waterfall Model",
      "Spiral Model",
      "Prototype Model"
    ],
    "answer": "গ"
  },
  {
    "id": 9,
    "question": "কোনটি পুনরাবৃত্তিমূলক এবং Incremental ডেভেলপমেন্টের উপর জোর দেয়?",
    "options": [
      "Waterfall Model",
      "Agile Model",
      "V-Model",
      "RAD Model"
    ],
    "answer": "খ"
  },
  {
    "id": 10,
    "question": "V-মডেলের অপর নাম কী?",
    "options": [
      "Volume Model",
      "Validation Model",
      "Verification and Validation Model",
      "View Model"
    ],
    "answer": "গ"
  },
  {
    "id": 11,
    "question": "V-মডেলের প্রথম দিকে কোন কার্যক্রম সংঘটিত হয়?",
    "options": [
      "Validation",
      "Verification",
      "Testing",
      "Maintenance"
    ],
    "answer": "খ"
  },
  {
    "id": 12,
    "question": "কোনটি Agile মডেলের একটি জনপ্রিয় রূপ?",
    "options": [
      "Waterfall",
      "V-Model",
      "Scrum",
      "Spiral"
    ],
    "answer": "গ"
  },
  {
    "id": 13,
    "question": "RAD মডেলের পূর্ণরূপ কী?",
    "options": [
      "Regular Application Development",
      "Rapid Access Database",
      "Rapid Application Development",
      "Robust Application Development"
    ],
    "answer": "গ"
  },
  {
    "id": 14,
    "question": "কোন মডেলটি ক্লায়েন্টের অস্পষ্ট প্রয়োজনীয়তা এর ক্ষেত্রে সবচেয়ে উপযুক্ত?",
    "options": [
      "Waterfall Model",
      "Prototyping Model",
      "V-Model",
      "Spiral Model"
    ],
    "answer": "খ"
  },
  {
    "id": 15,
    "question": "Spiral মডেলের প্রতিটি চক্রকে কী বলা হয়?",
    "options": [
      "Phase",
      "Step",
      "Iteration or Loop",
      "Block"
    ],
    "answer": "গ"
  },
  {
    "id": 16,
    "question": "কোন মডেলটি ডিজাইন এবং কোডিং-এর ওপর কম সময় দিয়ে দ্রুত ডেলিভারির ওপর বেশি জোর দেয়?",
    "options": [
      "Waterfall",
      "RAD",
      "Spiral",
      "V-Model"
    ],
    "answer": "খ"
  },
  {
    "id": 17,
    "question": "Prototyping মডেলে তৈরি প্রথম কার্যকর সংস্করণটিকে কী বলা হয়?",
    "options": [
      "Final Product",
      "Model",
      "Prototype",
      "Alpha Version"
    ],
    "answer": "গ"
  },
  {
    "id": 18,
    "question": "কোন মডেলে টেস্টিং কার্যক্রম ডেভেলপমেন্টের সাথে সমান্তরালভাবে শুরু হয়?",
    "options": [
      "Waterfall Model",
      "V-Model",
      "RAD Model",
      "Prototyping Model"
    ],
    "answer": "খ"
  },
  {
    "id": 19,
    "question": "একটি বৃহৎ ও জটিল প্রকল্পের জন্য কোন মডেলটি সর্বাধিক উপযুক্ত?",
    "options": [
      "Waterfall",
      "Spiral",
      "RAD",
      "Prototyping"
    ],
    "answer": "খ"
  },
  {
    "id": 20,
    "question": "Agile এর মূল নীতি অনুযায়ী, সর্বোচ্চ অগ্রাধিকার কাকে দেওয়া হয়?",
    "options": [
      "কঠোর ডকুমেন্টেশনকে।",
      "সফটওয়্যারের দ্রুত ও অবিচ্ছিন্ন ডেলিভারিকে।",
      "চুক্তির আলোচনার মাধ্যমে পরিবর্তন নিয়ন্ত্রণকে।",
      "দীর্ঘমেয়াদী পরিকল্পনার অনুসরণকে।"
    ],
    "answer": "খ"
  },
  {
    "id": 21,
    "question": "টেস্টিং-এর প্রাথমিক উদ্দেশ্য কী?",
    "options": [
      "সফটওয়্যারটিকে নিখুঁত প্রমাণ করা।",
      "সফটওয়্যারটির ত্রুটি খুঁজে বের করা।",
      "সফটওয়্যারের মূল্য নির্ধারণ করা।",
      "ক্লায়েন্টকে সন্তুষ্ট করা।"
    ],
    "answer": "খ"
  },
  {
    "id": 22,
    "question": "V-মডেলে সিস্টেম টেস্টিং-এর সমান্তরাল ধাপ কোনটি?",
    "options": [
      "High-Level Design",
      "Coding",
      "Requirement Analysis",
      "Low-Level Design"
    ],
    "answer": "ক"
  },
  {
    "id": 23,
    "question": "একটি সফটওয়্যারের ভেতরের কাঠামো এবং কোড সম্পর্কে জ্ঞান রেখে যে পরীক্ষা করা হয়, তাকে কী বলে?",
    "options": [
      "Black Box Testing",
      "White Box Testing",
      "Gray Box Testing",
      "Alpha Testing"
    ],
    "answer": "খ"
  },
  {
    "id": 24,
    "question": "টেস্টিং-এর কোনটি Non-Functional Testing-এর অংশ?",
    "options": [
      "Regression Testing",
      "Unit Testing",
      "Performance Testing",
      "Smoke Testing"
    ],
    "answer": "গ"
  },
  {
    "id": 25,
    "question": "কোনো সফটওয়্যারের ক্ষুদ্রতম অংশ (যেমন ফাংশন বা মডিউল) পরীক্ষা করাকে কী বলা হয়?",
    "options": [
      "Integration Testing",
      "System Testing",
      "Unit Testing",
      "UAT Testing"
    ],
    "answer": "গ"
  },
  {
    "id": 26,
    "question": "কোনো সফটওয়্যারের পূর্ববর্তী ভার্সনে কোনো পরিবর্তন আনার পর সেটি পুরোনো কার্যকারিতাকে নষ্ট করেনি, তা নিশ্চিত করার জন্য কোন টেস্টিং করা হয়?",
    "options": [
      "System Testing",
      "Regression Testing",
      "Sanity Testing",
      "Load Testing"
    ],
    "answer": "খ"
  },
  {
    "id": 27,
    "question": "ব্ল্যাক বক্স টেস্টিং-এর একটি কৌশল কোনটি?",
    "options": [
      "Path Coverage",
      "Loop Testing",
      "Equivalence Partitioning",
      "Statement Coverage"
    ],
    "answer": "গ"
  },
  {
    "id": 28,
    "question": "অ্যাক্সেপ্টেন্স টেস্টিং-এর প্রধান রূপ কোনটি, যা ক্লায়েন্ট দ্বারা সম্পাদিত হয়?",
    "options": [
      "Alpha Testing",
      "Beta Testing",
      "User Acceptance Testing",
      "Security Testing"
    ],
    "answer": "গ"
  },
  {
    "id": 29,
    "question": " his টেস্টার যখন কোড বা ইন্টারনাল স্ট্রাকচার না জেনে শুধু সফটওয়্যারের ফাংশনালিটি পরীক্ষা করেন, তখন তাকে কী বলে?".replace(" his ", ""),
    "options": [
      "White Box Testing",
      "Black Box Testing",
      "Structure Testing",
      "Integration Testing"
    ],
    "answer": "খ"
  },
  {
    "id": 30,
    "question": "স্ট্রেস টেস্টিং কী ধরনের টেস্টিং?",
    "options": [
      "Functional Testing",
      "Non-Functional Testing",
      "Maintenance Testing",
      "Static Testing"
    ],
    "answer": "খ"
  },
  {
    "id": 31,
    "question": "একাধিক মডিউল একত্রিত হওয়ার পর তাদের মধ্যে ডেটা ফ্লো এবং ইন্টারফেস পরীক্ষা করাকে কী বলা হয়?",
    "options": [
      "Unit Testing",
      "Integration Testing",
      "System Testing",
      "UAT Testing"
    ],
    "answer": "খ"
  },
  {
    "id": 32,
    "question": "টেস্টিং-এর কোন ধাপে সফটওয়্যারটিকে বিভিন্ন ব্রাউজার, অপারেটিং সিস্টেম বা হার্ডওয়্যারে পরীক্ষা করা হয়?",
    "options": [
      "Security Testing",
      "Compatibility Testing",
      "Usability Testing",
      "Installation Testing"
    ],
    "answer": "খ"
  },
  {
    "id": 33,
    "question": "বাগ (Bug), ফল্ট (Fault) বা ডিফেক্ট (Defect) বলতে কী বোঝানো হয়?",
    "options": [
      "সফটওয়্যারটির একটি নতুন ফিচার।",
      "ডেভেলপারদের দ্বারা তৈরি করা ত্রুটি।",
      "ত্রুটি, যার কারণে এটি প্রত্যাশিত ফলাফল হয়না।",
      "টেস্টিং রিপোর্ট।"
    ],
    "answer": "গ"
  },
  {
    "id": 34,
    "question": "Alpha Testing সাধারণত কারা করেন?",
    "options": [
      "ক্লায়েন্ট বা ব্যবহারকারীরা।",
      "বাইরের টেস্টিং কোম্পানি।",
      "সফটওয়্যার ডেভেলপার বা অভ্যন্তরীণ QA দল।",
      "হ্যাকাররা।"
    ],
    "answer": "গ"
  },
  {
    "id": 35,
    "question": "টেস্টিং প্রথম থেকেই শুরু হওয়া উচিত—এই নীতিটিকে কী বলা হয়?",
    "options": [
      "Exhaustive Testing",
      "Defect Clustering",
      "Early Testing",
      "Pesticide Paradox"
    ],
    "answer": "গ"
  }
]

with open('JSON Data/BPSC ICT Wizard/5. Software Enginnering.json', 'w', encoding='utf-8') as f:
    json.dump(soft_eng_mcqs, f, ensure_ascii=False, indent=2)

print('Saved 5. Software Enginnering.json with', len(soft_eng_mcqs), 'MCQs')
