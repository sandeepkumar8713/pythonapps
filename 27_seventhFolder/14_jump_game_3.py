# https://leetcode.com/problems/jump-game-iii/
# Question : Given an array of non-negative integers arr, you are initially positioned at
# start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i],
# check if you can reach to any index with value 0. Notice that you can not jump outside of
# the array at any time.
#
# Question Type : Generic
# Used : Do BFS from the start index. While push both fwd and back index in queue.
#        During BFS if we get 0 return True. After the loop return False.
# Logic: while que:
#           i = que.pop(0)
#           if arr[i] == 0:
#               return True
#           if i + arr[i] < n and vis[i + arr[i]] == 0:
#               que.append(i + arr[i])
#           if i - arr[i] >= 0 and vis[i - arr[i]] == 0:
#               que.append(i - arr[i])
#           vis[i] = 1
#        return False
# Complexity : O(n)


def canReach(arr, start):
    que = [start]
    n = len(arr)
    vis = [0] * n
    while que:
        i = que.pop(0)
        if arr[i] == 0:
            return True
        if i + arr[i] < n and vis[i + arr[i]] == 0:
            que.append(i + arr[i])
        if i - arr[i] >= 0 and vis[i - arr[i]] == 0:
            que.append(i - arr[i])
        vis[i] = 1
    return False


if __name__ == "__main__":
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    print(canReach(arr, start))
