from aluLib import *

window_width = 1500
window_height = 900

def niger():
    rectangle_height = window_height / 3
    # Set the orange color
    set_fill_color(1, 0.5, 0)

    # Only draw when clicking
    # What happens if we keep clicking?
    # Refer to the slides or to the aluLib guide for details
    # on the mouse functions below
    if is_mouse_pressed():
        draw_circle(mouse_x(), mouse_y(), window_height/9)

    # Draw the top rectangle
    draw_rectangle(0, 0, window_width, rectangle_height)

    # Draw bottom rectangle
    set_fill_color(0, 0.8, 0)
    draw_rectangle(0, 2*rectangle_height, window_width, rectangle_height)


start_graphics(niger, width=window_width, height=window_height)