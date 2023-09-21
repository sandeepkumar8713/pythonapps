# pyspark version : 3.4.1
# https://www.youtube.com/watch?v=_C8kWso4ne4

# Points
# 1. Get spark version
# 2. Load csv file
# 3. Print schema
# 4. Show data frame

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Practise').getOrCreate()

# print (spark.version)

# df_pyspark = spark.read.csv('files/test1.csv')
df_pyspark = spark.read.option('header', 'true').csv('files/test1.csv')

print(type(df_pyspark))

df_pyspark.printSchema()

df_pyspark.show()
