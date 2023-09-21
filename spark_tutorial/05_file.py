# Points
# 1. Aggregate and group by

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Agg').getOrCreate()

df_pyspark = spark.read.csv('files/test3.csv', header=True, inferSchema=True)

df_pyspark.show()

# Group by and sum
df_pyspark.groupBy('Name').sum().show()

# Average
df_pyspark.groupBy('Name').avg().show()

# Sum in department
df_pyspark.groupBy('Departments').sum().show()

# mean
df_pyspark.groupBy('Departments').mean().show()

# Count
df_pyspark.groupBy('Departments').count().show()

# Call agg function using dictionary
df_pyspark.agg({'Salary': 'sum'}).show()
