# http://buttercola.blogspot.com/2016/01/leetcode-generalized-abbreviation.html
# Question : Write a function to generate the generalized abbreviations of a word.
#
# Example:
# Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#
# Question Type : Easy
# Used : We have to go through all possibilities i.e. choose 0,1,2,3,4 char and convert to abbreviation.
#        A classic DFS + backtracking problem. A trick here is if we've already abbrivate part of a word,
#        we must jump at least a character.
#        For each character, choose either abbreviate or not.
#        when the position == word length, update the list else, continuously backtracking
#        if abbreviate, update current string, cnt = 0, pos+1
#        if not abbreviate, current string not update, cnt+1, pos+1
#        Logic : def generateHelper(start, word, resultList):
#        if start >= len(word): return
#        i = start
#        while i < len(word):
#           j = 1
#           while i + j <= len(word):
#               abbr = word[0:i] + str(j) + word[i+j:]
#               resultList.append(abbr)
#               generateHelper(i + 1 + len(str(j)), abbr, resultList)
#               j += 1
#           i += 1
# Complexity : O(2^m) = mC0 + mC1 + mC2 + mC3 + mC4


def generateAbbreviations(word):
    resultList = []
    resultList.append(word)

    generateHelper(0, word, resultList)
    return resultList


def generateHelper(start, word, resultList):
    if start >= len(word):
        return

    i = start
    while i < len(word):
        j = 1
        while i + j <= len(word):
            abbr = word[0:i] + str(j) + word[i+j:]
            resultList.append(abbr)
            generateHelper(i + 1 + len(str(j)), abbr, resultList)
            j += 1
        i += 1


if __name__ == "__main__":
    wordList = generateAbbreviations("word")
    for item in wordList:
        print(item)
