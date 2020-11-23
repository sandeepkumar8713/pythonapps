# Question : Given two arrays A1[] and A2[], sort A1 in such a way that the relative order among the elements will be
# same as those are in A2. For the elements not present in A2, append them at last in sorted order.
# Input: A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
#        A2[] = {2, 1, 8, 3}
# Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}
#
# Question Type : ShouldSee
# Used : Define your own comparator, Where compare indices of elements in A2 if present
#        1. If num1 and num2 both are in A2 then number with lower index in A2 will be treated smaller than other.
#        2. If only one of num1 or num2 present in A2, then that number will be treated smaller than the other which
#           doesn't present in A2.
#       3. If both are not in A2, then natural ordering will be taken.
# Complexity : O(n log n)

import functools


def search(key):
    if key in A2:
        return A2.index(key)
    else:
        return -1


def comparator(a, b):
    index1 = search(a)
    index2 = search(b)

    if index1 != -1 and index2 != -1:
        return index1 - index2
    elif index1 != -1:
        return -1
    elif index2 != -1:
        return 1
    else:
        return a-b


if __name__ == "__main__":
    A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8, 7, 5, 6, 9, 7, 5]
    A2 = [2, 1, 8, 3, 4]
    print(sorted(A1,  key=functools.cmp_to_key(comparator)))
