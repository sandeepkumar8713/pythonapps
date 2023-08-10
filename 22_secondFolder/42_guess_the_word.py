# https://leetcode.com/problems/guess-the-word/
# https://leetcode.com/problems/guess-the-word/discuss/411298/20-lines-of-python.
# Question : We are given a word list of unique words, each word is 6 letters long, and one word
# in this list is chosen as secret.You may call master.guess(word) to guess a word.  The guessed
# word should have type string and must be from the original list with 6 lowercase letters.
# This function returns an integer type, representing the number of exact matches
# (value and position) of your guess to the secret word. Also, if your guess is not
# in the given wordlist, it will return -1 instead. For each test case, you have
# 10 guesses to guess the word. At the end of any number of calls, if you have made 10
# or less calls to master.guess and at least one of these guesses was the secret, you
# pass the testcase.
#
# Example 1:
# Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
# Explanation:
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
#
# Question Type : Easy
# Used : Pre-compute similarity between two words. do that for every words.
#        Example: 'abcdef' and 'cccwqf' c on index 2 and f on index 5 matched.
#        so similarity score = 2. Save in wordEdge dict.
#        Pick One word and master.guess it. If it returns 6, we got match.
#        Else use the wordEdge, to find which all
#        words had same similarity score (Our secret is among them).
#        Repeat the above process. This way we would reduce the word list count.
# Logic: def findSecretWord(wordlist, master):
#        wordEdge = defaultdict(lambda: defaultdict(list))
#        for i in range(len(wordlist)):
#           for j in range(i+1, len(wordlist)):
#               word_1 = wordlist[i]
#               word_2 = wordlist[j]
#               simScore = similarity(word_1, word_2)
#               wordEdge[word_1][simScore].append(word_2)
#               wordEdge[word_2][simScore].append(word_1)
#
#        chance = 10
#        while chance > 0 and wordlist:
#           matched = master.guess(wordlist[0])
#           if matched == 6:
#               print "word found", (wordlist[0])
#               return
#           word = wordlist.pop(0)
#           wordlist = list(set(wordlist) & set(wordEdge[word][matched]))
#           chance -= 1
#        print "guess over"
# Complexity : O(n^2) n is count of words

from collections import defaultdict


def similarity(word_1, word_2):
    return len([i for i in range(6) if word_1[i] == word_2[i]])


class Master:
    def __init__(self, secret, wordList):
        self.secret = secret
        self.wordList = wordList[:]

    def guess(self, word):
        if word not in self.wordList:
            return -1
        return similarity(self.secret, word)


def findSecretWord(wordlist, master):
    wordEdge = defaultdict(lambda: defaultdict(list))

    for i in range(len(wordlist)):
        for j in range(i+1, len(wordlist)):
            word_1 = wordlist[i]
            word_2 = wordlist[j]
            simScore = similarity(word_1, word_2)
            wordEdge[word_1][simScore].append(word_2)
            wordEdge[word_2][simScore].append(word_1)

    # for key in wordEdge:
    #     print key, wordEdge[key]

    chance = 10
    while chance > 0 and wordlist:
        matched = master.guess(wordlist[0])
        if matched == 6:
            print("Word found:", (wordlist[0]))
            return
        word = wordlist.pop(0)
        # We keep wordList to make sure it has not been removed earlier.
        wordlist = list(set(wordlist) & set(wordEdge[word][matched]))
        # print matched
        # print wordlist
        chance -= 1

    print("Guess over")


if __name__ == "__main__":
    secret = "abcczz"
    wordlist = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
    master = Master(secret, wordlist)
    findSecretWord(wordlist, master)
