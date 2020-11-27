# Question : There are n people standing in a circle waiting to be executed. The counting out begins at some point
# in the circle and proceeds around the circle in a fixed direction. In each step, a certain number of people are
# skipped and the next person is executed. The elimination proceeds around the circle (which is becoming smaller
# and smaller as the executed people are removed), until only the last person remains, who is given freedom.
# Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person
# is killed in circle. The task is to choose the place in the initial circle so that you are the last one
# remaining and so survive.
# josephus(n, k) = (josephus(n - 1, k) + k-1) % n + 1
# josephus(1, k) = 1
#
# Question Type : ShouldSee
# Used : josephus(n, k) = (josephus(n - 1, k) + k-1) % n + 1
#        josephus(1, k) = 1
#        After the first person (kth from beginning) is killed, n-1 persons are left. So we call
#        josephus(n-1,k) to get the position with n-1 persons. But the position returned by josephus(n-1,k)
#        will consider the position starting from k%n + 1. So, we must make adjustments to the position
#        returned by josephus(n-1,k).
# Complexity : O(n)


def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


if __name__ == "__main__":
    n = 14
    k = 2
    print("The chosen place is ", josephus(n, k))
