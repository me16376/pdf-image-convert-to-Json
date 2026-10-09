import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

PUA_MAP = {
    '\uf0b0': '°',
    '\uf0a2': "'",
    '\uf0b4': '×',
    '\uf0a5': '∞',
    '\uf0d0': '∠',
    '\uf044': '△',
    '\uf061': 'α',
    '\uf05c': '∴',
    '\uf0e6': '(',
    '\uf0f6': ')',
    '\uf0e8': '(',
    '\uf0f8': ')',
    '\uf0e9': '[',
    '\uf0f9': ']',
    '\uf0ec': '{',
    '\uf0fc': '}',
    '\uf0ed': '{',
    '\uf0fd': '}',
    '\uf0ee': '{',
    '\uf0fe': '}',
    '\uf033': '3',
    '˚': '°',
    'і': 'ি',
}

base = 'JSON Data/Biddabari-NTRCA'

modified_count = 0
for root, dirs, files in os.walk(base):
    for f in sorted(files):
        if not f.endswith('.json'): continue
        p = os.path.join(root, f)
        with open(p, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        changed = False
        for q in data.get('questions', []):
            for field in ['question', 'explanation']:
                t = q.get(field, '')
                if t:
                    new_t = t
                    for k, v in PUA_MAP.items():
                        if k in new_t:
                            new_t = new_t.replace(k, v)
                    if new_t != t:
                        q[field] = new_t
                        changed = True
            opts = q.get('options', [])
            new_opts = []
            for o in opts:
                new_o = o
                for k, v in PUA_MAP.items():
                    if k in new_o:
                        new_o = new_o.replace(k, v)
                new_opts.append(new_o)
            if new_opts != opts:
                q['options'] = new_opts
                changed = True
        if changed:
            with open(p, 'w', encoding='utf-8') as fp:
                json.dump(data, fp, ensure_ascii=False, indent=2)
            modified_count += 1

print(f"Replaced PUA and non-standard symbols in {modified_count} files!")
