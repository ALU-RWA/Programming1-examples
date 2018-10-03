# Quick warm up question: print all positive multiples of
# 3 which are less than 257

# Set up a variable for the multiples, we begin at 0
multiple = 0

# As long as we are under 257, keep repeating the task.
while multiple < 257:
    # Print the multiple
    print(multiple)
    # Get to the next multiple by simply adding 3
    multiple = multiple + 3
