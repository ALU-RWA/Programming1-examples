# First, let's show an example of creating your own error.
# Say for example we are creating a function that divides two numbers,
# we want to raise an error whenever the denominator is zero

# The example is a bit redundant, as python already has a built in exception
# for division by 0, but it shows how it is set up.

def division(top, bottom):
    if bottom == 0:
        # Note the syntax here. We create a new Exception object, and
        # use the keyword "raise" to trigger the error
        raise Exception("Attempting to divide by 0. Don't do this!")
        # Note that raise immediately ends the function that contains it!
    return top/bottom

# Bring in these 2 lines of code to test the function, line 17 will print 2.5
# Line 19 instead will raise an error
# print(division(5, 2))
# print(division(5, 0))
#

# This is how all *Runtime errors* are coded up, you will encounter many like this, and create your own.
# How do we handle errors elegantly in our code? If you have end users (or a picky grader) then you really never want
# your code to show errors in any scenario. Thus the following syntax can be useful:

try:
    # You should wrap code that COULD error in a *try* statement
    # We could get an error in line 28 if the input isn't a number
    # We could also get an error in line 29 if we try to divide by 0
    user_input = int(input("Give me a number, 0 is ok, it won't cause an error"))
    division(8, user_input)
    print("Done trying")
except:
    # In all cases, if either of those lines raise an error, the code will jump
    # directly to line 35, and skip anything else in the try statement
    print("You gave me a bad input!")
    # After except, the program continues to the next line

print("Demo done")