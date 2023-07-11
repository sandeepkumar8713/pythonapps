# https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Question : Find the largest rectangular area possible in a given histogram where the largest
# rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars
# have same width and the width is 1 unit.
#
# Question Type : ShouldSee
# Used : 1) Create an empty stack.
#        2) Start from first bar, and do following for every bar 'hist[i]' where 'i' varies from 0 to n-1.
#           a) If stack is empty or hist[i] is higher than the bar at top of stack, then push 'i' to stack.
#           b) If this bar is smaller than the top of stack, then keep removing the top of stack while
#              top of the stack is greater. Let the removed bar be hist[tp]. Calculate area of rectangle
#              with hist[tp] as smallest bar. For hist[tp], the 'left index' is previous (previous to tp)
#              item in stack and 'right index' is 'i' (current index).
#        3) If the stack is not empty, then one by one remove all bars from stack and do step 2.b
#           for every removed bar.
#        updateMaxArea(stack, i, maxArea):
#        topIndex = stack.pop()
#        width = 0
#        if len(stack) == 0: width = i
#        else: width = i - stack[-1] - 1
#        areaWithTop = hist[topIndex] * width
#        return max(maxArea, areaWithTop)
#
#        def getMaxArea(hist):
#        n = len(hist), stack = []
#        maxArea = 0, i = 0
#        while i < n:
#           if len(stack) == 0 or hist[stack[-1]] < hist[i]:
#               stack.append(i)
#               i += 1
#           else:
#               maxArea = updateMaxArea(stack, i, maxArea)
#        while len(stack) == 0:
#           maxArea = updateMaxArea(stack, i, maxArea)
#        return maxArea
# Complexity : O(n)


def updateMaxArea(stack, i, maxArea):
    topIndex = stack.pop()
    width = 0
    if len(stack) == 0:
        width = i
    else:
        width = i - stack[-1] - 1
    # Assume topIndex as smallest bar
    areaWithTop = hist[topIndex] * width

    return max(maxArea, areaWithTop)


def getMaxArea(hist):
    n = len(hist)
    stack = []
    maxArea = 0

    i = 0
    while i < n:
        # If this bar is higher than the bar on top stack, push it to stack
        if len(stack) == 0 or hist[stack[-1]] < hist[i]:
            stack.append(i)
            i += 1
        else:
            maxArea = updateMaxArea(stack, i, maxArea)

    while len(stack) == 0:
        maxArea = updateMaxArea(stack, i, maxArea)

    return maxArea


if __name__ == "__main__":
    hist = [6, 2, 5, 4, 5, 1, 6]
    print(getMaxArea(hist))
