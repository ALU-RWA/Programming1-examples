# Define a function that takes a single parameter: number_of_repetitions
# The function will print as many lines as the number provided.
# Each third line will be different from the other 2.


def say(number_of_repetitions):
    # We set up a local variable for couting.
    count = 1
    # As long as our count IS NOT BIGGER than the provided number of repetitions
    while count <= number_of_repetitions:

        # If we have already printed 2 lines before:
        if (count % 3) == 0:
            # Print the special line
            print("Say what you need to sayayayayaa")
        # Otherwise, print the normal one.
        else:
            print("Say what you need to say")

        # Increase count. What would happen if we remove this line?
        count = count + 1

# Test for 2 lines: We should only see the regular "Say what you need to say"
say(2)
print("------------------------------------------------")
# Test for 7 lines: We should see the special line twice, happening after 2 normal lines
say(7)