# https://leetcode.com/discuss/interview-question/3930369/Microsoftor-OA-Queestion-or-OnCampus
# Question : There is an array A of N non-negative Integers. Any two Initial elements of A that are adjacent
# can be replaced with their merged equivalent. For example, given A = [2, 3, 15], pair (2, 3) can be replaced
# with 23, resulting in array [23, 15], and pair (3, 15) can be replaced with 315, resulting in array [2, 315].
# The result of the merge cannot be merged any further, so we can't get 2315 in the example above.
# What the maximum possible sum of elements of A after any number of merges?
# Write a function: int solution(int a[], int N);
# that, given an array A of N non-negative integers, returns the maximum sum of elements of A after any number
# of merges.
#
# TODO :: add used

def find_max_sum(inp_ar):
    n = len(inp_ar)
    dp = [0] * (n + 1)
    for i in range(n - 1):
        pair = int(str(inp_ar[i]) + str(inp_ar[i + 1]))
        #print (pair)
        dp[i + 2] = max(dp[i + 2], dp[i] + pair)  # merge

        dp[i + 1] = max(dp[i + 1], dp[i] + inp_ar[i])  # not merge

    return max(dp[n], dp[n-1])


if __name__ == "__main__":
    inp_ar = [2, 3, 15]
    print(find_max_sum(inp_ar))

    inp_ar = [2, 2, 3, 5, 4, 0]
    print(find_max_sum(inp_ar))

    # [3, 19191, 913]
    inp_ar = [3, 19, 191, 91, 3]
    print(find_max_sum(inp_ar))

    # [126, 1810, 10]
    inp_ar = [12, 6, 18, 10, 1, 0]
    print(find_max_sum(inp_ar))

    # [21, 0, 12, 91, 0]
    inp_ar = [2, 1, 0, 1, 2, 9, 1, 0]
    print(find_max_sum(inp_ar))
