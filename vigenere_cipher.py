import string

alphabet = [letter for letter in string.ascii_lowercase]


def create_key(word, key):
    word_secret = ""
    poz_of_key = 0
    for i in range(0, len(word)):
        if word[i].isalpha():
            word_secret += key[poz_of_key % len(key)]
            poz_of_key += 1
        else:
            word_secret += word[i]
    return word_secret


def encrypt_word(word, key):
    result = ""
    for i in range(0, len(word)):
        try:
            if word[i].isalpha():
                result += alphabet[(alphabet.index(word[i]) + alphabet.index(create_key(word, key)[i])) % 26]
            else:
                result += word[i]
        except Exception as e:
            print(e)
    return result


def decrypt_word(word, key):
    result = ""
    for i in range(0, len(word)):
        try:
            if word[i].isalpha():
                result += alphabet[(alphabet.index(word[i]) - alphabet.index(create_key(word, key)[i])) % 26]
            else:
                result += word[i]
        except Exception as e:
            print(e)
    return result


input_word = "Maine asta o sa fie problema pe care trebuie sa o rezolve, oameni care vor sa fie in echipa ta".lower()
input_key = "curs".lower()

print(encrypt_word(input_word, input_key))
print(decrypt_word(encrypt_word(input_word, input_key), input_key))