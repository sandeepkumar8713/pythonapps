# Similar https://www.geeksforgeeks.org/number-subsequences-string-divisible-n/
# https://stackoverflow.com/questions/54048132/number-of-subsequences-whose-sum-is-divisible-by-k
# Question : Given an array of both positive and negative number of size n. Write a program to return a subsequence
# whose sum is divisible by n else return -1.
#
# Input : [1, 2, -5, 11, 48, 29, 92, 29, 546, 32]  n = 10
# Output : True 48 + 2 = 50/10
#
# Input : [7 7 7 7 111 7 7 7 7 14] n = 10
# Output : True 70/10
#
# Used : TODO :: add used
# Complexity : O(n^2)


def countDivisibleSubseq(str, n):
    l = len(str)

    # division by n can leave only n remainder
    # [0..n-1]. dp[i][j] indicates number of
    # subsequences in string [0..i] which leaves
    # remainder j after division by n.
    dp = [[0 for x in range(l)]
          for y in range(n)]

    # Filling value for first digit in str
    dp[0][str[0] % n] |= True

    for i in range(1, l):

        # start a new subsequence with index i
        dp[i][str[i] % n] |= True

        for j in range(n):
            # exclude i'th character from all the
            # current subsequences of string [0...i-1]
            dp[i][j] |= dp[i - 1][j]

            # include i'th character in all the current
            # subsequences of string [0...i-1]
            dp[i][(j + str[i]) % n] |= dp[i - 1][j]

        # for item in dp:
        #     print(item)
        # print("")

    getValue(dp, str, n)

    return dp[l - 1][0]


def getValue(dp,str,n):
    result = []
    col = 0
    for i in range(n-1, -1, -1):
        if str[i] % n == 0:
            result = [str[i]]
            break
        if i >= 1 and dp[i-1][col] == 1:
            continue
        else:
            result.append(str[i])
            col = ((col + n) - abs(str[i])) % n
            if sum(result) % n == 0:
                break

    result.reverse()
    print(result)


if __name__ == "__main__":
    str = [1, 2, -5, 11, 23, 48, 92, 29, 546, 32]
    n = 10
    print(countDivisibleSubseq(str, n))

    str = [1, 2, -5, 11, 48, 29, 92, 29, 546, 32]
    n = 10
    print(countDivisibleSubseq(str, n))

    str = [5, 7, 19]
    n = 3
    print(countDivisibleSubseq(str, n))

    str = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    n = 10
    print(countDivisibleSubseq(str, n))

    str = [7, 7, 7, 7, 2, 7, 7, 7, 7, 14]
    n = 10
    print(countDivisibleSubseq(str, n))
