# Basic example for keyboard control. 3 keys are linked to 3 functions, each function draws a flag

from aluLib import *

window_width = 1500
window_height = 900

# These functions are the same as the solution
def benin():
    left_rectangle_width = window_width / 3
    right_rectangle_height = window_height / 2

    set_fill_color(0, 1, 0)
    draw_rectangle(0, 0, left_rectangle_width, window_height)

    set_fill_color(1, 1, 0)
    draw_rectangle(left_rectangle_width, 0, 2 * left_rectangle_width, right_rectangle_height)

    set_fill_color(1, 0, 0)
    draw_rectangle(left_rectangle_width, right_rectangle_height, 2 * left_rectangle_width, right_rectangle_height)


def niger():
    rectangle_height = window_height / 3

    # Draw top rectangle
    set_fill_color(1, 0.5, 0)

    draw_circle(window_width/2, window_height/2, window_height/9)
    draw_rectangle(0, 0, window_width, rectangle_height)

    set_fill_color(0, 1, 0)
    draw_rectangle(0, 2 * rectangle_height, window_width, rectangle_height)


def guinea():
    rectangle_width = window_width / 3

    set_fill_color(1, 0, 0)
    draw_rectangle(0, 0, rectangle_width, window_height)

    set_fill_color(1, 1, 0)
    draw_rectangle(rectangle_width, 0, rectangle_width, window_height)

    set_fill_color(0, 1, 0)
    draw_rectangle(2 * rectangle_width, 0, rectangle_width, window_height)


# The main function draws flag only when a given key is pressed
def main():
    # is_key_pressed takes one character as a parameter, and returns True or False,
    # based on whether or not that character was printed in that frame.
    if is_key_pressed("b"):
        benin()
    elif is_key_pressed("n"):
        # Clear erases the screen. This is important for the Niger flag.
        # What happens if you remove the call to clear?
        clear()
        niger()
    elif is_key_pressed("g"):
        guinea()


start_graphics(main, width=window_width, height=window_height)