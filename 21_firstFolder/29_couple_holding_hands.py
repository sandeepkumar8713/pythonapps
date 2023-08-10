# https://leetcode.com/problems/couples-holding-hands/
# https://leetcode.com/problems/couples-holding-hands/discuss/416598/PYTHON-Solution-Explained.-Faster-than-98.
# Question : N couples sit in 2N seats arranged in a row and want to hold hands. We want
# to know the minimum number of swaps so that every couple is sitting side by side.
# A swap consists of choosing any two people, then they stand up and switch seats.
# The people and seats are represented by an integer from 0 to 2N-1, the couples are
# numbered in order, the first couple being (0, 1), the second couple being (2, 3),
# and so on with the last couple being (2N-2, 2N-1).
# The couples' initial seating is given by row[i] being the value of the person who
# is initially sitting in the i-th seat.
#
# Example : Input: row = [0, 2, 1, 3]
# Output: 1
# Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
#
# Question Type : Generic
# Used : Make a location map. Loop the row, check adjacent elements. If not pair,
#        use location map to search its pair and swap.
#        Since pair can be 0,1 or 1,0 we are checking this by using mod operation.
# Logic: def minSwapsCouples(row):
#        location = {}
#        for i in range(len(row)):
#           location[row[i]] = i
#        num_swaps = 0
#        for i in range(0, len(row), 2):
#           if row[i] % 2 == 0:
#               if row[i + 1] != row[i] + 1:
#                   loc_partner = location[row[i] + 1]
#                   location[row[i + 1]] = loc_partner
#                   row[i + 1], row[loc_partner] = row[loc_partner], row[i + 1]
#                   num_swaps = num_swaps + 1
#           else:
#               if row[i + 1] != row[i] - 1:
#                   loc_partner = location[row[i] - 1]
#                   location[row[i + 1]] = loc_partner
#                   row[i + 1], row[loc_partner] = row[loc_partner], row[i + 1]
#                   num_swaps = num_swaps + 1
#        return num_swaps
# Complexity : O(n)


def minSwapsCouples(row):
    # create dictionary storing position in row for each person

    location = {}

    for i in range(len(row)):
        location[row[i]] = i  # location[person] returns the index of person in row

    num_swaps = 0
    for i in range(0, len(row), 2):
        if row[i] % 2 == 0:
            if row[i + 1] != row[i] + 1:
                loc_partner = location[row[i] + 1]  # get location of partner
                location[row[i + 1]] = loc_partner
                row[i + 1], row[loc_partner] = row[loc_partner], row[i + 1]  # update the swapped persons location
                num_swaps = num_swaps + 1
        else:
            if row[i + 1] != row[i] - 1:
                loc_partner = location[row[i] - 1]
                location[row[i + 1]] = loc_partner
                row[i + 1], row[loc_partner] = row[loc_partner], row[i + 1]
                num_swaps = num_swaps + 1
    return num_swaps


if __name__ == "__main__":
    row = [0, 2, 1, 3]
    print(minSwapsCouples(row))
