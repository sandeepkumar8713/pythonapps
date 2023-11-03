# Hi
# State_code, name, year
# 2005, 2010, 2015, 2020
#
# table t1
#
# with cte as ( select count(*) as total
#   from t1 where year = 2020
# )
#
# r1 as (select state_code, (count(*) / cte.total) * 100.0 as dist_2020
# from t1, cte where year = 2020
# group by state_code
# )
#
# r2 as (select state_code, (count(*) / cte.total) * 100.0 as dist_2015
# from t1, cte where year = 2015
# group by state_code
# )
#
# r3 as (select r1.state_code, abs(r1.dist_2020 - r2.dist_2015) as change_diff
# from r1 join r2 on r1.state_code = r2.state_code)
#
# select *
# from r3
# order by change_diff
#



