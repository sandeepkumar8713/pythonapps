# https://leetcode.com/problems/word-break-ii/
# https://leetcode.com/problems/word-break-ii/discuss/1509567/7-line-Python-DP-solution-easy-to-understand
# 22_secondFolder/35_word_break
# Question : Given a string s and a dictionary of strings wordDict, add spaces in s to construct a
# sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
# Example :
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
#
# Question Type : ShouldSee
# Used :
# Complexity :
#
# TODO ::

from collections import defaultdict


class Solution:
    def wordBreak(self, s, wordDict):
        # Use a dp dict to store until pos=i what could be the word break choices
        # e.g. s='abcd', dp[3] = [['abc', 'd'], ['ab', 'cd']] assuming they are valid words
        dp = defaultdict(list)
        # Initialize with pos=-1 an empty list of list, so when the first word come in, it finds pos=-1 to attach new words to it
        dp[-1] = [[]]

        for i in range(len(s)):
            for word in wordDict:
                # At pos=i, find forward if there is a substring end at pos=i that matches with a word in wordDict
                # Besides, dp[i-len(word)] should exist, otherwise there is no valid break-word choices at pos=i-len(word)
                if i >= len(word) - 1 and s[i + 1 - len(word):i + 1] == word and i - len(word) in dp:
                    # If yes, attach the new word to existing break choices at dp[i-len(word)] and add to current choices
                    dp[i] += [x + [word] for x in dp[i - len(word)]]

        return [' '.join(x) for x in dp[len(s) - 1]]  # the dp[last] corresponds to the result
