# Question : Implement ls output i.e try to maximize cols and minimize rows
# ➜  ~ ls
# Applications           Downloads              Music                  Public                 bla.sh  |
# Desktop                Library                Pictures               PycharmProjects        comDocs |
# Documents              Movies                 Postman                System.keychain.backup go      |

# Question Type : Asked
# Used : Binary Search, Guess col height

def will_fit(filenames, col_height, screen_width):
    overall_pos = 0
    for i in range(0, len(filenames), col_height):
        first_col = filenames[i: i + col_height]
        max_val = -1
        for filename in first_col:
            max_val = max(max_val, len(filename))
        overall_pos += max_val + 1
        if overall_pos > screen_width:
            return False
    return True


def print_ls(filenames, screen_width):
    left = 1  # valid value
    right = len(filenames)  # valid value
    while left < right:
        mid = left + (right - left) // 2
        if will_fit(filenames, mid, screen_width):
            left = mid  # retaining valid value
        else:
            right = mid + 1

    return left
