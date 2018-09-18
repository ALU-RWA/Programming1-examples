from aluLib import *

window_width = 1500
window_height = 900


def nigeria():

    rectangle_width = window_width / 3

    set_fill_color(0, 0.53, 0.32)

    draw_rectangle(0, 0, rectangle_width, window_height)
    draw_rectangle(2 * rectangle_width, 0, rectangle_width, window_height)


start_graphics(nigeria, width=window_width, height=window_height)