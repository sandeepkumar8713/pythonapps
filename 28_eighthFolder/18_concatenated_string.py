# https://leetcode.com/problems/concatenated-words/
# Given an array of strings words (without duplicates), return all the concatenated words in the given
# list of words. A concatenated word is defined as a string that is comprised entirely of at least two
# shorter words (not necesssarily distinct) in the given array.
#
# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# Question Type : Generic, Similar Added
# Used : DP with DFS
#        Break the word at each index.
#        Check if left substr is already in wordset
#           Check if right substr is already in wordset or call DFS on it.
#               return True
# Logic: def dfs(word):
#        if word in dp.keys(): return dp[word]
#        for i in range(min_len, len(word)):
#           left_substr = word[:i]
#           right_substr = word[i:]
#           if left_substr in words_set:
#               if right_substr in words_set or dfs(right_substr):
#                   dp[word] = True
#                   return True
#        dp[word] = False
#        return False
# Complexity : O(n * m) n is count of words and m is length of longest word

import sys


def find_all_concatenated(words):
    res = []
    words_set = set(words)
    min_len = sys.maxsize
    dp = dict()

    def dfs(word):
        if word in dp.keys():
            return dp[word]

        for i in range(min_len, len(word)):
            left_substr = word[:i]
            right_substr = word[i:]
            if left_substr in words_set:
                if right_substr in words_set or dfs(right_substr):
                    dp[word] = True
                    return True

        dp[word] = False
        return False

    for word in words:
        min_len = min(len(word), min_len)

    for word in words:
        if dfs(word):
            res.append(word)

    return res


if __name__ == "__main__":
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    print(find_all_concatenated(words))
