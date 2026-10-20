from PIL import Image
import os

img_p109 = r"Images\BPSC Non Tech\BPSC Bangla\p109.jpg"
img_p110 = r"Images\BPSC Non Tech\BPSC Bangla\p110.jpg"

os.makedirs("scratch", exist_ok=True)

if os.path.exists(img_p109):
    im = Image.open(img_p109)
    w, h = im.size
    # Crop middle-lower section where Q1203 resides
    # typically 2-column page
    c1 = im.crop((0, int(h * 0.4), w, int(h * 0.8)))
    c1.save("scratch/p109_crop.jpg")
    print(f"p109 saved, size {w}x{h}")

if os.path.exists(img_p110):
    im2 = Image.open(img_p110)
    w2, h2 = im2.size
    c2 = im2.crop((0, 0, w2, int(h2 * 0.6)))
    c2.save("scratch/p110_crop.jpg")
    print(f"p110 saved, size {w2}x{h2}")
