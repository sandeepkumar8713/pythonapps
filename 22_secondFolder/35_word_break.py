# https://leetcode.com/problems/word-break/
# https://leetcode.com/problems/word-break/discuss/413047/Clean-DP-solution-with-comments-Python
# Question : Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated sequence
# of one or more dictionary words. The same word in the dictionary may be reused
# multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
#
# Example : Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#
# Question Type : Generic
# Used : We will use dp here. At each index of word we try to break the inpStr. Check if left part is
#        already breakable (using dp) and check if substring in right side is present in wordSet.
#        Logic : def wordBreak(inpStr, wordSet):
#        n = len(inpStr)
#        dp = [True] + [False] * n
#        for i in range(len(inpStr) + 1):
#           if not dp[i]: continue
#           for word in wordSet:
#               if len(word) <= len(inpStr[i:]):
#                   if word == inpStr[i:i + len(word)]:
#                       dp[i + len(word)] = True
#        return dp[n]
# Complexity : O(m * n) n is length on inpStr and m is length of wordSet


def wordBreak(inpStr, wordSet):
    n = len(inpStr)
    dp = [True] + [False] * n

    for i in range(len(inpStr) + 1):
        # if dp[i] is False we cannot start a new word at i
        if not dp[i]:
            continue

        # check all words - we can repeatedly use them!
        for word in wordSet:
            # check if candidate word fits in remaining seq
            if len(word) <= len(inpStr[i:]):
                if word == inpStr[i:i + len(word)]:
                    # set dp to True where next word search starts
                    dp[i + len(word)] = True

    return dp[n]


if __name__ == "__main__":
    inpStr = "leetcode"
    wordSet = {"leet", "code"}
    print(wordBreak(inpStr, wordSet))
