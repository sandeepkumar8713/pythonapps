# https://leetcode.com/discuss/interview-experience/1461079/Google-or-SWE-(L3L4)-or-Dublin-Ireland-or-Reject
# Question : Given an array generate its double-shuffle i.e. double every array element and
# append it's double to the same array. Now shuffle this array randomly. For e.g. if the array is [1, 3, 2]
# then it's double is [1, 3, 2, 2, 6, 4]. Finally, shuffle this array randomly which can be [3, 4, 2, 1, 2, 6]
# Now given a double-shuffle array find it's original array.
#
# Example : if double-shuffle is [3, 4, 2, 1, 2, 6] then return [1, 2, 3] (in no particular order)
#
# Question Type : Easy
# Used : Make a dict of items and its freq
#        Loop over the given inpArr. If item and its half are present in map, append half in res array
#        Also decrease the freq of item and its half in mop
#        After the loop, if size of res is half of inpArr return res else return None
#        Logic :
#        for key in inpArr:
#           if map.get(key) == 0:
#               continue
#           half = key // 2
#           if key % 2 == 0 and half in map.keys():
#               res.append(half), map[half] -= 1, map[key] -= 1
#        if len(res) * 2 == len(inpArr): return res
# Complexity : O(n)


def findOrignalArr(inpArr):
    map = dict()
    res = []
    for item in inpArr:
        map[item] = map.get(item, 0) + 1

    for key in inpArr:
        if map.get(key) == 0:
            continue
        half = key // 2
        if key % 2 == 0 and half in map.keys():
            res.append(half)
            map[half] -= 1
            map[key] -= 1

    if len(res) * 2 == len(inpArr):
        return res

    return None


if __name__ == "__main__":
    inpArr = [3, 4, 2, 1, 2, 6]
    print(findOrignalArr(inpArr))

    inpArr = [4, 4, 2, 1, 2, 6]
    print(findOrignalArr(inpArr))
