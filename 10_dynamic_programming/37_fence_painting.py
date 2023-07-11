# https://cheonhyangzhang.gitbooks.io/leetcode-solutions/content/276-paint-fence.html
# https://leetcode.com/problems/paint-fence/
# Question : There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.
# Note: n and k are non-negative integers.
#
# Question Type : Generic
# Used : If n == 1, there would be k-ways to paint.
#        If n == 2, there would be two situations:
#           You paint same color with the previous post: k*1 ways to paint,
#               named it as same;
#           You paint differently with the previous post: k*(k-1) ways to paint this way,
#               named it as diff.
#        If n == 3,
#          Since previous two are in the same color, next one you could only paint differently,
#           and it would form one part of “paint differently” case in the n == 3 level, and
#           the number of ways to paint this way would equal to same*(k-1).
#          Since previous two are not the same, you can either paint the same color this time
#            (diff*1) ways to do so, or stick to paint differently (diff*(k-1)) times.
# Logic: if n == 1: return k
#        same = k
#        diff = k * (k - 1)
#        for _ in range(3, n + 1):
#           same, diff = diff, (same + diff) * (k - 1)
#        return same + diff
# Complexity : O(n)

def numWays(n, k):
    if k == 0 or n == 0:
        return 0
    if n == 1:
        return k

    same = k
    diff = k * (k - 1)
    for _ in range(3, n + 1):
        same, diff = diff, (same + diff) * (k - 1)

    return same + diff


if __name__ == "__main__":
    n = 3
    k = 2
    print(numWays(n, k))
