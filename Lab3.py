"""
 String, List - Level 2.0
"""


def count_hi(string):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    count = 0
    for i in range(len(string) - 1):
        if str(string[i] + string[i + 1]) == "hi":
            count += 1
    return count


def cat_dog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    isDog = 0
    isCat = 0
    for i in range(len(string) - 2):
        if str(string[i:i + 3]) == "dog":
            isDog += 1
        elif str(string[i:i + 3]) == "cat":
            isCat += 1
    if isDog == isCat:
        return True
    else:
        return False


def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    count = 0
    for i in range(len(string) - 3):
        if str(string[i]) == "c" and str(string[i + 1]) == "o" and str(string[i + 3]) == "e":
            count += 1
    return count


def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """
    if len(a) < len(b):
        a, b = b, a
    a, b = a.lower(), b.lower()
    return a[len(a) - len(b):] == b


def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    return count


def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    min = nums[0]
    max = nums[0]
    for i in range(len(nums) - 1):
        if nums[i + 1] <= min:
            min = nums[i + 1]
        elif max < nums[i + 1]:
            max = nums[i + 1]
    return max - min


def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    i = 0
    total = 0
    while i < len(nums):
        if nums[i] != 13:
            total += nums[i]
            i += 1
        else:
            i += 2
    return total


def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    ans = 0
    isIgnore = False
    for i in range(len(nums)):
        if nums[i] == 6:
            isIgnore = True
        if not isIgnore:
            ans += nums[i]
        if nums[i] == 7 and isIgnore:
            isIgnore = False
    return ans


def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False
