
def draw_circle(ic, x, y, r, color):
    """Function to draw a circle at given center with given
    radius and colour

    Args:
        ic (Draw Object): The Draw object on which the drawing should
            be done.
        x, y (int): Center of the circle
        r (int): Radius of the circle
        color: The color of the circle
    
    Returns:
        None
    """
    x, y, r = int(x), int(y), int(r) # Converting possible floats to int
    ic.ellipse([x-r, y-r, x+r, y+r], fill=color)

def concentric_circles(ic, x, y, max_r, circle_count, color, max_opacity):
    """Function to draw concentric circles
    
    Args:
        ic: Draw object to which to draw
        x, y (int): Center of circles
        max_r (int): Max radius of circles
        circle_count (int): Number of required circles
        color: color of the circle in RGB
        max_opacity (int): The max opacity for the innermost circle
    
    Returns:
        None
    """
    for i in range(circle_count):
        draw_circle(
            ic, 
            x, y,
            max_r*(circle_count-i)/circle_count,
            (*color, int(max_opacity*i/circle_count))
        )