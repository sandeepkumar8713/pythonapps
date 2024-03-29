# https://leetcode.com/problems/knight-dialer/
# Question : A chess knight can move as indicated in the chess diagram below:
# This time, we place our chess knight on any numbered key of a phone pad (indicated above),
# and the knight makes N-1 hops. Each hop must be from one key to another numbered key.
# Each time it lands on a key (including the initial placement of the knight),
# it presses the number of that key, pressing N digits total. How many distinct numbers can
# you dial in this manner? Since the answer may be large, output the answer modulo 10^9 + 7.
#
# Example 1: Input: 1
# Output: 10
#
# Example 2: Input: 2
# Output: 20
#
# Question Type : ShouldSee
# Used : Run a loop to iterate through each hop.
#           For this hop, consider all possible positions and its corresponding next position and keep adding the
#           respective count.
#        Remember to use two 1d arrays.
#        By hand or otherwise, have a way to query what moves are available at each square.
#        This implies the exact recursion for f.
#        For example, from 1 we can move to 6, 8, so f(1, n) = f(6, n-1) + f(8, n-1).
#        After, let's keep track of dp[start] = f(start, n), and update it for each n from 1, 2, ..., N.
#        At the end, the answer is f(0, N) + f(1, N) + ... + f(9, N) = sum(dp).
# Logic: def knightDialer(N):
#        dp = [1] * 10
#        for hops in xrange(N-1):
#           dp2 = [0] * 10
#           for node, count in enumerate(dp):
#               for nei in moves[node]:
#                   dp2[nei] += count
#                   dp2[nei] %= MOD
#               dp = dp2
#        return sum(dp) % MOD
# Complexity : O(n^2)

MOD = 10 ** 9 + 7
moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
         [1, 7, 0], [2, 6], [1, 3], [2, 4]]


def knightDialer(N):
    dp = [1] * 10
    for hops in range(N-1):
        dp2 = [0] * 10
        for node, count in enumerate(dp):
            for nei in moves[node]:
                dp2[nei] += count
                dp2[nei] %= MOD
        dp = dp2
    return sum(dp) % MOD


if __name__ == "__main__":
    N = 2
    print(knightDialer(N))
