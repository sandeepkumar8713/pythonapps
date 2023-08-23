# https://leetcode.com/problems/prison-cells-after-n-days/
# Question : There are 8 prison cells in a row and each cell is either occupied or vacant.
# Each day, whether the cell is occupied or vacant changes according to the following rules:
# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.
# You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the
# ith cell is vacant, and you are given an integer n.
# Return the state of the prison after n days (i.e., n such changes described above).
#
# Example : Input: cells = [0,1,0,1,1,0,0,1], n = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
#
# Question type : ShouldSee
# Used : Note, that there can be only 2^8 possible options for cells. It means, that after some number of iterations,
#        cells start to repeat, and we found a loop.
#        So we will save intermediate cell state in map, check if already exist.
#        If found, we have found the loop len. Now using this loop len, we will use remainder to remaining days.
# Logic: def prisonAfterNDays(cells, days_count):
#        found_dic = {}
#        for i in range(days_count):
#           cells_str = str(cells)
#           if cells_str in found_dic:
#               loop_len = i - found_dic[cells_str]
#               return prisonAfterNDays(cells, (days_count - i) % loop_len)
#           else:
#               found_dic[cells_str] = i
#               cells = next_step(cells)
#        return cells
#
#        def next_step(cells):
#        res = [0] * 8
#        for i in range(1, 7):
#           res[i] = int(cells[i - 1] == cells[i + 1])
#        return res
# Complexity : O(64)


def next_step(cells):
    res = [0] * 8
    for i in range(1, 7):
        res[i] = int(cells[i - 1] == cells[i + 1])
    return res


def prisonAfterNDays(cells, days_count):
    found_dic = {}
    for i in range(days_count):
        cells_str = str(cells)
        if cells_str in found_dic:
            loop_len = i - found_dic[cells_str]
            return prisonAfterNDays(cells, (days_count - i) % loop_len)
        else:
            found_dic[cells_str] = i
            cells = next_step(cells)

    return cells


if __name__ == "__main__":
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    days_count = 7
    print(prisonAfterNDays(cells, days_count))
