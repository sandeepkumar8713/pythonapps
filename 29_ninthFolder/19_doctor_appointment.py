# https://leetcode.com/discuss/interview-question/3842054/Microsoft-OA
# https://leetcode.com/discuss/interview-question/3839311/OA
# Question : There are N patients (numbered from 0 to N-1) who want to visit the doctor. The doctor has S possible
# appointment slots, numbered from 1 to S. Each of the patients has two preferences. Patient K would like to visit the
# doctor during either slot A[K] or slot B[K]. The doctor can treat only one patient during each slot.
# Is it possible to assign every patient to one of their preferred slots so that there will be at most one patient
# assigned to each slot? Write a function:
# int solution (int A[], int B[], int N, int S);
# that, given two arrays A and B, both of N integers, and an integer S, returns 1 if it is possible to assign every
# patient to one of their preferred slots, one patient to one slot, and 0 otherwise.
#
# 1. Given A = [1, 1, 3], B = [2, 2, 1] and S=3, the function should return 1. We could assign patients in the
# following way: [1, 2, 3], where the K-th element of the array represents the number of the slot to which patient K
# was assigned. Another correct assignment would be [2, 1, 3]. On the other hand, [2, 2, 1] would be an incorrect
# assignment as two patients would be assigned to slot 2.
#
# 2. Given A = [3,2,3,1], B = [1, 3, 1, 2] and S = 3, the function should return 0. There are only three slots
# available, but there are four patients who want to visit the doctor. It is therefore not possible to assign the
# patients to the slots so that only one patient at a time would visit the doctor.
#
# TODO :: add used

from collections import defaultdict


def can_assign(pref_a, pref_b, available_slots):
    pref_map = defaultdict(list)
    n = len(pref_a)

    for i in range(n):
        pref_map[pref_a[i] - 1].append(i)
        pref_map[pref_b[i] - 1].append(i)

    def dfs(c, i, color, all):
        if c[i] == color:
            return True

        if c[i] >= 0 and c[i] != color:
            return False

        c[i] = color
        all.append(i)

        for x in pref_map[color]:
            if color == pref_a[x] - 1:
                next_color = pref_b[x] - 1
            else:
                next_color = pref_a[x] - 1
            if x != i and not dfs(c, x, next_color, all):
                return False

        return True

    assignment = [-1] * n
    for i in range(n):
        if assignment[i] < 0:
            all = []
            if not dfs(assignment, i, pref_a[i] - 1, all):
                while len(all) != 0:
                    assignment[all.pop(-1)] = -1

                if not dfs(assignment, i, pref_b[i] - 1, all):
                    return 0

            for x in all:
                pref_map[pref_a[x] - 1].remove(x)
                pref_map[pref_b[x] - 1].remove(x)

    print(f"assignment = {assignment}")
    print(f"pref_map = {pref_map}")
    return 1


if __name__ == "__main__":
    A = [1, 1, 3]
    B = [2, 2, 1]
    S = 3
    print(f"Ans = {can_assign(A, B, S)}")

    A = [3, 2, 3, 1]
    B = [1, 3, 1, 2]
    S = 3
    print(f"Ans = {can_assign(A, B, S)}")

    A = [2, 5, 6, 5]
    B = [5, 4, 2, 2]
    S = 8
    print(f"Ans = {can_assign(A, B, S)}")

    # patient with index id 4,5,6 have preference only solt id 6,7 which cannot be allocated
    A = [1, 2, 1, 6, 8, 7, 8]
    B = [2, 3, 4, 7, 7, 8, 7]
    S = 10
    print(f"Ans = {can_assign(A, B, S)}")
