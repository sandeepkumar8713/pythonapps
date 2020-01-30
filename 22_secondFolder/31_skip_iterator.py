# https://leetcode.com/discuss/interview-question/341818/Google-or-Onsite-or-Skip-Iterator
# Question : Design a SkipIterator that supports a method skip(int val). When it is called the
# next element equals val in iterator sequence should be skipped. If you are not familiar with Iterators
# check similar problems.
#
# Example:
#
# SkipIterator itr = new SkipIterator([2, 3, 5, 6, 5, 7, 5, -1, 5, 10]);
# itr.hasNext(); // true
# itr.next(); // returns 2
# itr.skip(5);
# itr.next(); // returns 3
# itr.next(); // returns 6 because 5 should be skipped
# itr.next(); // returns 5
#
# Question Type : Easy
# Used : We maintain a dict of to be skipped elements with its freq.
#        Logic : class SkipIterator:
#        def __init__(self, arr):
#           self.arr = arr
#           self.skipMap = dict()
#           self.nextIndex = 0
#        def hasNext(self):
#           if self.nextIndex >= len(self.arr):
#               return False
#           return True
#        def next(self):
#           self.advance()
#           tobeSent = self.nextIndex
#           self.nextIndex += 1
#           return self.arr[tobeSent]
#        def skip(self, skipEle):
#           if skipEle not in self.skipMap:
#               self.skipMap[skipEle] = 1
#           else:
#               self.skipMap[skipEle] += 1
#        def advance(self):
#           nextEle = self.arr[self.nextIndex]
#           while nextEle in self.skipMap:
#               self.skipMap[nextEle] -= 1
#               self.nextIndex += 1
#               if self.skipMap[nextEle] == 0:
#                   del self.skipMap[nextEle]
#               nextEle = self.arr[self.nextIndex]
# Complexity : O(n)


class SkipIterator:
    def __init__(self, arr):
        self.arr = arr
        self.skipMap = dict()
        self.nextIndex = 0

    def hasNext(self):
        if self.nextIndex >= len(self.arr):
            return False
        return True

    def next(self):
        self.advance()
        tobeSent = self.nextIndex
        self.nextIndex += 1
        return self.arr[tobeSent]

    def skip(self, skipEle):
        if skipEle not in self.skipMap:
            self.skipMap[skipEle] = 1
        else:
            self.skipMap[skipEle] += 1

    def advance(self):
        nextEle = self.arr[self.nextIndex]
        while nextEle in self.skipMap:
            self.skipMap[nextEle] -= 1
            self.nextIndex += 1

            if self.skipMap[nextEle] == 0:
                del self.skipMap[nextEle]
            nextEle = self.arr[self.nextIndex]


if __name__ == "__main__":
    inpArr = [2, 3, 5, 6, 5, 7, 5, -1, 5, 10]
    itr = SkipIterator(inpArr)
    print(itr.hasNext()) # true
    print(itr.next())    # returns 2
    itr.skip(5)
    itr.skip(5)
    print(itr.next())    # returns 3
    print(itr.next())   # returns 6 because 5 should be skipped
    print(itr.next())    # returns 7 because 5 should be skipped
