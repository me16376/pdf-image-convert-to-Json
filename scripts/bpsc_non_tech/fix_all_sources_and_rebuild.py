import os
import sys
import re
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("Applying targeted fixes to source page files...")

# List of replacements in files: (filepath, old_text, new_text)
edits = [
    # 1. Bangla p59.py - कर्तव्य -> কর্তব্য
    (
        r"scripts/bpsc_non_tech/bangla/p59.py",
        "कर्तव्य",
        "কর্তব্য"
    ),
    # 2. Bangla p99.py - अनिष्ट -> অনিষ্ট
    (
        r"scripts/bpsc_non_tech/bangla/p99.py",
        "अनिष्ट",
        "অনিষ্ট"
    ),
    # 3. Bangla p32.py - split O-kar
    (
        r"scripts/bpsc_non_tech/bangla/p32.py",
        "\u09C7\u09BE",
        "\u09CB"
    ),
    # 4. Bangla p36.py - split O-kar
    (
        r"scripts/bpsc_non_tech/bangla/p36.py",
        "\u09C7\u09BE",
        "\u09CB"
    ),
    # 5. Bangla p37.py - split O-kar
    (
        r"scripts/bpsc_non_tech/bangla/p37.py",
        "\u09C7\u09BE",
        "\u09CB"
    ),
    # 6. Bangla p68.py - split O-kar
    (
        r"scripts/bpsc_non_tech/bangla/p68.py",
        "\u09C7\u09BE",
        "\u09CB"
    ),
    # 7. English p319.py - উদ্দীাপিত -> উদ্দীপিত
    (
        r"scripts/bpsc_non_tech/english/p319.py",
        "উদ্দীাপিত",
        "উদ্দীপিত"
    ),
    # 8. English p322.py - शब्द -> শব্দ
    (
        r"scripts/bpsc_non_tech/english/p322.py",
        "शब्द",
        "শব্দ"
    ),
    # 9. English p331.py - शब्द -> শব্দ
    (
        r"scripts/bpsc_non_tech/english/p331.py",
        "शब्द",
        "শব্দ"
    ),
    # 10. Intl Affairs p723.py - न्यूयॉर्क -> নিউইয়র্ক
    (
        r"scripts/bpsc_non_tech/international_affairs/p723.py",
        "নিউयॉर्क",
        "নিউইয়র্ক"
    ),
    # 11. Intl Affairs p724.py - न्यूयॉर्क -> নিউইয়র্ক
    (
        r"scripts/bpsc_non_tech/international_affairs/p724.py",
        "নিউयॉर्क",
        "নিউইয়র্ক"
    ),
    # 12. Intl Affairs p725.py - split O-kar
    (
        r"scripts/bpsc_non_tech/international_affairs/p725.py",
        "\u09C7\u09BE",
        "\u09CB"
    ),
    # 13. Intl Affairs p746.py - কंग्रेस -> কংগ্রেস
    (
        r"scripts/bpsc_non_tech/international_affairs/p746.py",
        "কং\u094d\u0930\u0947\u0938",
        "কংগ্রেস"
    ),
    (
        r"scripts/bpsc_non_tech/international_affairs/p746.py",
        "কंग्रेस",
        "কংগ্রেস"
    ),
    # 14. Math p1089.py - সর্বোচ্চ -> সর্বোচ্চ
    (
        r"scripts/bpsc_non_tech/math/p1089.py",
        "\u09C7\u09BE",
        "\u09CB"
    ),
    # 15. Bangladesh Affairs p566.py - ঘোড়াউত্ৰা (\u09F0) -> ঘোড়াউত্রা
    (
        r"scripts/bpsc_non_tech/bangladesh_affairs/p566.py",
        "\u0998\u09CB\u09DC\u09BE\u0989\u09A4\u09CD\u09F0\u09BE",
        "ঘোড়াউত্রা"
    ),
    # 16. International Affairs p742.py - বহুক্ৰীড়া (\u09F0) -> বহুক্রীড়া
    (
        r"scripts/bpsc_non_tech/international_affairs/p742.py",
        "\u09AC\u09B9\u09C1\u0995\u09CD\u09F0\u09C0\u09DC\u09BE",
        "বহুক্রীড়া"
    ),
]

for rel_path, old_str, new_str in edits:
    full_path = os.path.abspath(rel_path)
    if not os.path.exists(full_path):
        print(f"Skipping {rel_path} (does not exist)")
        continue
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {rel_path}")
    else:
        print(f"Target not found in {rel_path} (already fixed or different string)")

print("\nRebuilding all 7 subject JSONs...")
build_scripts = [
    r"scripts/bpsc_non_tech/bangla/build_bangla_json.py",
    r"scripts/bpsc_non_tech/english/build_english_json.py",
    r"scripts/bpsc_non_tech/bangladesh_affairs/build_bangladesh_affairs_json.py",
    r"scripts/bpsc_non_tech/international_affairs/build_international_affairs_json.py",
    r"scripts/bpsc_non_tech/science/build_science_json.py",
    r"scripts/bpsc_non_tech/ict/build_ict_json.py",
    r"scripts/bpsc_non_tech/math/build_math_json.py",
]

py_exe = sys.executable

for bs in build_scripts:
    res = subprocess.run([py_exe, bs], capture_output=True, text=True, encoding='utf-8')
    if res.returncode != 0:
        print(f"❌ Error running {bs}:\n{res.stderr}")
    else:
        # print last line of output
        lines = [line.strip() for line in res.stdout.strip().splitlines() if line.strip()]
        last_line = lines[-1] if lines else "OK"
        print(f"✓ Rebuilt {os.path.basename(bs)}: {last_line}")

print("\nRunning Master 7-Subject Audit...")
audit_res = subprocess.run([py_exe, r"scripts/bpsc_non_tech/audit_all_7_subjects.py"], capture_output=True, text=True, encoding='utf-8')
print(audit_res.stdout)
