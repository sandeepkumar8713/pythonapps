# https://leetcode.com/problems/word-break-ii/
# https://leetcode.com/problems/word-break-ii/discuss/1509567/7-line-Python-DP-solution-easy-to-understand
# 22_secondFolder/35_word_break
# Question : Given a string s and a dictionary of strings wordDict, add spaces in s to construct a
# sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
# Example : Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
#
# Question Type : SimilarAdded
# Used : We will use map here. At each index of word we try to break the inpStr. Check if left part is
#        already breakable (using map) and check if substring in right side is present in wordSet.
#        keep extending the wordlist at given index.
#        After the loop, return the word set from last index of map.
# Logic: def wordBreak(inpStr, wordSet):
#        map[0] = [[]]
#        for i in range(n + 1):
#           if i not in map: continue
#           for word in wordSet:
#               if len(word) <= len(inpStr[i:]):
#                   if word == inpStr[i:i + len(word)]:
#                       wordList = [x + [word] for x in map[i]]
#                       if i + len(word) in map:
#                           map[i + len(word)].extend(wordList)
#                       else:
#                           map[i + len(word)] = wordList
#        return [' '.join(x) for x in map[n]]
# Complexity : O(m * n) n is length on inpStr and m is length of wordSet


from collections import defaultdict


def wordBreak(inpStr, wordSet):
    n = len(inpStr)
    map = dict()
    map[0] = [[]]

    for i in range(n + 1):
        if i not in map:
            continue
        for word in wordSet:
            if len(word) <= len(inpStr[i:]):
                if word == inpStr[i:i + len(word)]:
                    wordList = [x + [word] for x in map[i]]
                    if i + len(word) in map:
                        # We got multiple chooses to break word at i + len(word), so should extend the wordlist
                        map[i + len(word)].extend(wordList)
                    else:
                        map[i + len(word)] = wordList

    return [' '.join(x) for x in map[n]]


if __name__ == "__main__":
    s = "catsanddog"
    wordSet = ["cat", "cats", "and", "sand", "dog"]
    print(wordBreak(s, wordSet))

