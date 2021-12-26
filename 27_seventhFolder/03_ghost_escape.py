# https://leetcode.com/problems/escape-the-ghosts/
# Question : You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at
# the point [0, 0], and you are given a destination point target = [xtarget, ytarget] that you
# are trying to get to. There are several ghosts on the map with their starting positions
# given as a 2D array ghosts, where ghosts[i] = [xi, yi] represents the starting position
# of the ith ghost. All inputs are integral coordinates. Each turn, you and all the ghosts
# may independently choose to either move 1 unit in any of the four cardinal directions:
# north, east, south, or west, or stay still. All actions happen simultaneously.
# You escape if and only if you can reach the target before any ghost reaches you.
# If you reach any square (including the target) at the same time as a ghost, it does
# not count as an escape. Return true if it is possible to escape regardless of how the
# ghosts move, otherwise return false.
#
# Example : Input: ghosts = [[1,0],[0,3]], target = [0,1]
# Output: true
# Explanation: You can reach the destination (0, 1) after 1 turn, while the ghosts located
# at (1, 0) and (0, 3) cannot catch up with you.
#
# Question Type : Easy
# Used : Loop over the given ghosts list. Find distance of each ghost from target.
#        Find min distance of all the distances calculated.
#        Find person's distance from target.
#        If ghost's min dist is less than person's dist return False else return True.
#        Logic :
#        for ghost in ghosts:
#           min_ghost = min(min_ghost, abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]))
#        if min_ghost <= abs(target[0]) + abs(target[1]):
#           return False
#        else:
#           return True
# Complexity : O(n) where n in number of ghosts


def escapeGhosts(ghosts, target):
    min_ghost = float('inf')
    for ghost in ghosts:
        min_ghost = min(min_ghost, abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]))
    if min_ghost <= abs(target[0]) + abs(target[1]):
        return False
    else:
        return True


if __name__ == "__main__":
    ghosts = [[1, 0], [0, 3]]
    target = [0, 1]
    print(escapeGhosts(ghosts, target))

    ghosts = [[1, 0]]
    target = [2, 0]
    print(escapeGhosts(ghosts, target))

    ghosts = [[5, 0], [-10, -2], [0, -5], [-2, -2], [-7, 1]]
    target = [7, 7]
    print(escapeGhosts(ghosts, target))
