# https://leetcode.com/problems/alphabet-board-path/
# https://leetcode.com/problems/alphabet-board-path/discuss/414431/python-O(n)-z-explanation
# Question : On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"],
# We may make the following moves:
#
# 'U' moves our position up one row, if the position exists on the board;
# 'D' moves our position down one row, if the position exists on the board;
# 'L' moves our position left one column, if the position exists on the board;
# 'R' moves our position right one column, if the position exists on the board;
# '!' adds the character board[r][c] at our current position (r, c) to the answer.
# (Here, the only positions that exist on the board are positions with letters on them.)
#
# Return a sequence of moves that makes our answer equal to target in the minimum number of moves.
# You may return any path that does so.
#
# Example : Input: target = "leet"
# Output: "DDR!UURRR!!DDD!"
#
# Question Type : Generic
# Used : Make a map : char : 2d index in the matrix.
#        Now from current position, see the target character. Using coordinate system, find out how much we have to go
#        up, down, left or right from current position.
#        Logic : class Solution:
#        def __init__(self):
#           self.charHash = {}
#           counter = 0
#           for char in "abcdefghijklmnopqrstuvwxyz":
#               self.charHash[char] = (counter // 5, counter % 5)
#               counter += 1
#        def alphabetBoardPath(self, target):
#           currPos = (0, 0), output = ''
#        for char in target:
#           [x, y] = self.charHash[char]
#            moveX = x - currPos[0]
#            moveY = y - currPos[1]
#            if moveY < 0:
#               output += 'L' * abs(moveY)
#            if moveX > 0:
#               output += 'D' * moveX
#            if moveX < 0:
#               output += "U" * abs(moveX)
#            if moveY > 0:
#               output += 'R' * moveY
#            output += '!'
#            currPos = (x, y)
#        return output
# Complexity : O(n)


class Solution:
    def __init__(self):
        self.charHash = {}
        counter = 0
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.charHash[char] = (counter // 5, counter % 5)
            counter += 1

    def alphabetBoardPath(self, target):
        currPos = (0, 0)
        output = ''
        for char in target:
            [x, y] = self.charHash[char]
            moveX = x - currPos[0]
            moveY = y - currPos[1]
            if moveY < 0:
                output += 'L' * abs(moveY)
            if moveX > 0:
                output += 'D' * moveX
            if moveX < 0:
                output += "U" * abs(moveX)
            if moveY > 0:
                output += 'R' * moveY

            output += '!'
            currPos = (x, y)
        return output


if __name__ == "__main__":
    inpStr = "leet"
    solution = Solution()
    print(solution.alphabetBoardPath(inpStr))
