# https://leetcode.com/problems/single-number-iii/
# Question : Given an integer array nums, in which exactly two elements appear only once and all the other
# elements appear exactly twice. Find the two elements that appear only once. You can return the answer
# in any order. You must write an algorithm that runs in linear runtime complexity and uses only constant
# extra space.
#
# Question Type : Generic
# Used : Run a loop over given input array, do xor operation on all elements.
#        Find right most set bit of xor. This is the first bit which is different b/w 2 single elements.
#        Run a loop over the elements again while creating 2 categories which for set and unset at RMSB.
#        So same elements will go to same category. Different number will go different category.
#        Logic:
#        for ele in inpArr:
#           xor ^= ele
#        rmsb = xor & -xor
#        single1 = 0, single2 = 0
#        for ele in inpArr:
#           if ele & rmsb:
#               single1 ^= ele
#           else:
#               single2 ^= ele
#        return single1, single2
# Complexity : O(n)

def find2Single(inpArr):
    xor = 0
    for ele in inpArr:
        xor ^= ele

    # right most set bit
    rmsb = xor & -xor

    single1 = 0
    single2 = 0

    for ele in inpArr:
        if ele & rmsb:
            single1 ^= ele
        else:
            single2 ^= ele

    return single1, single2


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 2, 5]
    print (find2Single(nums))

    nums = [-1, 0]
    print(find2Single(nums))
