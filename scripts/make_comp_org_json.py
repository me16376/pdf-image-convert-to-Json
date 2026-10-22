import json

comp_org_mcqs = [
  {
    "id": 1,
    "question": "How many bit register have in 8086 microprocessor? [8086 microprocessor এ কত বিট রেজিস্ট্রী রয়েছে] [BPSC ANE'19]",
    "options": [
      "4",
      "8",
      "16",
      "20"
    ],
    "answer": "C"
  },
  {
    "id": 2,
    "question": "During Arithmetic and Logic Operation, Data store in --------- [Arithmetic and Logic অপারেশনের সময় ডাটা জমা থাকে--- ] [BPSC AP’20]",
    "options": [
      "Accumulator",
      "Arithmetic Register",
      "Control Unit",
      "Logic Register"
    ],
    "answer": "A"
  },
  {
    "id": 3,
    "question": "ALU Located in Microprocessor --------- [Microprocessor এ ALU কোথায় থাকে ?] [BPSC AP’20]",
    "options": [
      "Fetch Unit",
      "Flags unit",
      "Control Unit",
      "Processing Unit"
    ],
    "answer": "D"
  },
  {
    "id": 4,
    "question": "Which Operation is faster in CPU..? [কোন অপারেশনটি ফাস্ট --] [BPSC ANE’19]",
    "options": [
      "Multiplication",
      "Addition",
      "Bitwise",
      "Division"
    ],
    "answer": "C"
  },
  {
    "id": 5,
    "question": "What is the address bit of 8 bit microprocessor? [৮ বিট মাইক্রোপ্রসেসরের Address বিট কত ?]",
    "options": [
      "4",
      "8",
      "16",
      "None"
    ],
    "answer": "C"
  },
  {
    "id": 6,
    "question": "Physical Connection between Microprocessor Memory and others Parts Called--? [মাইক্রোপ্রসেসর, মেমোরি ও অন্য পার্টসের মধ্যে ফিজিক্যাল সংযোগকে কি বলে ?] [BANK]",
    "options": [
      "Address bus",
      "Data Bus",
      "Path",
      "Hub"
    ],
    "answer": "A"
  },
  {
    "id": 7,
    "question": "Number of I/O access in 8086 Microprocessor? [ 8086 Microprocessor এ কতগুলো I/O একসেস করতে পারে----]",
    "options": [
      "2⁴",
      "2⁸",
      "2¹⁶",
      "2²⁰"
    ],
    "answer": "C"
  },
  {
    "id": 8,
    "question": "কম্পিউটারে CPU এবং মেমরি বা অন্যান্য উপাদানের মধ্যে প্রকৃত ডেটা বহন করে কোন বাস?",
    "options": [
      "অ্যাড্রেস বাস",
      "ডেটা বাস",
      "কন্ট্রোল বাস",
      "সিস্টেম বাস"
    ],
    "answer": "খ"
  },
  {
    "id": 9,
    "question": "নিচের কোন বাসটি এক-মুখী (Unidirectional) অর্থাৎ শুধুমাত্র CPU থেকে অন্যান্য উপাদানের দিকে তথ্য পাঠায়?",
    "options": [
      "ডেটা বাস",
      "অ্যাড্রেস বাস",
      "কন্ট্রোল বাস",
      "I/O বাস"
    ],
    "answer": "খ"
  },
  {
    "id": 10,
    "question": "ডেটা বাস সাধারণত দ্বি-মুখী (Bidirectional) হওয়ার কারণ কী?",
    "options": [
      "এটি শুধুমাত্র CPU-তে ডেটা পাঠায়।",
      "এটি শুধুমাত্র মেমরি অ্যাড্রেস বহন করে।",
      "এটি CPU এবং অন্যান্য অংশের মধ্যে উভয় দিকেই ডেটা আদান-প্রদান করতে পারে।",
      "এটি কন্ট্রোল সিগন্যাল বহন করে।"
    ],
    "answer": "গ"
  },
  {
    "id": 11,
    "question": "CPU যখন মেমরিতে কোনো ডেটা Read বা Write করবে, সেই কাজটি Control Bus কীভাবে নির্ধারণ করে?",
    "options": [
      "ডেটা বাসের গতি বাড়িয়ে।",
      "অ্যাড্রেস বাসের বিট সংখ্যা পরিবর্তন করে।",
      "Control Signals পাঠিয়ে",
      "প্রোগ্রাম কাউন্টারে মান পরিবর্তন করে।"
    ],
    "answer": "গ"
  },
  {
    "id": 12,
    "question": "নিচের কোনটি একটি একক চিপের মধ্যে CPU, RAM, ROM, I/O পোর্ট, টাইমার ইত্যাদি সমস্ত প্রয়োজনীয় অংশ একত্রিত করে?",
    "options": [
      "মাইক্রোকন্ট্রোলার",
      "মাইক্রোপ্রসেসর",
      "GPU",
      "ALU"
    ],
    "answer": "ক"
  },
  {
    "id": 13,
    "question": "মাইক্রোপ্রসেসর সাধারণত কোন ধরনের কাজের জন্য ব্যবহৃত হয়?",
    "options": [
      "এমবেডেড সিস্টেম নিয়ন্ত্রণ",
      "কমপ্লেক্স ডেটা প্রসেসিং ও মাল্টিটাস্কিং",
      "কম বিদ্যুৎ খরচের ডিভাইস নিয়ন্ত্রণ",
      "নির্দিষ্ট একক কাজ নিয়ন্ত্রণ"
    ],
    "answer": "খ"
  },
  {
    "id": 14,
    "question": "নিচের কোন ডিভাইস বা সিস্টেমে মাইক্রোকন্ট্রোলার ব্যবহৃত হয়?",
    "options": [
      "ল্যাপটপ",
      "স্মার্টফোন",
      "সার্ভার",
      "ওয়াশিং মেশিন"
    ],
    "answer": "ঘ"
  },
  {
    "id": 15,
    "question": "মাইক্রোপ্রসেসর এবং মাইক্রোকন্ট্রোলার-এর মধ্যে গতির পার্থক্য প্রসঙ্গে কোনটি সঠিক?",
    "options": [
      "মাইক্রোকন্ট্রোলার GHz, মাইক্রোপ্রসেসর MHz",
      "মাইক্রোপ্রসেসর উচ্চ গতি, মাইক্রোকন্ট্রোলার তুলনামূলকভাবে কম গতি",
      "উভয়ের গতি সমান।",
      "মাইক্রোকন্ট্রোলার-এর গতি শুধুমাত্র RAM-এর উপর নির্ভর করে।"
    ],
    "answer": "খ"
  },
  {
    "id": 16,
    "question": "সিপিইউ-এর অভ্যন্তরে অবস্থিত সবচেয়ে দ্রুত অ্যাক্সেসযোগ্য মেমরি কোনটি?",
    "options": [
      "RAM",
      "ROM",
      "Cache Memory",
      "রেজিস্টার"
    ],
    "answer": "ঘ"
  },
  {
    "id": 17,
    "question": "রেজিস্টারগুলো সাধারণত একাধিক কী দিয়ে গঠিত হয়?",
    "options": [
      "ট্রানজিস্টর",
      "ক্যাপাসিটর",
      "ফ্লিপ-ফ্লপ",
      "ডায়োড"
    ],
    "answer": "গ"
  }
]

with open('JSON Data/BPSC ICT Wizard/8. Computer Organization and Architecture.json', 'w', encoding='utf-8') as f:
    json.dump(comp_org_mcqs, f, ensure_ascii=False, indent=2)

print('Saved 8. Computer Organization and Architecture.json with', len(comp_org_mcqs), 'MCQs')
