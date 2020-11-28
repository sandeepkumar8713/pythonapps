# https://www.geeksforgeeks.org/program-best-fit-algorithm-memory-management/
# Question : Best fit allocates the process to a partition which is the smallest sufficient partition among the free
# available partitions.
#
# Input : blockSize[]   = {100, 500, 200, 300, 600};
#         processSize[] = {212, 417, 112, 426};
# Output:
# Process No.    Process Size    Block no.
#  1        212        4
#  2        417        2
#  3        112        3
#  4        426        5
#
# Question Type : ShouldSee
# Used : Maintain a array allocation of size n(process count) with value -1. It stores block ids
#        for the process.
#        Run 2 loops, First one loops over process and second one loops over blocks.
#           if blockSize[j] >= processSize[i]: if allocation[i] is -1: assign allocation[i] = j.
#           Else: compare with already assigned to get best block:
#                   if blockSize[allocation[i]] > blockSize[j]:
#                       allocation[i] = j
#           Once allocation is done for this process, update the block size of allocated block.
#           blockSize[allocation[i]] -= processSize[i]
# Complexity : O(m * n)


def bestFit(blockSize, processSize):
    m = len(blockSize)
    n = len(processSize)

    # It stores block ids for the process
    allocation = [-1] * n

    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if allocation[i] == -1:
                    allocation[i] = j
                else:
                    if blockSize[allocation[i]] > blockSize[j]:
                        allocation[i] = j

        if allocation[i] != -1:
            blockSize[allocation[i]] -= processSize[i]

    print("Process Size", "Block Id")
    for i in range(n):
        print(processSize[i], "         ", allocation[i] + 1)


if __name__ == "__main__":
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    bestFit(blockSize, processSize)
