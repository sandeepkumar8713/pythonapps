# Question : https://leetcode.com/discuss/interview-question/3770251/Microsoft-OA-Question
# Given a permutation array P (1-based indexing), find the total number of steps required to sort the same
# array using the permutation array.
# Constraints: n = arr.length 2<=n<=10^5
# Example: Say P =[2,5,4,3,1]
# Copy the array from P to arr arr = [2,5,4,3,1] step1 -> arr = [5,1,3,4,2] {Here the elements are arranged
# according to the permutation array, (i.e, permutation array P is considered here as index array to arrange
# elements) Here, 2nd element (5) comes 1st place because in P, 2 is at 1st position 5th element (1) comes
# 2nd place because in P, 5 is at 2nd position and so on...}
# step2 -> arr = [1,2,4,3,5] step3 -> arr = [2,5,4,3,1] step4 -> arr = [5,1,4,3,2] step5 -> arr = [1,2,3,4,5]
#
# TODO :: add used, check if better solution can be found

def is_increasing(inp_arr):
    for i in range(len(inp_arr) - 1):
        if inp_arr[i] > inp_arr[i + 1]:
            return False

    return True


def solve(inp_arr):
    v2 = inp_arr[:]
    n = len(inp_arr)
    ans = 0
    while True:
        if is_increasing(v2):
            break
        v3 = []
        for i in range(n):
            v3.append(v2[inp_arr[i] - 1])
        v2 = v3
        ans += 1

    return ans


if __name__ == "__main__":
    inp_arr = [2, 5, 4, 3, 1]
    print(solve(inp_arr))

    inp_arr = [3, 1, 2, 5, 4]
    print(solve(inp_arr))

    inp_arr = [3, 4, 2, 1]
    print(solve(inp_arr))
