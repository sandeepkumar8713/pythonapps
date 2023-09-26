# https://leetcode.com/problems/maximum-product-of-word-lengths/
# Question : Given a string array words, return the maximum value of length(word[i]) * length(word[j])
# where the two words do not share common letters. If no such two words exist, return 0.
#
# Example : Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
#
# Question Type : Generic
# Used : Make a bitmask for each word given in words list
#        Run 2 loops to make all possible pair of words
#        Do and operation of bit mask of each pair.
#        If ans is 0, then there is no overlap, so we can consider for product calculation.
#        Compare it with maxProd and update if required.
# Logic: maxProd = 0
#        for i in range(0, n - 1):
#           for j in range(i + 1, n):
#               if bitMaskList[i] & bitMaskList[j] == 0:
#                   prod = len(words[i]) * len(words[j])
#                   if prod > maxProd: maxProd = prod
#        return maxProd
# Complexity : O(n^2) where n is word count


def charToIndex(ch):
    return ord(ch) - ord('a')


def getBitMask(word):
    mainRegister = 0
    for ch in word:
        bitRepresent = 1
        i = charToIndex(ch)
        bitRepresent = bitRepresent << i
        mainRegister = mainRegister | bitRepresent
    return mainRegister


def maxProd(words):
    n = len(words)
    bitMaskList = []
    for word in words:
        bitMaskList.append(getBitMask(word))

    maxProd = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            # check no overlap
            if bitMaskList[i] & bitMaskList[j] == 0:
                prod = len(words[i]) * len(words[j])
                if prod > maxProd:
                    maxProd = prod
    return maxProd


if __name__ == "__main__":
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    print(maxProd(words))

    words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    print(maxProd(words))

    words = ["a", "aa", "aaa", "aaaa"]
    print(maxProd(words))
