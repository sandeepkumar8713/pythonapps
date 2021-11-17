# https://leetcode.com/problems/beautiful-arrangement/
# Question : Suppose you have n integers labeled 1 through n. A permutation of those n integers perm
# (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the
# following is true:
# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.
#
# Example : Input: n = 2
# Output: 2
#
# Question Type : ShouldSee
# Used : We have to use kind of backtracking. We have to permute all valid sequence.
#        First we pick 1, see at which all indices it can be placed. After placing it at
#        a valid index, repeat the above process for 2. It may continue till n. At this
#        point increment the counter by 1.
#        After the backtracking is complete, return counter value.
#        Logic :
#        def calculate(n, num, visited, count):
#        if num > n: count[0] += 1
#        for i in range(1, n+1):
#           if not visited[i] and (num % i == 0 or i % num == 0):
#             visited[i] = True
#             calculate(n, num + 1, visited, count)
#             visited[i] = False
#
#        calculate(n, 1, [False] * (n + 1), [0])
# Complexity : O(k) k is no. of valid permutation


def calculate(n, num, visited, count):
    if num > n:
        count[0] += 1

    for i in range(1, n+1):
        if not visited[i] and (num % i == 0 or i % num == 0):
            visited[i] = True
            calculate(n, num + 1, visited, count)
            visited[i] = False


def countArrangement(n):
    visited = [False] * (n + 1)
    count = [0]
    calculate(n, 1, visited, count)
    return count[0]


if __name__ == "__main__":
    n = 2
    print(countArrangement(n))

    n = 1
    print(countArrangement(n))
