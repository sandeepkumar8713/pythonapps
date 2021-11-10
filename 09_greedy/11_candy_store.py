# Question : In a candy store there are N different types of candies available and the prices
# of all the N different types of candies are provided. There is also an attractive offer by
# candy store. We can buy a single candy from the store and get at-most K other candies
# (all are different types) for free. Find minimum amount of money we have to spend to
# buy all the N different candies.
#
# Input :  price[] = {3, 2, 1, 4}
#                k = 2
# Output :  Min = 3, Max = 7
# Since k is 2, if we buy one candy we can take atmost two more for free.
# So in the first case we buy the candy which costs 1 and take candies worth 3 and 4 for
# free, also you buy candy worth 2 as well. So min cost = 1 + 2 = 3.
# In the second case we buy the candy which costs 4 and take candies worth 1 and 2 for
# free, also We buy candy worth 3 as well. So max cost = 3 + 4 = 7.
#
# Question Type : Generic
# Used : Sort the given array.
#        To find min, loop from left and reduce from right by k.
#        Loop while n >= 1.
#           Add arr[i] in sum and reduce n by k (n = n - k)
#        To find max, loop from right and increment left by k.
#        set start = 0 and end = 0
#        loop while end >= start, add arr[end] in sum,
#           reduce end = end - 1 and increment start = start + k
# Complexity : O(log n)


def findMinimum(arr, n, k):
    res = 0
    i = 0
    while n >= 1:
        res += arr[i]
        n = n - k
        i += 1

    return res


def findMaximum(arr, n, k):
    res = 0
    start = 0
    end = n - 1
    while end >= start:
        res += arr[end]
        start += k
        end -= 1

    return res


if __name__ == "__main__":
    arr = [3, 2, 1, 4]
    n = len(arr)
    k = 2
    arr.sort()
    print(findMinimum(arr, n, k), " ", findMaximum(arr, n, k))
