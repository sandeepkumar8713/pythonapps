# https://leetcode.com/problems/queue-reconstruction-by-height/
# Question : You are given an array of people, people, which are the attributes of some people in
# a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height
# hi with exactly ki other people in front who have a height greater than or equal to hi.
# Reconstruct and return the queue that is represented by the input array people.
# The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the
# attributes of the jth person in the queue (queue[0] is the person at the front of the queue).
#
# Example : Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
#
# Question Type : ShouldSee
# Used : Shorter person does not matter (invisible) to taller person, so insert taller person first.
#        People does not care about the people on their right, so insert the person with smaller k first.
#        Sort(descending order) the give array using h and k respectively as key.
#        Insert the element in ans list at k index while loop over sorted array.
#        Logic :
#        ans = []
#        people.sort(key=lambda x: (-x[0], x[1]))
#        for h, k in people:
#           ans.insert(k, [h, k])
#        return ans
# Complexity : 0(n log n)


def reconstructQueue(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    ans = []
    for h, k in people:
        # insert(index , value)
        ans.insert(k, [h, k])
    return ans


if __name__ == "__main__":
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print (reconstructQueue(people))

    people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    print(reconstructQueue(people))
