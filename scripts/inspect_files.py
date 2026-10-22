# -*- coding: utf-8 -*-
import json
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

fname = sys.argv[1]
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
end = int(sys.argv[3]) if len(sys.argv) > 3 else 9999

with open(f'JSON Data/BPSC ICT Wizard/{fname}', encoding='utf-8') as f:
    data = json.load(f)

for item in data[start:end]:
    q = item['question']
    opts = " | ".join(item['options'])
    ans = item['answer']
    print(f"Q{item['id']}: {q}")
    print(f"   Opts: {opts}")
    print(f"   Ans: {ans}")
