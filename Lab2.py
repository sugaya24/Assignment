"""
Basic python list problems -- no loops.
"""


def first_last6(nums):
    """
    Given a list of ints, return True if 6 appears as either the first or last element in the list.
    The list will be length 1 or more.
    """
    if len(nums) < 1:
        return nums
    else:
        if (nums[0] == 6 or nums[-1] == 6):
            return True
        else:
            return False


def same_first_last(nums):
    """
    Given a list of ints, return True if the list is length 1 or more, and the first element
    and the last element are equal.
    """
    if len(nums) < 1:
        return False
    else:
        if nums[0] == nums[-1]:
            return True
        else:
            return False


def common_end(a, b):
    """
    Given 2 lists of ints, a and b, return True if they have the same first element or they have the same last element.
    Both lists will be length 1 or more.
    """
    if not(len(a) > 0 and len(b) > 0):
        return False
    else:
        if (a[0] == b[-1]) or a[-1] == b[-1]:
            return True
        else:
            return False


def sum3(nums):
    """
    Given a list of ints length 3, return the sum of all the elements.
    """
    # return sum(nums)
    ans = 0
    for i in range(3):
        ans += nums[i]
    return ans


def rotate_left3(nums):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    """
    # nums = [nums[1], nums[2], nums[0]]
    nums = [*nums[1:], nums[0]]
    return nums


def reverse3(nums):
    """
    Given a list of ints length 3, return a new list with the elements in reverse order,
    so {1, 2, 3} becomes {3, 2, 1}.
    """
    # nums.reverse()
    ans = [0] * len(nums)
    for i in range(len(nums)):
        # ans.append(nums[len(nums) - i - 1])
        ans[i] = nums[len(nums) - i - 1]
    return ans


def max_ends3(nums):
    """
    Given a list of ints length 3, figure out which is larger, the first or last element in the list,
    and set all the other elements to be that value. Return the changed list.
    """
    if nums[0] > nums[-1]:
        large = nums[0]
    else:
        large = nums[-1]
    return [large] * 3


def make_ends(a):
    """
    Given a list of ints, return a new list length 2 containing the first and last elements from the original list.
    The original list will be length 1 or more.
    """
    if len(a) < 0:
        return a
    else:
        return [a[0], a[-1]]


def has23(nums):
    """
    Given an int list length 2, return True if it contains a 2 or a 3.
    """
    if (2 in nums) or (3 in nums):
        return True
    else:
        return False
