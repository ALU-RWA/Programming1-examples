# This example focuses on the local and global scope, and goes through 3 scenarios
# which demonstrate how Python handles scope.

# Scenario 1: Similarly named globals and locals
x = "Global"


def f1():
    x = "Local"
    # While there are 2 x variables, python finds the local one first
    # So the following should print "Local"
    print(x)


f1() # Print Local
print(x) # Print Global

# Scenario 2: Differently named globals and locals
g = "Global"
def f2():
    l = "local"
    print(g) # There is no g in the local scope, but there is one in the global
    print(l) # There is an l in the local scope, so we print that.


f2() # print gobal then local
print(g) # print global
print(l) # error! no l in the global scope. Remember, local variables are DELETED once their function finishes


# Scenario 3: Writing to a global
# Delete or comment out line 25 to test the scenario below
y = "Global"
def f3():
    global y # This is necessary to be able to modify a global variable FROM inside a function
    print(y)
    y = y + " Test" # Concatenate y with " Test"


f3() # What does this print?
f3() # What does this print?
print(y) # What about this one?

