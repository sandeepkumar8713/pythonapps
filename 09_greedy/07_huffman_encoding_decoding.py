# https://www.geeksforgeeks.org/huffman-decoding/
# Question : Huffman coding is a loss less data compression algorithm. The idea is to assign variable-length codes
# to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters.
# The most frequent character gets the smallest code and the least frequent character gets the largest code.
#
# Input Data : AAAAAABCCCCCCDDEEEEE
# Frequencies : A: 6, B: 1, C: 6, D: 2, E: 5
# Encoded Data :
# 0000000000001100101010101011111111010101010
# Huffman Tree: '#' is the special character used
#               for internal nodes as character field
#               is not needed for internal nodes.
#                #(20)
#              /       \
#         #(12)         #(8)
#      /      \        /     \
#     A(6)     C(6) E(5)     #(3)
#                          /     \
#                        B(1)    D(2)
# Code of 'A' is '00', code of 'C' is '01', ..
# Decoded Data : AAAAAABCCCCCCDDEEEEE
#
# Used : From the given input string, make of list of nodes whose fields are : data, freq, left and right
#        Using this list make a normal min heap.
#        Loop while min heap has only one element
#           pop twice from this min heap, tag them as left and right, merge them by(use '#' as data) summing their freq
#           and push merged node in the heap again
#        Pop this only element from the heap and tag it as root of tree.
#        Make a call to recursive function storeCodes with default in code as ""
#           If we find a leaf node, then save its char along with code
#           else make recursive call to left subtree while appending 0 to the code and 1 for right subtree, save
#        By doing this we will get dict of char and there code.
#        Now loop over the input string and covert char to codes using the above dict, this will give encoded string
#
#        To decode, loop through encoded string and travel the tree. From root, go to left if value is 0 or go to 1.
#           If node data is '#' continue else print the char
#        This will give the decoded string
# Complexity : O(n log n)

import operator


class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None


class Heap:
    def __init__(self, op):
        self.data = []
        self.size = 0
        self.op = op

    def heapify(self, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < self.size and self.op(self.data[left].freq, self.data[largest].freq):
            largest = left

        if right < self.size and self.op(self.data[right].freq, self.data[largest].freq):
            largest = right

        if largest is not i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify(largest)

    def buildHeap(self, arr):
        n = len(arr)
        self.size = n
        for i in xrange(n):
            self.data.append(arr[i])
        start = n/2 - 1
        for i in range(start, -1, -1):
            self.heapify(i)

    def removeTop(self):
        self.data[0], self.data[self.size-1] = self.data[self.size-1], self.data[0]
        temp = self.data[-1]
        del self.data[-1]
        self.size -= 1
        self.heapify(0)
        return temp

    def insert(self, ele):
        self.data.append(ele)
        self.size += 1
        n = self.size
        start = n / 2 - 1
        for i in range(start, -1, -1):
            self.heapify(i)


def storeCodes(root, codeMap, code):
    # pre order
    if root.data == "#":
        pass
    else:
        codeMap[root.data] = code
    if root.left:
        storeCodes(root.left, codeMap, code + "0")
    if root.right:
        storeCodes(root.right, codeMap, code + "1")


def makeTree(inpStr):
    hashDict = dict()
    for ele in inpStr:
        if ele in hashDict.keys():
            hashDict[ele] += 1
        else:
            hashDict[ele] = 1
    nodeList = []
    for data, freq in hashDict.items():
        nodeList.append(Node(data, freq))
    minHeap = Heap(operator.lt)
    minHeap.buildHeap(nodeList)

    # for item in minHeap.data:
    #     print item.data, item.freq

    while minHeap.size != 1:
        left = minHeap.removeTop()
        right = minHeap.removeTop()
        # print left.data, left.freq, right.data, right.freq
        mergedNode = Node("#", left.freq + right.freq)
        mergedNode.left = left
        mergedNode.right = right
        minHeap.insert(mergedNode)

    root = minHeap.removeTop()
    # codeMap = dict()
    # storeCodes(root, codeMap, "")
    # return root, codeMap

    return root


def decodeString(treeRoot,encodedString):
    currNode = treeRoot
    res = ""
    for ele in encodedString:
        if ele is "0":
            currNode = currNode.left
        elif ele is "1":
            currNode = currNode.right

        if currNode.left is None and currNode.right is None:
            res += currNode.data
            currNode = treeRoot

    return res


def encodeString(treeRoot, inpStr):
    codeMap = dict()
    storeCodes(treeRoot, codeMap, "")
    encodedString = ""
    for ele in inpStr:
        encodedString += codeMap[ele]
    return encodedString


if __name__ == "__main__":
    # inpStr = "AAAAAABCCCCCCDDEEEEE"
    inpStr = "geeksforgeeks"
    treeRoot = makeTree(inpStr)
    encodedString = encodeString(treeRoot, inpStr)
    decodedString = decodeString(treeRoot, encodedString)

    print "inpStr:", inpStr
    print "encodedString:", encodedString
    print "decodedString:", decodedString
