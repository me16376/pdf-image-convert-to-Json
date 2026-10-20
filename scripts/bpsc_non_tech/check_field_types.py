import json
import os
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

for name, fpath in SUBJECTS:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for idx, q in enumerate(data):
        opts = q.get("options")
        if not isinstance(opts, list):
            print(f"[{name}] QID {q.get('id')} index {idx} has options type {type(opts)}: {opts}")
        else:
            for oi, o in enumerate(opts):
                if not isinstance(o, str):
                    print(f"[{name}] QID {q.get('id')} opt {oi} is not str: {type(o)} = {o}")
        exp = q.get("explanation")
        if exp is not None and not isinstance(exp, str):
            print(f"[{name}] QID {q.get('id')} explanation is not str: {type(exp)} = {exp}")
        q_text = q.get("question")
        if not isinstance(q_text, str):
            print(f"[{name}] QID {q.get('id')} question is not str: {type(q_text)} = {q_text}")
print("Done structure validation check.")
