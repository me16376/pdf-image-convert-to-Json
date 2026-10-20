from PIL import Image

# 1. BD p551
im1 = Image.open(r"Images\BPSC Non Tech\BPSC Bangladesh affairs\p551.jpg")
w1, h1 = im1.size
im1.crop((0, int(h1 * 0.15), w1, int(h1 * 0.45))).save(r"scratch\bd_p551_crop.jpg")

# 2. Intl p751
im2 = Image.open(r"Images\BPSC Non Tech\BPSC International Affairs\p751.jpg")
w2, h2 = im2.size
im2.crop((0, int(h2 * 0.35), w2, int(h2 * 0.65))).save(r"scratch\intl_p751_crop.jpg")

# 3. ICT p915
im3 = Image.open(r"Images\BPSC Non Tech\BPSC ICT\p915.jpg")
w3, h3 = im3.size
im3.crop((0, int(h3 * 0.40), w3, int(h3 * 0.70))).save(r"scratch\ict_p915_crop.jpg")

# 4. Science p882
im4 = Image.open(r"Images\BPSC Non Tech\BPSC Science\p882.jpg")
w4, h4 = im4.size
im4.crop((0, int(h4 * 0.30), w4, int(h4 * 0.60))).save(r"scratch\sci_p882_crop.jpg")

print("Cropped all 4 verification targets.")
