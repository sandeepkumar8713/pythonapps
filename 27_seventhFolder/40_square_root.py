# https://leetcode.com/problems/sqrtx/
# Question : Given a non-negative integer x, return the square root of x
# rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# You have been given two integers 'N' and 'D', Your task is to find the square root of the
# number 'N' with precision up to 'D' decimal places i.e. the difference between your answer
# and the correct answer should be less than 10 ^ (-D).
# For example if N = 10 and D = 3, then your answer will be 3.162.
#
# Question Type : Generic
# Used : Binary search, from 0 to D, please make sure to increment the values
#        by the precision mentioned
# Logic: precision = 1
#        for _ in range(D):
#           precision /= 10
#        while left < right:
#           mid = left + ((right - left) / 2)
#           guess = mid * mid
#           if guess == N:
#               return mid
#           elif guess < N:
#               left = mid + precision
#           else:
#               right = mid - precision
#        return round(mid, D)
# Complexity : O(log n*10^D)
#              D is multiplied as we increased its left and right range

def sqrt(N, D):
    left = 0
    right = N

    precision = 1
    for _ in range(D):
        precision /= 10

    while left < right:
        mid = left + ((right - left) / 2)
        guess = mid * mid
        if guess == N:
            return mid
        elif guess < N:
            left = mid + precision
        else:
            right = mid - precision

    return round(mid, D)


if __name__ == "__main__":
    N = 10
    D = 3
    print (sqrt(N,D))
