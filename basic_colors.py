from random import randint
from PIL import Image, ImageDraw

scale_factor = 4 # Resize scaling for antialiasing
img_size = (500, 500) # Final image size desired

img_size_scaled = tuple(x*scale_factor for x in img_size)

img = Image.new("RGB", img_size_scaled)
ic = ImageDraw.Draw(img)

def draw_circle(x, y, r, color):
    """Function to draw a circle at given center with given
    radius and colour
    """
    x, y, r = int(x), int(y), int(r) # Converting possible floats to int
    ic.ellipse([x-r, y-r, x+r, y+r], fill=color)

for i in range(10):
    draw_circle(
        img_size_scaled[0]/2, img_size_scaled[1]/2,
        img_size_scaled[0]/2*(10-i)/10,
        (randint(0, 255), randint(0, 255), randint(0,255))
    )
# You can pass in list of tuples too!

img = img.resize(img_size, resample=Image.ANTIALIAS)
img.save("basic_colors.png")
