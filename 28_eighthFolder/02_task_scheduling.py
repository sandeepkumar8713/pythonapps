# Question : Given an array task_memory of n positive integers representing the amount of memory required to
# process each task, an array task_type of n positive integers representing the type of each task, and an
# integer max memory, find the minimum amount of time required for the server to process all the tasks.
# Each task takes 1 unit of time to process. The server can process at most two tasks in parallel only if
# they are of the same type and together require no more than max_memory units of memory.
#
# Example n = 4, task_memory= [7, 2, 3, 9], task_type = [1, 2, 1, 3], and max memory, =10.
# Output = 3
#
# Question type : Asked
# Used : Make a map of task types and memory requirements
#        Now for each value list in the map, find out pairs possible with value less than max memory.
#        Make a freq dict, keep track of min and max task
#        Now run loop from min to max and find all the possible pair.
# Logic: def find_pair_count(tasks, target):
#        for task in tasks:
#           task_dict[task] = task_dict.get(task, 0) + 1
#           left = min(left, task)
#           right = max(right, task)
#        pair_count = 0
#        while left < right:
#           if left + right <= target:
#             pair_count += min(task_dict[left], task_dict[right])
#             left += 1
#             while left not in task_dict:
#                 left += 1
#           right -= 1
#           while right not in task_dict:
#             right -= 1
#        return pair_count
# Complexity : O(n) space is O(n)

import sys


def find_pair_count(tasks, target):
    task_dict = dict()
    left = sys.maxsize
    right = -sys.maxsize
    for task in tasks:
        task_dict[task] = task_dict.get(task, 0) + 1
        left = min(left, task)
        right = max(right, task)

    pair_count = 0
    while left < right:
        if left + right <= target:
            pair_count += min(task_dict[left], task_dict[right])
            left += 1
            while left not in task_dict:
                left += 1

        right -= 1
        while right not in task_dict:
            right -= 1

    return pair_count


def scheduling(task_memory, task_type, max_memory):
    n = len(task_memory)
    task_map = {}
    i = 0
    while i < n:
        mem = task_memory[i]
        task = task_type[i]
        task_map[task] = task_map.get(task, []) + [mem]
        i += 1

    time_taken = 0
    for _, tasks in task_map.items():
        if len(tasks) == 1:
            time_taken += 1
            continue
        else:
            pair_count = find_pair_count(tasks, max_memory)
            time_taken += len(tasks) - pair_count

    return time_taken


if __name__ == "__main__":
    task_memory = [7, 2, 3, 9]
    task_type = [1, 2, 1, 3]
    max_memory = 10
    print(scheduling(task_memory, task_type, max_memory))
