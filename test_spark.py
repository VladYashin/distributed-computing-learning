from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('MyApp').getOrCreate()

print('Spark is running: ', spark)

spark.stop()