from aluLib import *

window_width = 1500
window_height = 900

def main():

    rectangle_width = window_width / 3

    # draw left most rectangle in red
    set_fill_color(0, 0.53, 0.32)
    draw_rectangle(0, 0, rectangle_width, window_height)

    # draw right most rectangle in green
    draw_rectangle(2 * rectangle_width, 0, rectangle_width, window_height)


start_graphics(main, width=window_width, height=window_height)