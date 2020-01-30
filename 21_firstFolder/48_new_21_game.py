# https://leetcode.com/problems/new-21-game/
# Question : Alice plays the following game, loosely based on the card game "21".
# Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she
# gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw
# is independent and the outcomes have equal probabilities. Alice stops drawing numbers when she gets K or more points.
# What is the probability that she has N or less points?
#
# Example : Input: N = 10, K = 1, W = 10
# Output: 1.00000
# Explanation:  Alice gets a single card, then stops.
#
# Question Type : ShouldSee
# Used : See the link for explanation.
#        Logic : def new21Game(N, K, W):
#        dp = [0.0] * (N + W + 1)
#        for k in xrange(K, N + 1): dp[k] = 1.0
#        S = min(N - K + 1, W)
#        for k in xrange(K - 1, -1, -1):
#           dp[k] = S / float(W)
#           S += dp[k] - dp[k + W]
#        return dp[0]
# Complexity : O(n)


def new21Game(N, K, W):
    dp = [0.0] * (N + W + 1)
    # dp[x] = the answer when Alice has x points
    for k in range(K, N + 1):
        dp[k] = 1.0

    S = min(N - K + 1, W)
    # S = dp[k+1] + dp[k+2] + ... + dp[k+W]
    for k in range(K - 1, -1, -1):
        dp[k] = S / float(W)
        S += dp[k] - dp[k + W]

    return dp[0]


if __name__ == "__main__":
    N = 10
    K = 1
    W = 10
    print(new21Game(N, K, W))
