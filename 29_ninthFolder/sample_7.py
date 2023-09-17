from pyspark.sql import SparkSession
from pyspark.sql import functions as F


class ChargePointsETLJob:
    # input_path = 'data/input/electric-chargepoints-2017.csv'
    # output_path = 'data/output/chargepoints-2017-analysis'

    input_path = '29_ninthFolder/electric-chargepoints-2017.csv'
    output_path = '29_ninthFolder/chargepoints-2017-analysis'

    def __init__(self):
        self.spark_session = (SparkSession.builder
                              .master("local[*]")
                              .appName("ElectricChargePointsETLJob")
                              .getOrCreate())

    def extract(self):
        # print ("extracting")
        return self.spark_session.read.csv(self.input_path, header=True)

    def transform(self, df):
        df = df.withColumn('PluginDuration', df['PluginDuration'].cast("double").alias('PluginDuration'))

        for col in df.dtypes:
            print(col[0] + " , " + col[1])

        # new_df = df.where(df.CPID == 'AN03155') ANO6056
        # new_df.show(100)

        res_df = df.groupBy("CPID").agg(F.round(F.max('PluginDuration'),2).alias('max_duration'),
                               F.round(F.avg('PluginDuration'),2 ).alias('avg_duration'))\
            .withColumnRenamed("CPID", "chargepoint_id")

        # res_df.show(1000)
        return res_df

    def load(self, df):
        df.write.mode('overwrite').parquet(self.output_path)
        print ("saved")

    def run(self):
        self.load(self.transform(self.extract()))

class SampleClass:
    output_path = 'chargepoints-2017-analysis'

    def __init__(self):
        self.spark_session = (SparkSession.builder
                              .master("local[*]")
                              .appName("ElectricChargePointsETLJob")
                              .getOrCreate())

    def read(self):
        df = self.spark_session.read.parquet(self.output_path, header=True)
        df.show(1000)

        for col in df.dtypes:
            print(col[0] + " , " + col[1])


if __name__ == "__main__":
    job = ChargePointsETLJob()
    job.run()
    # s = SampleClass()
    # s.read()

