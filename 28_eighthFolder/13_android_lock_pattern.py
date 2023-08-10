# https://leetcode.com/problems/android-unlock-patterns/
# https://medium.com/@rebeccahezhang/leetcode-351-android-unlock-patterns-d9bae4a8a958
# Question : Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9,
# count the total number of unlock patterns of the Android lock screen, which consist of
# minimum of m keys and maximum n keys.
# Rules for a valid pattern:
# 1. Each pattern must connect at least m keys and at most n keys.
# 2. All the keys must be distinct.
# 3. If the line connecting two consecutive keys in the pattern passes through any other keys,
#    the other keys must have previously selected in the pattern. No jumps through non selected
#    key is allowed.
# 4. The order of keys used matters.
#
# Question Type : Generic
# Used : We will do DP with DFS
#        In each case, we use DFS to count the number of valid paths from the current number (1–9)to the
#        remaining numbers. To optimize, calling DFS less than 9 times, we can use the symmetry of the
#        3 by 3 matrix. If we start from 1 or 3 or 7 or 9, the valid paths number should be the same.
#        One of the invalid case can be: I want to create a pattern using 1 and 3. First you touch 1, moving
#        your finger to the right to reach 3 — oh no, there is 2 in the middle that we don’t want it in my password!
# Logic: res = 0
#        for i in range(m, n + 1):
#           res += dfs(visited, skip, 1, i - 1) * 4
#           res += dfs(visited, skip, 2, i - 1) * 4
#           res += dfs(visited, skip, 5, i - 1)
#        return res
#
#        def dfs(visited, skip, curr, remaining):
#        if remaining < 0: return 0
#        if remaining == 0: return 1
#        visited[curr] = True
#        res = 0
#        for next in range(1, 10):
#           skip_num = skip.get((curr, next))
#           if (not visited[next]) and (skip_num is None or visited[skip_num]):
#               res += dfs(visited, skip, next, remaining - 1)
#        visited[curr] = False
#        return res
# Complexity : O(10*(m-n))

def dfs(visited, skip, curr, remaining):
    if remaining < 0:
        return 0
    if remaining == 0:
        return 1

    visited[curr] = True
    res = 0
    for next in range(1, 10):
        skip_num = skip.get((curr, next))
        if (not visited[next]) and (skip_num is None or visited[skip_num]):
            res += dfs(visited, skip, next, remaining - 1)

    visited[curr] = False
    return res


def count_valid_patterns(m, n):
    skip = dict()
    visited = dict()
    for i in range(1, 10):
        visited[i] = False

    skip[(1, 3)] = skip[(3, 1)] = 2
    skip[(1, 7)] = skip[(7, 1)] = 4
    skip[(3, 9)] = skip[(9, 3)] = 6
    skip[(7, 9)] = skip[(9, 7)] = 8
    skip[(1, 9)] = skip[(9, 1)] = skip[(2, 8)] = skip[(8, 2)] = 5
    skip[(3, 7)] = skip[(7, 3)] = skip[(4, 6)] = skip[(6, 4)] = 5

    res = 0
    for i in range(m, n + 1):
        res += dfs(visited, skip, 1, i - 1) * 4
        res += dfs(visited, skip, 2, i - 1) * 4
        res += dfs(visited, skip, 5, i - 1)

    return res


if __name__ == "__main__":
    m = 1
    n = 1
    print(count_valid_patterns(m, n))
