# https://leetcode.com/problems/3sum/
# Question : Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
#
# Example : Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Question Type : Easy
# Used : Sort the given input array.
#        Run a loop over the input array. For each ele at i, find other 2 ele b/w i + 1 and n - 1
#        i.e. l and r, keep increasing l and decreasing r to find appropriate sum.
#        Append i, l, r in res whose sum is 0.
#        Return res.
#        Logic:
#        inpArr.sort()
#        for i in range(n):
#           l = i + 1
#           r = n - 1
#           if i > 0 and inpArr[i] == inpArr[i-1]:
#               continue
#           while l < r:
#               if inpArr[i] + inpArr[l] + inpArr[r] == 0:
#                   res.append([inpArr[i], inpArr[l],inpArr[r]])
#                   l += 1
#                   while l < r and inpArr[l] == inpArr[l-1]:
#                       l += 1
#               elif inpArr[i] + inpArr[l] + inpArr[r] > 0:
#                   r -= 1
#               else:
#                   l += 1
#        return res
# Complexity : O(n)


def threeSum(inpArr):
    inpArr.sort()
    n = len(inpArr)
    res = []

    for i in range(n):
        l = i + 1
        r = n - 1
        if i > 0 and inpArr[i] == inpArr[i-1]:
            continue

        while l < r:
            if inpArr[i] + inpArr[l] + inpArr[r] == 0:
                res.append([inpArr[i], inpArr[l],inpArr[r]])
                l += 1
                while l < r and inpArr[l] == inpArr[l-1]:
                    l += 1
            elif inpArr[i] + inpArr[l] + inpArr[r] > 0:
                r -= 1
            else:
                l += 1

    return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print (threeSum(nums))
