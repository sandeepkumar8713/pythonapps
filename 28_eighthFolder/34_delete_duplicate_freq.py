# Question : Find minimum number of delete to make the frequency of each element unique
#
# Example : Input : [1, 1, 1, 2, 2, 2]
# Output : 1 (Either delete 1 or 2 once to make freq unique)
#
# Question Type : Asked
# Used : Make a freq dict.
#        Make a set of unique_values and dict of duplicate_values.
#        Run a loop on duplicate_values
#           Keep reducing its freq unless it is unique or 0.
#           Keep count of number of deletes.
#        return delete_count
# Complexity : O(n)

def solution(inpArr):
    # Implement your solution here
    freq_dict = dict()
    for item in inpArr:
        freq_dict[item] = freq_dict.get(item, 0) + 1

    unique_values = set()
    duplicate_values = dict()
    for key, value in freq_dict.items():
        if value in unique_values:
            duplicate_values[key] = value
        unique_values.add(value)

    result = 0
    for key, value in duplicate_values.items():
        value -= 1
        result += 1
        while value in unique_values and value > 0:
            value -= 1
            result += 1
        if value > 0:
            unique_values.add(value)

    return result


if __name__ == "__main__":
    print(solution([1, 1, 1, 2, 2, 2]))
    print(solution([5, 3, 3, 2, 5, 2, 3, 2]))
    print(solution([127, 15, 3, 8, 10]))
    print(solution([10000000, 10000000, 5, 5, 5, 2, 2, 2, 0, 0]))
