# Write a command line application or script which parses a cron string and expands each field
# to show the times at which it will run. You may use whichever language you feel most
# comfortable with.
#
# Please do not use existing cron parser libraries for this exercise. Whilst it’s generally a good
# idea to use pre-built libraries, we want to assess your ability to create your own!
#
# You should only consider the standard cron format with five time fields (minute, hour, day of
# month, month, and day of week) plus a command, and you do not need to handle the special
# time strings such as "@yearly". The input will be on a single line.
#
# The cron string will be passed to your application as a single argument.
# ~$ your-program ＂d＂
#
# The output should be formatted as a table with the field name taking the first 14 columns and
# the times as a space-separated list following it.
#
# For example, the following input argument:
# */15 0 1,15 * 1-5 /usr/bin/find

# *	any value
# ,	value list separator
# -	range of values
# /	step values
# @yearly
# minute, hour, day of month, month, and day of week

# minute 0 15 30 45
# hour 0
# day of month 1 15
# month 1 2 3 4 5 6 7 8 9 10 11 12
# day of week 1 2 3 4 5
# command /usr/bin/find

# minute check values
# */15
# */67
# */4
# */40
# */00
# */0
# */59
# */60

# valid expression
# */1,15
# */5,1-4
# 23,0-7
# */5,1-4,10/4
# 10-20/6
# yearly

# invalid expression
# 20-10

import re


def get_regular_expression():
    reg_map = dict()
    reg_map['minute'] = '(0?[0-9]|[0-5][0-9])'
    reg_map['hour'] = '(0?[0-9]|[1][0-9]|[2][0-3])'
    reg_map['day_of_month'] = '(0?[1-9]|[12][0-9]|[3][0-1])'
    reg_map['month'] = '(0?[1-9]|[1][0-2])'
    reg_map['day_of_week'] = '(0?[0-6])'

    return reg_map


# def type_of_range(sub_str, lower_limit, upper_limit):
#     # division
#     regexp_1 = re.compile(r'^\*/([1-9]|[0-5][0-9])$')
#     matched_1 = regexp_1.search(sub_str)
#
#     # comma
#     regexp_2 = re.compile(r'^([0-9]|[0-5][0-9])(,([0-9]|[0-5][0-9]))*$')
#     matched_2 = regexp_2.search(sub_str)
#
#     # hypen
#     regexp_3 = re.compile(r'^([0-9]|[0-5][0-9])-([0-9]|[0-5][0-9])$')
#     matched_3 = regexp_3.search(sub_str)
#
#     # every value *
#     regexp_4 = re.compile(r'^\*$')
#     matched_4 = regexp_4.search(sub_str)
#
#     result = set()
#     if matched_1:
#         sub_string = matched_1.group(1)
#         interval = int(sub_string)
#         checkout = 0
#         while checkout <= upper_limit:
#             result.add(checkout)
#             checkout += interval
#     elif matched_2:
#         sub_string = matched_2.group()
#         checkout_strs = sub_string.split(",")
#         for values in checkout_strs:
#             result.add(int(values))
#     elif matched_3:
#         sub_string = matched_3.group()
#         checkout_strs = sub_string.split("-")
#         start = int(checkout_strs[0])
#         end = int(checkout_strs[1])
#         for value in range(start, end + 1):
#             result.add(int(value))
#     elif matched_4:
#         for value in range(lower_limit, upper_limit + 1):
#             result.add(int(value))
#
#     return sorted(list(result))

def parse_hypen(atom, reg_exp):
    sub_result = set()
    exp = '^' + reg_exp + '-' + reg_exp + '$'
    regexp_1 = re.compile(exp)
    matched_1 = regexp_1.search(atom)
    if matched_1:
        checkout_strs = atom.split("-")
        start = int(checkout_strs[0])
        end = int(checkout_strs[1])
        for value in range(start, end + 1):
            sub_result.add(int(value))

    return sub_result


def parse_star(lower_limit, upper_limit):
    result = set()
    for value in range(lower_limit, upper_limit + 1):
        result.add(value)
    return result


# 5/5
# */5,1-4,10/4
# 10-20/6
# */-56
def parse_division(atom, reg_exp, lower_limit, upper_limit):
    subatomic = atom.split('/')
    result = set()
    sub_result = find_range_from_atom(subatomic[0], reg_exp, lower_limit, upper_limit)
    interval = convert_atom_to_time(subatomic[1], reg_exp)

    sorted_list = sorted(list(sub_result))
    if len(sorted_list) == 0:
        # TODO : add error
        pass

    start = sorted_list[0]
    if len(sorted_list) == 1:
        end = upper_limit
    else:
        end = sorted_list[-1]

    while start <= end:
        result.add(start)
        start += interval

    return result


def convert_atom_to_time(atom, reg_exp):
    exp = '^' + reg_exp + '$'
    regexp = re.compile(exp)
    matched = regexp.search(atom)
    if matched:
        return int(atom)

    # TODO :: handle error
    return None


# */-56 invalid
def find_range_from_atom(atom, reg_exp, lower_limit, upper_limit):
    result = set()
    if '*' == atom:
        result = parse_star(lower_limit, upper_limit)
    elif '/' in atom:
        sub_result = parse_division(atom, reg_exp, lower_limit, upper_limit)
        result = result.union(sub_result)
    elif '-' in atom:
        sub_result = parse_hypen(atom, reg_exp)
        result = result.union(sub_result)
    else:
        sub_result = convert_atom_to_time(atom, reg_exp)
        result.add(sub_result)

    return result


def atoms_parser(atoms, reg_exp, lower_limit, upper_limit):
    result = set()
    for atom in atoms:
        sub_result = find_range_from_atom(atom, reg_exp, lower_limit, upper_limit)
        result = result.union(sub_result)

    print(sorted(list(result)))


def minute_parser(sub_str):
    # TODO :: add validation
    valid_chars = {'0,1,2,3,4,5,6,7,8,9,*,/,-'}
    valid_chars.add(',')

    atoms = sub_str.split(",")
    reg_map = get_regular_expression()
    reg_exp = reg_map['minute']
    lower_limit = 0
    upper_limit = 59
    atoms_parser(atoms, reg_exp, lower_limit, upper_limit)


def hour_parser(sub_str):
    atoms = sub_str.split(",")
    reg_map = get_regular_expression()
    reg_exp = reg_map['hour']
    lower_limit = 0
    upper_limit = 23
    atoms_parser(atoms, reg_exp, lower_limit, upper_limit)


def day_of_month_parser(sub_str):
    atoms = sub_str.split(",")
    reg_map = get_regular_expression()
    reg_exp = reg_map['day_of_month']
    lower_limit = 1
    upper_limit = 31
    atoms_parser(atoms, reg_exp, lower_limit, upper_limit)


def month_parser(sub_str):
    atoms = sub_str.split(",")
    reg_map = get_regular_expression()
    reg_exp = reg_map['month']
    lower_limit = 1
    upper_limit = 12
    atoms_parser(atoms, reg_exp, lower_limit, upper_limit)


def day_of_week_parser(sub_str):
    atoms = sub_str.split(",")
    reg_map = get_regular_expression()
    reg_exp = reg_map['day_of_week']
    lower_limit = 0
    upper_limit = 6
    atoms_parser(atoms, reg_exp, lower_limit, upper_limit)


## TODO :: add scope of the project (input output)

def find_run_interval(inpStr):
    sub_strs = inpStr.split(" ")
    print(sub_strs)

    minute_parser(sub_strs[0])
    hour_parser(sub_strs[1])
    day_of_month_parser(sub_strs[2])
    month_parser(sub_strs[3])
    day_of_week_parser(sub_strs[4])


if __name__ == "__main__":
    inpStr = "*/15 0 1,15 * 1-5 /usr/bin/find"
    find_run_interval(inpStr)
    print()

    # inpStr = "* 0 1,15 * 1-5 /usr/bin/find"
    # find_run_interval(inpStr)
    # print()
    #
    # inpStr = "10-20 0 1,15 * 1-5 /usr/bin/find"
    # find_run_interval(inpStr)
    # print()
    #
    # inpStr = "10,5,0,8,45 0 1,15 * 1-5 /usr/bin/find"
    # find_run_interval(inpStr)
    # print()
    #
    # inpStr = "5/15 0 1,15 * 1-5 /usr/bin/find"
    # find_run_interval(inpStr)
    # print()

    # inpStr = "*/5,1-4,10/4 0 1,15 * 1-5 /usr/bin/find"
    # find_run_interval(inpStr)
    # print()

    # inpStr = "10-20/5 0 1,15 * 1-5 /usr/bin/find"
    # find_run_interval(inpStr)
    # print()
