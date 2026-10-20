import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/bpsc_non_tech/audit_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

for subj, issues in report.items():
    print(f"\n=== {subj} Samples ===")
    foreign_chars = set()
    for iss in issues:
        if iss['type'] == 'FOREIGN_SCRIPT':
            for c in iss['chars']:
                foreign_chars.add(f"{c} (U+{ord(c):04X})")
    print("Foreign chars found:", list(foreign_chars)[:10])
    
    # Check leading option markers
    lead = [iss for iss in issues if iss['type'] == 'LEADING_OPT_MARKER']
    if lead:
        print("Leading opt markers:", [l['text'] for l in lead[:5]])
        
    # Check isolated kars
    iso = [iss for iss in issues if iss['type'] == 'ISOLATED_KAR']
    if iso:
        print("Sample isolated kars:", [f"{i['sample']} -> {i['chars']}" for i in iso[:3]])
        
    # Check broken prefixes
    bp = [iss for iss in issues if iss['type'] == 'BROKEN_BENGALI_PREFIX']
    if bp:
        print("Sample broken prefixes:", [f"{i['match']} in '{i['sample']}'" for i in bp[:3]])
