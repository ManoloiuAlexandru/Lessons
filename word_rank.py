''' Write a program that gets from input a sentence, counts word frequencies, and prints one line for each
word, in descending order of frequency '''

word_rank = dict()


def count_word(word, sentence):
    word_rank[word] = sentence.count(word)


text = input()
words_in_text = text.split()

for word in words_in_text:
    count_word(word, text)

sorted_keys = sorted(word_rank.items(), key=lambda kv: kv[1], reverse=True)
for key in sorted_keys:
    print(key[0], " rank:", key[1])
