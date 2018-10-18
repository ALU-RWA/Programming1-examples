# This is a very simple function that takes a number x, and returns
# 2*x + 1

def f(x):
    y = 2*x + 1
    return y


result = f(10)
# notice that the line above will not print anything. return doesn't display any information
# we have however stored the return value in the variable result, so let's display it now:
print(result) # should print 21

# As with mathematical functions, functions with return values can be combined:
print(f(f(10))) # should print 43. f(10) returns 21, which becomes the input to the f function again, returning 43

# You don't always need a return value. For example look at this function:
def print_hi():
    print("Hi")

# This is not a particularly useful function, we can call it and we will see Hi on the console
print_hi()

# Did it return anything? let's test it:
# Note that we call print_hi again, so you will see another Hi in the output
result = print_hi()

# result stores the return value of the function, but in our function definition, we didn't return anything!
# What would this result to?
print(result) # should print None

# implicitly, when you don't return anything, it's as if we had defined the function like this:
def say_hello():
    print("Hello")
    return None

