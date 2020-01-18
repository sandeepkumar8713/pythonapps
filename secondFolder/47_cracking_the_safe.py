# https://leetcode.com/problems/cracking-the-safe/
# Question : While entering a password, the last n digits entered will automatically be matched against
# the correct password. For example, assuming the correct password is "345", if you type "012345",
# the box will open because the correct password matches the suffix of the entered password.
# Return any password of minimum length that is guaranteed to open the box at some point of entering it.
#
# Example : Input: n = 1, k = 2
# Output: "01"
# Note: "10" will be accepted too.
#
# Example : Input: n = 2, k = 2
# Output: "00110"
# Note: "01100", "10011", "11001" will be accepted too.
#
# Used : def crackSafe(n, k):
#        M = k**(n-1)
#        P = []
#        for i in xrange(k):
#           for q in xrange(M):
#               P.append(q*k+i)
#        ans = []
#        for i in xrange(k**n):
#           j = i
#           while P[j] >= 0:
#               ans.append(str(j / M))
#               P[j], j = -1, P[j]
#        return "".join(ans) + "0" * (n-1)
# Complexity : O(k^n)


def crackSafe(n, k):
    M = k**(n-1)

    P = []
    for i in xrange(k):
        for q in xrange(M):
            P.append(q*k+i)

    ans = []
    for i in xrange(k**n):
        j = i
        while P[j] >= 0:
            ans.append(str(j / M))
            P[j], j = -1, P[j]

    return "".join(ans) + "0" * (n-1)


if __name__ == "__main__":
    n = 1
    k = 2
    print crackSafe(n, k)

    n = 2
    k = 2
    print crackSafe(n, k)

    n = 4
    k = 2
    print crackSafe(n, k)
