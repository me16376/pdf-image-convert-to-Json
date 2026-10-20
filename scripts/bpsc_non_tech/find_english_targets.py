import os
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

eng_scripts = glob.glob(r"scripts\bpsc_non_tech\english\p*.py")
targets = [62, 512, 582, 899, 975, 1086, 1306, 1347]
found = {}

for f in eng_scripts:
    with open(f, "r", encoding="utf-8") as rf:
        content = rf.read()
    for t in targets:
        if f'"id": {t}' in content or f"'id': {t}" in content:
            found[t] = os.path.basename(f)

print("Target question locations in English page scripts:")
for t in sorted(targets):
    print(f"  QID {t}: {found.get(t, 'Not found')}")
