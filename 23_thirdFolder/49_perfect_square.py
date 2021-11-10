# https://leetcode.com/problems/perfect-squares/
# Question : Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example : Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Question Type : Generic, SimilarAdded
# Used : We convert the problem into graph. From given num, we try to traverse to all possible
#        squares using BFS. Insert the difference into queue and search for next square.
#        By bfs we will make sure that we reach the zero fastest by keep counting the layers
#        of square added in each path.
#        Logic : def numSquares(n):
#        squares = []
#        for i in range(1, n/2 + 1): squares.append(i ** 2)
#        count = 1, queue = [n]
#        while len(queue) > 0:
#           size = len(queue)
#           for i in range(size):
#               num = queue.pop(0)
#               for square in squares:
#                   if num == square: return count
#                   if num < square: break
#                   queue.append(num - square)
#           count += 1
#        return count
# Complexity : O(n^2)


def numSquares(n):
    squares = []
    for i in range(1, n/2 + 1):
        squares.append(i ** 2)
    count = 1
    queue = [n]

    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            num = queue.pop(0)
            for square in squares:
                if num == square:
                    return count
                if num < square:
                    break
                queue.append(num - square)
        count += 1

    return count


if __name__ == "__main__":
    n = 12
    print(numSquares(n))

    n = 13
    print(numSquares(n))

    n = 1000
    print(numSquares(n))
