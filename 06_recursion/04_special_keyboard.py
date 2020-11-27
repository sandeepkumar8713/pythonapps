# https://www.geeksforgeeks.org/how-to-print-maximum-number-of-a-using-given-four-keys/
# Question : Imagine you have a special keyboard with the following keys:
# Key 1:  Prints 'A' on screen
# Key 2: (Ctrl-A): Select screen
# Key 3: (Ctrl-C): Copy selection to buffer
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
#
# If you can only press the keyboard for N times (with the above four keys), write a program to produce maximum numbers
# of A's. That is to say, the input parameter is N (No. of keys that you can press), the output is M (No. of As that
#  you can produce).
#
# Question Type : ShouldSee
# Used : Level 1: if less than 7 then return same number
#        Level 2:  Definition of a breakpoint is that instance after which we need to only press Ctrl-A,
#                  Ctrl-C once and the only Ctrl-V's afterwards to generate the optimal length.
#                  If we loop from N-3 to 1 and choose each of these values for the break-point, and compute
#                  that optimal string they would produce. Like 16 from 9 keystrokes.
#        Level 3: Use level 2 values, do Ctrl-A, Ctrl-C once and the only Ctrl-V's afterwards to generate
#                 the optimal length. Here formula is : curr = (n-b-1)*screen[b-1]
#                 (b is the no. of keystrokes already entered before copy)
#        This solved through dynamic programming.
#        Logic :
#        for n in range(7, N+1, 1):
#           screen[n-1] = 0
#           for b in range(n-3, 0, -1):
#               curr = (n-b-1) * screen[b-1]
#               if curr > screen[n-1]:
#                   screen[n-1] = curr
#        return screen[N-1]
# Complexity : O(n^2)


def findOptimal(N):
    if N < 7:
        return N

    screen = [0] * N

    for n in range(1, 7, 1):
        screen[n-1] = n

    for n in range(7, N+1, 1):
        screen[n-1] = 0
        # find b, for which no. of A's is optimal
        for b in range(n-3, 0, -1):
            curr = (n-b-1) * screen[b-1]
            if curr > screen[n-1]:
                # use this for backtrace
                # print b, screen[b-1], n, curr
                screen[n-1] = curr

    return screen[N-1]


if __name__ == "__main__":
    # N = 9
    N = 14
    print(findOptimal(N))
