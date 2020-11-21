# https://leetcode.com/problems/candy/solution/
# https://www.hackerrank.com/challenges/candies/problem
# Question : There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Example :
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
#
# Question Type : Easy
# Used : Initially give 1 candy to each child. Make left and right loop, and increase candy count if neighbours have
#        higher rating.
#        Logic :
#        for i in range(1, n):
#           if ratings[i] > ratings[i-1]: candies[i] = candies[i-1] + 1
#        for i in range(n-2, 0, -1):
#           if ratings[i] > ratings[i+1]: candies[i] = max(candies[i], candies[i+1] + 1)
#        return sum(candies)
# Complexity : O(n)


def minCandy(ratings):
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(n-2, 0, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    return sum(candies)


if __name__ == "__main__":
    # ratings = [1, 0, 2]
    ratings = [1, 2, 2]
    print(minCandy(ratings))
