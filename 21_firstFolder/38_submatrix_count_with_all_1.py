# https://www.geeksforgeeks.org/number-of-submatrices-with-all-1s/
# Question : Given a N*N matrix containing only 0s and 1s, the task is to count the number of
# submatrices containing all 1s.
#
# Examples: Input : arr[][] = {{1, 1, 1},
#                    {1, 1, 1},
#                    {1, 1, 1}}
# Output : 36
# Explanation: All the possible submatrices will have only 1s. Since, there are 36 submatrices in total, ans = 36
#
# Question Type : ShouldSee
# Used : def findPrefixCount(p_arr, arr):
#        for i in range(0, n):
#           for j in range(n - 1, -1, -1):
#               if not arr[i][j]: continue
#               if j != n - 1: p_arr[i][j] += p_arr[i][j + 1]
#               p_arr[i][j] += arr[i][j]
#        def matrixAllOne(arr):
#        p_arr = [[0 for i in range(n)] for j in range(n)]
#        findPrefixCount(p_arr, arr)
#        ans = 0
#        for j in range(0, n):
#           i = n - 1
#           q = []
#           to_sum = 0
#           while i >= 0:
#               c = 0
#               while len(q) != 0 and q[-1][0] > p_arr[i][j]:
#                   to_sum -= (q[-1][1] + 1) * (q[-1][0] - p_arr[i][j])
#                   c += q[-1][1] + 1
#                   q.pop()
#               to_sum += p_arr[i][j]
#               ans += to_sum
#               q.append((p_arr[i][j], c))
#               i -= 1
#        return ans
# Complexity : O(n^2)


def findPrefixCount(p_arr, arr):
    for i in range(0, n):
        for j in range(n - 1, -1, -1):

            if not arr[i][j]:
                continue

            if j != n - 1:
                p_arr[i][j] += p_arr[i][j + 1]

            p_arr[i][j] += arr[i][j]


# sub-matrices with all 1s
def matrixAllOne(arr):
    p_arr = [[0 for i in range(n)] for j in range(n)]

    findPrefixCount(p_arr, arr)

    # variable to store the final answer
    ans = 0

    for j in range(0, n):
        i = n - 1
        q = []
        to_sum = 0

        while i >= 0:
            c = 0
            while len(q) != 0 and q[-1][0] > p_arr[i][j]:
                to_sum -= (q[-1][1] + 1) * \
                          (q[-1][0] - p_arr[i][j])

                c += q[-1][1] + 1
                q.pop()

            to_sum += p_arr[i][j]
            ans += to_sum

            q.append((p_arr[i][j], c))
            i -= 1

    return ans


if __name__ == "__main__":
    arr = [[1, 1, 0],
           [1, 0, 1],
           [0, 1, 1]]

    n = 3
    print(matrixAllOne(arr))
