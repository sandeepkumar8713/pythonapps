# https://leetcode.com/problems/asteroid-collision/solution/
# Question : We are given an array asteroids of integers representing asteroids in a row. For each asteroid,
# the absolute value represents its size, and the sign represents its direction (positive meaning right, negative
# meaning left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
# Two asteroids moving in the same direction will never meet.
#
# Example : Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
#
# Question Type : Easy
# Used : Use a stack to store result. When a new item arrives, check if it negative and smaller or equal than top of
#        stack and condition of collision is satisfied i.e: (item< 0 <stack[-1]). If required pop the top of stack.
#        If item collision condition is not satisfied simply push the item in stack.
#        for item in asteroids:
#           while stack and item < 0 < stack[-1]:
#               if stack[-1] < -item:
#                   stack.pop(), continue
#               elif stack[-1] == -item:
#                 stack.pop()
#               break
#           else:
#               stack.append(item)
#        return stack
# Complexity : O(n)


def asteroidCollision(asteroids):
    stack = []
    for item in asteroids:
        # Loop while there is element in stack and item is negative and top of stack is positive
        # This condition takes care of asteroids going left and right.
        while stack and item < 0 < stack[-1]:
            if stack[-1] < -item:
                # Top in stack is small so destroyed, item is not destroyed yet, so keep looping
                stack.pop()
                continue
            elif stack[-1] == -item:
                # Top in stack is same as item, both item and top is destroyed. So break the loop.
                stack.pop()
            # Item is smaller than top, so item is destroyed
            break
        else:
            stack.append(item)
    return stack


if __name__ == "__main__":
    asteroids = [5, 10, -5]
    print(asteroidCollision(asteroids))

    asteroids = [-2, -1, 1, 2]
    print(asteroidCollision(asteroids))
