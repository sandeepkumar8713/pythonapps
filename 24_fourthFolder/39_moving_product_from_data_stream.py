# https://medium.com/@null00/moving-product-from-data-stream-6b32c4290178
# https://leetcode.com/discuss/interview-question/364396/
# Question : Design a data structure to calculate the moving product of all elements in a sliding window of size k.
# All methods should work in O(1) time. Follow up: what if k a parameter of getProduct() function?
#
# Example:
# SlidingWindow window = new SlidingWindow(3);
# window.add(1); // [1]
# window.add(2); // [1, 2]
# window.getProduct(); // 2
# window.add(3); // [1, 2, 3]
# window.getProduct(); // 6
# window.add(4); // [2, 3, 4]
# window.getProduct(); // 24
#
# Question Type : Generic
# Used : For simple question, keep a list of window elements, zeroCount and runningProduct.
#        When a new element comes, insert it in queue, if 0 increment zeroCount else multiply it with runningProduct.
#        Remove top element from queue, divide product with it if not zero.
#        When getProduct is called, if zeroCount > 0: return 0 else return runningProduct
#        For follow up question, maintain a list of cumulativeProduct. For product, divide index n by index n - k
# Logic: def add(self, val):
#        previousProduct = 1
#        if len(self.cumulativeProduct) > 0: previousProduct = self.cumulativeProduct[-1]
#        if val == 0: self.recentZeroIndex = self.count, val = 1
#        self.cumulativeProduct.append(val * previousProduct)
#        self.count += 1
#        def getProduct(self, k):
#        if self.recentZeroIndex < self.count - k:
#           return self.cumulativeProduct[self.count - 1] / self.cumulativeProduct[self.count - k - 1]
#        return 0
# Complexity : O(1)


class SlidingWindow:
    def __init__(self):
        self.cumulativeProduct = []
        self.recentZeroIndex = -1
        self.count = 0

    # This this simple question
    # def add(self, val):
    #     self.queue.append(val)
    #     if val == 0:
    #         self.zeroCount += 1
    #     else:
    #         self.product *= val
    #
    #     if len(self.queue) > self.k:
    #         d = self.queue.pop(0)
    #         if d == 0:
    #             self.zeroCount -= 1
    #         else:
    #             self.product /= d
    #
    # def getProduct(self):
    #     if self.zeroCount > 0:
    #         return 0
    #     else:
    #         return self.product

    def add(self, val):
        previousProduct = 1
        if len(self.cumulativeProduct) > 0:
            previousProduct = self.cumulativeProduct[-1]

        if val == 0:
            self.recentZeroIndex = self.count
            val = 1

        self.cumulativeProduct.append(val * previousProduct)
        self.count += 1

    def getProduct(self, k):
        if self.recentZeroIndex < self.count - k:
            return self.cumulativeProduct[self.count - 1] / self.cumulativeProduct[self.count - k - 1]

        return 0


if __name__ == "__main__":
    slidingWindow = SlidingWindow()
    slidingWindow.add(1)
    slidingWindow.add(0)
    slidingWindow.add(2)
    slidingWindow.add(3)
    slidingWindow.add(4)
    slidingWindow.add(5)

    print(slidingWindow.getProduct(1))
    print(slidingWindow.getProduct(2))
    print(slidingWindow.getProduct(3))
    print(slidingWindow.getProduct(4))
    print(slidingWindow.getProduct(5))
