# https://www.geeksforgeeks.org/python-program-for-arranging-the-students-according-to-their-marks-in-descending-order/
# Question : Consider a class of 20 students whose names and marks are given to you. The task is to arrange the
# students according to their marks in decreasing order. Write a python program to perform the task.
#
# Question Type : Easy
# Used : Use the sorted func with key as second element i.e. score
#         result = sorted(inpArr, key=lambda x: x[1])
# Complexity : O(n log n)

def sort_based_on_marks(inpArr):
    result = sorted(inpArr, key=lambda x: x[1])
    print(result)


if __name__ == "__main__":
    inpArr = [("Arun", 78),
               ("Geeta", 86),
               ("Shilphi", 65)]
    sort_based_on_marks(inpArr)
