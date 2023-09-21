
def add_elements(inp_arr):
    n = len(inp_arr)

    if n == 1:
        return inp_arr[:]

    left = 0
    right = n - 1
    result = []
    while left < right:
        left_ele = inp_arr[left]
        right_ele = inp_arr[right]

        total = 0
        if left_ele >= 0:
            total += left_ele
        else:
            left += 1
            continue

        if right_ele >= 0:
            total += right_ele
        else:
            right -= 1
            continue

        result.append(total)
        left += 1
        right -= 1

    # print (left, right)
    if (right - left) == 2 or left == right:
        left_ele = inp_arr[left]
        if left_ele >= 0:
            result.append(left_ele)

    return result

class Employee:
    def __init__(self, name, age, role, salary):
        self.name = name
        self.age= age
        self.role = role
        self.salary = salary

def find_avg_of_salary(employee_list, keyword):
    total = 0
    count = 0
    for e in employee_list:
        if keyword in e.role:
            total += e.salary
            count += 1

    return total/count


def make_employee_object_list(emp_list):
    employee_list = []
    for emp in emp_list:
        e = Employee(**emp)
        employee_list.append(e)

    keyword = 'Mrg'
    avg_manager_sal = find_avg_of_salary(employee_list, keyword)
    # print(avg_manager_sal)

    result = []
    for e in employee_list:
        if keyword not in e.role:
            if e.salary > avg_manager_sal:
                result.append(e)

    return result



if __name__ == "__main__":
    # a = [1, 2, 3, 4]
    # print(add_elements(a))
    #
    # a = [1, 2, 3, 4, 5]
    # print(add_elements(a))
    #
    # a = [5]
    # print(add_elements(a))

    #    0  1  2   3  4
    # a = [1, 2, 3, -4, 5]
    # print(add_elements(a))
    #
    # a = [1, 2, -3, -4, 5]
    # print(add_elements(a))

    # a = [1, 2, -3, -4, 5, 6, 7, 8, -9, 10]
    # print(add_elements(a))

    ## Any engineer whose sal is greater than avg of all manager

    emp_list = [{'name': 'Alice', 'age': 26, 'role': 'Software Eng 1', 'salary': 55000},
     {'name': 'Bob', 'age': 24, 'role': 'Software Eng, Staff', 'salary': 45000},
     {'name': 'Charlie', 'age': 30, 'role': 'Mrg 1', 'salary': 65000},
     {'name': 'Diana', 'age': 28, 'role': 'Software Eng, SR 1', 'salary': 60000},
     {'name': 'Eric', 'age': 27, 'role': 'Mrg 2', 'salary': 60000},
     {'name': 'Frank', 'age': 36, 'role': 'Sr Mrg 1', 'salary': 40000}]

    result_list = make_employee_object_list(emp_list)
    for e in result_list:
        print(e.name)

# ls -lR |
