# Question : Given two sequences, find the length of longest subsequence present in both of
# them. A subsequence is a sequence that appears in the same relative order, but not
# necessarily contiguous. Example: LCS for input Sequences ABCDGH and AEDFHR is ADH of length 3.
#
# Question Type : Generic
# Used : Call a recursive function lcs(X,Y,m,n)
#        If length of either of X or Y is 0 return 0
#        else If X[m-1] == Y[n-1] return 1 + lcs(X, Y, m - 1, n - 1) (If same increment value and call function)
#        else return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n)) (If not same, we have two option either to keep
#           element from X or Y. So call func on both and return the max value)
# Complexity : O(2^n)


def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(lcs(X, Y, len(X), len(Y)))
