# We will create a function that takes a parameter n
# then returns the first n numbers of the fibonacci sequence in a list
# Recall the fibonacci sequence starts with 1, 1, 2, 3, 5, 8, 13 ...


# For the sake of this exercise, I will assume that n is not negative
def fib(n):
    # If n is 0, we just return an empty list
    if n == 0:
        return []

    # If n is 1, we just return the first fibonacci number
    # Since we said this should be in a list, we create a list that only contains 0
    if n == 1:
        return [1]

    # If we got to this point, we know n is not 0 or 1.
    # We now can start building up the fibonacci sequence
    result = [1, 1]

    while len(result) < n:
        # Figure out the sum of the last 2 elements we've seen so far
        sum_of_last_two = result[len(result) - 1] + result[len(result) - 2]

        # Add the sum to the end of the list
        # Recall that append INCREASES THE LENGTH OF THE LIST, so the loop condition is changing
        result.append(sum_of_last_two)

    # We get out of the loop once the result list is as big as we want, we can now return it
    return result

print(fib(5))