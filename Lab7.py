""" Recursion """

# Palindrome is a word, phrase, or sequence that reads the same
# backward as forward.

# Examples)
# is_palindrome(madam) -> True
# is_palindrome(racecar) -> True
# is_palindrome(pizza) -> False


def is_palindrome(word):
    """
    Check if a given string input (word) is a palindrome.
    You must write your solution recursively. (no loops)
    :param word: string input
    :return: True if word is palindrome, otherwise False
    """
    # for i in range(len(s) // 2):
    #     if s[i] != s[len(s) - 1 - i]:
    #         return False
    # return True

    # base
    if len(word) == 0:
        return True
    # recur
    if word[0] == word[-1]:
        return is_palindrome(word[1:len(word) - 1])
    else:
        return False


# print(is_palindrome("madam"))
# print(is_palindrome("racecar"))
# print(is_palindrome("pizza"))
