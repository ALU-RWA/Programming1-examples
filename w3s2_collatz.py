# Here we create a function that performs Collatz' conjecture on a parameter
# The function will PRINT each intermediate step, and RETURN how many steps there were


def collatz(initial_number):
    # Good practice: Let's avoid overwriting the initial parameter.
    number = initial_number

    # Let's set an initial count of 0.
    count = 0

    print("We are going from " + str(initial_number) + " to 1")

    # We must repeat the operation as long as number is not 1.
    while number != 1:
        # If the number is even, divide it by 2
        if number % 2 == 0:
            number = number // 2

        # Else if it is odd, multiply by 3, then add 1
        else:
            number = (number * 3) + 1

        # Print the new number.
        print(number)
        # Keep track that we took 1 extra step.
        count = count + 1

    # Outside the loop, once we have reached 1, it is time to RETURN how many steps
    # We've taken. Note that return IMMEDIATELY ENDS THE FUNCTION
    return count

    # This will never print, as it is after the function
    print("Goodbye")


# Why does return matter? well it allows us to get information out of a function
# Print gives information back to our eyes, we get to read something about the results of our code
# If however, you want THE REST OF YOUR PROGRAM to be aware of that result, then you must RETURN it
# count is a local variable in the collatz function. Once the function is done, its value will be lost
# Return is a way to get that value OUT of the function:
steps_for_3 = collatz(3)
steps_for_5 = collatz(5)
print(steps_for_3 > steps_for_5)
# Now in our program we can leverage the work that the collatz function did.
# Obviously, you could've just printed the count, ran the function for 3 and 5, then figured out which one
# Takes more steps. But what if I asked you to find which number between 1 and 1000 takes the most steps?
# that would take you forever while printing. Next class, it will take us 15 minutes of coding.
# because we will RETURN that value back to our code, and write more code to find the max for us.


