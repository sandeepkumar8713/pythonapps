# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
# Question : There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].
# Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay
# them according to the following rules:
# Every worker in the paid group should be paid in the ratio of their quality compared to other workers
# in the paid group.
# Every worker in the paid group must be paid at least their minimum wage expectation.
# Return the least amount of money needed to form a paid group satisfying the above conditions.
#
# Example : Input: quality = [10,20,5], wage = [70,50,30], K = 2
# Output: 105.00000
# Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
#
# Question Type : ShouldSee
# Used : At least one worker is paid their minimum wage expectation. We call him captain worker. Other worker will be
#        paid as their sumOfQuality * ratioOfCaptain.
#        For each captain worker that will be paid their minimum wage expectation, let's calculate
#        the cost of hiring K workers where each point of quality is worth wage[captain] / quality[captain] dollars.
#        Logic : def mincostToHireWorkers(quality, wage, K):
#        from fractions import Fraction
#        workers = sorted((Fraction(w, q), q, w)
#                      for q, w in zip(quality, wage))
#        ans = float('inf')
#        pool = []
#        sumq = 0
#        for ratio, q, w in workers:
#           heapq.heappush(pool, -q)
#           sumq += q
#           if len(pool) > K: sumq += heapq.heappop(pool)
#           if len(pool) == K: ans = min(ans, ratio * sumq)
#        return float(ans)
# Complexity : O(n log n)

import heapq


def mincostToHireWorkers(quality, wage, K):
    from fractions import Fraction
    workers = sorted((Fraction(w, q), q, w)
                     for q, w in zip(quality, wage))

    ans = float('inf')
    pool = []
    sumq = 0
    for ratio, q, w in workers:
        print(ratio, q, w)
        heapq.heappush(pool, -q)
        sumq += q

        if len(pool) > K:
            sumq += heapq.heappop(pool)

        if len(pool) == K:
            # Consider this as captain worker
            ans = min(ans, ratio * sumq)

    return float(ans)


if __name__ == "__main__":
    quality = [3, 1, 10, 10, 1]
    wage = [4, 8, 2, 2, 7]
    K = 3
    print(mincostToHireWorkers(quality, wage, K))

