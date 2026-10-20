import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r"JSON Data\BPSC Non Tech"

def inspect(subj, qid, rel_path):
    fpath = f"{BASE}\\{rel_path}"
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    q = next(item for item in data if item["id"] == qid)
    print(f"\n==========================================")
    print(f"[{subj}] QID {qid} (page {q.get('page')})")
    print("Question:", q.get("question"))
    print("Options:", q.get("options"))
    print("Answer:", q.get("answer"))
    print("Explanation:", q.get("explanation"))

inspect("Bangladesh Affairs", 153, r"Bangladesh Affairs\Bangladesh_Affairs.json")
inspect("International Affairs", 421, r"International Affairs\International_Affairs.json")
inspect("ICT", 24, r"ICT\ICT.json")
inspect("Science", 25, r"Science\Science.json")
inspect("Science", 116, r"Science\Science.json")
