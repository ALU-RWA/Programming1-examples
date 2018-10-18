# Define a list for female names, and a list for male names:

female_names = ["Akosua", "Adwoa", "Abenaa", "Akua", "Yaa", "Afua", "Ama"]
male_names = ["Kwasi", "Kwadwo", "Kwabena", "Kwaku", "Yaw", "Kofi", "Kwame"]


# Define simple functions that check if a day or a month
# is valid. They will return True or False
def is_invalid_month(m):
    return m < 0 or m > 12

def is_invalid_day(d):
    return d < 0 or d > 31

# Prompt the user for their date of birth
print("So you want to know your Akan name? Which day of the week where you born?")


# Remember that the input we get from the user is a String.
# We want to do some math with those numbers shortly, so we use the int() function to convert the input String
# into a number.
day = int(input("DD\n"))

# While the user is giving us wrong day, ask them for a new one
while is_invalid_day(day):
    print("Valid days are between 1 and 12")
    day = int(input("DD\n"))


# Repeat for months
month = int(input("MM\n"))

while is_invalid_month(month):
    print("Valid months are between 1 and 12")
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

gender = input("Type F for female or M for male\n")
# The code below will decide what the name should be. We create the variable name here. That's the "box" we will put the
# name in once we figure it out.
# Think about what could happen with the code if we removed line 27?
name = ''

# Figure out the appropriate name.
if gender == 'F' or gender == 'f':
    name = female_names[day_of_week]
elif gender == 'M' or gender == 'm':
    name = male_names[day_of_week]
else:
    print("You gave me the wrong input")

# Print the name
print("You would've been called " + name)
