# https://leetcode.com/discuss/interview-question/3863650/Microsoft-OA
# Question : We are provided with a plan of an industrial village, represented by an array A consisting of N integers.
# The K-th value (for K within the range O...N-1) represents a field which may contain:
# a forest consisting of A[k] trees (if A[k] is positive);
# an industrial building (if A[K] is non-positive), producing -A[K] units of pollution.
#
# One tree is able to neutralize one unit of pollution. Our goal is to make every neighborhood sustainable, i.e. for
# every field, the sum of its value and the values of its neighbors (adjacent fields to the left and right) should be
# greater than or equal to zero. To achieve this goal, we can plant additional trees in any chosen field
# (note that we can plant trees in fields containing industrial buildings).
#
# For example, given A = [1, -3, 2], there is one tree in the field number 0, an industrial building producing 3
# units of pollution in field number 1 and two trees in field number 2. The sums of values of the fields and their
# neighbors are 1 + (-3) = -2 for field number 0, 1 + (-3) + 2 = 0 for field number 1, and (-3) + 2 = -1 fo
# field number 2. The neighborhoods of fields 0 and 2 are not sustainable, as their sums are negative. After
# planting two trees in field 1, we obtain A = [1, -1, 2]. In the new array, the sums are respectively 0, 2, and 1,
# which makes every neighborhood sustainable What is the minimum number of trees we have to plant in order to
# make every field's neighborhood sustainable?
#
# TODO :: add used

def add_min_tree(inp_arr):
    new_arr = [0] + inp_arr + [0]
    left = 1
    right = len(inp_arr)
    result = 0
    while left <= right:
        currPoll = new_arr[left - 1] + new_arr[left] + new_arr[left + 1]
        if currPoll < 0:
            result += -currPoll
            if new_arr[left] < 0:
                new_arr[left] += -currPoll
            elif new_arr[left + 1] < 0:
                new_arr[left + 1] += -currPoll

        if left == right:
            break

        currPoll = new_arr[right - 1] + new_arr[right] + new_arr[right + 1]
        if currPoll < 0:
            result += -currPoll
            if new_arr[right] < 0:
                new_arr[right] += -currPoll
            elif new_arr[right - 1] < 0:
                new_arr[right - 1] += -currPoll

        left += 1
        right -= 1

    return result


if __name__ == "__main__":
    inp_arr = [1, -3, 2]
    print(add_min_tree(inp_arr))

    inp_arr = [-3, 2, 4, -5, 3]
    print(add_min_tree(inp_arr))

    inp_arr = [-2, 1, -3, 1]
    print(add_min_tree(inp_arr))
