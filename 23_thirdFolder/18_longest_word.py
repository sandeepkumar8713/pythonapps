# CTCI : Q17_15_Longest_Word
# Question : Given a list of words, write a program to find the longest word made of other words
# in the list.
#
# Question Type : Generic
# Used : Sort the given word list based on length. Make a map and set all the values as true.
#        This map tells weather the given word is original word or not.
#        Now call this function over each of the word which tells weather it can be build
#        using other words.
#        We try to break the word at each element
#        def canBuildWord(word, originalWord, map):
#           if word in map and not originalWord:
#               return map[word]
#           for i in range(1, len(word)):
#               left = word[0:i], right = word[i:]
#               if left in map and map[left] and canBuildWord(right, False, map):
#                   return True
#           if not originalWord: map[word] = False
#           return False
# Complexity : O(n ^ 2)

import functools


def comparator(item1, item2):
    if len(item1) < len(item2):
        return -1
    elif len(item1) > len(item2):
        return 1
    else:
        return 0


def canBuildWord(word, originalWord, map):
    if word in map and not originalWord:
        return map[word]

    for i in range(1, len(word)):
        left = word[0:i]
        right = word[i:]
        if left in map and map[left] and canBuildWord(right, False, map):
            return True

    if not originalWord:
        map[word] = False
    return False


def printLongestWord(wordList):
    map = dict()
    for word in wordList:
        map[word] = True
    wordList = sorted(wordList, key=functools.cmp_to_key(comparator))
    longestWord = ""
    for word in wordList:
        if canBuildWord(word, True, map):
            print (word)
            if len(longestWord) < len(word):
                longestWord = word
    return longestWord


if __name__ == "__main__":
    wordList = ["be", "cause", "because", "tester", "testing", "testingtester", "test"]
    print ("Longest Word = %s" % printLongestWord(wordList))
