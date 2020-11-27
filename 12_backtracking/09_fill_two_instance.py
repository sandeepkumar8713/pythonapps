# https://www.geeksforgeeks.org/fill-two-instances-numbers-1-n-specific-way/
# Question : Given a number n, create an array of size 2n such that the array contains 2 instances of every
# number from 1 to n, and the number of elements between two instances of a number i is equal to i. If such a
# configuration is not possible, then print the same.
#
# Examples:
# Input: n = 3
# Output: res[] = {3, 1, 2, 1, 3, 2}
#
# Question Type : Generic
# Used : Make a res array with size 2n.
#        Run a loop i from 0 to 2n-curr-1:
#           place curr at i and i + curr + 1 and recurr for next curr - 1
#           If recurr function return True, then return true else backtrack
#        return False
#        fillUtil(res, curr, n):
#        if curr == 0: return True
#        for i in range(2 * n - curr - 1):
#           if res[i] == 0 and res[i + curr + 1] == 0:
#               res[i] = res[i + curr + 1] = curr
#               if fillUtil(res, curr - 1, n): return True
#               res[i] = 0, res[i + curr + 1] = 0
#        return False
# Complexity : O(n ^ n)


def fillUtil(res, curr, n):
    if curr == 0:
        return True

    # Try placing two instances of 'curr' at all possible locations till solution is found
    for i in range(2 * n - curr - 1):
        # Two 'curr' should be placed at 'curr+1' distance
        if res[i] == 0 and res[i + curr + 1] == 0:

            # Place two instances of 'curr'
            res[i] = res[i + curr + 1] = curr

            # Recur to check if the above placement leads to a solution
            if fillUtil(res, curr - 1, n):
                return True

            # If solution is not possible, then backtrack
            res[i] = 0
            res[i + curr + 1] = 0
    return False


def fill(n):
    res = [0] * (2 * n)

    if fillUtil(res, n, n):
        print(res)
    else:
        print("Not Possible")


if __name__ == '__main__':
    fill(7)
