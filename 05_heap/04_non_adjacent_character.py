# # https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/
# Question : Given a string with repeated characters, task is rearrange characters in a string so that no two
# adjacent characters are same.
# Input: aaabb
# Output: ababa
#
# Input: aa
# Output: Not Possible
#
# Input: aaaabc
# Output: Not Possible
#
# Question Type : Generic
# Used : Make a array of objects whose attributes are char and its frequency. Make a maxHeap(Priority Queue) out of
#        this array. Loop while maxHeap is not empty. Pop top element from maxHeap, append the char to the result
#        string. If previous element freq is more 0 again insert it in maxHeap. Make current element as previous after
#        decrementing its frequency by 1.
#        Logic :
#        prev = Key('#', -1)
#        resStr = ''
#        while maxHeap.getCount() != 0:
#           key = maxHeap.removeTop()
#           resStr = resStr + key.char
#           if prev.freq > 0:
#               maxHeap.insert(prev)
#           key.freq -= 1
#           prev = key
#        if len(resStr) == len(inputStr):
#           print(resStr)
#        else:
#           print("not possible")
# Complexity : insert : (n log n) remove top : (log n) total : n (n log n)


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
        for i in range(n):
            self.data.append(arr[i])
        start = n//2 - 1
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
        start = n // 2 - 1
        for i in range(start, -1, -1):
            self.heapify(i)

    def getTop(self):
        return self.data[0]

    def getCount(self):
        return self.size


def rearrangeString(inputStr):
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

    prev = Key('#', -1)
    resStr = ''
    while maxHeap.getCount() != 0:
        key = maxHeap.removeTop()
        resStr = resStr + key.char

        if prev.freq > 0:
            maxHeap.insert(prev)
        key.freq -= 1
        prev = key

    if len(resStr) == len(inputStr):
        print(resStr)
    else:
        print("not possible")


if __name__ == "__main__":
    rearrangeString("bbbbaa")
    rearrangeString("aaabb")


