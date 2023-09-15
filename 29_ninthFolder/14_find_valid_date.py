# https://leetcode.com/discuss/interview-question/3863650/Microsoft-OA/2000815
# Question : There is a string representing a date in "MM-DD" format, where MM denotes a month in a two-digit
# format and DD denotes a day in a two-digit format. Some digits were replaced by "?". Replace all the question
# marks with digits (0-9) in such a way as to obtain the latest possible date.
# Assume that the maximum number of days in each month is as follows:
# mm | month | number of days
# 01 | January | 31
# 02 | February | 28
# 03 | March | 31
# 04 | April | 30
# 05 | May | 31
# 06 | June | 30
# 07 | July | 31
# 08 | August | 31
# 09 | September | 30
# 10 | October | 31
# 11 | November | 30
# 12 | December | 31
#
# TODO :: add used

max_days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_matching(chk_month, chk_day, given_month, given_day, result):
    chk_month_str = str(chk_month)
    chk_day_str = str(chk_day)
    if chk_month < 10:
        chk_month_str = '0' + chk_month_str
    if chk_day < 10:
        chk_day_str = '0' + chk_day_str
    chk_date = chk_month_str + chk_day_str
    given_date = given_month + given_day
    for i in range(4):
        if given_date[i] == '?':
            continue
        else:
            if given_date[i] != chk_date[i]:
                return False

    result[0] = chk_month_str + "-" + chk_day_str
    return True


def get_valid_date(inp_str):
    sub_strs = inp_str.split("-")
    given_month = sub_strs[0]
    given_day = sub_strs[1]
    result = ["XX-xx"]

    for chk_month in range(12, 0, -1):
        chk_day = max_days_per_month[chk_month - 1]
        if is_matching(chk_month, chk_day, given_month, given_day, result):
            return result

    return result


if __name__ == "__main__":
    inp_str = "?1-31"
    print (get_valid_date(inp_str))

    inp_str = "02-??"
    print(get_valid_date(inp_str))

    inp_str = "??-4?"
    print(get_valid_date(inp_str))

    inp_str = "09-31"
    print(get_valid_date(inp_str))
