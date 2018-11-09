alu_quote = "take ownership"
# Indexing into Strings
print(alu_quote[10])

# Length of String: len returns how many characters are in a string
# Think of a character as the act of typing a key. Spaces and punctuation are characters too!
print(len(alu_quote))


# Strings are immutable
# The following line will trigger an error
#alu_quote[0] = 'T'

# print each character in the String:
counter = 0
while (counter <= len(alu_quote) - 1):
    print(alu_quote[counter])
    counter = counter + 1


# Demonstrate startswith
print(alu_quote.startswith("take ownership"))
print(alu_quote.startswith("ta"))

# Demonstrate the "in" syntax
# "some string" in "the main string" will return true or false
# depending on whether the sequence "some string" can be found, in the exact order, in the main string
test = "t" in alu_quote and "k" in alu_quote
print(test)

# Lots of functions return booleans based on what kind of string we have
text = "fourteen"
print(text.isnumeric())
print(text.isalnum())
print(text.isalpha())

# Demonstrate 'split'

student_info = "Salmane, Tamo, Niger, ALC Mauritius"
print(student_info)
result = student_info.split(' ')
print(result)
print(alu_quote.split(" "))
