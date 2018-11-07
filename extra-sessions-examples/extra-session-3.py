# Demo 1: Different ways to get a string

# Using quotation marks
alu = 'Do hard things'
#
# Using string concatenation
alu1 = 'Do'
alu2 = ' Hard things'

alu = alu1 + alu2

# Getting user input
alu = str(input('Type something about ALU: '))
print(alu)


# Using the str() function
our_boolean = True
print(type(our_boolean))  # The variable is of type boolean
our_boolean_to_str = str(our_boolean)
print(type(our_boolean_to_str))  # # The variable is of type string


# Demo: string as list
alu = 'Do hard things'
# Indexing a string
print(alu[4])

# Getting the length of a string
print(len(alu))

# Iterating over a string
i = 0

while i < len(alu):

    print(alu[i])
    i = i + 1

# Assigning a new character
alu[1] = 'f'  # This triggers an error because lists are immutable


# Practice 1: is_palindrome
# This function prints whether the word input by the user is a palindrome
def is_palindrome():
    word = input('Type your word: ')

    "'This is what we wrote in class, but it prints too many times'"
    # i = 0
    # while i < len(word)/2:
    #     if word[i] == word[len(word) - 1 - i]:
    #         print(word + ' is a palindrome')
    #     else:
    #         print(word + ' is not a palindrome')
    #
    #     i = i + 1

    "'This ensures we only print once'"
    is_word_palindrome = True

    i = 0
    while i < len(word) / 2:
        if word[i] != word[len(word) - 1 - i]:
            is_word_palindrome = False

        i = i + 1

    if is_word_palindrome:
        print(word + ' is a palindrome')
    else:
        print(word + ' is not a palindrome')


# Let's test the function
is_palindrome()


# This block allows us to get the biggest value in a list
numbers_list = [7, 6, 4, 246, -9, 8]

biggest_so_far = numbers_list[0]  # We start with the first number in the list as the biggest one

i = 0
while i < len(numbers_list):
    if biggest_so_far < numbers_list[i]:  # Check if this current number is bigger than the biggest seen so far
        biggest_so_far = numbers_list[i]  # If it is indeed bigger, then it becomes the new biggest number

    i = i + 1

print(biggest_so_far)


# Practice 2: get_longest_word
# This function takes a sentence as a parameter and prints the longest word and its number of characters

def get_longest_word(sentence):
    sentence_as_list = sentence.split(' ')  # We split our sentence into individual words and store them in a list

    longest_word_so_far = sentence_as_list[0]  # We start with the first word in the list as the longest one

    count = 0
    while count < len(sentence_as_list):
        # Check if this current word is longer than the longest seen so far
        if len(longest_word_so_far) < len(sentence_as_list[count]):
            # If it is indeed longer, then it becomes the new longest word
            longest_word_so_far = sentence_as_list[count]

        count = count + 1

    print('Longest word is: ' + longest_word_so_far + ' with ' + str(len(longest_word_so_far)) + ' characters')


get_longest_word('The quick brown fox jumped over the lazy dog.')  # Should tell us 'jumped' is the longest word
