import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

fpath = r"c:\Users\bdCalling\Downloads\Mosabber\pdf-image-convert-to-Json\JSON Data\BPSC Non Tech\English\English.json"
with open(fpath, "r", encoding="utf-8") as f:
    data = json.load(f)

target_ids = [62, 512, 582, 899, 975, 1086, 1306, 1347]
for q in data:
    if q["id"] in target_ids:
        print(f"\n==========================================")
        print(f"QID {q['id']} (p.{q.get('page')})")
        print("Question:", q.get("question"))
        print("Options:", q.get("options"))
        print("Answer:", q.get("answer"))
        print("Explanation:", q.get("explanation"))
