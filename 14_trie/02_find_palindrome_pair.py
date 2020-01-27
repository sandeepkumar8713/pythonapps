# https://www.geeksforgeeks.org/palindrome-pair-in-an-array-of-words-or-strings/
# Question : Given a list of words, find if any of the two words can be joined to form a palindrome.
#
# Question Type : Generic
# Used : Insert all the words in reverse in trie. Loop over all input string once again. If fully found return true.
#        If partially found, check if remaining is palindrome. If yes, return true.
#        We have to maintain unique id for each word in trie. In trie node add a field ids which is a list of id of word
#        character is present in. Add endingWordID in trie node. Also add field palindromeIndex which is a map of
#        wordID and length of palindrome.
# insert() : Call insert(inpStr, wordId). Reverse the given inpStr. Set temp = root and loop over of each character
#               of inpStr. Convert char to index. Check if index is present in children or not. If not present insert
#               newNode. Call func isPalindrome(inpStr, level, inpStrLen-1) to check if remaining subString is
#               palindrome or not. If true: set temp.palindromeIndex[wordId] = inpStrLen - level. Append wordID in
#               list temp.ids. Then go to child : temp = temp.children[index]
#            Once the loop gets over, set temp.isEndOfWord and temp.endingWordID
# search() : Call insert(inpStr, wordId). set found = false and set temp = root. Loop over inpStr. Convert char to index
#               Check if this word in trie ends here and remaining substring in inpStr is palindrome. If true :
#                   print inpStr, inpWords[temp.endingWordID] and found = true
#               Check if index is not present, return found else go to children : temp = temp.children[index]
#            Once the loop gets over, If temp is not None and this is the end char :
#               print inpStr, inpWords[temp.endingWordID] and found = true
#            If inpStr is ended and there are letters in this trie after inpStr, which is palindrome. Then loop over
#               keys of palindromeIndex and do this : print inpStr, inpWords[wordId] and found = True
#            return found
# Complexity : O(n * k^2) Where n is the number of words in the list and k is the maximum length that is
#              checked for palindrome.


MAX_CHAR = 26


def isPalindrome(inpStr, i, len):
    if i == len:
        return True
    while i <= len:
        if inpStr[i] != inpStr[len]:
            return False
        i += 1
        len -= 1

    return True


def charToIndex(ch):
    return ord(ch) - ord('a')


class TrieNode:
    def __init__(self):
        self.children = [None] * MAX_CHAR
        self.isEndOfWord = False
        self.palindromeIndex = {}
        self.ids = []
        self.endingWordID = -1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, inpStr, wordId):
        temp = self.root
        inpStr = inpStr[::-1]
        inpStrLen = len(inpStr)
        for level in range(inpStrLen):
            index = charToIndex(inpStr[level])
            if not temp.children[index]:
                temp.children[index] = TrieNode()
            # if next word is palindrome
            if isPalindrome(inpStr, level, inpStrLen-1):
                temp.palindromeIndex[wordId] = inpStrLen - level
            temp.ids.append(wordId)
            temp = temp.children[index]

        temp.isEndOfWord = True
        temp.endingWordID = wordId

    def search(self, inpStr):
        found = False
        temp = self.root
        inpStrLen = len(inpStr)
        for level in range(inpStrLen):
            index = charToIndex(inpStr[level])
            # If this word in trie ends here and remaining is palindrome
            if temp.isEndOfWord and isPalindrome(inpStr, level, inpStrLen - 1):
                print(inpStr, inpWords[temp.endingWordID])
                found = True
            if not temp.children[index]:
                return found
            temp = temp.children[index]

        if temp is not None and temp.isEndOfWord:
            print(inpStr, inpWords[temp.endingWordID])
            found = True

        # if inpStr is ended and there are letters in this trie after inpStr, which is palindrome
        if temp is not None and len(temp.palindromeIndex.keys()) > 0:
            for wordId in temp.palindromeIndex.keys():
                print(inpStr, inpWords[wordId])
                found = True

        return found


def checkPalindromePair(words):
    trie = Trie()
    wordId = 0
    for word in words:
        trie.insert(word, wordId)
        wordId += 1

    for word in words:
        if not trie.search(word):
            print("Can't find word that can be appended to:", word)


if __name__ == '__main__':
    # inpWords = ["geekf", "geeks", "or", "keeg", "abc", "bc"]
    # inpWords = ['dnas', 'sandeeppee']
    # inpWords = ['eppeednas', 'sande']
    inpWords = ['dnas', 'sandeeppee', 'eppeednas', 'sande']
    checkPalindromePair(inpWords)
