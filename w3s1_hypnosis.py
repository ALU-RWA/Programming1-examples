# This demo is meant to showcase animations using aluLib.
# The hypnosis method will alternate between calling 3 different functions: version1(), version2(), and version3()

# This will be done thanks to a global variable which counts how often we've called the hypnosis function
from aluLib import *

window_width = 400
window_height = 400
count = 0 # This will count how many times we've called hypnosis.


# This function draws 3 circles at the center of the screen, one inside the other.
# Each circle has a different color
def version1():
    set_fill_color(1, 0, 0)
    draw_circle(window_width/2, window_height/2, 150)

    set_fill_color(1, 1, 1)
    draw_circle(window_width/2, window_height/2, 100)

    set_fill_color(0, 1, 0)
    draw_circle(window_width/2, window_height/2, 50)

# the version2() and version3() functions are similar to version1(), except for the colors.
def version2():
    set_fill_color(1, 1, 1)
    draw_circle(window_width/2, window_height/2, 150)

    set_fill_color(0, 1, 0)
    draw_circle(window_width/2, window_height/2, 100)

    set_fill_color(1, 0, 0)
    draw_circle(window_width/2, window_height/2, 50)


def version3():
    set_fill_color(0, 1, 0)
    draw_circle(window_width/2, window_height/2, 150)

    set_fill_color(1, 0, 0)
    draw_circle(window_width/2, window_height/2, 100)

    set_fill_color(1, 1, 1)
    draw_circle(window_width/2, window_height/2, 50)


# This function decides which of the versions to draw, based on the count of how often we've drawn things
def hypnosis():
    global count # we want to change a global variable here, so this line is needed

    # If count is 0, 3, 6, 9, 12.... call version1()
    if count % 3 == 0:
        version1()
    # Else if count is 1, 4, 7, 10, 13..... call version2()
    elif count % 3 == 1:
        version2()
    # Else if count is 2, 5, 8, 11, 14..... call version3()
    elif count % 3 == 2:
        version3()

    # Increase the count by 1
    count = count + 1

# Notice the framerate parameter below.
# Framerate is the number of times PER SECOND that the function will get called,
# and things get drawn on the window
# By default, the framerate is 40, meaning we draw 40 times per second.
# This also means that by default, start_graphics ALWAYS animates things.
# The key to animation is making sure the function we are drawing changes behaviour each time.
start_graphics(hypnosis, framerate=10, width=window_width, height=window_height)
