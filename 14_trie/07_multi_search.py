# CTCI : Q17_17_Multi_Search
# Question : Given a string band an array of smaller strings T, design a method to search b for
# each small string in T.
#
# Example:
# T = {"is", "ppi", "hi", "sis", "i", "ssippi"}
# b = "mississippi"
#
# Question Type : Generic
# Used : Insert the words of the array in trie.
#        Now loop through each character of big word. Find all the words present in trie which start
#        with this character. Save the words and its is location (in big word) in a map.
#        After the loop complete return the map
#
#        searchAll(big, smalls):
#        trie = createTreeFromStrings(smalls, big)
#        for i in range(0, len(big)):
#           wordsFound = findStringsAtLoc(trie, big, i)
#           for word in wordsFound:
#           if word in lookup: lookup[word].append(i)
#           else: lookup[word] = [i]
#        return lookup
# Complexity : O(kt + bk) k is the length of the longest string in T, b is the length of the bigger string,
#              and t is the number of smaller strings within T

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


def createTreeFromStrings(smalls, big):
    trie = Trie()
    for word in smalls:
        if len(word) < len(big):
            trie.insert(word)
    return trie


def findStringsAtLoc(trie, big, start):
    strings = []
    index = start
    root = trie.root
    while index < len(big):
        char = big[index]
        root = root.children[charToIndex(char)]
        if root is None:
            break
        if root.isEndOfWord:
            strings.append(big[start:index+1])
        index += 1
    return strings


def searchAll(big, smalls):
    lookup = dict()
    trie = createTreeFromStrings(smalls, big)
    for i in range(0, len(big)):
        wordsFound = findStringsAtLoc(trie, big, i)
        for word in wordsFound:
            if word in lookup:
                lookup[word].append(i)
            else:
                lookup[word] = [i]
    return lookup


if __name__ == "__main__":
    big = "mississippi"
    smalls = ["is", "ppi", "hi", "sis", "i", "mississippi"]
    locations = searchAll(big, smalls)
    print(locations)
