import json

dig_elec_mcqs = [
  {
    "id": 1,
    "question": "Which one is complement of 100? [নিচের কোনটি ১০০ এর কমপ্লিমেন্ট] 12th BCS",
    "options": [
      "111",
      "101",
      "011",
      "001"
    ],
    "answer": "C"
  },
  {
    "id": 2,
    "question": "Which is the binary of (52)₁₆ ? [ নিচের কোনটি (52)₁₆ এর বাইনারি] 13th BCS",
    "options": [
      "01010010",
      "01110011",
      "00001100",
      "11110000"
    ],
    "answer": "A"
  },
  {
    "id": 3,
    "question": "How many bits are in BCD [BCD তে কতগুলো বিট থাকে]?",
    "options": [
      "4",
      "8",
      "12",
      "16"
    ],
    "answer": "A"
  },
  {
    "id": 4,
    "question": "Which one is not Octal number? [নিচের কোনটি অক্টাল নাম্বার নয়] 13th BCS",
    "options": [
      "91",
      "15",
      "77",
      "101"
    ],
    "answer": "A"
  },
  {
    "id": 5,
    "question": "Which is the 1's Complement of 10101111? [10101111 এর ১ এর পরিপূরক কত ?] 14th BCS",
    "options": [
      "1111 1111",
      "00000000",
      "01010000",
      "11000011"
    ],
    "answer": "C"
  },
  {
    "id": 6,
    "question": "What is the 2's complement of (12)₁₀ [(12)₁₀ এর ২ এর পরিপূরক কত ?] ?",
    "options": [
      "00001100",
      "11111100",
      "11110011",
      "11110100"
    ],
    "answer": "C"
  },
  {
    "id": 7,
    "question": "(1011)₂ + (0101)₂ কত? 16th BCS",
    "options": [
      "1100",
      "11000",
      "01100",
      "None"
    ],
    "answer": "D"
  },
  {
    "id": 8,
    "question": "What is the subsequent value of the series 1,8,F ? [1,8,F এর পরের সংখ্যা কত?]",
    "options": [
      "A",
      "B",
      "16",
      "22"
    ],
    "answer": "C"
  },
  {
    "id": 9,
    "question": "(100)₂ + (AA)₁₆ = ?",
    "options": [
      "1AA",
      "1B",
      "AF",
      "AE"
    ],
    "answer": "D"
  },
  {
    "id": 10,
    "question": "Which one is the equivalent Binary number of (B5D)₁₆ ? [(B5D)₁₆ এর বাইনারি কত ?]",
    "options": [
      "101101011101",
      "101101011100",
      "101101010101",
      "101101011001"
    ],
    "answer": "A"
  },
  {
    "id": 11,
    "question": "11100010 has a decimal value of ..... ? [11100010 এর ডেসিমেল ভ্যালু কত ?]",
    "options": [
      "252",
      "255",
      "226",
      "220"
    ],
    "answer": "C"
  },
  {
    "id": 12,
    "question": "(300)₁₀ convert into Hexadecimal, will be..... ? [(300)₁₀ এর হেক্সাডেসিমেল কত?] BPSC NE'19",
    "options": [
      "C3",
      "12C",
      "C2",
      "A2C"
    ],
    "answer": "B"
  },
  {
    "id": 13,
    "question": "Which one is Universal Gate ? [নিচের কোনটি ইউনিভার্সাল গেট ?] Mutiple Bank, BPSC",
    "options": [
      "AND",
      "XOR",
      "OR",
      "NAND"
    ],
    "answer": "D"
  },
  {
    "id": 14,
    "question": "Which gate's output is the complement of its input? [নিচের কোনটি তার ইনপুটের পূরক?]",
    "options": [
      "AND Gate",
      "OR Gate",
      "NOT Gate",
      "XOR Gate"
    ],
    "answer": "C"
  },
  {
    "id": 15,
    "question": "“একটা ইনপুট ১ হলে আউটপুট ১ হবে” নিচের কোন গেট অনুযায়ী?",
    "options": [
      "AND",
      "XOR",
      "OR",
      "NOT"
    ],
    "answer": "C"
  },
  {
    "id": 16,
    "question": "What is the fundamental building block of all digital electronic circuits?[Digital Electronics এর মূল ভিত্তি কি? ]",
    "options": [
      "Transistor",
      "Resistor",
      "Capacitor",
      "Logic Gate"
    ],
    "answer": "D"
  },
  {
    "id": 17,
    "question": "The output of a NOR gate is high (1) only when: [একটা NOR গেটের আউটপুট ১ হবে যখন ...]",
    "options": [
      "All inputs are low (0).",
      "All inputs are high (1).",
      "One input is high and the other is low.",
      "The inputs are different."
    ],
    "answer": "A"
  },
  {
    "id": 18,
    "question": "If the inputs to an XOR gate are both high (1), the output will be: [XOR গেটের ইনপুট দুইটাই ১ হলে আউটপুট হবে ...]",
    "options": [
      "1",
      "0",
      "Undefined",
      "The same as the input"
    ],
    "answer": "B"
  },
  {
    "id": 19,
    "question": "A+(A·B) সমীকরণকে সরল করলে হবে?",
    "options": [
      "A+B",
      "B",
      "A",
      "A·B"
    ],
    "answer": "C"
  },
  {
    "id": 20,
    "question": "A ইনপুটকে দুইবার কমপ্লিমেন্ট করলে আউটপুট হবে?",
    "options": [
      "A'",
      "1",
      "0",
      "A"
    ],
    "answer": "D"
  },
  {
    "id": 21,
    "question": "A+(B+C)=(A+B)+C এটা কোন সূত্র?",
    "options": [
      "Distributive Theorem",
      "Commutative Theorem",
      "Associative Theorem",
      "Absorption Theorem"
    ],
    "answer": "D"
  },
  {
    "id": 22,
    "question": "A+A এর আউটপুট কত হবে?",
    "options": [
      "1",
      "0",
      "A",
      "2A"
    ],
    "answer": "C"
  },
  {
    "id": 23,
    "question": "De Morgan's এর সূত্রানুযায়ী A + B এর বার = ?",
    "options": [
      "A'+B'",
      "A'·B",
      "A'·B'",
      "A·B'"
    ],
    "answer": "C"
  }
]

with open('JSON Data/BPSC ICT Wizard/4. Digital Electronics.json', 'w', encoding='utf-8') as f:
    json.dump(dig_elec_mcqs, f, ensure_ascii=False, indent=2)

print('Saved 4. Digital Electronics.json with', len(dig_elec_mcqs), 'MCQs')
