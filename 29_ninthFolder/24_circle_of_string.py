# https://leetcode.com/discuss/interview-question/3794861/Microsoft-OA-Questions
# Question : There is a list A made of N strings, each of length 2. Two strings can be connected together if
# the letter ending the first string is the same as the letter beginning the second string. For example,
# the two strings "ab" and "bc" can be connected, as "ab" ends with a "b" character and "ba" begins with a "b"
# character. Potentially more string can be connected to form a longer chain if the last letter of the previous
# string is the same as the first letter of the next string, e.g. "ab"-"ba"-"ac"-"cb".
# For every K from 0 to N-1, check if all the strings A[0], AKI can be connected together. Strings can be
# reordered, but must not be reversed.
# Write a function:
# char solution(char *A[], int N);
# that, given an array A consisting of N strings, each of length 2, returns a string of length N. The K-th
# character of the string should be '1' if strings A[0]..A[K] can be connected into a single string, or 'O'
# otherwise.
#
# For A= ["he", "T", "lo", "el"], the function should return "1001":
# [he] is already a single string→1
# ["he", "11"] cannot be connected → 0
# ["he", "", "lo"] cannot be connected → 0
# ["he", "II", "lo", "el"] can be connected into "he"-"el"-"-"lo"→1
#
# TODO :: add used

def check(nodes):
    ctr = 0
    zeroes = 0
    for _, v in nodes.items():
        p = v
        if abs(p[0] - p[1]) >= 1:
            ctr += 1
        if p[0] == 0 and p[1] == 0: # handles self refrential nodes like "ll"
            zeroes += 1

    if ctr > 2 or zeroes > 1:
        return False
    if zeroes == 1 and ctr > 0:
        return False

    return True

def find_solution(inp_list):
    nodes = {}
    n = len(inp_list)
    ans = ""
    for i in range(n):
        word = inp_list[i]
        print
        first = word[0]
        last = word[1]

        if first == last and nodes.get(first) == nodes.get(last):
            nodes[first] = (0, 0)
        else:
            (in_deg, out_deg) = nodes.get(first, (0, 0))
            nodes[first] = (in_deg, out_deg + 1)

            (in_deg, out_deg) = nodes.get(last, (0, 0))
            nodes[last] = (in_deg + 1, out_deg)

        if check(nodes):
            ans += "1"
        else:
            ans += "0"

    return ans


if __name__ == "__main__":
    inp_list = ["he", "ll", "lo", "el"]
    print(find_solution(inp_list))

    inp_list = ["ab", "ba", "bq"]
    print(find_solution(inp_list))

    inp_list = ["ee", "ea", "eg"]
    print(find_solution(inp_list))
