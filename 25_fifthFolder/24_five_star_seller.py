# https://leetcode.com/discuss/interview-question/933383/
# Third-party companies that sell their products on Amazon.com are able to analyze the customer reviews for
# their products in real time. Imagine that Amazon is creating a category called "five-star sellers" that will
# only display products sold by companies whose average percentage of five-star reviews per-product is at or
# above a certain threshold. Given the number of five-star and total reviews for each product a company sells,
# as well as the threshold percentage, what is the minimum number of additional five-star reviews the company
# needs to become a five-star seller?
#
# Example: Let's say there are 3 products (n = 3) where productRatings = [[4,4], [1,2], [3, 6]],
# and the percentage ratings Threshold = 77. The first number for each product in productRatings denotes the
# number of fivestar reviews, and the second denotes the number of total reviews. Here is how we can get the seller
# to reach the threshold with the minimum number of additional five-star reviews:
# Before we add more five-star reviews, the percentage for this seller is ((4 / 4) + (1/2) + (3/6))/3 = 66.66%
# If we add a five-star review to the second product, the percentage rises to ((4 / 4) + (2/3) +(3/6))/3 = 72.22%
# If we add another five-star review to the second product, the percentage rises to ((4 / 4) + (3/4) + (3/6))/3 = 75.00%
# If we add a five-star review to the third product, the percentage rises to ((4/4) + (3/4) + (4/7))/3 = 77.38%
# At this point, the threshold of 77% has been met. Therefore, the answer is 3 because that is the minimum number
# of additional five-star reviews the company needs to become a five-star seller.
#
# Question Type : Generic
# Used : Make a max heap out of the products. Where the matching condition is that, node at top will have
#        highest improved rate. i.e. choose the product to add new item whose rating improve the most,
#        thus increasing the overall average.
#        fiveStarSellers(ratings, threshold):
#        avgRatings = 0, count = 0
#        total5Stars = 0, N = len(ratings)
#        ratingList = []
#        for item in ratings:
#           total5Stars += item[0] / item[1]
#           ratingList.append(Ratings(item))
#        avgRatings = total5Stars / N
#        heapq.heapify(ratingList)
#        while avgRatings < threshold and ratingList:
#           r = heapq.heappop(ratingList)
#           avgRatings += (((r.data[0] + 1) / (r.data[1] + 1)) - r.data[0] / r.data[1]) / N
#           r.data[0] += 1, r.data[1] += 1
#           heapq.heappush(ratingList, r)
#           count += 1
#        return count
# Complexity : O(n + k log n) where k is number of additions

import heapq


class Ratings(object):
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        ax, ay = self.data[0], self.data[1]
        bx, by = other.data[0], other.data[1]

        return -((ax + 1) / (ay + 1) - (ax / ay)) <= -((bx + 1) / (by + 1) - (bx / by))


def fiveStarSellers(ratings, threshold):
    avgRatings = 0
    total5Stars, N = 0, 0
    count = 0
    N = len(ratings)
    ratingList = []

    for item in ratings:
        total5Stars += item[0] / item[1]
        ratingList.append(Ratings(item))

    avgRatings = total5Stars / N
    heapq.heapify(ratingList)

    while avgRatings < threshold and ratingList:
        r = heapq.heappop(ratingList)
        avgRatings += (((r.data[0] + 1) / (r.data[1] + 1)) - r.data[0] / r.data[1]) / N
        r.data[0] += 1
        r.data[1] += 1
        heapq.heappush(ratingList, r)
        count += 1
    return count


if __name__ == "__main__":
    print(fiveStarSellers([[4, 4], [1, 2], [3, 6]], 0.77))
    print(fiveStarSellers([[9, 10]], 0.91))
    print(fiveStarSellers([[1, 3], [1, 4]], 0.6))
