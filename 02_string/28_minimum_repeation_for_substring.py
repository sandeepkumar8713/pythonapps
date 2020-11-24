# https://www.geeksforgeeks.org/minimum-number-of-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it/
# Question : Given two strings A and B. The task is to find the minimum number of times A has to be repeated such
# that B is a substring of it. If no such solution exists print -1.
#
# Examples: Input : A = "abcd", B = "cdabcdab"
# Output : 3
#
# Input : A = "ab", B = "cab"
# Output : -1
#
# Question Type : Generic
# Used : Keep appending A to S, until len(S) < len(B). Then check if B is substring of S.
#        If true return append count.
#        Else check once more with S+A.
#        Else return -1.
# Complexity : O(n * n) Substring matching for string of size n


def minRepetation(A, B):
    ans = 1
    S = A
    while len(S) < len(B):
        S += A
        ans +=1

    if B in S:
        return ans

    if B in (S+A):
        return ans + 1

    return -1


if __name__ == "__main__":
    A = "abcd"
    B = "cdabcdab"

    # A = "ab"
    # B = "cab"
    print(minRepetation(A, B))

