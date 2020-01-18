# Question : Given a partially filled 9*9 2D array 'grid[9][9]', the goal is to assign digits (from 1 to 9)
# to the empty cells so that every row, column, and sub grid of size 3*3 contains exactly one instance of the
# digits from 1 to 9.
#
# Used : Make call to recursive function solveSudoku(grid).
#           It finds the first unvisited cell in grid, if not found, print grid and return true.
#           Else row = unvisitedCell[0] col = unvisitedCell[1]
#           Run a loop from num 0 to 9, to check which one will fit at grid[row][col]. Check if it is safe to set num.
#               (Check that num should not appear in that row, col or box). If is it safe then set grid[row][col] = num.
#               Call solveSudoku again. If it returns true, return true and exit. Else grid[row][col] = 0, and continue
#               the loop.
#           If we are out of loop, return false. (Not possible)
# Complexity : O(N!)


def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False


def used_in_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i + row][j + col] == num:
                return True
    return False


def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3,
                                                                                                 col - col % 3, num)


def solveSudoku(grid):
    unvisitedCell = [0, 0]

    if not find_empty_location(grid, unvisitedCell):
        # If no empty location found print arr
        for item in grid:
            print item
        return True

    row = unvisitedCell[0]
    col = unvisitedCell[1]

    # consider digits 1 to 9
    for num in range(1, 10):
        if check_location_is_safe(grid, row, col, num):
            grid[row][col] = num

            if solveSudoku(grid):
                return True
            # backtracking
            grid[row][col] = 0

    return False


if __name__ == "__main__":
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if not solveSudoku(grid):
        print "No solution exists"
