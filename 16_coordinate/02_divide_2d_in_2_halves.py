# https://leetcode.com/discuss/interview-question/317383/Google-onsite-Divide-points-into-two-equal-halves
# Question : Give a set of points in a 2D plane. You need to pick two points such that, if you drew a line connecting these points, it would divide the points into two equal halves.
# You can assume that solution always exists.
#
# Question Type : OddOne
# Used : Find the left most point (so the slope is with in 180° range), lets call it point A
#        calculate slope from point A to all the other points
#        Sort the slopes (this will be done in nlog(n) time)
#        return Point A and Median point of slopes
#
# TODO :: add code
#