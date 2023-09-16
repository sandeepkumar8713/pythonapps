# https://leetcode.com/discuss/interview-question/3819090/MICROSOFT-OA
# Question : There is a board made of two rows and N columns. The board is represented by two strings,
# rowl and row2, made of characters 'R', 'W' and/or '?'. A board is balanced if, in each row and in each column,
# the number of characters 'R' is equal to the number of characters W.
# For example, the following board is balanced:
# ?RW?WR ?WR?RW
# and the following board is not balanced:
# W?WR? R??W?
# The question marks (?) can be replaced with 'W or 'R'. What is the minimum number of replacements needed to
# balance the board?
#
# TODO :: add used

def compute(ch):
    if ch == 'R':
        return 1
    elif ch == 'W':
        return -1
    return 0


def diff_in_row(row):
    diff = 0
    for ch in row:
        diff += compute(ch)
    return diff


def find_min_replacement(row_1, row_2):
    result = 0
    ques = 0
    n = len(row_1)

    row_1 = list(row_1)
    row_2 = list(row_2)

    for i in range(n):
        if row_1[i] == '?' and row_2[i] == '?':
            ques += 1
        elif (row_1[i] == 'W' and row_2[i] == 'R') or (row_1[i] == 'R' and row_2[i] == 'W'):
            pass
        else:
            if row_1[i] == '?':
                row_1[i] = 'R' if row_2[i] == 'W' else 'W'
                result += 1

            if row_2[i] == '?':
                row_2[i] = 'R' if row_1[i] == 'W' else 'W'
                result += 1

    # R is positive and W is negative
    diff_1 = diff_in_row(row_1)
    diff_2 = diff_in_row(row_1)

    if abs(diff_1) > n // 2:
        return -1

    if abs(diff_2) > n // 2:
        return -1

    total_diff = abs(diff_1) + abs(diff_2)
    if total_diff > 2 * ques:
        result = -1
    else:
        result += total_diff

    return result


if __name__ == "__main__":
    row_1 = "W?WR?"  # "W?WRR"
    row_2 = "R??R?"  # "R?RWW"
    assert find_min_replacement(row_1, row_2) == 3

    row_1 = "R?R??"
    row_2 = "??W??"
    assert find_min_replacement(row_1, row_2) == 5

    row_1 = "RR?"
    row_2 = "?R?"
    assert find_min_replacement(row_1, row_2) == -1

    row_1 = "WWW??"
    row_2 = "RRR??"
    assert find_min_replacement(row_1, row_2) == -1

    row_1 = "?RW?WR"
    row_2 = "?WR?RW"
    assert find_min_replacement(row_1, row_2) == 0

    row_1 = "W?WR?" # W?WRR
    row_2 = "R??W?" # R?RWW
    assert find_min_replacement(row_1, row_2) == 3
