# https://leetcode.com/problems/word-ladder/
# CTCI : Q17_22_Word_Transformer
# Question : Given a dictionary, and two words 'start' and 'target' (both of same length).
# Find length of the smallest chain from 'start' to 'target' if it exists, such that adjacent
# words in the chain only differ by one character and each word in the chain is a valid word
# i.e., it exists in the dictionary. It may be assumed that the 'target' word exists in
# dictionary and length of all dictionary words is same.
#
# Example:
# Input:  Dictionary = {POON, PLEE, SAME, POIE, PLEA, PLIE, POIN}
#              start = TOON
#              target = PLEA
# Output: 7
# Explanation: TOON - POON - POIN - POIE - PLIE - PLEE - PLEA
#
# Question Type : Generic
# Used : We should do BFS. Insert start word in queue along with distance covered. Loop over
#        the element in the queue until target is found. Pop the element(temp) from the queue.
#        Find the words which are 1 distance away from temp. Add these element along with
#        distance in the queue. Remove temp word from wordList. If temp is target, return
#        distance covered.
# Logic: item = QItem(start, 1)
#        queue.append(item)
#        while len(queue) > 0:
#           curr = queue.pop(0)
#           for word in wordList:
#               temp = word
#               if isadjacent(curr.word, temp):
#                 item.word = temp
#                 item.len = curr.len + 1
#                 queue.append(item)
#                 wordList.remove(temp) # Like marking visited
#                 if temp == target:
#                     return item.len
# Complexity : O(n*2m) n is number of words and m is length of the string


def isadjacent(a, b):
    count = 0
    n = len(a)
    for i in range(n):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            break

    return True if count == 1 else False


# A queue item to store word and minimum chain length
# to reach the word.
class QItem():
    def __init__(self, word, len):
        self.word = word
        self.len = len


def shortestChainLen(start, target, wordList):
    # Create a queue for BFS and insert 'start' as source vertex
    queue = []
    item = QItem(start, 1)
    queue.append(item)

    while len(queue) > 0:
        curr = queue.pop(0)
        for word in wordList:
            temp = word
            if isadjacent(curr.word, temp):
                # Add the dictionary word to Q
                item.word = temp
                item.len = curr.len + 1
                queue.append(item)

                # Remove from dictionary so that this word is not processed again. This is
                # like marking visited
                wordList.remove(temp)

                # If we reached target
                if temp == target:
                    return item.len


if __name__ == "__main__":
    D = []
    D.append("poon")
    D.append("plee")
    D.append("same")
    D.append("poie")
    D.append("plie")
    D.append("poin")
    D.append("plea")

    start = "toon"
    target = "plea"
    print("Length of shortest chain is: %d" % shortestChainLen(start, target, D))
