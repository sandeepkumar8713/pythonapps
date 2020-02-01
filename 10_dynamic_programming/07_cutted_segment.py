# https://hackerranksolutionc.blogspot.com/2017/10/cutted-segments.html
# Question : Given an integer N denoting the Length of a line segment. you need to cut the line segment in such a
# way that the cut length of a line segment each time is integer either x , y or z. and after performing all
# cutting operation the total number of cutted segments must be maximum.
#
# Question Type : SimilarAdded
# Used : Similar to before problem
#        Here we are maintaining a memory table. table : dp (lineSegmentLength+1). Initialize all as -1.
#        dp[0] = 0
#        Run a loop from start (minimum cut allowed) to lineSegmentLength
#           Run a loop for each of the element in allowed cut
#               if i >= lineCut and  dp[i - lineCut] != -1 (check if this cut is allowed or not by checking both
#                   left and right)
#               dp[i] = max(dp[i], dp[i-lineCut] + 1) Choose current value or cut at length lineCut and get dp for
#                   remaining line segment, dp[i-lineCut] + 1
#        return dp[lineSegmentLength]
# Complexity : O(n)


def maxSegment(allowedCut,lineSegmentLength):
    dp = [-1] * (lineSegmentLength+1)
    start = min(allowedCut)
    dp[0] = 0

    for i in range(start, lineSegmentLength+1):
        for lineCut in allowedCut:
            if i >= lineCut and dp[i - lineCut] != -1:
                dp[i] = max(dp[i], dp[i-lineCut] + 1)

    return dp[lineSegmentLength]


if __name__ == "__main__":
    lineSegmentLength = 4
    allowedCut = [2, 1, 1]

    # lineSegmentLength = 5
    # allowedCut = [5, 3, 2]
    print(maxSegment(allowedCut, lineSegmentLength))
