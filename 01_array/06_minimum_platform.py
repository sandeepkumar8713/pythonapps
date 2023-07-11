# Similar : https://leetcode.com/problems/meeting-rooms-ii/
# Question : Given arrival and departure times of all trains that reach a railway station,
# find the minimum number of platforms required for the railway station so that no train waits.
#
# Question Type : Generic
# Used : Sort the arrival and departure array
#        Now loop through them, if a new bus is arriving in i while another bus is not
#        departed in j then, add new platform else remove one platform, and keep track
#        of highest platform count till now.
#        Note that if there is clash, i is inc (to show next arrival)
#        else j is inc (to show last departure)
# Logic: findPlatform(arr, dep):
#        platformNeeded = 1
#        result = 1
#        i = 1, j = 0
#        while i < n and j < n:
#           if arr[i] < dep[j]:
#               platformNeeded += 1
#               i += 1
#               result = max(result, platformNeeded)
#           else:
#               platformNeeded -= 1
#               j += 1
#        return result
# Complexity : O(n log n)


def findPlatform(arr, dep):
    n = len(arr)
    arr.sort()
    dep.sort()

    platformNeeded = 1
    result = 1
    i = 1
    j = 0

    while i < n and j < n:
        # if a new bus is arriving while another bus is not departed then add new platform
        if arr[i] < dep[j]:
            platformNeeded += 1
            i += 1
            result = max(result, platformNeeded)
        else:
            platformNeeded -= 1
            j += 1

    return result


if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print("Minimum platfrom required:", findPlatform(arr, dep))

    arr = [900, 940, 970]
    dep = [910, 950, 980]
    print("Minimum platfrom required:", findPlatform(arr, dep))
