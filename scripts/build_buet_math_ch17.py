# -*- coding: utf-8 -*-
"""
Builder for BUET Pattern Math Chapter 17: ম্যাট্রিক্স ও নির্ণায়ক
Pages: 425 - 427
Total Questions: 1
"""

import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

questions = [
    {
        "id": 1,
        "question": "What are eigen values of the following 2×2 matrix [[2, -1], [-4, 5]]? [LPGL-ME-25]",
        "options": [
            "-1 and 1",
            "1 and 6",
            "2 and 5",
            "4 and -1"
        ],
        "answer": "b",
        "explanation": "ব্যাখ্যাঃ\nLet, A = [[2, -1], [-4, 5]]\n|A - λI| = 0\n⇒ |2 - λ    -1|\n  |-4    5 - λ| = 0\n⇒ (2 - λ)(5 - λ) - (-1 × -4) = 0\n⇒ 10 - 7λ + λ² - 4 = 0\n⇒ λ² - 7λ + 6 = 0\n⇒ (λ - 1)(λ - 6) = 0\n∴ λ = 1, 6 (Ans.)"
    }
]

out_dir = r"JSON Data\BUET Patern\Math"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "ম্যাট্রিক্স ও নির্ণায়ক.json")

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Saved {len(questions)} questions to {out_path}")
