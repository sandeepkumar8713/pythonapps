# https://www.geeksforgeeks.org/trie-insert-and-search/
# Question : Trie is an efficient information retrieval data structure. Using Trie, search complexities can be
# brought to optimal limit (key length). Using Trie, we can search the key in O(M) time. However the penalty
# is on Trie storage requirements.
#
# Every node of Trie consists of multiple branches. Each branch represents a possible character of keys. We need to
# mark the last node of every key as end of word node. A Trie node field isEndOfWord is used to distinguish the node
# as end of word node
#
# Used : Here node would have two fields: children (list of length 26) and isEndOfWord (marker to tell if word ends)
#        Define a func charToIndex(ch), it converts given char to integer b/w 0 to 25. To be used as index in children.
# Insert : Set temp = root and loop over the character in the inpStr. Call charToIndex(ch) to get its index.
#               If this index is not in children, assign a newNode to it.
#               Now traverse in the children : temp = temp.children[index].
#          Once the loop gets over mark temp as end : temp.isEndOfWord = True
# Search : Set temp = root and loop over the character in the inpStr. Call charToIndex(ch) to get its index.
#               If this index is not in children, return False.
#               Else traverse in the children : temp = temp.children[index].
#          Once the loop gets over. If temp is not None and temp.isEndOfWord return True.
# Complexity : insert O(m) search O(m) where m is length of input string

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

    def subStringSearch(self, insStr):
        temp = self.root
        for level in range(len(insStr)):
            index = charToIndex(insStr[level])
            if not temp.children[index]:
                return None
            temp = temp.children[index]
        return temp

    def search(self, insStr):
        temp = self.subStringSearch(insStr)
        if temp is None:
            return False
        else:
            return temp.isEndOfWord


if __name__ == '__main__':
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    output = ["Not present in trie", "Present in tire"]
    t = Trie()
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))
