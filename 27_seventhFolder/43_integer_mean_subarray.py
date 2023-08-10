# https://www.geeksforgeeks.org/generate-a-matrix-with-mean-of-each-subarray-of-each-row-as-an-integer/
# Question : Given two integers M and N, the task is to generate an MxN matrix having elements in
# range [1, MxN] such that the average of any subarray of any row is an integer. If it is not possible
# to do so, return -1.
#
# Examples:
# Input: M = 2, N = 3
# Output:
# 1 3 5
# 2 4 6
#
# Question Type : ShouldSee
# Used : Arrange in such a manner that each row has either all even numbers or all odd numbers.
#        Check if there are equal numbers of odd and even numbers and the MxN must be even.
#        If the number of rows is odd then, a valid arrangement is not possible because the odd and even elements
#        cannot be kept together. There will always be at least one row having both odd and even elements.
# Logic: if n == 1:
#           for i in range(1, m + 1):
#               print(i)
#           return
#        if m % 2 == 1:
#           print(-1)
#           return
#        else:
#           for i in range(1, m + 1):
#               num = i
#               for j in range(1, n + 1):
#                   print(num, end=" ")
#                   num += m
#               print("")
#           return
# Complexity : O(m*n)


def validArrangement(m, n):
    # m is row count
    # n is col count
    if n == 1:
        for i in range(1, m + 1):
            print(i)
        return

    # If m is odd, not possible
    if m % 2 == 1:
        print(-1)
        return

    else:
        for i in range(1, m + 1):
            num = i
            for j in range(1, n + 1):
                print(num, end=" ")
                num += m
            print("")
        return


# For each row, value will start from i+1 and increment with m

if __name__ == "__main__":
    m = 2
    n = 3
    validArrangement(m, n)
