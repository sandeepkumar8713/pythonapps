# Points
# 1. inferSchema=True, to consider data types mentioned in the CSV file
# 2. List all columns
# 3. Get only few columns
# 4. Get summary of data (count, mean, stddev, min, max)
# 5. Adding Columns in data frame
# 6. Drop column
# 7. Rename column

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Dataframe').getOrCreate()

df_pyspark = spark.read.option('header', 'true').csv('files/test1.csv', inferSchema=True)

df_pyspark.printSchema()

print(df_pyspark.dtypes)

print(df_pyspark.columns)

df_pyspark.select(['Name', 'Experience']).show()

print(df_pyspark['Name'])

df_pyspark.describe().show()

# Add another column and deriving its value from existing column
df_pyspark = df_pyspark.withColumn('Experience After 2 year', df_pyspark['Experience'] + 2)

# Drop column
df_pyspark=df_pyspark.drop('Experience After 2 year')

# Rename
df_pyspark.withColumnRenamed('Name','New Name')
