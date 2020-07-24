"""Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/"""


def freqAlphabets(s):
    # define the dictionary
    d = {'1': 'a',
         '2': 'b',
         '3': 'c',
         '4': 'd',
         '5': 'e',
         '6': 'f',
         '7': 'g',
         '8': 'h',
         '9': 'i',
         '10#': 'j',
         '11#': 'k',
         '12#': 'l',
         '13#': 'm',
         '14#': 'n',
         '15#': 'o',
         '16#': 'p',
         '17#': 'q',
         '18#': 'r',
         '19#': 's',
         '20#': 't',
         '21#': 'u',
         '22#': 'v',
         '23#': 'w',
         '24#': 'x',
         '25#': 'y',
         '26#': 'z'}

    final_string = ''
    i = len(s) - 1
    # we start from the end of the string 
    while i >= 0:
        # we check if the char at the i position is a # if it is we jump 2 char so we can have the key
        if s[i] == '#':
            current_string = s[i - 2:i + 1]
            i = i - 3
        else:
            current_string = s[i]
            i -= 1
        # we add the current string from the dictionary to the final string
        final_string = final_string + d[current_string]
    # we reverse the string 
    final_string = final_string[::-1]
    return final_string


if __name__ == '__main__':
    print(freqAlphabets("10#11#12"))
