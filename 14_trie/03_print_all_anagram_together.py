# CTCI : Q10_02_Group_Anagrams
# https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together-set-2/
# Question : Given an array of words, print all anagrams together. For example, if the given array is
# {"cat", "dog", "tac", "god", "act"}, then output may be "cat tac act dog god".
#
# Question Type : Asked
# Used : In trie Node add two fields : children (list of size 26) and wordEndingID
#        (list of id of words ending at this node)
#        Loop over the given list of words. Sort the word and insert it in Trie and also insert its id,
#        where the word ends.
#        Now traverse the Trie again (DFS) and if there are id in wordEndingID: print them
# Logic: def traverseUtils(self, root, res, inp_strs):
#        temp = root
#        for child in temp.children.values():
#           self.traverseUtils(child, res, inp_strs)
#           res_2 = []
#           for index in child.index_list:
#               res_2.append(inp_strs[index])
#           if len(res_2) > 0:
#               res.append(res_2)
#        return res
# Complexity : O(n * m * log m) + O(m * n) m is MAX_CHAR and n is word count

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.index_list = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, inpStr, wordId):
        temp = self.root
        for ch in inpStr:
            if ch not in temp.children:
                temp.children[ch] = TrieNode()
            temp = temp.children[ch]

        temp.index_list.append(wordId)

    def traverseUtils(self, root, res, inp_strs):
        temp = root
        for child in temp.children.values():
            self.traverseUtils(child, res, inp_strs)
            res_2 = []
            for index in child.index_list:
                res_2.append(inp_strs[index])
            if len(res_2) > 0:
                res.append(res_2)

        return res

    def traverse(self, inp_strs):
        res = []
        self.traverseUtils(self.root, res, inp_strs)
        return res


def group_similar(inp_strs):
    trie = Trie()

    wordId = 0
    for word in inp_strs:
        trie.insert(sorted(word), wordId)
        wordId += 1

    return trie.traverse(inp_strs)


if __name__ == '__main__':
    inpWords = ["cat", "dog", "tac", "god", "act", "gdo"]
    print(group_similar(inpWords))
