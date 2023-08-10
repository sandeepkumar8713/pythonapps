# https://www.geeksforgeeks.org/auto-complete-feature-using-trie/
# Question : We are given a Trie with a set of strings stored in it. Now the user types in a prefix of his search
# query, we need to give him all recommendations to auto-complete his query based on the strings stored in the Trie.
# We assume that the Trie stores past searches by the users.
# 
# For example if the Trie store {"abc", "abcd", "aa", "abbbaba"} and the User types in "ab" then he must be shown
# {"abc", "abcd", "abbbaba"}.
#
# Question Type : Generic
# Used : Insert all the words in trie.
#        Search for given query using standard Trie search algorithm.
#        If query prefix itself is not present, return -1 to indicate the same.
#        If query is present and is end of word in Trie, print query.
#        Else recursively print all nodes under subtree of last matching node for which
#        isEndOfWord is True.
# Logic: class TrieNode:
#        def __init__(self):
#           self.children = [None] * MAX_CHAR
#           self.isEndOfWord = False
#        def insert(self, insStr):
#           temp = self.root
#           for level in range(len(insStr)):
#               index = charToIndex(insStr[level])
#               if not temp.children[index]:
#                   temp.children[index] = TrieNode()
#               temp = temp.children[index]
#        temp.isEndOfWord = True
# Complexity : O(n * m) while inserting words in trie

MAX_CHAR = 26


def charToIndex(ch):
    return ord(ch) - ord('a')


def indexToChar(i):
    return chr(i + ord('a'))


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

    def search(self, insStr):
        temp = self.root
        for level in range(len(insStr)):
            index = charToIndex(insStr[level])
            if not temp.children[index]:
                return False
            temp = temp.children[index]

        if temp is not None and temp.isEndOfWord:
            print(insStr)
            return True
        elif temp is not None:
            searchFullWord(temp, insStr)
            return True
        return False


def searchFullWord(root, resStr):
        if root.isEndOfWord is True:
                print(resStr)

        for i in range(MAX_CHAR):
            if root.children[i] is not None:
                char = indexToChar(i)
                searchFullWord(root.children[i], resStr + char)


if __name__ == "__main__":
    words = ["abc", "abcd", "aa", "abbbaba"]
    t = Trie()
    for word in words:
        t.insert(word)

    if not t.search("abc"):
        print("not found")

    print
    if not t.search("ab"):
        print("not found")

    print("")
    if not t.search("ss"):
        print("not found")
