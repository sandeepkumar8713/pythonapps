# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# Similar : 25_fifthFolder/46_burst_ballons
# Question : We are playing the Guessing Game. The game will work as follows:
# I pick a number between 1 and n.
# You guess a number.
# If you guess the right number, you win the game.
# If you guess the wrong number, then I will tell you whether the number I picked is higher or lower,
# and you will continue guessing.
# Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
# Given a particular n, return the minimum amount of money you need to guarantee a win regardless of
# what number I pick.
#
# Example : Input: n = 10
# Output: 16
#
# Question Type : Generic, SimilarAdded
# Used : For each number, assume it is the root of the BST, call the function on left and right
#        (take the max, because we want the worst case), and for each assumption (for each number as a root)
#        take the min between all assumptions. (min of the max)
# Complexity :


def getMoneyAmount(n):
    dp = dict()

    def dfs(l, r):
        if l >= r - 1:
            return 0

        if (l, r) not in dp:
            ans = float('inf')
            for curr in range(l, r):
                ans = min(max(dfs(l, curr), dfs(curr + 1, r)) + curr, ans)
            dp[(l, r)] = ans
        return dp[(l, r)]

    return dfs(1, n + 1)


if __name__ == "__main__":
    n = 10
    print(getMoneyAmount(n))
