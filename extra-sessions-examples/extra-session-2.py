# Demo 1: Days of the week

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Practice 1: The first ten Fibonacci numbers

ten_fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Demo 2:
# Adding and removing days from initial list
days_of_the_week.append("Sunday")  # this will add "Sunday" to the end of the list
days_of_the_week.insert(5, "Saturday")  # this will add "Saturday" at position 5


# Practice 2: More robust fibonacci
# The function should return a list that contains the first ‘n’ elements of the Fibonacci series
def fibonacci(n):
    # We first take care of our two initial cases when n is 1 or 2
    if n == 1:
        fib_list = [0]  # When n is 1, there should only be one value in the list
        return fib_list
    elif n == 2:
        fib_list = [0, 1]  # When n is 2, there should only be two values in the list
        return fib_list
    elif n > 2:
        fib_list = [0, 1]  # When n is greater than 2, we start our list with the first two values and derive the rest
        count = 0
        while count < n - 2:  # Since our list already contains the first two elements, the loop runs (n - 2) times
            # This gets the two last values is our list, add them together, and append the result to the list
            fib_list.append(fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2])
            count = count + 1
        return fib_list


# Let's try the fibonacci() function
print(fibonacci(5))  # This should print [0, 1, 1, 2, 3]


# Practice - First duplicate


# It takes a list and a repeated value as parameters
# It should return the index of the second occurrence of repeated value
def find_second_instance(input_list, repeated_value):

    # We use the outer loop to find the first time repeated_value appears
    first_index = 0
    while first_index < len(input_list):
        if input_list[first_index] == repeated_value:
            # second_index starts from first_index + 1
            # because the second instance of repeated_value is necessarily after the first instance
            second_index = first_index + 1

            # This inner loop finds the second time repeated_value appears
            while second_index < len(input_list):
                if input_list[first_index] == input_list[second_index]:
                    # Once we've found it we return second_index right away and exit the function
                    return second_index
                second_index = second_index + 1
        first_index = first_index + 1


# Let's try it
quiz_list = [0, 1, 0, 2, 2, 1, 0]
print(find_second_instance(quiz_list, 1))  # We should see 5
