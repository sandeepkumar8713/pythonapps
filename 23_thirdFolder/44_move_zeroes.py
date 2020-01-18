# https://leetcode.com/problems/move-zeroes/
# Question : Given an array nums, write a function to move all 0's to the end of it while maintaining the relative
# order of the non-zero elements.
#
# Consider a n-ary tree (i.e. each parent node has at least one children (except the leafs) and up to n).
# Some children nodes may be missing, i.e. a parent node could have only n/2 children.
# The order of the children nodes matters here and, referring to them with their index i, a parent node with a child
# at index i is different than a parent node without a child at index i.
# That is, the missing children nodes can be positioned anywhere between the index 0 and n - 1, and are represented
# by None values innode.children. Write a recursive, in-place function which moves all missing children (i.e. the
# None values) to the right of the children list, and consequently, the valid children to the left.
# Don't return anything, write an in-place function.
# Examples:
# Suppose we consider 5-ary trees.
# 1 - A root node with the following list of children: [NodeA, Null, Null, NodeB, NodeC]would see its list of
# children changed to [NodeA, NodeB, NodeC, Null, Null].
# 2 - This needs to be done for every parent node in the tree which have a non-empty list of children. Hence,
# supposing NodeAhas the following list of children: [Null, Null, Null, Null, NodeD], this list would be thus
# changed to [NodeD, Null, Null, Null, Null].
#
# Example: Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Used : Run a loop, keep track of index where lastNonZeroFoundAt index. When a non zero element is found, swap it with
#        lastNonZeroFoundAt index and increment the index:
#        Logic : def moveZeroes(inpArr):
#        lastNonZeroFoundAt = 0
#        for i in range(len(inpArr)):
#           if inpArr[i] != 0:
#               inpArr[lastNonZeroFoundAt], inpArr[i] = inpArr[i], inpArr[lastNonZeroFoundAt]
#               lastNonZeroFoundAt += 1
#        return inpArr
# Complexity : O(n)


def moveZeroes(inpArr):
    lastNonZeroFoundAt = 0
    for i in range(len(inpArr)):
        if inpArr[i] != 0:
            inpArr[lastNonZeroFoundAt], inpArr[i] = inpArr[i], inpArr[lastNonZeroFoundAt]
            lastNonZeroFoundAt += 1
    return inpArr


if __name__ == "__main__":
    inpArr = [0, 1, 0, 3, 12]
    print moveZeroes(inpArr)

    inpArr = [15, 0, 1, 0, 3, 12]
    print moveZeroes(inpArr)
