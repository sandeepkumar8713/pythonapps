# https://leetcode.com/discuss/interview-question/3839353/Microsoft-OA
# Question : You are given a matrix consisting of N rows and M columns. Each cell of the matrix contains
# one digit (0-9). Cells are adjacent if they share a common edge. It is possible to move from one cell to
# another directly only if they are adjacent.
# Find the largest group of cells such that:
# 1. you can get from any cell in the group to any other by moving only through cells that belong to the group.
# 2. the difference between the largest and the smallest values of the cells in the group is at most 1.
# Write a function:
# int solution(vector< vector<int> > &A);
# that, given a matrix A of N rows and M columns containing integers from the range 0-9, returns the maximal
# size of the group, fulfilling the above criteria.
#
# Example : Input :
# matrix = [[3, 4, 6],
#            2, 7, 6]]
# Output : 6, 6, 7 make a group so output is 3
# TODO :: add used

def find_group_size(inp_mat):
    m = len(inp_mat)
    n = len(inp_mat[0])
    grp_size = 0
    mark = [[-1] * n for _ in range(m)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def bfs(a, i, j):
        if mark[i][j] == a or inp_mat[i][j] < a or inp_mat[i][j] > a + 1:
            return 0

        mark[i][j] = a
        queue = []
        queue.append((i, j))
        r = 1
        while len(queue) != 0:
            (x, y) = queue.pop(0)
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if 0 <= next_x < m and 0 <= next_y < n and \
                        mark[next_x][next_y] != a and a <= inp_mat[next_x][next_y] <= a + 1:
                    mark[next_x][next_y] = a
                    queue.append((next_x, next_y))
                    r += 1

        return r

    for a in range(0, 10):
        for i in range(m):
            for j in range(n):
                grp_size = max(grp_size, bfs(a, i, j))

    return grp_size


if __name__ == "__main__":
    inp_mat = [[3, 4, 6],
               [2, 7, 6]]
    print(find_group_size(inp_mat))

    inp_mat = [[3, 3, 5, 6],
               [6, 7, 2, 2],
               [5, 2, 3, 8],
               [5, 9, 2, 3],
               [1, 2, 3, 4]]
    print(find_group_size(inp_mat))

    inp_mat = [[4, 4, 2, 4, 4, 4]]
    print(find_group_size(inp_mat))

    inp_mat = [[0],
               [3],
               [5]]
    print(find_group_size(inp_mat))
