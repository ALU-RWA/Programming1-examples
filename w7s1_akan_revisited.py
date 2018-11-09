# In this example, we further improve our user input
# By checking if the input is a number

def is_invalid_day(d):
    # if d is not a numeric string, then we should return True
    # if d is numeric, then check if it's lower than 1 or bigger than 31
    if not d.isnumeric():
        return True
    else:
        int_value = int(d)
        return int_value < 1 or int_value > 31


input_day = input("DD\n")


# While the user is giving us wrong day, ask them for a new one
while is_invalid_day(input_day):
    print("Valid days are between 1 and 31")
    input_day = input("DD\n")

print("our input day is: ")
print(input_day)
