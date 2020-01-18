# https://leetcode.com/problems/single-number-ii/discuss/400770/Python-faster-than-97.6-with-math
# https://leetcode.com/problems/single-number-ii/
# Question : Given a non-empty array of integers, every element appears three times except for one, which appears
# exactly once. Find that single one. Your algorithm should have a linear runtime complexity. Could you implement it
# without using extra memory?
#
# Example : Input: [2,2,3,2]
# Output: 3
#
# Used : Make a set of given inpArr. Sum it and multiply by 3. Subtract it with sum of inpArr. We will get the twice of
#        missing number.
#        Logic :
#        sumOfSet = 3 * sum(set(inpArr))
#        sumOfInpArr = sum(inpArr)
#        return (sumOfSet - sumOfInpArr) // 2
# Complexity : O(n)


def findSingleNumber(inpArr):
    sumOfSet = 3 * sum(set(inpArr))
    sumOfInpArr = sum(inpArr)
    return (sumOfSet - sumOfInpArr) // 2


if __name__ == "__main__":
    # inpArr = [2, 2, 3, 2]
    inpArr = [0, 1, 0, 1, 0, 1, 99]
    print findSingleNumber(inpArr)
