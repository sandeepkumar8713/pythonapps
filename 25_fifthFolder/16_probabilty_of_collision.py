# https://www.geeksforgeeks.org/probability-of-collision-between-two-trucks/
# Question : Given two strings S and T, where S represents the first lane in which vehicles move from
# left to right and T represents the second lane in which vehicles move from right to left. Vehicles can
# be of either B (bike), C (car) or T (truck). The task is to find the probability of collision between
# two trucks.
#
# Example : Input: S = “TCCBCTTB”, T = “BTCCBBTT”
# Output: 0.194444
# Explanation: Total collision = 7
# Total accident = 36
# Therefore, the probability can be calculated by 7/36 = 0.19444.
#
# Question Type : ShouldSee
# Used : Find total number of accident. Find truck collision count.
#        count_of_accident(a, b):
#        n = len(a), m = len(b)
#        if n > m: return (m * (m + 1)) / 2
#        else: return (n * (n + 1)) / 2 + (m - n) * n
#
#        count_of_collision(a, b):
#        ans = 0, truckCountB = 0
#        for i in range(0, m):
#           if b[i] == 'T': truckCountB += 1
#        i = 0
#        while i < m and i < n:
#           if a[i] == 'T': ans += truckCountB
#           if b[i] == 'T': truckCountB -= 1
#           i += 1
#        return ans
# Complexity :O(n)


def count_of_accident(a, b):
    n = len(a)
    m = len(b)

    if n > m:
        return (m * (m + 1)) / 2
    else:
        return (n * (n + 1)) / 2 + (m - n) * n


def count_of_collision(a, b):
    n = len(a)
    m = len(b)
    ans = 0
    truckCountB = 0
    for i in range(0, m):
        if b[i] == 'T':
            truckCountB += 1
    i = 0
    print(truckCountB)
    while i < m and i < n:
        if a[i] == 'T':
            ans += truckCountB
        if b[i] == 'T':
            # Since b is moving left side, T collision count will keep on decreasing.
            truckCountB -= 1
        i += 1
    return ans


def findProbability(a, b):
    total_outcome = count_of_accident(a, b)
    favourable_outcome = count_of_collision(a, b)
    print(favourable_outcome / total_outcome)


if __name__ == "__main__":
    S = "TCCBCTTB"
    T = "BTCCBBTT"
    # S = "TC"
    # T = "TT"
    findProbability(S, T)
