# Points
# 1. Based on Age and Experience predict salary using Apache Mlib

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Missing').getOrCreate()

training = spark.read.csv('files/test1.csv', header=True, inferSchema=True)

training.show()

from pyspark.ml.feature import VectorAssembler

featureassembler = VectorAssembler(inputCols=["age", "Experience"], outputCol="Independent Features")

output = featureassembler.transform(training)

finalized_data = output.select("Independent Features", "Salary")

from pyspark.ml.regression import LinearRegression

# train test split
train_data, test_data = finalized_data.randomSplit([0.75, 0.25])
regressor = LinearRegression(featuresCol='Independent Features', labelCol='Salary')
regressor = regressor.fit(train_data)

print(regressor.coefficients)

print(regressor.intercept)

pred_results = regressor.evaluate(test_data)

pred_results.predictions.show()

trainingSummary = regressor.summary
print("MAE: %f" % trainingSummary.meanAbsoluteError)
print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
print("r2: %f" % trainingSummary.r2)
