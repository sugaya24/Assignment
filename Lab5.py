""" Sorting Practice Problems """

# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.


def sort_half(alist):
    for _ in alist:
        for i in range(len(alist) // 2 - 1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        for j in range((len(alist) // 2), len(alist) - 1):
            if alist[j] < alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.


def merge_two(A, B):
    # A[i]とB[j]を比較
    # 超えるまでappend
    result = []
    i = 0
    j = 0
    aflag = True
    bflag = True
    while True:
        if i == len(A):
            aflag = False
        if j == len(B):
            bflag = False

        if aflag and bflag:
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
        elif aflag and not bflag:
            result.append(A[i])
            i += 1
        elif bflag and not aflag:
            result.append(B[j])
            j += 1

        if i == len(A) and j == len(B):
            break
    return result


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.


def replace_negative(mylist):
    result = []
    for i in mylist:
        if i < 0:
            result.append(0)
        else:
            result.append(i)
    return result
