import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'JSON Data\BPSC Non Tech\Bangla\Bangla.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for qid in [409, 830, 888]:
    q = next(item for item in data if item['id'] == qid)
    print(f"\n=== QID {qid} (p.{q.get('page')}) ===")
    print("Q:", q.get('question'))
    print("Options:", q.get('options'))
    print("Ans:", q.get('answer'))
    print("Exp:", q.get('explanation'))
