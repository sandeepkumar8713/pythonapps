# https://www.geeksforgeeks.org/dynamic-programming-set-17-palindrome-partitioning/
# Question : Given a string, a partitioning of the string is a palindrome partitioning if every substring of the
# partition is a palindrome. For example, "aba|b|bbabb|a|b|aba" is a palindrome partitioning of "ababbbabbababa".
# Determine the fewest cuts needed for palindrome partitioning of a given string. For example, minimum 3 cuts are
# needed for "ababbbabbababa". The three cuts are "a|babbbab|b|ababa". If a string is palindrome, then minimum 0
# cuts are needed. If a string of length n containing all different characters, then minimum n-1 cuts are needed.
#
# Question Type : Generic
# Used : Call a recursive function minPalinPartition. Maintain a map dp size : n*n such that
#        dp[i][j] is return true if inpStr[i..j] is palindrome. Maintain a array minCuts size : n
#        such that minCuts[i] gives min cuts for inpStr[0..i].
#        Run a loop from length L : 2 to n.
#           Run a loop from i: 0 to n-L. set otherEnd j = i + L - 1.
#           If L == 2:  dp[i][j] = inpStr[i] == inpStr[j]
#           else: dp[i][j] = inpStr[i] == inpStr[j] and dp[i + 1][j - 1]
#        Now loop from i: 0 to n:
#           if dp[0][i] is True: minCuts[i] = 0
#           Else : loop from j : 0 to i:
#                   if dp[j+1][i] == True and 1 + minCuts[j] < minCuts[i]:
#                       minCuts[i] = minCuts[j] + 1 (take via path)
#        return minCuts[n-1]
# Complexity : O(n^2)


import sys


def minPalinPartition(inpStr):
    n = len(inpStr)

    minCuts = [sys.maxsize] * n

    dp = []
    for i in range(n):
        dp.append([False] * n)

    # 1 char is a palindrome
    for i in range(n):
        dp[i][i] = True

    # L is length of string
    for L in range(2, n + 1):
        for i in range(0, n - L):
            j = i + L - 1
            if L == 2:
                dp[i][j] = inpStr[i] == inpStr[j]
            else:
                dp[i][j] = inpStr[i] == inpStr[j] and dp[i + 1][j - 1]

    for i in range(n):
        # the word itself is a palindrome
        if dp[0][i] is True:
            minCuts[i] = 0
        else:
            # if we cut at j, and check if j+1 to i is palindrome, then take via path
            for j in range(0, i):
                if dp[j + 1][i] and 1 + minCuts[j] < minCuts[i]:
                    minCuts[i] = minCuts[j] + 1

    return minCuts[n - 1]


if __name__ == "__main__":
    inpStr = "ababbbabbababa"
    print(minPalinPartition(inpStr))
