# Prompt the user for their date of birth
print("So you want to know your Akan name? Which day of the week where you born?")

# Remember that the input we get from the user is a String.
# We want to do some math with those numbers shortly, so we use the int() function to convert the input String
# into a number.
day = int(input("DD\n"))
month = int(input("MM\n"))
year = int(input("YYYY\n"))

# The following is one of many methods for figuring out the day of the week a specific date occured.
# If you are curious about what is going, check out this page: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
# Ultimately, the math below should give us a number between 0 and 6, where 0 is Sunday, and 6 is Saturday

# Recall the difference between the '/' operator and the '//' operator
y_temp = year - (14 - month) // 12
x_temp = y_temp + (y_temp // 4) - (y_temp // 100) + (y_temp // 400)
m_temp = month + 12*((14 - month) // 12) - 2
day_of_week = (day + x_temp + 31 * m_temp // 12) % 7

# Time to figure out if we are dealing with a Female or a Male.
gender = input("Type M if you are male, F if you are female\n")

# The code below will decide what the name should be. We create the variable name here. That's the "box" we will put the
# name in once we figure it out.
# Think about what could happen with the code if we removed line 27?
name = ''

# Figure out the appropriate name.
if gender == 'F' or gender == 'f':
    if day_of_week == 0:
        name = 'Akosua'
    elif day_of_week == 1:
        name = 'Adwoa'
    elif day_of_week == 2:
        name = 'Abenaa'
    elif day_of_week == 3:
        name = 'Akua'
    elif day_of_week == 4:
        name = 'Yaa'
    elif day_of_week == 5:
        name = 'Afua'
    elif day_of_week == 6:
        name = 'Ama'
    else:
        print("Not a valid day of the week")
elif gender == 'M':
    if day_of_week == 0:
        name = 'Kwasi'
    elif day_of_week == 1:
        name = 'Kwadwo'
    elif day_of_week == 2:
        name = 'Kwabena'
    elif day_of_week == 3:
        name = 'Kwaku'
    elif day_of_week == 4:
        name = 'Yaw'
    elif day_of_week == 5:
        name = 'Kofi'
    elif day_of_week == 6:
        name = 'Kwame'
    else:
        print("Not a valid day of the week")
else:
    print("You typed the wrong thing")
# Print the name
print("You would've been called " + name)
