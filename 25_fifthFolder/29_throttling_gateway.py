# https://leetcode.com/discuss/interview-question/700965/throttling-gateway
# Question : The gateway has the following limits:
# The number of transactions in any given second cannot exceed 3.
# The number of transactions in any given 10 second period cannot exceed 20. A ten-second period includes all
# requests arriving from any time max(1, T-9) to T (inclusive of both) for any valid time T.
# The number of transactions in any given minute cannot exceed 60. Similar to above, 1 minute is from max(1, T-59) to T.
# Any request that exceeds any of the above limits will be dropped by the gateway. Given the times at which different
# requests arrive sorted ascending, find how many requests will be dropped.
# Note: Even if a request is dropped it is still considered for future calculations. Although, if a request is to be
# dropped due to multiple violations, it is still counted only once.
# Example
# n = 27
# requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11 ]
#
# Question Type : ShouldSee
# Used : Make a list, each element consisting to 2 values: arrival time, reqCount. Now loop over this arrivalList.
#        At each index, find sum of requests till 0 secs, 20 secs and 60 secs back. If the sum is more than the limit
#        add the diff in dropped count. Also keep track of already dropped requests. If requests are already dropped,
#        we don't need to drop again.
#        gatewayLimit(inpArr):
#        dropped = 0
#        for arrivalTime, count in arrivalList:
#           alreadyDropped = False
#           req_main[arrivalTime] = count
#           start = max(0, arrivalTime - 59)
#           last60_sum = sum(req_main[start:arrivalTime + 1])
#           if last60_sum > 60:
#               alreadyDropped = True
#               dropped += last60_sum - 60
#           start = max(0, arrivalTime-9)
#           last10_sum = sum(req_main[start:arrivalTime+1])
#           if last10_sum > 20 and not alreadyDropped:
#               alreadyDropped = True
#               dropped += last10_sum - 20
#           if count > 3 and not alreadyDropped:
#             dropped += count - 3
#        return dropped
# Complexity : O(n)


def gatewayLimit(inpArr):
    arrivalTime = 1
    reqCount = 0
    arrivalList = []
    maxArriavalTime = max(inpArr)
    req_main = [0] * (maxArriavalTime + 1)
    for time in inpArr:
        if arrivalTime == time:
            reqCount += 1
        else:
            arrivalList.append([arrivalTime, reqCount])
            arrivalTime = time
            reqCount = 1
    arrivalList.append([arrivalTime, reqCount])

    dropped = 0
    for arrivalTime, count in arrivalList:
        alreadyDropped = False
        req_main[arrivalTime] = count

        start = max(0, arrivalTime - 59)
        last60_sum = sum(req_main[start:arrivalTime + 1])
        if last60_sum > 60:
            alreadyDropped = True
            dropped += last60_sum - 60

        start = max(0, arrivalTime-9)
        last10_sum = sum(req_main[start:arrivalTime+1])
        if last10_sum > 20 and not alreadyDropped:
            alreadyDropped = True
            dropped += last10_sum - 20

        if count > 3 and not alreadyDropped:
            dropped += count - 3
    print(dropped)


if __name__ == "__main__":
    k = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
    gatewayLimit(k)

    k = [1, 1, 1, 1, 2]
    gatewayLimit(k)

    k = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]
    gatewayLimit(k)

    k = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9,
         10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 14,
         16, 16, 16, 16, 16, 16, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19,
         20, 20, 20, 20, 20]
    gatewayLimit(k)
