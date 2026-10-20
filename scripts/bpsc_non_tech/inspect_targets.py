import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def show(path, qid):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"\n*** {path} (Q{qid}) ***")
    pattern = rf'\{{\s*["\']id["\']:\s*{qid}\b.*?\}}'
    m = re.search(pattern, text, re.DOTALL)
    if m:
        print(m.group(0))
    else:
        print("Not found by regex, searching by id in lines:")
        for line in text.splitlines():
            if f'"id": {qid}' in line or f"'id': {qid}" in line:
                print("  ", line)

show('scripts/bpsc_non_tech/bangla/p59.py', 368)
show('scripts/bpsc_non_tech/bangla/p99.py', 1025)
show('scripts/bpsc_non_tech/bangla/p32.py', 32)
show('scripts/bpsc_non_tech/bangla/p36.py', 66)
show('scripts/bpsc_non_tech/bangla/p37.py', 85)
show('scripts/bpsc_non_tech/bangla/p68.py', 504)
show('scripts/bpsc_non_tech/english/p319.py', 362)
show('scripts/bpsc_non_tech/english/p322.py', 409)
show('scripts/bpsc_non_tech/english/p331.py', 542)
show('scripts/bpsc_non_tech/international_affairs/p723.py', 23)
show('scripts/bpsc_non_tech/international_affairs/p724.py', 33)
show('scripts/bpsc_non_tech/international_affairs/p725.py', 45)
show('scripts/bpsc_non_tech/international_affairs/p746.py', 322)
show('scripts/bpsc_non_tech/math/p1089.py', 614)
