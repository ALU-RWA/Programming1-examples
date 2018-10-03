# We figure out how to use loops to keep a user from
# giving us bad input.


# This function returns True or False, based on the provided test_value
# If the value could be a month, i.e between 1 and 12, then we return false
# If the value is not a valid month, return True
def invalid_month(test_value):
    return 1 > test_value or test_value > 12


# Ask for user input
month = int(input("Please type the month you were born: MM\n"))

# As long as the input is invalid, keep asking the user:
# invalid_month will give us True or False
# if it gives us True, the loop executes again, otherwise we move on
while invalid_month(month):
    # Recall that we ALWAYS should modify the variable used in our loop conditions from
    # inside our loop.

    # In our case, month should change. We should make sure to update it to the new user input
    month = int(input("Valid months are between 1 and 12 inclusive, try again!\n"))

print("We have a month now!")
