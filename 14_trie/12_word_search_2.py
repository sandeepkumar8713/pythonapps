# https://leetcode.com/problems/word-search-ii/
# Similar : https://leetcode.com/problems/word-search/
# Question : Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are
# horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# Example : Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
# Question Type : Generic
# Used : Make trie using the given word list. Now run 2 loops over the given matrix and check if
#        that char is present in the trie. if yes, continue further until word is reached.
#        Make use of # in matrix to denote used characters.
# Logic: class TrieNode():
#        def __init__(self):
#           self.children = dict()
#           self.word = ''
#        def build_trie(words):
#        trie = TrieNode()
#        for word in words:
#           temp = trie
#           for ch in word:
#               if ch not in temp.children:
#                   temp.children[ch] = TrieNode()
#               temp = temp.children[ch]
#           temp.word = word
#        return trie
#
#        walk(board, i, j, trie, m, n):
#        if trie.word:
#           res_list.append(trie.word)
#           trie.word = ''
#        if i < 0 or i >= m or j < 0 or j >= n or not board[i][j] in trie.children:
#           return False
#        cur_ch = board[i][j]
#        board[i][j] = '#'
#        walk(board, i + 1, j, trie.children[cur_ch], m, n)
#        walk(board, i - 1, j, trie.children[cur_ch], m, n)
#        walk(board, i, j + 1, trie.children[cur_ch], m, n)
#        walk(board, i, j - 1, trie.children[cur_ch], m, n)
#        board[i][j] = cur_ch
# Complexity : O(m*n*l) where m and n are rows and cols board. l is count of words

res_list = list()


class TrieNode():
    def __init__(self):
        self.children = dict()
        self.word = ''


def walk(board, i, j, trie, m, n):
    if trie.word:
        res_list.append(trie.word)
        trie.word = ''

    if i < 0 or i >= m or j < 0 or j >= n or not board[i][j] in trie.children:
        return False

    cur_ch = board[i][j]
    board[i][j] = '#'
    walk(board, i + 1, j, trie.children[cur_ch], m, n)
    walk(board, i - 1, j, trie.children[cur_ch], m, n)
    walk(board, i, j + 1, trie.children[cur_ch], m, n)
    walk(board, i, j - 1, trie.children[cur_ch], m, n)
    board[i][j] = cur_ch


def build_trie(words):
    trie = TrieNode()
    for word in words:
        temp = trie
        for ch in word:
            if ch not in temp.children:
                temp.children[ch] = TrieNode()
            temp = temp.children[ch]
        temp.word = word
    return trie


def findWords(board, words):
    m = len(board)
    n = len(board[0])
    if len(words) == 0 or m == 0:
        return res_list
    trie = build_trie(words)
    for i in range(m):
        for j in range(n):
            walk(board, i, j, trie, m, n)

    return res_list


if __name__ == "__main__":
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(findWords(board, words))
