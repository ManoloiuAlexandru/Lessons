"""
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 
https://leetcode.com/problems/goat-latin/
"""


class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u']
        result = ""
        to_add_at_end = "a"
        list_of_words = S.split()
        for word in list_of_words:
            if word[0].lower() in vowel:
                word += "ma"
            elif word[0].lower() not in vowel:
                word += word[0] + "ma"
                word = word[1:]
            word += to_add_at_end
            to_add_at_end += "a"
            result += word + " "
        result = result.strip()
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.toGoatLatin("Each word consists of lowercase and uppercase letters only"))
