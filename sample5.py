from collections import defaultdict


# def solution(A):
#     # Implement your solution here
#     freq_map = defaultdict(int)
#     for item in A:
#         freq_map[item] = freq_map.get(item, 0) + 1
#
#     max_value = 0
#     for key, value in freq_map.items():
#         if key == value:
#             max_value = max(max_value, key)
#
#     return max_value

def is_interesting(temp):
    uniq_set = set()
    for item in temp:
        if item != ":":
            uniq_set.add(item)

    if len(uniq_set) <= 2:
        return True
    return False

def num_to_str(num):
    if num < 10:
        return '0' + str(num)
    return str(num)

def increment_time(temp):
    times = temp.split(":")
    hr = int(times[0])
    min = int(times[1])
    sec = int(times[2])

    if sec < 59:
        sec += 1
    else:
        sec = 0
        if min < 59:
            min += 1
        else:
            min = 0
            hr += 1

    return num_to_str(hr) + ":" + num_to_str(min) + ":" + num_to_str(sec)


def solution(S, T):
    # Implement your solution here
    start_time = S
    end_time = T
    temp = start_time
    count = 0
    while temp != end_time:
        if is_interesting(temp):
            count += 1
        temp = increment_time(temp)
    if is_interesting(end_time):
        count += 1

    return count

if __name__ == "__main__":
    # A = [3, 8, 2, 3, 3, 2]
    #
    # A = [7, 1, 2, 8, 2]
    #
    # A = [3, 1, 4, 1, 5]
    # print(solution(A))
    #
    # A = [5, 5, 5, 5, 5]
    # print(solution(A))

    S = "15:15:00"
    T = "15:15:12"
    print(solution(S, T))

    S = "22:22:21"
    T = "22:22:23"
    print(solution(S, T))
