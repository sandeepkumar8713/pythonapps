# Question : Suppose there is a circle. There are n petrol pumps on that circle. You are given two sets of data.
# 1. The amount of petrol that every petrol pump has.
# 2. Distance from that petrol pump to the next petrol pump.
# Calculate the first point from where a truck will be able to complete the circle (The truck will stop at each petrol
# pump and it has infinite capacity). Expected time complexity is O(n). Assume for 1 litre petrol, the truck can go 1
# unit of distance.
#
# Question Type : Generic
# Used : We can use a Queue to store the current tour. We first enqueue first petrol pump to the queue, we keep
# enqueueing petrol pumps till we either complete the tour, or current amount of petrol becomes negative. If the
# amount becomes negative, then we keep dequeueing petrol pumps till the current amount becomes positive or queue
# becomes empty.
# Complexity : O(n)  If we consider the items between start and end as part of a circular queue, we can observe that
# every item is enqueued at most two times to the queue.


class PetrolPump:
    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance


def printTour(arr):
    n = len(arr)
    start = 0
    end = 1

    curr_petrol = arr[start].petrol - arr[start].distance
    while (end != start or curr_petrol < 0):
        while (curr_petrol < 0 and start != end):

            # Remove starting petrol pump. Change start
            curr_petrol -= arr[start].petrol - arr[start].distance
            start = (start + 1) % n

            # If 0 is being considered as start again, then
            # there is no possible solution
            if start == 0:
                return -1

        # Add a petrol pump to current tour
        curr_petrol += arr[end].petrol - arr[end].distance
        end = (end + 1) % n

    return start


if __name__ == "__main__":
    arr = [PetrolPump(6, 4), PetrolPump(3, 6), PetrolPump(7, 3)]
    start = printTour(arr)

    print("No solution" if start == -1 else "start =", start)
