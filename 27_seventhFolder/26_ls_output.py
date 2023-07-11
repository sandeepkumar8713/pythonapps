# Question : Implement ls output i.e try to maximize cols and minimize rows.
# Given a list of sorted filenames, we need to find minimum number of rows to show all the files
# within the given screen width.
# ➜  ~ ls
# Applications           Downloads              Music                  Public                 bla.sh                 |
# Desktop                Library                Pictures               PycharmProjects        comDocs                |
# Documents              Movies                 Postman                System.keychain.backup go                     |
#
# Question Type : Asked
# Used : Binary Search, Guess minimum row count
#        Notice that column width is defined by largest filename in the given list.
#        Choose left as 1 and right as length of filename. Now run a binary search b/w left to right.
#        mid will be the row count. Check if this row count will fit all the files. If yes, set right to mid
#        else set left to mid + 1.
# Logic: will_fit(filenames, row_count, screen_width):
#        max_val = -1
#        for filename in filenames:
#           max_val = max(max_val, len(filename))
#        col_count = math.ceil(len(filenames) / row_count)
#        overall_pos = (max_val + 1) * col_count
#        if overall_pos > screen_width: return False
#        return True
#        print_ls(filenames, screen_width):
#        left = 1, right = len(filenames)
#        while left < right:
#           mid = left + (right - left) // 2
#           if will_fit(filenames, mid, screen_width):
#               right = mid
#           else:
#               left = mid + 1
#        return left
# Complexity : O(n log n)

import math


def will_fit(filenames, row_count, screen_width):
    max_val = -1
    for filename in filenames:
        max_val = max(max_val, len(filename))
    col_count = math.ceil(len(filenames) / row_count)
    overall_pos = (max_val + 1) * col_count
    if overall_pos > screen_width:
        return False
    return True


def print_ls(filenames, screen_width):
    # Try to minimize row_count
    left = 1  # valid value
    right = len(filenames)  # valid value
    while left < right:
        mid = left + (right - left) // 2
        if will_fit(filenames, mid, screen_width):
            right = mid  # retaining valid value
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    filenames_1 = ['Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music',
                   'Pictures', 'Postman', 'Public', 'PycharmProjects', 'System.keychain.backup',
                   'bla.sh', 'comDocs', 'go']
    filenames_2 = ['Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music',
                   'Pictures', 'Postman', 'Public', 'PycharmProjects', 'comDocs', 'cow.txt', 'dog.txt',
                   'go', 'pet.txt', 'pet3.txt', 'projects', 'rat_1.txt', 'rat_2.txt', 'rat_3.txt', 'screenshot']
    print(print_ls(filenames_1, 153))
    print(print_ls(filenames_2, 153))
