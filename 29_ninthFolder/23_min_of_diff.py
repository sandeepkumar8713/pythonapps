# https://leetcode.com/discuss/interview-question/3794861/Microsoft-OA-Questions
# Question : There is an array A consisting of N Integers. Divide them into three non-empty groups. In each group we
# calculate the difference between the largest and smallest integer. Our goal is to make the maximum of these
# differences as small as possible.
# For example, given A= [11,5,3, 12, 6, 8, 1,7,4], we can divide the elements into three groups:
# [3,1,4]-the difference between elements is 3;
# [5,6,8,7]-the difference is also 3;
# [11,12]-the difference is 1.
# The maximum difference equals 3, which is the minimum possible result

def check(diff, inp_arr):
    i = 0
    j = -1
    for id in range(1, len(inp_arr)):
        if inp_arr[id] - inp_arr[i] <= diff:
            continue

        if i == 0:
            i = id
        else:
            j = id
            break

    if inp_arr[-1] - inp_arr[j] <= diff:
        return True

    return False


# def is_valid(diff, inp_arr):
#     print(inp_arr)
#     n = len(inp_arr)
#     i = 0
#     j = 1
#     # [5, 5, 5, 10, 10]
#     # [4, 5, 7, 10, 10, 12, 12, 12]
#
#     # 0..i-1, i..j-1, j..n-1
#     while j < n and inp_arr[-1] - inp_arr[j] >= diff:
#         j += 1
#
#     while i <= j - 1 and inp_arr[j - 1] - inp_arr[i] > diff:
#         i += 1
#
#     print(i, j, diff)
#     return inp_arr[i - 1] - inp_arr[0] <= diff


def find_max_diff(inp_arr):
    inp_arr.sort()
    n = len(inp_arr)
    ans = -1
    left = 0
    right = inp_arr[-1] - inp_arr[0]
    while left <= right:
        mid = left + (right - left) // 2
        response = check(mid, inp_arr)
        if response:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    # for mid in range(left, right + 1):
    #     if check(mid, inp_arr):
    #         return mid

    return ans


if __name__ == "__main__":
    inp_arr = [11, 5, 3, 12, 6, 8, 1, 7, 4]
    print(find_max_diff(inp_arr))

    inp_arr = [10, 14, 12, 1000, 11, 15, 13, 1]
    print(find_max_diff(inp_arr))

    inp_arr = [4, 5, 7, 10, 10, 12, 12, 12]
    print(find_max_diff(inp_arr))

    inp_arr = [5, 10, 10, 5, 5]
    print(find_max_diff(inp_arr))
