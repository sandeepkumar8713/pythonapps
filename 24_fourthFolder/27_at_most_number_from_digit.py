# https://leetcode.com/articles/numbers-at-most-n-given-digit-set/
# Question : We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6','7','8','9'}.
# (Note that '0' is not included.) Now, we write numbers using these digits, using each digit as many times
# as we want.  For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.
# Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.
#
# Used : First, call a positive integer X valid if X <= N and X only consists of digits from D. Our goal is to find
#        the number of valid integers. Say N has K digits. If we write a valid number with k digits (k < K), then there
#        are (D.length} ^ k possible numbers we could write, since all of them will definitely be less than N.
#        Logic : atMostNGivenDigitSet(D, N):
#        string = str(N), K = len(string)
#        dp = [0] * K + [1]
#        for i in xrange(K-1, -1, -1):
#           for d in D:
#               if d < string[i]: dp[i] += len(D) ** (K-i-1)
#               elif d == string[i]: dp[i] += dp[i+1]
#        return dp[0] + sum(len(D) ** i for i in xrange(1, K))
# Complexity : O(log N * m) m is digit count N is max Number


def atMostNGivenDigitSet(D, N):
    string = str(N)
    K = len(string)
    dp = [0] * K + [1]
    # dp[i] = total number of valid integers if N was "N[i:]"

    for i in xrange(K-1, -1, -1):
        # Compute dp[i]
        for d in D:
            if d < string[i]:
                dp[i] += len(D) ** (K-i-1)
            elif d == string[i]:
                dp[i] += dp[i+1]

    return dp[0] + sum(len(D) ** i for i in xrange(1, K))


if __name__ == "__main__":
    D = ["1", "3", "5", "7"]
    N = 100
    print atMostNGivenDigitSet(D, N)
