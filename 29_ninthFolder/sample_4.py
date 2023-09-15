# sql
# "+-----------+--------------+----------+
# |  Source   | Destination  | Distance |
# +-----------+--------------+----------+
# |  Mumbai   |  Bangalore   |   300    |
# | Bangalore |    Mumbai    |   300    |
# |   Delhi   |   Chennai    |   700    |
# |  Chennai  |    Delhi     |   700    |
# |  Nagpur   |     Pune     |   500    |
# |   Pune    |    Nagpur    |   500    |
# +-----------+--------------+----------+
#
# "+---------+--------------+----------+
# | Source  | Destination  | Distance |
# +---------+--------------+----------+
# | Mumbai  | Bangalore    | 300      |
# | Delhi   | Chennai      | 700      |
# | Nagpur  | Pune         | 500      |
# +---------+--------------+----------+
#"

# sql, one way route, mumbai to bangalore :

# with cte as (select distinct(source) as dist_source from trips)
# with cte_1 as (select distinct(source Destination) from trips);
# with cte_1 as (select contact(source, '_', destination) as pair from trips);
#
# select contact(source, '_', destination) from trips
# union
# select contact(destination, '_', source) from trips
#
# create table new_table as select * from trips;
#
# delete p1 from new_table p1, trips p2
# where p1.source = p2.destination and p1.destination = p2.source and p1.rowno > p2.rowno;

# n=3
# 1,5,2,2,7,12,87,34,2
# [[1, 5, 2],
# [2, 7, 12],
# [87, 34, 2]]

import math

def find_diag_diff(n, inp_list):
    inp_mat = []
    left_to_right = 0
    right_to_left = 0
    for i in range(n):
        row = []
        for j in range(n):
            item = inp_list[i*n +  j]
            row.append(item)

            if i == j:
                left_to_right += item

            if (i + j) == n-1:
                right_to_left += item

        inp_mat.append(row)

    print (left_to_right)
    print (right_to_left)

    return abs(left_to_right-right_to_left)


if __name__ == "__main__":
    inp_list=[1, 5, 2, 2, 7, 12, 87, 34, 2]
    n = 3
    print(find_diag_diff(n, inp_list))

    n = 4
    inp_list =[1, 7, 23, 87, 45, 98, 12, 56, 76, 98, 12, 87, 34, 87, 41, 33]
    print(find_diag_diff(n, inp_list))




