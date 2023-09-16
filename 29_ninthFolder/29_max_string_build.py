# https://leetcode.com/discuss/interview-question/3841436/Microsoft-OA
# Question : 1 What is the maximum number of strings from S that can be built?
# Write a function: int solution (vector<string> &S, int K):
# that, given an array S and an integer K, returns the maximum number of strings from S that can be built
#
# Examples:  Given S = ["abc", "abb", "cb", "a", "bbb"] and K = 2,
# the function should return 3. Strings "abb" "a" and "bbb" can be built using the two letters 'a' and 'b'.
#
# N is an integer within the range [150,000]
# K is an integer within the range [1.10]
# each string in S has a length within the range [115]:
# each string in S is made from only the first ten lowercase letters of the alphabet ('a'))
#
# TODO :: add used

def make(word):
    bit_vector = 0
    for ch in word:
        bit_vector |= 1 << (ord(ch) - ord('a'))
    return bit_vector


def solution(inp_list, k):
    have = [0] * 1024
    for word in inp_list:
        have[make(word)] += 1

    count = [0] * 1024
    result = 0
    for i in range(1, 1024):
        # unset LSB set bit
        count[i] = count[i & (i - 1)] + 1
        if count[i] > k:
            continue

        may = 0
        j = i
        while j:
            may += have[j]
            j = (j - 1) & i
        result = max(result, may)

    return result


if __name__ == "__main__":
    inp_list = ["abc", "abb", "cb", "a", "bbb"]
    k = 2
    print(solution(inp_list, k))

    inp_list = ["adf", "jjbh", "jcgj", "eij", "adf"]
    k = 3
    print(solution(inp_list, k))

    inp_list = ["abcd", "efgh"]
    k = 3
    print(solution(inp_list, k))

    inp_list = ["bc", "edf", "fde", "dge", "abcd"]
    k = 4
    print(solution(inp_list, k))
