""" Write a program that gets from input a sentence, counts word frequencies, and prints one line for each
word, in descending order of frequency """

# Dictionary for the words
word_rank = dict()


# Function that populates the dictionary like this:
# {word:how many times the words appeared in the sentence}
def count_word(word, sentence):
    word_rank[word] = sentence.count(word)


# The sentence
text = input()
# Split the sentence in a list of words
words_in_text = text.split()

# For each word in the sentence apply the count_word function
for word in words_in_text:
    count_word(word, text)

# Create a dictionary that has the keys,sorted in reverse, of the word_rank dictionary
sorted_keys = sorted(word_rank.items(), key=lambda kv: kv[1], reverse=True)
# Iterate through the sorted_keys dictionary and print word rank: the word_rank
for key in sorted_keys:
    print(key[0], " rank:", key[1])
