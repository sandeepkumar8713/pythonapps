# https://massivealgorithms.blogspot.com/2019/03/leetcode-805-split-array-with-same.html
# https://leetcode.com/problems/split-array-with-same-average/
# https://leetcode.com/problems/split-array-with-same-average/discuss/120830/DP-with-bitset-over-size
# Question : In a given integer array A, we must move every element of A to either list B or list C.
# (B and C initially start empty.)
# Return true if and only if after such a move, it is possible that the average value of B is equal
# to the average value of C, and B and C are both non-empty.
#
# Example : Input: [1,2,3,4,5,6,7,8]
# Output: true
#
# Question Type : ShouldSee
# Used : Make a array of size sum. Bit n of dp[s] tells me whether it's possible
#        to build a subset of size n with sum s
#        p = [1] * (totalSum + 1)
#        for item in inpArr:
#           remainderSum = totalSum - item
#           while remainderSum >= 0:
#               p[remainderSum+item] |= p[remainderSum] << 1
#               remainderSum -= 1
#        i = 1
#        while i < n:
#           if (totalSum * i) % n == 0 and p[(totalSum * i) / n] & 1 << i:
#               return True
#           i += 1
#        return False
# Complexity : O(n * m) where m is sum
# TODO :: Look for other solution as, here n can't go beyond 32


def splitArraySameAverage(inpArr):
    totalSum = sum(inpArr)
    n = len(inpArr)
    p = [1] * (totalSum + 1)
    for item in inpArr:
        remainderSum = totalSum - item
        while remainderSum >= 0:
            p[remainderSum+item] |= p[remainderSum] << 1
            remainderSum -= 1
    i = 1
    while i < n:
        if (totalSum * i) % n == 0 and p[(totalSum * i) // n] & 1 << i:
            return True
        i += 1
    return False


def givePair(n):
    res = set()
    for i in range(n):
        for j in range(n):
            if i != j:
               if (j, i) not in res:
                res.add((i, j))

    return res


def test(inpArr):
    totalSum = sum(inpArr)
    res = givePair(len(inpArr))
    for pair in res:
        A = inpArr[pair[0]] + inpArr[pair[1]]
        B = totalSum - A
        if A / 2 == B / 6:
            print(pair)


if __name__ == "__main__":
    inpArr = [1, 2, 3, 4, 5, 6, 7, 8]
    #inpArr = [7,8]
    print(splitArraySameAverage(inpArr))
    test(inpArr)
