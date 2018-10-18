# Given a list and a value, let's write a function that returns how many times
# The value is found in the list

def count(some_list, some_value):
    # We want to go through the whole list, and check each element
    # Whenever we find an element that matches some_value, we should count up
    result = 0
    # We use the result variable to keep track of how often we find some_value,
    # We will return this variable at the end.

    # Now let's go through the whole list. We should get really, REALLY used to
    # this approach to seeing all elements in a list:
    # First we set a variable to indicate which element we want to check
    # index will represent where in the list we are looking
    index = 0
    # Remember, the positions in a list go from 0, to the length of the list - 1
    # We can therefore set up our loop like this
    while index < len(some_list):

        # Ask: Is the element at this index the same as the value we are looking for?
        if some_list[index] == some_value:
            # Yes!, increase result by 1
            result += 1

        # We always want to increase index
        index += 1

    return result


# Now let's test this. Remember: returning a value doesn't show it, so we
# will want to print to convince ourselves:
print(count([1, 1, 2, 3, 1], 1)) # should print 3
print(count(['Morocco', 'Algeria', 'Tunisia'], 'Egypt')) # should print 0

