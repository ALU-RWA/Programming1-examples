# This is how you can create a dictionary directly
# You should immediately think of dictionaries in Python when
# you see {}

# This dictionary connects Strings to Strings
# In particular, it connects an Kinyarwanda word to an English word
#
k_to_e_dictionary = {'Ikaramu': 'pen', 'Amafaranga': 'money', 'Amata': 'Milk'}

# To get the value linked to a given key, index into the dictionary using the key
print(k_to_e_dictionary.get('Umva'))

# You can overwrite existing values using this syntax.
# k_to_e_dictionary['Amata'] = 'Cheese'
#
# # Using the same syntax, you can also add new key/value pairs to the dictionary
# k_to_e_dictionary['Kane'] = 'Four'
#
# # Note that the dictionary now contains the key:value pair Kane:Four
# print(k_to_e_dictionary)
#
# # Looping over a dictionary can be done easily:
# # in this loop, the key variable will be one of the keys of the dictionary each time
# # The loop will end once the keys are done.
# for key in k_to_e_dictionary:
#     print(key)
#     print(k_to_e_dictionary[key])
#
# # We create an empty dictionary here, and we will use it to connect
# # the same words, except that now the english words will be the key, and the
# # rwandan words the value
# e_to_k_dictionary = {}
#
# # Now we loop over the keys of k_to_e_dictionary
# # note that you can give any name you want to the variable in the 'for' statement
# for kinyarwanda_word in k_to_e_dictionary:
#     english_word = k_to_e_dictionary[kinyarwanda_word] # Get the english word associated to the k word
#     # Now we add both words to the new dictionary, except with the english word as the key now
#
#     k_to_e_dictionary[english_word] = kinyarwanda_word
