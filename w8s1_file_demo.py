# This is how we open a file aiming to READ it
tweet_file = open('tweets.txt', 'r')

# one way to iterate through the lines in the file is the
# for loop below:
for tweet in tweet_file:
    # This splits the line into words, we are assuming here that whoever typed only used 1 space between words.
    # Recall that split returns a list, so we can loop over all its elements like we have done in the past
    words = tweet.split(" ")

    n = 0
    while n < len(words):

        if words[n].startswith("#"):
            print(words[n])
        n += 1  # n = n + 1

# There are other ways to read a file. tweet_file.read() returns a String containing all its content
# tweet_file.readlines() returns a list of strings, each containing one line from the file

# Be polite!
tweet_file.close()

# open a new file with the intent to WRITE
# Remember that w OVERwrites the content, if you want to ADD to an existing file, use
# open(path_to_file, 'a')

tweet_file = open("tweets.txt", 'w')

tweet_file.write("\nWe are done!")
tweet_file.write("Wait wait I'm not done")
tweet_file.close()
