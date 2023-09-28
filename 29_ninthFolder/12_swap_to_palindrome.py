# https://www.geeksforgeeks.org/count-minimum-swap-to-make-string-palindrome
# Question : Given a string S, the task is to find out the minimum no of adjacent swaps required to make
# string s palindrome. If it is not possible, then return -1.
#
# Example : Input: aabcb
# Output: 3
# Explanation:
# After 1st swap: abacb
# After 2nd swap: abcab
# After 3rd swap: abcba
#
# Used : Take two pointers left and right.
#        Run a loop for it.
#           Within it run another run loop for l and r.
#               dec r until values are diff.
#               if l == r:
#                  swap ele at r and r + 1
#                  continue
#                   inc count
#               else:
#                  while r < right:
#                    swap ele at r and r + 1
#                    inc count
#        return count
# TODO :: add used

def minSwap(inp_arr):
    inp_arr = list(inp_arr)
    freq_dict = {}
    for i in inp_arr:
        freq_dict[i] = freq_dict.get(i, 0) + 1

    odd = 0
    for i in freq_dict:
        if freq_dict[i] % 2 != 0:
            odd += 1
    # If we found more than one odd number
    if odd > 1:
        return -1

    result = 0
    left = 0
    right = len(inp_arr) - 1
    while left < right:
        l = left
        r = right
        # loop while element don't match
        while inp_arr[l] != inp_arr[r]:
            r -= 1
        if l == r:
            # swap only once
            # When we found odd element move towards middle
            inp_arr[r], inp_arr[r + 1] = inp_arr[r + 1], inp_arr[r]
            result += 1
            continue
        else:
            # swap till end
            # Normal element move towards right of string
            while r < right:
                inp_arr[r], inp_arr[r + 1] = inp_arr[r + 1], inp_arr[r]
                r += 1
                result += 1
        left += 1
        right -= 1
    return result


if __name__ == "__main__":
    inpt_str = "aabcc"
    print(minSwap(inpt_str))
