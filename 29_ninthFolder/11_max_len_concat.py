# https://leetcode.com/discuss/interview-question/3942584/Microsoft-Interview.
# Question : You are give 3 integers aa=5 , ab=0 ,bb=2. These number tell the minimum number of occurrence.
# You have to use 3 string "AA" , "AB" and "BB". We need to create a string of maximum length where the string
# concatenation should not create "AAA" or "BBB" together.
#
# Complexity : ShouldSee
# Used : Find min,max value of 'AA' and 'BB'
#        Make list consisting of min chars repeated min number of times.
#        Now make result with alternating chars using the above list.
#        Append max chars at the start of result once.
#        Now add 'AB' either at the start if max is 'AA' else at the end of result
#        return result
# Logic: max_str = 'AA' if aa > bb else 'BB'
#        min_count = min(aa, bb)
#        max_count = max(aa, bb)
#        construct_s = [get_opposite(max_str)] * min_count if min_count > 0 else []
#        result = ''
#        for item in construct_s:
#           result += item
#           result += get_opposite(item)
#        if max_count > min_count:
#           result = max_str + result
#        if ab > 0:
#           if max_str == 'AA': result = 'AB' + result
#           else: result = result + 'AB'
#        return result
# Complexity : O(n)

def get_opposite(s):
    if s == 'AA':
        return 'BB'
    return 'AA'


def get_max_concat_str(aa, ab, bb):
    max_str = 'AA' if aa > bb else 'BB'
    min_count = min(aa, bb)
    max_count = max(aa, bb)
    construct_s = [get_opposite(max_str)] * min_count if min_count > 0 else []
    result = ''
    for item in construct_s:
        result += item
        result += get_opposite(item)

    if max_count > min_count:
        result = max_str + result

    if ab > 0:
        if max_str == 'AA':
            result = 'AB' + result
        else:
            result = result + 'AB'
    return result


if __name__ == "__main__":
    print(get_max_concat_str(5, 0, 2))
