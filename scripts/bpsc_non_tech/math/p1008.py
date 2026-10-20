# scripts/bpsc_non_tech/math/p1008.py

PAGE_NUM = 1008

QUESTIONS = [
    {
        "id": 40,
        "page": PAGE_NUM,
        "question": "How many linear factors of 8 + 4x + 6x² + 3x³ - 2x⁴ - x⁵ have? [BB-2026]",
        "options": [
            "0",
            "1",
            "2",
            "3"
        ],
        "answer": "ঘ",
        "explanation": "8 + 4x + 6x² + 3x³ - 2x⁴ - x⁵\n= -(x⁵ + 2x⁴ - 3x³ - 6x² - 4x - 8)\n= -{x⁴(x + 2) - 3x²(x + 2) - 4(x + 2)}\n= -(x + 2)(x⁴ - 3x² - 4)\n= -(x + 2)(x⁴ - 4x² + x² - 4)\n= -(x + 2){x²(x² - 4) + 1(x² - 4)}\n= -(x + 2)(x² - 4)(x² + 1)\n= -(x + 2)(x + 2)(x - 2)(x² + 1)\nSo liner factor 3 (Ans.)"
    },
    {
        "id": 41,
        "page": PAGE_NUM,
        "question": "The factors of 4x⁴ + 1 is— [BB-2026]",
        "options": [
            "(2x² + 2x - 1)(2x² - 2x + 1)",
            "(2x² + 2x + 1)(2x² - 2x - 1)",
            "(2x² + 2x - 1)(2x² - 2x - 1)",
            "(2x² + 2x + 1)(2x² - 2x + 1)"
        ],
        "answer": "ঘ",
        "explanation": "4x⁴ + 1\n= (2x²)² + (1)²\n= (2x² + 1)² - 2.2x².1\n= (2x² + 1)² - 4x²\n= (2x² + 1)² - (2x)²\n= (2x² + 1 + 2x)(2x² + 2 - 2x)\n= (2x² + 2x + 1)(2x² - 2x + 1) (Ans.)"
    },
    {
        "id": 42,
        "page": PAGE_NUM,
        "question": "A train 220 m long is moving at 45 km/h. The time taken by the train to cross a tunnel 260 m long, is - [BB-2026]",
        "options": [
            "25.4 sec",
            "35.4 sec",
            "38.4 sec",
            "40.4 sec"
        ],
        "answer": "গ",
        "explanation": "Total distance covered by train = (220 + 260)m = 480m\nNow, 45km/h = 45 × 5/18 m/s = 25/2 m/s\nSo, Taken the time to cross a tunnel\n= 480 / (25/2)\n= 480 × 2/25\n= 38.4 Sec (Ans.)"
    },
    {
        "id": 43,
        "page": PAGE_NUM,
        "question": "Two trucks 300 km away are travelling towards each other with a constant speed. Truck A is moving at a constant 70 km/h while Truck B is moving at a constant speed 50 km/h. How long does it take for them to meet? [BB-2026]",
        "options": [
            "5 hrs",
            "3 hrs",
            "2.5 hrs",
            "6 hrs"
        ],
        "answer": "গ",
        "explanation": "Relative Speed of two trucks in\n= (70 + 50) kmh⁻¹\n= 120 km/h\nSo, Time taken to meet = 300 / 120 = 2.5 hrs (Ans.)"
    },
    {
        "id": 44,
        "page": PAGE_NUM,
        "question": "A restaurant makes 20% profit after selling a set menu at a discount of 20%. What is the percentage increase of marked price? [BB-2026]",
        "options": [
            "30%",
            "20%",
            "40%",
            "50%"
        ],
        "answer": "ঘ",
        "explanation": "Let the cost price be 100 Tk.\nSo, at 20% profit selling price = 120% of 100 = 120 Tk.\nAgain,\nLet market price be = x after discount market price.\nSp will be 80% of x\nATQ\n80% of x = 120\n⇒ 80x / 100 = 120\n⇒ 80x = 120 × 100\n⇒ x = (120 × 100) / 80\n∴ x = 150 Tk.\nSo, Market price Increased = 150 - 100 = 50% (Ans.)"
    },
    {
        "id": 45,
        "page": PAGE_NUM,
        "question": "A ladder rests against a wall that is perpendicular to the ground. If the bottom of the ladder is 4m away from the bottom of the wall, while the tip of the ladder is at a height of 3m, what is the length of the ladder? [BB-2026]",
        "options": [
            "7m",
            "3.5m",
            "5m",
            "2.5m"
        ],
        "answer": "গ",
        "explanation": "Given that,\nDistance of the bottom of the ladder from the wall, AB = 3m\nand Height of the top of the ladder from the wall, BC = 4m\nLet, the length of the ladder, AC = ?\nAccording to the phythagoras theorem—\nAC² = AB² + BC²\n⇒ AC² = 3² + 4²\n⇒ AC² = 9 + 16\n⇒ AC = √25\n∴ AC = 5m\n∴ Length of the ladder 5m (Ans.)"
    },
    {
        "id": 46,
        "page": PAGE_NUM,
        "question": "A box having height 2m, length 10m and width 7m have the top lid open. What is the surface area of the box? [BB-2026]",
        "options": [
            "138",
            "118",
            "104",
            "208"
        ],
        "answer": "ক",
        "explanation": "Given that,\nheight, h = 2m\nlength, l = 10m\nand width, w = 7m\nwe know that,\nSurface area of the box = 2(hl + lw + hw) - l × w\n= 2(2 × 10 + 10 × 7 + 2 × 7) - 10 × 7\n= 2(20 + 70 + 14) - 70\n= 2 × 104 - 70\n= 208 - 70\n= 138m²\n∴ Surface area of the box 138m² (Ans.)"
    },
    {
        "id": 47,
        "page": PAGE_NUM,
        "question": "x - 1/x = 7. What is the value of x² + 1/x²? [BB-2026]",
        "options": [
            "14",
            "21",
            "51",
            "49"
        ],
        "answer": "গ",
        "explanation": "Given that,\nx - 1/x = 7\n∴ x² + 1/x² = (x - 1/x)² + 2.x.1/x\n= 7² + 2\n= 49 + 2\n= 51 (Ans.)"
    }
]
