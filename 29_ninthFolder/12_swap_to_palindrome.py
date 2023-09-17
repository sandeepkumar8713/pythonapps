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
# TODO :: add used

# Python implementation of program
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
        while inp_arr[l] != inp_arr[r]:
            r -= 1
        if l == r:
            # When we found odd element move towards middle
            inp_arr[r], inp_arr[r + 1] = inp_arr[r + 1], inp_arr[r]
            result += 1
            continue
        else:
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
