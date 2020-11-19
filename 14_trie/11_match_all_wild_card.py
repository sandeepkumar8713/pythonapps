# https://careercup.com/question?id=5708250171834368
# Question : Given the entire dictionary of English words, what data structure will you use to efficiently store and
# match the custom regex string like "D*sk", where * represents any single alphabet, and return the list
# of matched words?
#
# Used : Make a Trie for all the words in dictionary. Do iterative search of the given inpStr in trie. If * is
#        encountered in inpStr then loop over all the characters at current level in trie and call the recursive search
#        again. While doing so all keep track of matched words.
#        getMatchedStringsUtils(temp, inpStr, stack, matchedWords, startLevel):
#        for level in range(startLevel, len(inpStr)):
#           inpChar = inpStr[level]
#           if inpChar == '*':
#               for index in range(0, MAX_CHAR):
#                   if temp.children[index]:
#                       matchingChar = indexToChar(index)
#                       stack.append(matchingChar)
#                       getMatchedStringsUtils(temp.children[index], inpStr, stack[::], matchedWords, level + 1)
#                       stack.pop()
#               return
#           else:
#               stack.append(inpChar)
#               index = charToIndex(inpChar)
#               if not temp.children[index]: return
#               temp = temp.children[index]
#        if temp.isEndOfWord: matchedWords.append(''.join(stack))
# Complexity : 26 * O(d) where d is depth of trie node

MAX_CHAR = 26


def charToIndex(ch):
    return ord(ch) - ord('a')


def indexToChar(index):
    return chr(index + ord('a'))


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

    def getMatchedStringsUtils(self, temp, inpStr, stack, matchedWords, startLevel):
        for level in range(startLevel, len(inpStr)):
            inpChar = inpStr[level]

            if inpChar == '*':
                for index in range(0, MAX_CHAR):
                    if temp.children[index]:
                        matchingChar = indexToChar(index)
                        stack.append(matchingChar)
                        self.getMatchedStringsUtils(temp.children[index], inpStr, stack[::], matchedWords, level + 1)
                        stack.pop()
                return
            else:
                stack.append(inpChar)
                index = charToIndex(inpChar)
                if not temp.children[index]:
                    return
                temp = temp.children[index]

        if temp.isEndOfWord:
            matchedWords.append(''.join(stack))
        return

    def search(self, inpStr):
        stack = []
        matchedWords = []
        self.getMatchedStringsUtils(self.root, inpStr, stack, matchedWords, 0)
        return matchedWords


if __name__ == '__main__':
    keys = ["the", "a", "there", "anaswe", "any", "by", "their", "disk", "dusk"]
    output = ["Not present in trie", "Present in tire"]
    t = Trie()
    for key in keys:
        t.insert(key)

    print(t.search("the"))
    print(t.search("sandeep"))
    print(t.search("d*sk"))
    print(t.search("d*s*"))
    print(t.search("***k"))
    print(t.search("*"))
    print(t.search("***"))
