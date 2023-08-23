# Google
# Question : Find Local Maximum from a given array.A value is Local Maximum if it is greater than its
# adjacent values. Lets take this a step further. Instead of returning an array of numbers (the local maximal),
# recursively find local max.
#
# Example : Input : [1, 2, 3, 1, 4, 1]
# Output : [3, 4]
#
# Question Type : Easy
# Used : Recursion
# Logic : def find_peaks_utils(inp_arr, result):
#         n = len(inp_arr)
#         i = 0, res = []
#         for i in range(1, n - 1):
#           if inp_arr[i - 1] < inp_arr[i] > inp_arr[i + 1]:
#               res.append(inp_arr[i])
#         if len(res) > 0:
#           result.append(res)
#           find_peaks_utils(res, result)
# Complexity : O(n!)

def find_peaks_utils(inp_arr, result):
    n = len(inp_arr)
    i = 0
    res = []
    for i in range(1, n - 1):
        if inp_arr[i - 1] < inp_arr[i] > inp_arr[i + 1]:
            res.append(inp_arr[i])

    if len(res) > 0:
        result.append(res)
        find_peaks_utils(res, result)


def find_peaks(inp_arr):
    result = []
    find_peaks_utils(inp_arr, result)
    return result


if __name__ == "__main__":
    # nums = [1, 6, 4, 10, 5, 9, 3]
    # print(find_peaks(nums))

    nums = [1, 2, 3, 2, 1, -1, 3, 4, 2, 3, 3, 3]
    print(find_peaks(nums))
