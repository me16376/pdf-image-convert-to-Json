# -*- coding: utf-8 -*-
"""
Builder for BUET Pattern Math Chapter 12: আংশিক ভগ্নাংশ
Pages 371-373, 1 Question
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

data = [
    {
        "id": 1,
        "question": "1/{(x+1)(x+3)} এর আংশিক ভগ্নাংশের মান কোনটি? [BSCPLC-CSE/EEE-24]",
        "options": [
            "1/(x+1) + 1/{2(x+3)}",
            "1/(x+1) - 1/{2(x+3)}",
            "1/{2(x+1)} - 1/{2(x+3)}",
            "1/{2(x+1)} + 1/{2(x+3)}"
        ],
        "answer": "গ",
        "explanation": "1/{(x+1)(x+3)} = A/(x+1) + B/(x+3) - - - (i)\n(i) নং কে (x+1)(x+3) দ্বারা গুণ করে, 1 = A(x+3) + B(x+1) - - - (ii)\nx = -1 হলে (ii) নং হতে, A = 1/2\nx = -3 হলে (ii) নং হতে, B = -1/2\nসুতরাং, 1/{(x+1)(x+3)} = 1/{2(x+1)} - 1/{2(x+3)} (Ans.)"
    }
]

out_dir = os.path.join("JSON Data", "BUET Patern", "Math")
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "আংশিক ভগ্নাংশ.json")

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {out_file} with {len(data)} questions.")
