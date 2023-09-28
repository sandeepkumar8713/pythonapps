# https://leetcode.com/discuss/interview-question/3862314/Microsoft-OA-question
# Similar : 10_dynamic_programming/12_optimal_game_strategy.py
# Question : There is a array.In that Array either you can take first two element first and last element, or last two
# element ....and remove those element you have a P-value ...P-value represents that the, score you can remove is fixed
# every time means the starting score what you have removed must be carray forwarded. score is the sum of 2 element
# you remove. what is the maximum no of element you can remove ?
#
# Example : input : [1, 12, 3, 14, 5, 6, 7]
# Output : 4 (1,12 and 6,7)
#
# TODO :: add used
# Used : DP with DFS
#        We need to call DFS thrice for 3 possible combination of target.
#        In DFS, pick two elements only if their sum matches target
#        For all 3 possible pair, find the max result.
#        For memory, use dict DP where key being (marker, left, right)
#        marker being 0, 1, 2 signifying 3 possible targets.


def max_remove(inp_arr):
    n = len(inp_arr)
    dp = {}

    def dfs(left, right, marker, target):
        if left >= right:
            return 0

        if (marker, left, right) in dp:
            return dp[(marker, left, right)]

        first_two = 0
        first_last = 0
        last_two = 0

        if left + 1 < n and inp_arr[left] + inp_arr[left + 1] == target:
            first_two = 2 + dfs(left + 2, right, marker, target)

        if inp_arr[left] + inp_arr[right] == target:
            first_last = 2 + dfs(left + 1, right - 1, marker, target)

        if right - 1 >= 0 and inp_arr[right - 1] + inp_arr[right] == target:
            last_two = 2 + dfs(left, right - 2, marker, target)

        dp[(marker, left, right)] = max(max(first_two, first_last), last_two)
        return dp[(marker, left, right)]

    first_two_target = inp_arr[0] + inp_arr[1]
    first_last_target = inp_arr[0] + inp_arr[-1]
    last_two_target = inp_arr[-2] + inp_arr[-1]

    res_1 = dfs(0, n - 1, 0, first_two_target)
    res_2 = dfs(0, n - 1, 1, first_last_target)
    res_3 = dfs(0, n - 1, 2, last_two_target)

    return max(max(res_1, res_2), res_3)


if __name__ == "__main__":
    inp_arr = [1, 12, 3, 14, 5, 6, 7]
    print(max_remove(inp_arr))
