# Demo 1:


# Function print_favorite_number with no parameter
def print_favorite_number():
    favorite_number = 17
    print(favorite_number)


print_favorite_number()


# Function print_favorite_number with a parameter
def print_favorite_number(favorite_number):
    print(favorite_number)


print_favorite_number(3)


# Practice 1

# Let's create a function called print_name
# It takes no parameters
# All it does is printing your name
def print_name():
    print("Salmane")


print_name()


# Let's now create a print_full_name function which takes two parameters: first_name and last_name
# It should print the full name using the given parameters
def print_full_name(first_name, last_name):
    print(first_name + " " + last_name)


print_full_name("Abdoulaye", "Kante")


# Demo 2: Collatz
# Take a single parameter. That will be the number that begins the sequence
# Print each intermediate number
# Return how many iterations (steps) it took to get to 1
def collatz(initial_number):
    number_of_steps = 0
    while not(initial_number == 1):
        if initial_number % 2 == 0:  # If the number is even, divide it by two
            initial_number = initial_number / 2
        else:  # If it's odd, multiply by three and add one
            initial_number = initial_number * 3 + 1

        number_of_steps = number_of_steps + 1  # Increment the number of step

    return number_of_steps


# Let's call collatz
print(collatz(7))  # This prints 16


# Calling collatz twice
# We can only do this because the function returns a value
# If we were printing it, then the second call would use a None as a parameter
# and that results in an error
print(collatz(collatz(3)))


# Practice 2
# get_full_name function
def get_full_name(first_name, last_name):
    # Let's get the full name by combining first_name and last_name
    full_name = first_name + " " + last_name

    # Now let's return it
    return full_name


# get_age_in_ten_years function
def get_age_in_ten_years(current_age):
    # In 10 years, the age will be current_age + 10
    age_in_ten_years = current_age + 10

    # Now let's return it
    return age_in_ten_years


# get_information function
def get_information(first_name, last_name, current_age, country):
    # Our list should have full_name, age_in_ten_years, and country
    # We know how to get all of the functions we've defined
    # You can always call a function inside another one
    full_name = get_full_name(first_name, last_name)
    age_in_ten_years = get_age_in_ten_years(current_age)

    # Let's create our list and populate it
    info_list = [age_in_ten_years, country, full_name]

    # Now we return our list
    return info_list


# introduce_me function
def introduce_me(information_list):
    # Remember to use the index in the list for the position of each piece of information
    # Since we want age in twenty years, then we should call get_age_in_ten_years() once more
    # Remember to turn the age you are getting into a String with the str() function
    print("Hello there, \nMy name is: " + information_list[2] +
          "\nI am from: " + information_list[1] +
          "\nI will be: " + str(get_age_in_ten_years(information_list[0])) + " years old in twenty years.")


# Let's call the function
introduce_me(get_information("Kevin", "De Bruyne", 27, "Belgium"))


