import os
import sys
import json
import re
import pymupdf
import easyocr
import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

# Mapping for answer table vectors (verified mathematically)
ANS_ITEM_MAP = {
    34: 'ক',
    33: 'খ',
    31: 'গ',
    28: 'ঘ',
    76: 'খ+গ',
}

def extract_answer_table(drawings, min_x, max_x, min_y, max_y):
    """Extract answers from উত্তরমালা table using vector items or fallback"""
    # Answer cells are arranged in rows
    cells = []
    for d in drawings:
        r = d['rect']
        if min_x <= r.x0 <= max_x and min_y <= r.y0 <= max_y:
            w = r.x1 - r.x0
            h = r.y1 - r.y0
            if w < 20 and h < 15 and len(d['items']) > 5:
                cells.append((r.y0, r.x0, len(d['items']), r))
    
    # Sort into rows by y
    cells.sort(key=lambda c: (round(c[0] / 12), c[1]))
    
    # Identify answers: they have items in ANS_ITEM_MAP or are in the answer rows
    answers = {}
    ans_idx = 1
    # Typically rows alternate: Number row (১, ২..), Answer row (গ, ক..)
    # Group cells by y roughly
    rows = []
    cur_row = []
    cur_y = None
    for c in cells:
        if cur_y is None or abs(c[0] - cur_y) < 8:
            cur_row.append(c)
            cur_y = c[0]
        else:
            if cur_row:
                cur_row.sort(key=lambda x: x[1])
                rows.append(cur_row)
            cur_row = [c]
            cur_y = c[0]
    if cur_row:
        cur_row.sort(key=lambda x: x[1])
        rows.append(cur_row)
        
    for r in rows:
        # Check if this row contains answer items
        ans_in_row = [ANS_ITEM_MAP.get(c[2]) for c in r if ANS_ITEM_MAP.get(c[2])]
        if len(ans_in_row) >= 4:
            for c in r:
                ans_char = ANS_ITEM_MAP.get(c[2], 'ক')
                answers[ans_idx] = ans_char
                ans_idx += 1
                if ans_idx > 25:
                    break
    return answers

print("Extraction script template ready.")
