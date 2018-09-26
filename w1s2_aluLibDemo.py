from aluLib import *

window_width = 1000
window_height = 600


def nigeria():
    rectangle_width = window_width / 3
    set_fill_color(0, 0.53, 0.32)

    # draw_rectangle needs 4 parameters
    # parameter 1: the X coordinate of the top left corner of the rec.
    # parameter 2: the Y coordinate of the top left corner of the rec.
    # parameter 3: how wide should this rec. be?
    # parameter 4: how high should this rec. be?
    draw_rectangle(0, 0, rectangle_width, window_height)

    draw_rectangle(2 * rectangle_width, 0, rectangle_width, window_height)


def nigeria2():
    rectangle_width = window_width / 3
    set_fill_color(0, 0.53, 0.32)

    # draw_rectangle needs 4 parameters
    # parameter 1: the X coordinate of the top left corner of the rec.
    # parameter 2: the Y coordinate of the top left corner of the rec.
    # parameter 3: how wide should this rec. be?
    # parameter 4: how high should this rec. be?
    draw_rectangle(0, 0, 500, 900)

    draw_rectangle(1000, 0, 500, 900)


start_graphics(nigeria, width=window_width, height=window_height)