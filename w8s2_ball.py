from aluLib import *

class Ball:

    def __init__(self, start_x, start_y, radius, start_v_x, start_v_y):
        # Location and velocities of the ball.
        self.x = start_x
        self.y = start_y

        self.v_x = start_v_x
        self.v_y = start_v_y

        self.radius = radius  # radius (in pixels)

        # Color of the ball, for drawing purposes.
        self.r = 0.5
        self.g = 0.5
        self.b = 0.5

    def draw(self):
        disable_stroke()
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x, self.y, self.radius)
        enable_stroke()

        self.x += self.v_x
        self.y += self.v_y

    # not currently used, but would change the velocity of the ball
    def set_speed(self, new_vx, new_vy):
        self.v_x = new_vx
        self.v_y = new_vy

    # Allows us to print the ball object
    def __str__(self):
        return(str(self.x) + ", " + str(self.y))


