

def solution(A):
    # Implement your solution here
    left = 0
    right = 0
    n = len(A)
    uniq_set = set()
    uniq_set.add(A[left])
    max_len = 0
    while left < n -1 and right < n - 1:
        if len(uniq_set) > 2:
            uniq_set.remove(A[left])
            left += 1
        else:
            right += 1
            uniq_set.add(A[right])

        if len(uniq_set) <= 2:
            max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    A = [4, 2, 2, 4, 2]
    print(solution(A))

    A = [1, 2, 3, 2]
    print(solution(A))

    A = [0, 5, 4, 4, 5, 12]
    print(solution(A))

    A = [4, 4]
    print(solution(A))
