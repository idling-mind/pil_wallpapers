from random import choice
from PIL import Image, ImageDraw
from colorlovers import get_top_pallet
from draw_shapes import draw_circle

scale_factor = 4 # Resize scaling for antialiasing
img_size = (1920, 1080) # Final image size desired

img_size_scaled = tuple(x*scale_factor for x in img_size)

img = Image.new("RGB", img_size_scaled)
ic = ImageDraw.Draw(img, "RGBA") # Specified RGBA

pallet = get_top_pallet(13) # Getting a top pallet

step = 120*scale_factor
# 120x120 is the size of each square area on a 1920x1080 px image
# if we divide it into a 16x9 squares.

for i in range(16+2):
    for j in range(9+2):
        draw_circle(
            ic, 
            step*i, step*j,
            step, 
            f"#{pallet[i%len(pallet)]}66" # Opacity set at 66 (in hex)
        )

img = img.resize(img_size, resample=Image.ANTIALIAS)
img.save("circle_pattern2.png")
