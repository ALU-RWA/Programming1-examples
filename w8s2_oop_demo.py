from w8s2_ball import *

# Ball() takes 5 parameters:
# x and y of the ball
# radius of the ball
# vx and vy, changes to x and y respectively

# We call the constructor here by using the Class name, followed by the parameters
# of the __init__ method we defined in the class
ball_1 = Ball(50, 50, 10, 2, 2)
ball_2 = Ball(50, 350, 10, 2, -2)
ball_3 = Ball(300, 250, 10, -2, -2)

# we can interact with the ball objects in a few different ways
def main():
    clear()
    # This is how we call a method of the class (in other words, any function defined within Ball)
    # the pattern is object_name.method_name()
    # For example this will draw the ball
    ball_1.draw()
    # You can also treat the attributes of the ball, which we define in the constructor
    # As regular variables, reading their value and assigning it to what is needed.
    # The pattern is object_name.attribute

    # As you read about OOP, attributes are often called by different names like:
    # properties, fields, or instance variables.
    print(ball_1.x)
    ball_2.draw()
    ball_3.draw()


start_graphics(main)
