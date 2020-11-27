# https://www.geeksforgeeks.org/print-valid-words-possible-using-characters-array/
# Question : Given a dictionary and a character array, print all valid words that are possible using
# characters from the array.
#
# Input : Dict - {"go","bat","me","eat","goal",
#                                 "boy", "run"}
#         arr[] = {'e','o','b', 'a','m','g', 'l'}
# Output : go, me, goal.
#
# Question Type : Generic
# Used : Prepare a trie using given words. Make a hash set of input characters.
#        Call recursive function searchWord(root, hashSet, resStr)
#           If root isEndOfWord print resStr
#           Loop over the character in hashSet. If that char is present in children of root,
#               then call searchWord() over that child and append the char to resStr.
#               searchWord(root.children[charToIndex(char)], hashSet, resStr + char)
# Complexity : To prepare Trie O(n * m) where n is number of words and m is max length of word
#              To search one word O(k * m) where k is length of input character

MAX_CHAR = 26


def charToIndex(ch):
    return ord(ch) - ord('a')


class TrieNode:
    def __init__(self):
        self.children = [None] * MAX_CHAR
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, insStr):
        temp = self.root
        for level in range(len(insStr)):
            index = charToIndex(insStr[level])
            if not temp.children[index]:
                temp.children[index] = TrieNode()
            temp = temp.children[index]

        temp.isEndOfWord = True


def searchWord(root, hashSet, resStr):
    if root.isEndOfWord is True:
        print(resStr)

    # I have got the bag of char, traverse the trie to see if a word can be found using this bag
    for char in hashSet:
        if root.children[charToIndex(char)] is not None:
            searchWord(root.children[charToIndex(char)], hashSet, resStr + char)


def printAllWords(inpArr, trie):
    hashSet = set()
    for char in inpArr:
        hashSet.add(char)

    resStr = ""
    searchWord(trie.root, hashSet, resStr)


if __name__ == '__main__':
    words = ["go", "bat", "me", "eat", "goal", "boy", "run", "goale"]
    inpArr = {'e', 'o', 'b', 'a', 'm', 'g', 'l'}
    t = Trie()
    for word in words:
        t.insert(word)

    printAllWords(inpArr, t)
