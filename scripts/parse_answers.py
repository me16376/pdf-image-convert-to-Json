import sys
import json
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

ITEMS_MAP = {
    34: 'ক',
    33: 'খ',
    31: 'গ',
    28: 'ঘ',
    76: 'খ+গ',
}

def get_answers_on_page(page, y_min=0, y_max=850, x_min=0, x_max=600):
    d = page.get_drawings()
    ans_objs = [
        x for x in d 
        if x_min <= x['rect'].x0 <= x_max 
        and y_min <= x['rect'].y0 <= y_max 
        and len(x['items']) in ITEMS_MAP
        and (x['rect'].x1 - x['rect'].x0) < 20
        and (x['rect'].y1 - x['rect'].y0) < 20
    ]
    # Sort into rows by y
    ans_objs.sort(key=lambda o: (round(o['rect'].y0 / 15), o['rect'].x0))
    return [(o['rect'].x0, o['rect'].y0, len(o['items']), ITEMS_MAP[len(o['items'])]) for o in ans_objs]

if __name__ == '__main__':
    doc = pymupdf.open('PDF/Saif Sir NTRCA Suggestion/saif-sir-ntrca-suggestion.pdf')
    # Page 12 is index 11
    res = get_answers_on_page(doc[11], y_min=130, y_max=245, x_min=340, x_max=560)
    print(f"Found {len(res)} answer marks:")
    # Group by row
    rows = {}
    for x, y, it, ans in res:
        row_key = round(y / 15)
        rows.setdefault(row_key, []).append((x, y, ans))
    
    count = 1
    for rk in sorted(rows.keys()):
        row = sorted(rows[rk], key=lambda item: item[0])
        print(f"Row y~{rk*15}: {[item[2] for item in row]}")
        for item in row:
            print(f"{count}: {item[2]}", end=" | ")
            count += 1
        print()
