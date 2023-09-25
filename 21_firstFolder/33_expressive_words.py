# https://leetcode.com/problems/expressive-words/solution/
# Question : Sometimes people repeat letters to represent extra feeling, such as
# "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo",
# we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".
# For some given string S, a query word is stretchy if it can be made to be equal to
# S by any number of applications of the following extension operation: choose a group
# consisting of characters c, and
# add some number of characters c to the group so that the size of the group is 3 or more.
#
# Example: Input:
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
#
# Question Type : Generic
# Used : Make a function getCharCount() which returns unique chars and respective freq in tuple
#        Now compare S with each word. If the unique char doesn't match skip it. Else each char
#        count should be equal or more in S then increase count by 1.
# Logic: def expressiveWords(S, words):
#        uniqueCharTuple, count = getCharCount(S)
#        ans = 0
#        for word in words:
#           uniqueCharCount2, count2 = getCharCount(word)
#           if uniqueCharCount2 != uniqueCharTuple: continue
#           match = True
#           for c1, c2 in zip(count, count2):
#               match = match and (c1 >= max(c2, 3) or c1 == c2)
#            ans += match
#        return ans
# Complexity : O(nm) n is the length of words (at least 1), and m is the maximum length of
#              a word.


def getCharCount(word):
    freqDict = dict()
    uniqueCharTuple = ()
    for c in word:
        if c in freqDict.keys():
            freqDict[c] += 1
        else:
            freqDict[c] = 1
            uniqueCharTuple = uniqueCharTuple + (c,)
    charCountTuple = ()
    for c in uniqueCharTuple:
        charCountTuple = charCountTuple + (freqDict[c],)
    return uniqueCharTuple, charCountTuple


def expressiveWords(S, words):
    uniqueCharTuple, count = getCharCount(S)
    ans = 0
    for word in words:
        uniqueCharCount2, count2 = getCharCount(word)
        if uniqueCharCount2 != uniqueCharTuple:
            continue
        match = True
        for c1, c2 in zip(count, count2):
            match = match and (c1 >= max(c2, 3) or c1 == c2)
        ans += match

    return ans


if __name__ == "__main__":
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(expressiveWords(S, words))
