import json
import os
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"JSON Data\BPSC Non Tech"
for p in os.listdir(base_dir):
    p_dir = os.path.join(base_dir, p)
    if os.path.isdir(p_dir):
        js = glob.glob(os.path.join(p_dir, "*.json"))
        if js:
            with open(js[0], "r", encoding="utf-8") as f:
                data = json.load(f)
            missing = sum(1 for q in data if not q.get("page"))
            print(f"{p:<28}: Total {len(data):>5} | Missing page field: {missing:>5}")
