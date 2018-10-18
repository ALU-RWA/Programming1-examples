test_list = ['a', 'b', 'c', 'd', 'e']

# Let's print our test list so that we see how i looks like at the beginning
print(test_list)

# The first position in our list is 0. Let's store that in first_index
first_index = 0

# The last position in our list is the length of the list, minus 1. Let's store that too
last_index = len(test_list) - 1

# Now we want to swap the element of the list at first_index with the one at last_index,
# Then move to the next pair of elements to swap.
# the next pair can be found by first_index increasing by 1, and last_index decreasing by 1
while first_index < len(test_list) / 2:
    # Remember we talked about swapping variables: We must first store the information somewhere
    savior = test_list[first_index]
    # Now that the value at first_index is safe, we can replace it in the list
    test_list[first_index] = test_list[last_index]
    # Finally, we bring back the saved value, and put it at last_index
    test_list[last_index] = savior

    # Increase first index
    first_index = first_index + 1
    # Decrease last index
    last_index = last_index - 1

print(test_list)


