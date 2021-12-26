# https://leetcode.com/problems/domino-and-tromino-tiling/
# Question : You have two types of tiles: a 2 x 1 domino shape and a tromino shape.
# You may rotate these shapes. Given an integer n, return the number of ways to tile an
# 2 x n board. Since the answer may be very large, return it modulo 109 + 7.
# In a tiling, every square must be covered by a tile. Two tilings are different if
# and only if there are two 4-directionally adjacent cells on the board such that exactly
# one of the tilings has both squares occupied by a tile.
#
# Question Type : ShouldSee
# Used : For example, I drew out the 2 by 4, and I noticed that I could basically make it a
#        2 by 3 tiling, but I add another 2 by 1 tile, and I can do this twice. So I knew my
#        recursive solution had to have a call to the n-1'th case, I also knew that it needs
#        to be multiplied by two because you can add the 2 by 1 tile to either end.
#        func(n) = 2 * func(n-1) + func(n-3)
#        Logic :
#        if n == 1: return 1
#        if n == 2: return 2
#        if n == 3: return 5
#        mod = 1000000007
#        three_down = 1, two_down = 2, one_down = 5
#        for i in range(4, n + 1):
#           tmp = (2 * one_down + three_down) % mod
#           three_down = two_down
#           two_down = one_down
#           one_down = tmp
#        return one_down
# Complexity : O(n)


def numTilings(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 5
    mod = 1000000007
    three_down = 1
    two_down = 2
    one_down = 5
    for i in range(4, n + 1):
        tmp = (2 * one_down + three_down) % mod
        three_down = two_down
        two_down = one_down
        one_down = tmp

    return one_down


if __name__ == "__main__":
    n = 3
    print(numTilings(n))

    n = 5
    print(numTilings(n))
