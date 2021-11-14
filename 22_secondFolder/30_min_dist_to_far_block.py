# https://leetcode.com/discuss/interview-question/285144/Google-or-Onsite-or-Minimize-the-distance-to-the-farthest-point
# Question : Assume you're looking to move, and have a set of amenities that you want to have
# easy access to from your new home. You have found a neighborhood you like, each block of which
# has zero or more amenities. How would you pick the block to live in such that the farthest
# distance to any amenity in your list is minimized?
#
# Example:
# Say your list contains {school, grocery}, and the blocks are as follows:
# 1: restaurant, grocery
# 2: movie theater
# 3: school
# 4:
# 5: school
#
# The ideal choice would be block 2, such that the distances to the grocery and the nearest school are 1 each.
# Living on block 1 or 3 would make one of the distances zero, but the other one 2.
#
# Question Type : Generic
# Used : It comes down to sliding window problem, which has all the amenities with shortest length.
#        Run a loop over the input block, keep adding the blocks to window. Within this loop,
#        run another loop, i.e. window has all the amenities:
#           keep removing elements from left side and update min window len.
#        Return mid of left and right of window.
#        Logic : def pickBlock(allAmenities, blocks):
#        block = 0, minLen = sys.maxint, window = dict()
#        lo = 0, hi = 0
#        while hi < len(blocks):
#           addBlockToWindow(blocks[hi], allAmenities, window)
#           while len(window) == len(allAmenities):
#               length = hi - lo
#               if length < minLen:
#                   minLen = length
#                   block = (lo + hi) / 2
#               removeBlockFromWindow(blocks[lo], allAmenities, window)
#               lo += 1
#           hi += 1
#        return block + 1
#        def addBlockToWindow(block, allAmenities, window):
#        for amenity in block:
#           if amenity in allAmenities:
#               if amenity in window:
#                   window[amenity] += 1
#               else:
#                   window[amenity] = 1
# Complexity : O(n)

import sys


def pickBlock(allAmenities, blocks):
    block = 0
    minLen = sys.maxsize
    window = dict()
    lo = 0
    hi = 0
    while hi < len(blocks):
        addBlockToWindow(blocks[hi], allAmenities, window)
        while len(window) == len(allAmenities):
            length = hi - lo
            if length < minLen:
                minLen = length
                block = (lo + hi) / 2
            removeBlockFromWindow(blocks[lo], allAmenities, window)
            lo += 1
        hi += 1

    return block + 1


def addBlockToWindow(block, allAmenities, window):
    for amenity in block:
        if amenity in allAmenities:
            if amenity in window:
                window[amenity] += 1
            else:
                window[amenity] = 1


def removeBlockFromWindow(block, allAmenities, window):
    for amenity in block:
        if amenity in allAmenities:
            window[amenity] -= 1
            if window[amenity] == 0:
                del window[amenity]


if __name__ == "__main__":
    allAmenities = ['restaurant', 'grocery', 'movie', 'theater', 'school']
    blocks = [[],
              ['restaurant', 'grocery'],
              ['movie', 'theater'],
              ['school'],
              [],
              ['school']]

    print(pickBlock(allAmenities, blocks))

