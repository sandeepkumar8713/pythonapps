# https://www.geeksforgeeks.org/rearrange-a-string-so-that-all-same-characters-become-at-least-d-distance-away/
# Question : Given a string and a positive integer d. Some characters may be repeated in the given string.
# Rearrange characters of the given string such that the same characters become d distance away from each other.
# Note that there can be many possible rearrangements, the output should be one of the possible rearrangements.
# If no such arrangement is possible, that should also be reported.
#
# Used : Let the given string be str and size of string be n
#        Traverse str, store all characters and their frequencies in a Max Heap MH. The value of frequency decides the
#           order in MH. Heapify the MH.
#        Take a resStr list and mark all element as '\0'
#        Do following while MH is not empty.
#           Extract the Most frequent character(top from MH). Let the extracted character be x and its frequency be f.
#           Find the first available position in str, i.e., find the first '\0' in str.
#           if p + dDist * k >= n: return "not possible"
#           Let the first position be p. Fill x at p, p+d,.. p+(f-1)d
#        return
# Complexity : O(n + mLog(MAX)) so O(n)
#              n : length of input string, m : count of distinct character, MAX : maximum possible different char(256)


import operator


class Key:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq


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

    def buildHeap(self, arr, n):
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


def rearrangeString(inputStr, dDist):
    n = len(inputStr)
    inpDict = dict()
    for char in inputStr:
        if char in inpDict.keys():
            inpDict[char] += 1
        else:
            inpDict[char] = 1

    inputList = []
    for char, freq in inpDict.items():
        inputList.append(Key(char, freq))

    maxHeap = Heap(operator.gt)
    maxHeap.buildHeap(inputList, len(inputList))

    resStr = ['\0'] * n

    for i in xrange(len(inputList)):
        top = maxHeap.removeTop()

        # Find the first available position in str[]
        p = i
        while resStr[p] != '\0':
            p += 1

        for k in xrange(top.freq):
            # If the index goes beyond size, then string cannot be rearranged.
            if p + dDist * k >= n:
                return "Cannot be rearranged"

            # Fill top.c at p, p+d, p+2d, .. p+(f-1)d
            resStr[p + dDist * k] = top.char

    return ''.join(resStr)


if __name__ == "__main__":
    print rearrangeString("aaa", 3)
    print rearrangeString("aabbcc", 3)
