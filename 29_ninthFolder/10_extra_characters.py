# https://leetcode.com/problems/extra-characters-in-a-string/
# Question : You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s
# into one or more non-overlapping substrings such that each substring is present in dictionary. There may
# be some extra characters in s which are not present in any of the substrings.
# Return the minimum number of extra characters left over if you break up s optimally.
#
# Example 1: Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8.
# There is only 1 unused character (at index 4), so we return 1.
#
# Used : Trie with DP (like boxstacking but in reverse)
#        Initialize dp[start] with dp[start + 1] + 1.
#        Traverse the trie starting from the root and follow the characters of the substring, checking if
#           each character exists in the trie.
#        If a character is not found in the trie, break out of the for loop.
#        If a valid substring is found in the trie (node.is_word == true), update dp[start] by taking the
#           minimum of its current value and dp[end + 1].
#        Finally, return the value at dp[0].
# Logic: def minExtraChar(s, dictionary):
#        n = len(s)
#        root = self.buildTrie(dictionary)
#        dp = [0] * (n + 1)
#        for start in range(n - 1, -1, -1):
#           dp[start] = dp[start + 1] + 1
#           node = root
#           for end in range(start, n):
#               if s[end] not in node.children:
#                   break
#               node = node.children[s[end]]
#               if node.is_word:
#                   dp[start] = min(dp[start], dp[end + 1])
#        return dp[0]
# Complexity : O(N^2 + M⋅K)
# Let N be the total characters in the string.
# Let M be the average length of the strings in dictionary.
# Let K be the length of the dictionary.

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
        return root

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = self.buildTrie(dictionary)
        dp = [0] * (n + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]


if __name__ == "__main__":
    s = "leetscode"
    dictionary = ["leet", "code", "leetcode"]

    solution = Solution()
    print(solution.minExtraChar(s, dictionary))

    s = "sayhelloworld"
    dictionary = ["hello", "world"]
    print(solution.minExtraChar(s, dictionary))
