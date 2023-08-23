# https://johnkyon.github.io/2019/03/31/kick/
# Question : As the football coach at your local school, you have been tasked with picking a team of exactly P
# students to represent your school. There are N students for you to pick from. The i-th student has a skill
# rating Si, which is a positive integer indicating how skilled they are.
# You have decided that a team is fair if it has exactly P students on it and they all have the same skill rating.
# That way, everyone plays as a team. Initially, it might not be possible to pick a fair team, so you will give
# some of the students one-on-one coaching. It takes one hour of coaching to increase the skill rating of any
# student by 1. The competition season is starting very soon (in fact, the first match has already started!),
# so you'd like to find the minimum number of hours of coaching you need to give before you are able to pick a
# fair team.
#
# Example : Input : n = 4, k = 3, skills = [3, 1, 9, 100]
# Output : 14
#
# Question Type : Generic
# Used : Sort the given input array.
#        We will use sliding window of size k adding the diff wrt to right most element of window.
#        However, while removing left, subtract diff of ele and prev_high.
#        While adding right, add diff of high and prev_high multiplied by (k - 1)
#        Keep track of minimum training time while looping.
# Logic: inp_arr = sorted(skills)
#        high = inp_arr[k - 1]
#        for i in range(0, k):
#           training_time += high - inp_arr[i]
#        min_time = training_time
#        prev_high = high
#        for i in range(k, n):
#           high = inp_arr[i]
#           training_time -= prev_high - inp_arr[i - k]
#           training_time += (high - prev_high) * (k - 1)
#           prev_high = high
#           min_time = min(min_time, training_time)
#        return min_time
# Complexity : O(n log n)


def find_min_time(n, k, skills):
    inp_arr = sorted(skills)
    training_time = 0
    high = inp_arr[k - 1]
    for i in range(0, k):
        training_time += high - inp_arr[i]

    min_time = training_time
    prev_high = high
    for i in range(k, n):
        high = inp_arr[i]
        training_time -= prev_high - inp_arr[i - k]  # remove old diff
        training_time += (high - prev_high) * (k - 1)
        prev_high = high
        min_time = min(min_time, training_time)
    return min_time


if __name__ == "__main__":
    k = 3
    skills = [3, 1, 9, 100]
    print(find_min_time(len(skills), k, skills))

    k = 2
    skills = [5, 5, 1, 2, 3, 4]
    print(find_min_time(len(skills), k, skills))

    k = 5
    skills = [7, 7, 1, 7, 7]
    print(find_min_time(len(skills), k, skills))
