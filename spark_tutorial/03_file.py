# Points
# 1. Drop rows having null values
# 2. Drop rows having null values, upto the threshold
# 3. Drop rows having null values, if a specific column has it
# 4. Replace null values
# 5. Imputer function used. Add new columns for existing columns with null values replaced with median.

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Practise').getOrCreate()

df_pyspark = spark.read.csv('files/test2.csv', header=True, inferSchema=True)

# df_pyspark.printSchema()
# df_pyspark.show()

# Drop rows with null values
df_pyspark.na.drop().show()

# any==how, drop rows where any column have null value
df_pyspark.na.drop(how="any").show()

# threshold, if a row has 3 or more null values, delete the row
df_pyspark.na.drop(how="any", thresh=3).show()

# Apply drop na only on few specific columns
df_pyspark.na.drop(how="any", subset=['Age']).show()

# Replace null value with specified value
df_pyspark.na.fill('Missing Values', ['Experience', 'age']).show()

from pyspark.ml.feature import Imputer

# Add new columns for existing columns with null values replaced with median
imputer = Imputer(
    inputCols=['age', 'Experience', 'Salary'],
    outputCols=["{}_imputed".format(c) for c in ['age', 'Experience', 'Salary']]
).setStrategy("median")
imputer.fit(df_pyspark).transform(df_pyspark).show()
