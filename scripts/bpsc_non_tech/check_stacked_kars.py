import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\bdCalling\Downloads\Mosabber\pdf-image-convert-to-Json\JSON Data\BPSC Non Tech"
SUBJECTS = [
    ("Bangla", os.path.join(BASE_DIR, "Bangla", "Bangla.json")),
    ("English", os.path.join(BASE_DIR, "English", "English.json")),
    ("Bangladesh Affairs", os.path.join(BASE_DIR, "Bangladesh Affairs", "Bangladesh_Affairs.json")),
    ("International Affairs", os.path.join(BASE_DIR, "International Affairs", "International_Affairs.json")),
    ("Science", os.path.join(BASE_DIR, "Science", "Science.json")),
    ("ICT", os.path.join(BASE_DIR, "ICT", "ICT.json")),
    ("Math", os.path.join(BASE_DIR, "Math", "Math.json")),
]

# Legacy Bijoy split kars:
# 1. E-kar + A-kar: U+09C7 + U+09BE -> should be O-kar U+09CB
# 2. E-kar + Ou-length-mark: U+09C7 + U+09D7 -> should be Ou-kar U+09CC
# 3. Double kars: াা, িি, ীী, ুু, ূূ, ৃৃ, েে, ৈৈ, োো, ৌৌ,্্
RE_SPLIT_O_KAR = re.compile(r'\u09C7\u09BE')
RE_SPLIT_OU_KAR = re.compile(r'\u09C7\u09D7')
RE_DOUBLE_KAR = re.compile(r'([\u09BE-\u09CC\u09CD])\1+')

print("=== SCANNING FOR STACKED & DOUBLE KARS ===")

total_stacked_o = 0
total_stacked_ou = 0
total_double_kars = 0

for name, fpath in SUBJECTS:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    sub_so = 0
    sub_sou = 0
    sub_dk = 0
    for q in data:
        all_texts = [q.get("question", "")] + q.get("options", []) + [q.get("explanation", "")]
        for txt in all_texts:
            if not isinstance(txt, str):
                continue
            so = len(RE_SPLIT_O_KAR.findall(txt))
            sou = len(RE_SPLIT_OU_KAR.findall(txt))
            dk = len(RE_DOUBLE_KAR.findall(txt))
            sub_so += so
            sub_sou += sou
            sub_dk += dk
    print(f"[{name}] Split O-kar: {sub_so} | Split Ou-kar: {sub_sou} | Double kar: {sub_dk}")
    total_stacked_o += sub_so
    total_stacked_ou += sub_sou
    total_double_kars += sub_dk

print(f"\nGRAND TOTALS: Split O-kar: {total_stacked_o} | Split Ou-kar: {total_stacked_ou} | Double kar: {total_double_kars}")
