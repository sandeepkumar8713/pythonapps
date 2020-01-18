# https://leetcode.com/discuss/interview-question/390551/
# Question : Given a char grid (o represents an empty cell and x represents a target object) and an API
# getResponse which would give you a response w.r.t. to your previous position. Write a program to find
# the object. You can move to any position.
#
# enum Response {
# 	HOTTER,  // Moving closer to target
# 	COLDER,  // Moving farther from target
# 	SAME,    // Same distance from the target as your previous guess
# 	EXACT;   // Reached destination
# }
#
# // Throws an error if 'row' or 'col' is out of bounds
# public Response getResponse(int row, int col) {
# 	// black box
# }
#
# Example : Input:
# [['o', 'o', 'o'],
#  ['o', 'o', 'o'],
#  ['x', 'o', 'o']]
# Output: [2, 0]
#
# Used : We assume size of grid is given. We do binary search for closest row, from first column. Similarly, closest
#        column, from first row.
#        Logic : def rowBSearch(self, start, end):
#        while self.x_left_bound <= self.x_right_bound:
#           mid = (start + end) // 2
#           self.cur_x, self.cur_y = mid, 0
#           if self.get_response(mid, 0) == Response.EXACT or (
#               self.get_response(mid + 1, 0) != Response.HOTTER and self.get_response(mid - 1, 0) != Response.HOTTER):
#               return mid
#           elif self.get_response(mid + 1, 0) == Response.HOTTER:
#               self.x_left_bound = mid + 1
#           else:
#               self.x_right_bound = mid - 1
# Complexity : O(log n)


from enum import Enum


class Response(Enum):
    HOTTER = Enum.auto()
    COLDER = Enum.auto()
    SAME = Enum.auto()
    EXACT = Enum.auto()


class Solution:
    def __init__(self, grid):
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])  # it says at least one x exists, so m, n > 0r
        self.cur_x, self.cur_y = -1, -1  # current position is (self.cur_x, self.cur_y)
        self.x_left_bound, self.x_right_bound = 0, self.m - 1
        self.y_top_bound, self.y_bottom_bound = 0, self.n - 1

    def get_response(self, row, col):
        pass
        # blackbox

    def columnBSearch(self, start, end):
        while self.y_top_bound <= self.y_bottom_bound:
            mid = (start + end) // 2
            self.cur_x, self.cur_y = 0, mid
            if self.get_response(0, mid) == Response.EXACT or (
                    self.get_response(0, mid + 1) != Response.HOTTER and self.get_response(0, mid - 1) != Response.HOTTER):
                return mid
            elif self.get_response(0, mid + 1) == Response.HOTTER:  # compare (self.cur_x, self.cur_y) = (0, mid) with (0, mid + 1)
                self.y_top_bound = mid + 1
            else:
                self.y_bottom_bound = mid - 1

    def rowBSearch(self, start, end):
        while self.x_left_bound <= self.x_right_bound:
            mid = (start + end) // 2
            self.cur_x, self.cur_y = mid, 0
            if self.get_response(mid, 0) == Response.EXACT or (
                    self.get_response(mid + 1, 0) != Response.HOTTER and self.get_response(mid - 1, 0) != Response.HOTTER):
                return mid
            elif self.get_response(mid + 1, 0) == Response.HOTTER:  # compare (self.cur_x, self.cur_y) = (mid, 0) with (mid + 1, 0)
                self.x_left_bound = mid + 1
            else:
                self.x_right_bound = mid - 1

    def find_object(self):
        closest_x_pos = self.row_bsearch(0, self.m - 1)
        closest_y_pos = self.column_bsearch(0, self.n - 1)
        return [closest_x_pos, closest_y_pos]
