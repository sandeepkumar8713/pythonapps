# https://leetcode.com/problems/longest-string-chain/
# Question : You are given an array of words where each word consists of lowercase English letters.
# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere
# in wordA without changing the order of the other characters to make it equal to wordB.
# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1
# is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is
# trivially a word chain with k == 1. Return the length of the longest possible word
# chain with words chosen from the given list of words.
#
# Example : Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"]
#
# Question Type : ShouldSee
# Used : This is similar to box stacking. We avoid 2 loops by sorting the array based on len.
#        Make a dp (dict) where key is word and value is chain len till that word.
#        Loop over the words array. For each ele, break it into all possible sub words
#        and check if sub words is already present in dp and update max len value.
#        Insert the word in dp with max chain len.
#        Logic:
#        words = sorted(words, key=len)
#        dp = {}, overrallMax = 0
#        for word in words:
#           chainLen = 1
#           for i in range(len(word)):
#               current_splice = word[:i] + word[i + 1:]
#               if current_splice in dp:
#                   chainLen = max(chainLen, dp[current_splice])
#           dp[word] = chainLen + 1
#           overrallMax = max(overrallMax, chainLen)
#        return overrallMax
# Complexity : O(n log n + n * k) where n is word count, k is length of longest word.


def longestStrChain(words):
    words = sorted(words, key=len)
    dp = {}
    overrallMax = 0

    for word in words:
        chainLen = 1
        for i in range(len(word)):
            current_splice = word[:i] + word[i + 1:]
            if current_splice in dp:
                chainLen = max(chainLen, dp[current_splice])

        dp[word] = chainLen + 1
        overrallMax = max(overrallMax, chainLen)

    return overrallMax


if __name__ == "__main__":
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(longestStrChain(words))
