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

# for col in df.dtypes:
#   print(col[0] + " , " + col[1])
# df_pyspark.printSchema()
# df_pyspark.show()
# print(df_pyspark.columns)
# df_pyspark.select(['Name', 'Experience']).show()
# df_pyspark.filter("Salary<=20000").show()
# df_pyspark.filter(~(df_pyspark['Salary'] <= 20000)).show()
# df_pyspark.groupBy('Name').sum().show()  Salary columns  will be choosen automatically
# df_pyspark.agg({'Salary': 'sum'}).show()

# from pyspark.sql import SparkSession
# from pyspark.sql import functions as F
# df = df.withColumn('PluginDuration', df['PluginDuration'].cast("double").alias('PluginDuration'))
# res_df = df.groupBy("CPID").agg(F.round(F.max('PluginDuration'),2).alias('max_duration'),
#          F.round(F.avg('PluginDuration'),2 ).alias('avg_duration'))\
#          .withColumnRenamed("CPID", "chargepoint_id")
