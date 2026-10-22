# -*- coding: utf-8 -*-
import json
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

fname = sys.argv[1]
start_idx = int(sys.argv[2]) if len(sys.argv) > 2 else 0
end_idx = int(sys.argv[3]) if len(sys.argv) > 3 else 9999

with open(fname, encoding='utf-8') as f:
    data = json.load(f)

for item in data[start_idx:end_idx]:
    ans_val = item['answer']
    print(f"[{item['id']}] {item['question']}")
    for idx, opt in enumerate(item['options']):
        marker = " <== ANS" if (ans_val in ['A','B','C','D'] and ['A','B','C','D'].index(ans_val) == idx) or (ans_val in ['ক','খ','গ','ঘ'] and ['ক','খ','গ','ঘ'].index(ans_val) == idx) else ""
        print(f"    {chr(65+idx)}. {opt}{marker}")
    print()
