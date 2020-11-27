# CTCI : Q10_02_Group_Anagrams
# https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together-set-2/
# Question : Given an array of words, print all anagrams together. For example, if the given array is
# {"cat", "dog", "tac", "god", "act"}, then output may be "cat tac act dog god".
#
# Question Type : ShouldSee
# Used : In trie Node add two fields : children (list of size 26) and wordEndingID
#        (list of id of words ending at this node)
#        Loop over the given list of words. Sort the word and insert it in Trie and also insert its id,
#        where the word ends.
#        Now traverse the Trie again (DFS) and if there are id in wordEndingID: print them
# Complexity : O(n * m * log m) + O(m)    m is MAX_CHAR and n is word count

MAX_CHAR = 26


def charToIndex(ch):
    return ord(ch) - ord('a')


class TrieNode:
    def __init__(self):
        self.children = [None] * MAX_CHAR
        self.wordEndingID = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, inpStr, wordId):
        temp = self.root
        inpStrLen = len(inpStr)
        for level in range(inpStrLen):
            index = charToIndex(inpStr[level])
            if not temp.children[index]:
                temp.children[index] = TrieNode()
            temp = temp.children[index]

        temp.wordEndingID.append(wordId)

    def traverseUtils(self,root):
        temp = root
        for child in temp.children:
            # Do DFS here
            if child is not None:
                self.traverseUtils(child)
                for wordId in child.wordEndingID:
                    print (inpWords[wordId]),

    def traverse(self):
        self.traverseUtils(self.root)


def printAllAnagramTogether(words):
    trie = Trie()
    wordId = 0
    for word in words:
        trie.insert(sorted(word), wordId)
        wordId += 1

    trie.traverse()


if __name__ == '__main__':
    inpWords = ["cat", "dog", "tac", "god", "act", "gdo"]
    printAllAnagramTogether(inpWords)
