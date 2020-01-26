# Question : Given an array consisting cost of toys. Given an integer K depicting the amount with you.
# Maximise the number of toys you can have with K amount.
#
# Question Type : Easy
# Used : Sort the given array of costs. Run a loop to over them while the sum is less than K.
#        Return the value of count.
# Complexity : O(n log n)


def maxToys(costs,K):
    costs.sort()
    sum = 0
    count = 0

    for cost in costs:
        sum += cost
        if sum <= K:
            count += 1
        else:
            break

    return count


if __name__ == "__main__":
    costs = [1, 12, 5, 111, 200, 1000, 10]
    K = 50
    print("Maximum toys that can be bought are:", maxToys(costs, K))
