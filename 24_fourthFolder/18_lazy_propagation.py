# https://www.geeksforgeeks.org/lazy-propagation-in-segment-tree/
# Question : Write a function which takes start and end index and return their range sum. We
# have used the same "Sum of given Range" problem to explain Lazy propagation. He then asked
# range update in best optimised way. I told him Lazy propagation. I had to write code for
# segment tree with lazy propagation.
#
# Question Type : Generic
# Used : updateRange(us, ue)
#        1) If current segment tree node has any pending update, then first add that pending update to current node.
#        2) If current node's range lies completely in update query range.
#           a) Update current node
#           b) Postpone updates to children by setting lazy value for children nodes.
#        3) If current node's range overlaps with update range, follow the same approach as above simple update.
#               a) Recur for left and right children.
#               b) Update current node using results of left and right calls.
#        Logic :
#        def getSumUtil(self, segStart, segEnd, queryStart, queryEnd, index):
#           if self.lazy[index] != 0:
#               self.tree[index] += (segEnd - segStart + 1) * self.lazy[index]
#               if segStart != segEnd:
#                   self.lazy[index * 2 + 1] += self.lazy[index]
#                   self.lazy[index * 2 + 2] += self.lazy[index]
#               self.lazy[index] = 0
#           if segStart > segEnd or segStart > queryEnd or segEnd < queryStart: return 0
#           if segStart >= queryStart and segEnd <= queryEnd: return self.tree[index]
#           mid = (segStart + segEnd) / 2
#           return self.getSumUtil(segStart, mid, queryStart, queryEnd, index * 2 + 1) + \
#               self.getSumUtil(mid + 1, segEnd, queryStart, queryEnd, index * 2 + 2)
#        def updateRangeUtil(self, segStart, segEnd, queryStart, queryEnd, index, diff):
#           if self.lazy[index] != 0:
#               self.tree[index] += (segEnd - segStart + 1) * self.lazy[index]
#           if segStart != segEnd:
#               self.lazy[index * 2 + 1] += self.lazy[index]
#               self.lazy[index * 2 + 2] += self.lazy[index]
#           self.lazy[index] = 0
#           if segStart > segEnd or segStart > queryEnd or segEnd < queryStart:
#               return 0
#           if segStart >= queryStart and segEnd <= queryEnd:
#               self.tree[index] += (segEnd - segStart + 1) * diff
#               if segStart != segEnd:
#                   self.lazy[index * 2 + 1] += diff
#                   self.lazy[index * 2 + 2] += diff
#           return
#           mid = (segStart + segEnd) // 2
#           self.updateRangeUtil(segStart, mid, queryStart, queryEnd, index * 2 + 1, diff)
#           self.updateRangeUtil(mid + 1, segEnd, queryStart, queryEnd, index * 2 + 2, diff)
#           self.tree[index] = self.tree[index * 2 + 1] + self.tree[index * 2 + 2]
# Complexity : Tree construction O(n) Update O(log n) Sum O(log n)

MAX = 1000


class LazySegmentTree:
    def __init__(self):
        self.tree = [0] * MAX
        self.lazy = [0] * MAX
        self.size = -1

    def constructUtil(self, inpArr, segStart, segEnd, index):
        if segStart > segEnd:
            return

        if segStart == segEnd:
            self.tree[index] = inpArr[segStart]
            return

        mid = (segStart + segEnd) // 2
        self.constructUtil(inpArr, segStart, mid, index * 2 + 1)
        self.constructUtil(inpArr, mid + 1, segEnd, index * 2 + 2)
        self.tree[segStart] = self.tree[segStart * 2 + 1] + self.tree[segStart * 2 + 2]

    def construct(self, inpArr):
        self.size = len(inpArr)
        self.constructUtil(arr, 0, self.size - 1, 0)

    def getSumUtil(self, segStart, segEnd, queryStart, queryEnd, index):
        if self.lazy[index] != 0:
            self.tree[index] += (segEnd - segStart + 1) * self.lazy[index]

            if segStart != segEnd:
                self.lazy[index * 2 + 1] += self.lazy[index]
                self.lazy[index * 2 + 2] += self.lazy[index]
            self.lazy[index] = 0

        if segStart > segEnd or segStart > queryEnd or segEnd < queryStart:
            return 0

        # If this segment lies in range
        if segStart >= queryStart and segEnd <= queryEnd:
            return self.tree[index]

        mid = (segStart + segEnd) // 2
        return self.getSumUtil(segStart, mid, queryStart, queryEnd, index * 2 + 1) + \
               self.getSumUtil(mid + 1, segEnd, queryStart, queryEnd, index * 2 + 2)

    def getSum(self, queryStart, queryEnd):
        if queryStart < 0 or queryEnd > self.size - 1 or queryStart > queryEnd:
                print("Invalid Input")
                return -1

        return self.getSumUtil(0, self.size - 1, queryStart, queryEnd, 0)

    def updateRangeUtil(self, segStart, segEnd, queryStart, queryEnd, index, diff):
        if self.lazy[index] != 0:
            self.tree[index] += (segEnd - segStart + 1) * self.lazy[index]

            if segStart != segEnd:
                self.lazy[index * 2 + 1] += self.lazy[index]
                self.lazy[index * 2 + 2] += self.lazy[index]
            self.lazy[index] = 0

        if segStart > segEnd or segStart > queryEnd or segEnd < queryStart:
            return 0

        # If this segment lies in range
        if segStart >= queryStart and segEnd <= queryEnd:
            self.tree[index] += (segEnd - segStart + 1) * diff

            if segStart != segEnd:
                self.lazy[index * 2 + 1] += diff
                self.lazy[index * 2 + 2] += diff
            return

        mid = (segStart + segEnd) // 2
        self.updateRangeUtil(segStart, mid, queryStart, queryEnd, index * 2 + 1, diff)
        self.updateRangeUtil(mid + 1, segEnd, queryStart, queryEnd, index * 2 + 2, diff)
        self.tree[index] = self.tree[index * 2 + 1] + self.tree[index * 2 + 2]

    def updateRange(self, queryStart, queryEnd, diff):
        self.updateRangeUtil(0, self.size - 1, queryStart, queryEnd, 0, diff)


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    lazySegmentTree = LazySegmentTree()
    lazySegmentTree.construct(arr)
    print(lazySegmentTree.getSum(1, 3))
    lazySegmentTree.updateRange(1, 5, 10)
    print(lazySegmentTree.getSum(1, 3))
