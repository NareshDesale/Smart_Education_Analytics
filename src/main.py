from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Smart Education Analytics Docker Test") \
    .master("local[*]") \
    .getOrCreate()

print("Spark Started Successfully")
print("Spark Version:", spark.version)

xapi_df = spark.read.csv("data/xAPI-Edu-Data.csv", header=True, inferSchema=True)

print("xAPI Dataset Records:", xapi_df.count())
xapi_df.show(5)

spark.stop()