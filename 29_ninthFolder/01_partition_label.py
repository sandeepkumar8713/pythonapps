# https://leetcode.com/problems/partition-labels/
# Question : You are given a string s. We want to partition the string into as many parts as possible so that each
# letter appears in at most one part.
# i.e. We need to partition just after max reach of a character.
# Note that the partition is done so that after concatenating all the parts in order, the
# resultant string should be s. Return a list of integers representing the size of these parts.
#
# Example : Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
#
# Question Type : ShouldSee
# Used : Keep track of max reach of each character.
#        When we reach the max reach, while looping over the input array do partition.
#        Also reset max_reach and count.
# Logic: for i in range(len(inp_str)):
#        count = count + 1
#        if last_pos[inp_str[i]] > max_reach:
#           max_reach = last_pos[inp_str[i]]
#        if i == max_reach:
#           res.append(count)
#           max_reach = 0
#           count = 0
#        return res
# Complexity : O(n)

def partition_labels(inp_str):
    last_pos = dict()
    for i in range(len(inp_str)):
        last_pos[inp_str[i]] = i
    max_reach = 0
    res = []
    count = 0

    for i in range(len(inp_str)):
        count = count + 1
        if last_pos[inp_str[i]] > max_reach:
            max_reach = last_pos[inp_str[i]]

        if i == max_reach:
            res.append(count)
            max_reach = 0
            count = 0
    return res


if __name__ == "__main__":
    inp_str = "ababcbacadefegdehijhklij"
    print(partition_labels(inp_str))

    inp_str = "eccbbbbdec"
    print(partition_labels(inp_str))
