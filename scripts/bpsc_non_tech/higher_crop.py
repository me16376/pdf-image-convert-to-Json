from PIL import Image

im109 = Image.open(r"Images\BPSC Non Tech\BPSC Bangla\p109.jpg")
w, h = im109.size

# Q1203 is higher up in right column
q1203_crop = im109.crop((int(w * 0.45), int(h * 0.20), w, int(h * 0.50)))
q1203_crop.save(r"scratch\q1203_higher.jpg")

print("Saved higher crop for Q1203.")
