# -*- coding: utf-8 -*-
import sys
import os
from PIL import Image

def slice_page(page_num):
    img_path = f"Images/BPSC Non Tech/BPSC English/p{page_num}.jpg"
    if not os.path.exists(img_path):
        print(f"Error: {img_path} not found")
        sys.exit(1)
        
    im = Image.open(img_path)
    w, h = im.size
    print(f"Processing p{page_num}.jpg: size = {w}x{h}")
    
    out_dir = r"C:\Users\bdCalling\.gemini\antigravity-ide\brain\47f718db-3571-4d81-b2b8-b4c073d26d9d"
    os.makedirs(out_dir, exist_ok=True)
    
    # 2 columns, top and bottom, plus table at bottom
    # Left column: x: 0.05 to 0.52
    # Right column: x: 0.48 to 0.98
    # Top: y: 0.03 to 0.52
    # Bottom: y: 0.48 to 0.90
    # Table: y: 0.88 to 0.98, x: 0.05 to 0.98
    
    left_top = im.crop((int(w * 0.01), int(h * 0.02), int(w * 0.53), int(h * 0.52)))
    left_bot = im.crop((int(w * 0.01), int(h * 0.48), int(w * 0.53), int(h * 0.90)))
    right_top = im.crop((int(w * 0.47), int(h * 0.02), int(w * 0.99), int(h * 0.52)))
    right_bot = im.crop((int(w * 0.47), int(h * 0.48), int(w * 0.99), int(h * 0.90)))
    table = im.crop((int(w * 0.03), int(h * 0.86), int(w * 0.98), int(h * 0.99)))
    
    left_top.save(os.path.join(out_dir, f"p{page_num}_left_top.jpg"), quality=95)
    left_bot.save(os.path.join(out_dir, f"p{page_num}_left_bot.jpg"), quality=95)
    right_top.save(os.path.join(out_dir, f"p{page_num}_right_top.jpg"), quality=95)
    right_bot.save(os.path.join(out_dir, f"p{page_num}_right_bot.jpg"), quality=95)
    table.save(os.path.join(out_dir, f"p{page_num}_table.jpg"), quality=95)
    
    print(f"Saved slices for p{page_num}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        slice_page(int(sys.argv[1]))
    else:
        print("Usage: py slice_page.py <page_num>")
