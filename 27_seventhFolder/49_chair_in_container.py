# https://leetcode.com/discuss/interview-question/3522829/WayFair-Online-Assessmentor-Need-help-with-this
# A lot of containers have arrived at Wayfair fulfillment center represented as an array A.
# In each container, there are Alil number of chairs. The order of chairs in the containers is as
# follows: chairs numbered 1 to A[0] are in the first container, chairs numbered A[0] + 1 to A[1]
# are in the second container, chairs numbered A[1] + 1 to A[2] are in the third container, and so on.
# Now, you are given an array B representing chair IDs, and you have to find the container to which
# each chair belongs. Return an array containing all the container indexes referring to each chair ID.
#
# Example: Input: A = [12, 7, 3, 4, 9], B = [1,25, 11]
# Output: [1,5, 3]
# Explaniotion : cumulative array =  [2, 9, 12, 16, 25]
# As chair Id 1 belongs to 1st container.
# Chair id 25 belongs to last container i.e 5
# Chair Id 11 belongs to 3rd container
#
# Question Type : Generic
# Used : Find  cumulative array and then do binary search to find the position.
# Complexity : O(n + log n)
# TODO :: add code
