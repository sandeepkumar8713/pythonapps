# https://leetcode.com/problems/frog-jump/
# Question : A frog is crossing a river. The river is divided into some number of units, and at
# each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not
# jump into the water.
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog
# can cross the river by landing on the last stone. Initially, the frog is on the first stone and
# assumes the first jump must be 1 unit.
# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units.
# The frog can only jump in the forward direction.
#
# Question : ShouldSee
# Used : We will use DP with DFS. Where DP[curr, prev_k] tells if it is possible to get to last element,
#        if frog is at curr position, and it reached there by prev_k units.
#        We should run DFS from second position.
#        We need to loop over stones from current pos to the end.
#        From the given position, we should jump in 3 possible positions whose units belong to either,
#        prev_k - 1, prev_k, prev_k + 1.
#        While doing DFS, keep track of subresult in memo_dict.
# Logic: def dfs(stones, curr, prev_k, memo_dict):
#        n = len(stones)
#        if curr >= n: return False
#        if curr == (n - 1): return True
#        res = memo_dict.get((curr, prev_k))
#        if res is not None: return res
#        res = False
#        for proposed_pos in range(curr + 1, n):
#           units = stones[proposed_pos] - stones[curr]
#           if units in [prev_k - 1, prev_k, prev_k + 1]:
#               res |= dfs(stones, proposed_pos, units, memo_dict)
#        memo_dict[(curr, prev_k)] = res
#        return res
# Complexity : O(n*k)

def dfs(stones, curr, prev_k, memo_dict):
    n = len(stones)
    if curr >= n:
        return False

    if curr == (n - 1):
        return True

    res = memo_dict.get((curr, prev_k))
    if res is not None:
        return res

    res = False
    for proposed_pos in range(curr + 1, n):
        units = stones[proposed_pos] - stones[curr]
        if units in [prev_k - 1, prev_k, prev_k + 1]:
            res |= dfs(stones, proposed_pos, units, memo_dict)

    memo_dict[(curr, prev_k)] = res
    return res


def can_jump(stones):
    # key : (current_position, prev_k)
    memo_dict = dict()
    return dfs(stones, 1, 1, memo_dict)


if __name__ == "__main__":
    stones = [0, 1, 3, 5, 6, 8, 12, 17]
    print(can_jump(stones))

    stones = [0, 1, 2, 3, 4, 8, 9, 11]
    print(can_jump(stones))
