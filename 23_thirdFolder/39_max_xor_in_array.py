# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# Question : Given a non-empty array of numbers, a0, a1, a2,... , an-1, where 0 <= ai < 2^31.
# Find the maximum result of ai XOR aj, where 0 < i, j < n. Could you do this in O(n) runtime?
#
# Example: Input: [3, 10, 5, 25, 2, 8]
# Output: 28
# Explanation: The maximum result is 5 ^ 25 = 28.
#
# Question Type : ShouldSee
# Used : Make a trie of 2 children 0 and 1. Run a loop for each element. Insert the binary equivalent of the number
#        in trie and also traverse with opposite bit to find perfect pair for this element and keep updating xor result.
#        After the insertion update maxXor. After the array loop return maxXor.
#        Logic : def findMaxXor(inpArr):
#        root = Trie(), maxXor = 0
#        for num in inpArr:
#           curXor = 0, node = root, nodeXor = root
#           for j in range(31, -1, -1):
#               bit = (num >> j) & 1
#               if node.children[bit] is None:
#                   node.children[bit] = Trie()
#               node = node.children[bit]
#               toggleBit = 1 if bit == 0 else 0
#               if nodeXor.children[toggleBit] is not None:
#                   curXor = (curXor << 1) | 1
#                   nodeXor = nodeXor.children[toggleBit]
#               else:
#                   curXor = curXor << 1
#                   nodeXor = nodeXor.children[bit]
#           maxXor = max(maxXor, curXor)
#        return maxXor
# Complexity : O(n)


class Trie:
    def __init__(self):
        self.isWord = False
        self.children = [None, None]


def findMaxXor(inpArr):
    root = Trie()
    maxXor = 0
    for num in inpArr:
        curXor = 0
        node = root
        nodeXor = root
        for j in range(31, -1, -1):
            bit = (num >> j) & 1
            # insert the bit
            if node.children[bit] is None:
                node.children[bit] = Trie()
            node = node.children[bit]

            # Search for opposite number
            toggleBit = 1 if bit == 0 else 0
            if nodeXor.children[toggleBit] is not None:
                curXor = (curXor << 1) | 1
                nodeXor = nodeXor.children[toggleBit]
            else:
                curXor = curXor << 1
                nodeXor = nodeXor.children[bit]
        maxXor = max(maxXor, curXor)

    return maxXor


if __name__ == "__main__":
    inpArr = [3, 10, 5, 25, 2, 8]
    print(findMaxXor(inpArr))
