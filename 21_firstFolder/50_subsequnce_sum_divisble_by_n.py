# https://stackoverflow.com/questions/54048132/number-of-subsequences-whose-sum-is-divisible-by-k
# Similar https://www.geeksforgeeks.org/number-subsequences-string-divisible-n/
# Question : Given an array of both positive and negative number of size n. Write a program
# to return a subsequence whose sum is divisible by n else return -1.
#
# Input : [1, 2, -5, 11, 48, 29, 92, 29, 546, 32]  n = 10
# Output : True 48 + 2 = 50/10
#
# Input : [7 7 7 7 111 7 7 7 7 14] n = 10
# Output : True 70/10
#
# Question Type : Asked
# Used : We take dp approach here. Make a 2d array dp of size n*n, initial value set to 0.
#        dp[i][j] indicates whether subsequences in string [0..i] leaves remainder j after division by n.
#        While loop through the 2d matrix we come 3 possible ways to set the value.
#        1. str[i] when divided by n gives j. So dp[i][j] = True
#        2. If we exclude str[i] to form subsequence, use the previous subresult. dp[i][j] |= dp[i - 1][j]
#        3. If we include str[i] to form subsequence, add the previous subresult with str[i] to set
#           value in this row. So dp[i][(j + inpArr[i]) % n] |= dp[i - 1][j] (use previous rem j)
#        Subsequence is possible if dp[n - 1][0] is True.
# Logic: def countDivisibleSubseq(inpArr):
#        n = len(inpArr)
#        dp = [[0 for x in range(n)]
#                 for y in range(n)]
#        dp[0][inpArr[0] % n] |= True
#        for i in range(1, n):
#           dp[i][inpArr[i] % n] |= True
#           for j in range(n):
#               dp[i][j] |= dp[i - 1][j]
#               dp[i][(j + inpArr[i]) % n] |= dp[i - 1][j]
#        if dp[n - 1][0] == 1:
#           return getValue(dp, inpArr, n)
#        else:
#           return -1
#
#        def getValue(dp,str,n):
#        result = [], col = 0
#        for i in range(n-1, -1, -1):
#           if str[i] % n == 0:
#               result = [str[i]], break
#           if i >= 1 and dp[i-1][col] == 1:
#               continue
#           else:
#               result.append(str[i])
#               col = ((col + n) - abs(str[i])) % n
#               if sum(result) % n == 0: break
#        result.reverse()
#        return result
# Complexity : O(n^2)


def countDivisibleSubseq(inpArr):
    n = len(inpArr)

    # division by n can leave only n remainder
    # [0..n-1]. dp[i][j] indicates number of
    # subsequences in string [0..i] which leaves
    # remainder j after division by n.
    dp = [[0 for x in range(n)]
          for y in range(n)]

    # Filling value for first digit in str
    dp[0][inpArr[0] % n] |= True

    for i in range(1, n):

        # start a new subsequence with index i
        dp[i][inpArr[i] % n] |= True

        for j in range(n):
            # exclude i'th character from all the
            # current subsequences of string [0...i-1]
            dp[i][j] |= dp[i - 1][j]

            # include i'th character in all the current
            # subsequences of string [0...i-1]
            dp[i][(j + inpArr[i]) % n] |= dp[i - 1][j]

    if dp[n - 1][0] == 1:
        return getValue(dp, inpArr, n)
    else:
        return -1


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
    return result


if __name__ == "__main__":
    str = [1, 2, -5, 11, 23, 48, 92, 29, 546, 32]
    print(countDivisibleSubseq(str))

    str = [1, 2, -5, 11, 48, 29, 92, 29, 546, 32]
    print(countDivisibleSubseq(str))

    str = [5, 7, 19]
    print(countDivisibleSubseq(str))

    str = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
    print(countDivisibleSubseq(str))

    str = [7, 7, 7, 7, 2, 7, 7, 7, 7, 14]
    print(countDivisibleSubseq(str))
