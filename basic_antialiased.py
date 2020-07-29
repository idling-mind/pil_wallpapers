from PIL import Image, ImageDraw

scale_factor = 4 # Resize scaling for antialiasing
img_size = (500, 500) # Final image size desired

img_size_scaled = tuple(x*scale_factor for x in img_size)

img = Image.new("RGB", img_size_scaled)
ic = ImageDraw.Draw(img)

ic.ellipse([(0, 0), img_size_scaled], fill="RED")
# You can pass in list of tuples too!

img = img.resize(img_size, resample=Image.ANTIALIAS)
img.save("basic_antialiased.png")
