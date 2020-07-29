from PIL import Image, ImageDraw

scale_factor = 4 # Resize scaling for antialiasing
img_size = (1920, 1080) # Final image size desired

img_size_scaled = tuple(x*scale_factor for x in img_size)

img = Image.new("RGB", img_size_scaled)
ic = ImageDraw.Draw(img, "RGBA") # Specified RGBA

def draw_circle(x, y, r, color):
    """Function to draw a circle at given center with given
    radius and colour
    """
    x, y, r = int(x), int(y), int(r) # Converting possible floats to int
    ic.ellipse([x-r, y-r, x+r, y+r], fill=color)

def concentric_circles(x, y, max_r, circle_count, color, max_opacity):
    for i in range(circle_count):
        draw_circle(
            x, y,
            max_r*(circle_count-i)/circle_count,
            (*color, int(max_opacity*i/circle_count))
        )
        # Tip for beginners: *color will unpack the tuple and
        # make it as if we typed `color[0], color[1]`
centers = [
    (0,0), 
    (img_size_scaled[0],0), 
    (0, img_size_scaled[1]), 
    (img_size_scaled[0], img_size_scaled[1]),
    #(img_size_scaled[0]/2, img_size_scaled[1]/2)
]

for c in centers:
    concentric_circles(
        *c,
        img_size_scaled[0]/2,
        10, (255, 0, 0), 50
    )

img = img.resize(img_size, resample=Image.ANTIALIAS)
img.save("circle_pattern1.png")
