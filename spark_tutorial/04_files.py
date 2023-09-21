# Points
# 1. Filter operation
# 2. | or, & and
# 3. ~ negate

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('dataframe').getOrCreate()

df_pyspark = spark.read.csv('files/test1.csv', header=True, inferSchema=True)

# Salary of the people less than or equal to 20000
df_pyspark.filter("Salary<=20000").show()

df_pyspark.filter("Salary<=20000").select(['Name', 'age']).show()

df_pyspark.filter(df_pyspark['Salary'] <= 20000).show()

df_pyspark.filter((df_pyspark['Salary'] <= 20000) &
                  (df_pyspark['Salary'] >= 15000)).show()

df_pyspark.filter(~(df_pyspark['Salary'] <= 20000)).show()
