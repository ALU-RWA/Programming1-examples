# Prompt for user input:
# birth date, broken into day, month, and year.
# gender.

# Compute day of the week when you were born.
# Print day of the week.

print("So you want to know your Akan name? Which day of the week where you born?")
day = int(input("DD\n"))
month = int(input("MM\n"))
year = int(input("YYYY\n"))

y_temp = year - (14 - month) // 12
x_temp = y_temp + (y_temp // 4) - (y_temp // 100) + (y_temp // 400)
m_temp = month + 12*((14 - month) // 12) - 2
day_of_week = (day + x_temp + 31 * m_temp // 12) % 7

print(day_of_week)

gender = input("Type M if you are male, F if you are female\n")

name = ''

# Print out the appropriate name.
if (gender == 'F'):
     if (day_of_week == 0):
         name = 'Akosua'
     elif (day_of_week == 1):
         name = 'Adwoa'
     elif (day_of_week == 2):
         name = 'Abenaa'
     elif (day_of_week == 3):
         name = 'Akua'
     elif (day_of_week == 4):
         name = 'Yaa'
     elif (day_of_week == 5):
         name = 'Afua'
     elif (day_of_week == 6):
         name = 'Ama'
     else:
         print("Not a valid day of the week")
else:
    if (day_of_week == 0):
        name = 'Kwasi'
    elif (day_of_week == 1):
        name = 'Kwadwo'
    elif (day_of_week == 2):
        name = 'Kwabena'
    elif (day_of_week == 3):
        name = 'Kwaku'
    elif (day_of_week == 4):
        name = 'Yaw'
    elif (day_of_week == 5):
        name = 'Kofi'
    elif (day_of_week == 6):
        name = 'Kwame'
    else:
        print("Not a valid day of the week")

print("You would've been called " + name)