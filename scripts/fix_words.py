# -*- coding: utf-8 -*-
"""
Apply word-by-word quality improvements to all JSON files in JSON Data/BPSC ICT Wizard/
Fixes broken characters, typos, spacing anomalies, and punctuation.
"""
import json
import os
import re
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = "JSON Data/BPSC ICT Wizard"

def clean_text(text):
    if not isinstance(text, str):
        return text
    # remove double spaces
    text = re.sub(r' {2,}', ' ', text)
    # remove space before punctuation
    text = re.sub(r'\s+([?,;:])', r'\1', text)
    # trim
    text = text.strip()
    return text

# 1. Fix '2. Computer Programming.json'
p2_path = os.path.join(base_dir, "2. Computer Programming.json")
with open(p2_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item["question"] = clean_text(item["question"])
    item["options"] = [clean_text(opt) for opt in item["options"]]
    
    if item["id"] == 18:
        item["question"] = item["question"].replace("আউটপুট হবে?", "আউটপুট কী হবে?")
    elif item["id"] == 20:
        item["question"] = item["question"].replace("কিভাবে arr অ্যারের শেষ এলিমেন্টস একসেস করা যাবে?", "কীভাবে arr অ্যারের শেষ এলিমেন্ট অ্যাক্সেস করা যাবে?")

with open(p2_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Updated 2. Computer Programming.json")

# 2. Fix '3. Data Communication and Networking.json'
p3_path = os.path.join(base_dir, "3. Data Communication and Networking.json")
with open(p3_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item["question"] = clean_text(item["question"])
    item["options"] = [clean_text(opt) for opt in item["options"]]
    
    if item["id"] == 15:
        item["options"] = [opt.replace("SMPT", "SMTP") for opt in item["options"]]
    elif item["id"] == 19:
        item["question"] = item["question"].replace("আছি", "আছে")

with open(p3_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Updated 3. Data Communication and Networking.json")

# 3. Fix '4. Digital Electronics.json'
p4_path = os.path.join(base_dir, "4. Digital Electronics.json")
with open(p4_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item["question"] = clean_text(item["question"])
    item["options"] = [clean_text(opt) for opt in item["options"]]
    
    if item["id"] == 13:
        item["question"] = item["question"].replace("Mutiple", "Multiple")
    elif item["id"] == 16:
        item["question"] = item["question"].replace("circuits?[Digital", "circuits? [Digital").replace("কি? ]", "কী?]")

with open(p4_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Updated 4. Digital Electronics.json")

# 4. Fix '7. Data Structure and Algorithm.json'
p7_path = os.path.join(base_dir, "7. Data Structure and Algorithm.json")
with open(p7_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item["question"] = clean_text(item["question"])
    item["options"] = [clean_text(opt) for opt in item["options"]]
    
    if item["id"] == 10:
        item["question"] = item["question"].replace("field on is Data", "fields, one is Data,")
    elif item["id"] == 13:
        item["options"] = [re.sub(r'[\s,]+', ', ', opt) if ',' in opt else opt for opt in item["options"]]
        item["options"] = [opt.replace('*, ', '*').replace('/, ', '/').replace('+, ', '+').replace('-, ', '-') for opt in item["options"]]
        item["options"] = ["*, /, %, +, -", "/, %, *, +, -", "%, /, *, +, -", "-, +, *, /, %"]
    elif item["id"] == 30:
        item["question"] = item["question"].replace("Buble sort", "Bubble sort")
    elif item["id"] == 32:
        item["question"] = item["question"].replace("Algorithm e code", "Algorithm-এ code")

with open(p7_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Updated 7. Data Structure and Algorithm.json")

# 5. Fix '8. Computer Organization and Architecture.json'
p8_path = os.path.join(base_dir, "8. Computer Organization and Architecture.json")
with open(p8_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item["question"] = clean_text(item["question"])
    item["options"] = [clean_text(opt) for opt in item["options"]]

with open(p8_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Updated 8. Computer Organization and Architecture.json")

# 6. Fix '9. Operating System.json'
p9_path = os.path.join(base_dir, "9. Operating System.json")
with open(p9_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item["question"] = clean_text(item["question"])
    item["options"] = [clean_text(opt) for opt in item["options"]]
    
    if item["id"] == 51:
        item["question"] = item["question"].replace("Burst Time ms হয়", "Burst Time 12 ms হয়")

with open(p9_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Updated 9. Operating System.json")

# 7. Fix 'BCS Computer পার্ট.json'
bcs_path = os.path.join(base_dir, "BCS Computer পার্ট.json")
with open(bcs_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item["question"] = clean_text(item["question"])
    item["options"] = [clean_text(opt) for opt in item["options"]]
    
    qid = item["id"]
    if qid == 13:
        item["options"] = [opt.replace("Kasparasky", "Kaspersky") for opt in item["options"]]
    elif qid == 17:
        item["options"] = [opt.replace("Phising", "Phishing") for opt in item["options"]]
    elif qid == 21:
        item["options"] = [opt.replace("Andrid", "Android") for opt in item["options"]]
    elif qid == 23:
        item["options"] = [opt.replace("Netware", "Network") for opt in item["options"]]
    elif qid == 30:
        item["question"] = item["question"].replace("Clould", "Cloud")
        item["options"] = ["CaaS", "IaaS", "PaaS", "SaaS"]
    elif qid == 32:
        item["options"] = [opt.replace("Randm Frequesncy", "Random Frequency").replace("Random Frequesncy", "Random Frequency") for opt in item["options"]]
    elif qid == 33:
        item["question"] = item["question"].replace("চিহ্নটি- ই", "চিহ্নটি ই")
    elif qid == 43:
        item["question"] = item["question"].replace("অন্যালগ", "অ্যানালগ")
    elif qid == 47:
        item["question"] = item["question"].replace("Multi- tasking", "Multi-tasking")
    elif qid == 50:
        item["question"] = item["question"].replace("দূরত্ব সবচেয়ে কম কত?", "দূরত্ব সবচেয়ে কম?")
    elif qid == 51:
        # options: standard 100 1's complement options
        item["options"] = ["111", "101", "011", "001"]
    elif qid == 72:
        item["question"] = item["question"].replace("sheduling", "scheduling")
    elif qid == 74:
        item["options"] = [opt.replace("Ecplorer", "Explorer") for opt in item["options"]]
    elif qid == 80:
        item["question"] = item["question"].replace("প্রোটকল", "প্রোটোকল")
    elif qid == 84:
        item["options"] = [opt.replace("lip-lop", "flip-flop") for opt in item["options"]]
    elif qid == 104:
        item["options"] = [opt.replace("Registors", "Registers") for opt in item["options"]]
    elif qid == 106:
        item["question"] = item["question"].replace("আদান প্রদানে", "আদান-প্রদানে").replace("কি?", "কী?")
    elif qid == 110:
        item["question"] = item["question"].replace("মেমোরীটি", "মেমোরিটি")
    elif qid == 116:
        item["options"] = [opt.replace("Interconection", "Interconnection") for opt in item["options"]]
    elif qid == 129:
        item["options"] = [opt.replace("ekanei.com", "ekhanei.com") for opt in item["options"]]
    elif qid == 137:
        item["options"] = [opt.replace("Bill Gatea", "Bill Gates") for opt in item["options"]]

with open(bcs_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Updated BCS Computer পার্ট.json")

# Clean all other files in directory to ensure general cleanliness
for fname in os.listdir(base_dir):
    if fname.endswith(".json"):
        fpath = os.path.join(base_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        changed = False
        for item in data:
            q_clean = clean_text(item["question"])
            opts_clean = [clean_text(opt) for opt in item["options"]]
            if q_clean != item["question"] or opts_clean != item["options"]:
                item["question"] = q_clean
                item["options"] = opts_clean
                changed = True
        if changed:
            with open(fpath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Cleaned whitespace in {fname}")

print("All fixes applied successfully!")
