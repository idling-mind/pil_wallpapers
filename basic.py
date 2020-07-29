from PIL import Image, ImageDraw

img = Image.new("RGB", (500, 500))
ic = ImageDraw.Draw(img)

ic.ellipse([0, 0, 500, 500], fill="RED")

img.save("basic.png")
